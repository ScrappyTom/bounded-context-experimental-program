"""Verify pinned sources and the cross-study information-economics episode ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def git_bytes(repository: Path, *args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        capture_output=True,
    ).stdout


def git_text(repository: Path, *args: str) -> str:
    return git_bytes(repository, *args).decode("utf-8").strip()


def _missing_covers(missingness: dict[str, Any], path: str) -> bool:
    parts = path.split(".")
    candidates = [".".join(parts[:index]) for index in range(len(parts), 0, -1)]
    return any(candidate in missingness and str(missingness[candidate]).strip() for candidate in candidates)


def verify_sources(lock: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]]]:
    failures: list[str] = []
    observed: list[dict[str, Any]] = []
    repositories = lock.get("repositories", {})
    resolved: dict[str, str] = {}

    for repository_id, item in repositories.items():
        repository = Path(item["path"])
        commit = item["commit"]
        try:
            actual = git_text(repository, "rev-parse", f"{commit}^{{commit}}")
        except (OSError, subprocess.CalledProcessError) as exc:
            failures.append(f"cannot resolve {repository_id} commit: {exc}")
            continue
        resolved[repository_id] = actual
        if actual != commit:
            failures.append(f"commit mismatch for {repository_id}: expected {commit}, observed {actual}")

    seen_source_ids: set[str] = set()
    seen_objects: set[tuple[str, str]] = set()
    for source in lock.get("sources", []):
        source_id = source["source_id"]
        repository_id = source["repository_id"]
        path = source["path"]
        if source_id in seen_source_ids:
            failures.append(f"duplicate source_id: {source_id}")
        seen_source_ids.add(source_id)
        if (repository_id, path) in seen_objects:
            failures.append(f"duplicate pinned object: {repository_id}:{path}")
        seen_objects.add((repository_id, path))
        if repository_id not in repositories:
            failures.append(f"unknown repository_id for {source_id}: {repository_id}")
            continue
        repository = Path(repositories[repository_id]["path"])
        commit = repositories[repository_id]["commit"]
        try:
            blob_oid = git_text(repository, "rev-parse", f"{commit}:{path}")
            payload = git_bytes(repository, "show", f"{commit}:{path}")
        except (OSError, subprocess.CalledProcessError) as exc:
            failures.append(f"cannot read pinned source {source_id}: {exc}")
            continue
        sha256 = hashlib.sha256(payload).hexdigest()
        size_bytes = len(payload)
        if blob_oid != source["blob_oid"]:
            failures.append(f"blob mismatch for {source_id}")
        if sha256 != source["sha256"]:
            failures.append(f"SHA-256 mismatch for {source_id}")
        if size_bytes != source["size_bytes"]:
            failures.append(f"size mismatch for {source_id}")
        observed.append(
            {
                "source_id": source_id,
                "repository_id": repository_id,
                "commit": commit,
                "path": path,
                "blob_oid": blob_oid,
                "sha256": sha256,
                "size_bytes": size_bytes,
            }
        )
    return failures, observed


def verify_episodes(
    ledger: dict[str, Any], schema: dict[str, Any], lock: dict[str, Any]
) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    required = set(schema["required_episode_fields"])
    regimes = set(schema["regime_values"])
    owners = set(schema["owner_values"])
    demand_values = set(schema["information_demand_values"])
    capacity_values = set(schema["capacity_effect_values"])
    utility_values = set(schema["utility_values"])
    source_ids = {item["source_id"] for item in lock["sources"]}
    repository_commits = {
        repository_id: item["commit"] for repository_id, item in lock["repositories"].items()
    }
    episodes = ledger.get("episodes", [])
    by_id: dict[str, dict[str, Any]] = {}
    boundaries: set[tuple[Any, ...]] = set()

    for episode in episodes:
        episode_id = episode.get("episode_id", "<missing>")
        if not re.fullmatch(r"IEE-\d{3}", episode_id):
            failures.append(f"invalid episode_id: {episode_id}")
        if episode_id in by_id:
            failures.append(f"duplicate episode_id: {episode_id}")
        by_id[episode_id] = episode
        omitted = sorted(required - set(episode))
        if omitted:
            failures.append(f"{episode_id} missing fields: {', '.join(omitted)}")
            continue
        unknown_sources = sorted(set(episode["source_ids"]) - source_ids)
        if unknown_sources:
            failures.append(f"{episode_id} has unknown sources: {', '.join(unknown_sources)}")
        boundary = episode["boundary"]
        boundary_fields = schema["boundary_identity_fields"]
        missing_boundary = [field for field in boundary_fields if field not in boundary]
        if missing_boundary:
            failures.append(f"{episode_id} missing boundary fields: {', '.join(missing_boundary)}")
        else:
            identity = tuple(boundary[field] for field in boundary_fields)
            if identity in boundaries:
                failures.append(f"duplicate canonical boundary: {identity}")
            boundaries.add(identity)
            repository_id = boundary["repository_id"]
            if repository_id not in repository_commits:
                failures.append(f"{episode_id} has unknown boundary repository: {repository_id}")
            elif boundary["commit"] != repository_commits[repository_id]:
                failures.append(f"{episode_id} boundary commit differs from source lock")

        if episode["regime"] not in regimes:
            failures.append(f"{episode_id} invalid regime: {episode['regime']}")
        if episode["owner"] not in owners:
            failures.append(f"{episode_id} invalid owner: {episode['owner']}")
        outcome = episode["outcome"]
        if outcome.get("information_demand") not in demand_values:
            failures.append(f"{episode_id} invalid information_demand")
        if outcome.get("capacity_effect") not in capacity_values:
            failures.append(f"{episode_id} invalid capacity_effect")
        if outcome.get("utility") not in utility_values:
            failures.append(f"{episode_id} invalid utility")

        missingness = episode["missingness"]
        if not isinstance(missingness, dict):
            failures.append(f"{episode_id} missingness must be an object")
            missingness = {}
        for parent_name in ("costs", "outcome"):
            for name, value in episode[parent_name].items():
                path = f"{parent_name}.{name}"
                if value is None and not _missing_covers(missingness, path):
                    failures.append(f"{episode_id} null {path} lacks explicit missingness")
        evaluation = episode["evaluation"]
        if evaluation is None:
            if not _missing_covers(missingness, "evaluation"):
                failures.append(f"{episode_id} null evaluation lacks explicit missingness")
        else:
            for field in ("basis_id", "metric", "before", "after", "scale_max", "quality_class"):
                if field not in evaluation:
                    failures.append(f"{episode_id} evaluation missing {field}")
                elif evaluation[field] is None and not _missing_covers(missingness, f"evaluation.{field}"):
                    failures.append(f"{episode_id} null evaluation.{field} lacks explicit missingness")
            scale = evaluation.get("scale_max")
            for field in ("before", "after"):
                value = evaluation.get(field)
                if value is not None and scale is not None and not 0 <= value <= scale:
                    failures.append(f"{episode_id} evaluation.{field} outside scale")
            if evaluation.get("closure_readiness") not in {"ready", "not_ready", "not_adjudicated"}:
                failures.append(f"{episode_id} invalid closure_readiness")

    seen_groups: set[str] = set()
    for group in ledger.get("comparison_groups", []):
        group_id = group["group_id"]
        if group_id in seen_groups:
            failures.append(f"duplicate comparison group: {group_id}")
        seen_groups.add(group_id)
        members = []
        for episode_id in group["episode_ids"]:
            if episode_id not in by_id:
                failures.append(f"comparison {group_id} references unknown episode {episode_id}")
            else:
                members.append(by_id[episode_id])
        if len(set(group["episode_ids"])) != len(group["episode_ids"]):
            failures.append(f"comparison {group_id} repeats an episode")
        if group.get("same_evaluation_basis_required"):
            bases = {
                episode["evaluation"]["basis_id"]
                for episode in members
                if episode["evaluation"] is not None
            }
            if len(bases) != 1 or len(members) != len(group["episode_ids"]):
                failures.append(f"comparison {group_id} lacks one common evaluation basis")

    summaries = {
        "episode_count": len(episodes),
        "comparison_group_count": len(ledger.get("comparison_groups", [])),
        "repository_counts": dict(sorted(Counter(e["boundary"]["repository_id"] for e in episodes).items())),
        "regime_counts": dict(sorted(Counter(e["regime"] for e in episodes).items())),
        "operation_counts": dict(sorted(Counter(e["operation"] for e in episodes).items())),
        "utility_counts": dict(sorted(Counter(e["outcome"]["utility"] for e in episodes).items())),
        "capacity_effect_counts": dict(sorted(Counter(e["outcome"]["capacity_effect"] for e in episodes).items())),
        "information_demand_counts": dict(sorted(Counter(e["outcome"]["information_demand"] for e in episodes).items())),
        "submitted_count": sum(bool(e["outcome"]["submitted"]) for e in episodes),
        "candidate_changed_count": sum(bool(e["outcome"]["candidate_changed"]) for e in episodes),
        "evaluated_count": sum(e["evaluation"] is not None for e in episodes),
        "not_ready_submission_count": sum(
            bool(e["outcome"]["submitted"])
            and e["evaluation"] is not None
            and e["evaluation"]["closure_readiness"] == "not_ready"
            for e in episodes
        ),
        "gpu_calls": 0,
    }
    return failures, summaries


def verify(lock: dict[str, Any], schema: dict[str, Any], ledger: dict[str, Any]) -> dict[str, Any]:
    source_failures, sources = verify_sources(lock)
    episode_failures, summaries = verify_episodes(ledger, schema, lock)
    failures = source_failures + episode_failures
    return {
        "passed": not failures,
        "failures": failures,
        "source_mode": "pinned_git_objects",
        "source_count": len(sources),
        "source_size_bytes": sum(source["size_bytes"] for source in sources),
        "sources": sources,
        **summaries,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, default=ROOT / "analysis" / "INFORMATION_ECONOMICS_SOURCE_LOCK.json")
    parser.add_argument("--schema", type=Path, default=ROOT / "analysis" / "INFORMATION_ECONOMICS_EPISODE_SCHEMA.json")
    parser.add_argument("--ledger", type=Path, default=ROOT / "analysis" / "INFORMATION_ECONOMICS_EPISODES.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    result = verify(lock, schema, ledger)
    receipt = {
        "schema_version": "information-economics-ledger-receipt-v0",
        "lock_sha256": hashlib.sha256(args.lock.read_bytes()).hexdigest(),
        "episode_schema_sha256": hashlib.sha256(args.schema.read_bytes()).hexdigest(),
        "episode_ledger_sha256": hashlib.sha256(args.ledger.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest(),
        **result,
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
