from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AGGREGATE_PATH = ROOT / "PROGRAM_STAGE_AGGREGATE.json"


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def verify(aggregate: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    stages = aggregate.get("stages")
    if not isinstance(stages, list):
        stages = []
        failures.append("stages must be a list")

    expected_ids = [f"S{index:02d}" for index in range(1, 42)]
    observed_ids = [stage.get("stage_id") for stage in stages if isinstance(stage, dict)]
    if observed_ids != expected_ids:
        failures.append(f"stage IDs differ: {observed_ids!r}")

    allowed_types = {"measured", "eligibility", "offline_audit", "reconciliation"}
    calls = 0
    tokens = 0
    experiment_commits: set[tuple[str, str]] = set()
    for stage in stages:
        if not isinstance(stage, dict):
            failures.append("stage must be an object")
            continue
        stage_id = stage.get("stage_id", "unknown")
        if stage.get("stage_type") not in allowed_types:
            failures.append(f"{stage_id}: invalid stage_type")
        model_calls = stage.get("model_calls")
        serialized_tokens = stage.get("serialized_tokens")
        if not isinstance(model_calls, int) or model_calls < 0:
            failures.append(f"{stage_id}: invalid model_calls")
        if not isinstance(serialized_tokens, int) or serialized_tokens < 0:
            failures.append(f"{stage_id}: invalid serialized_tokens")
        if stage.get("included_in_follow_on_totals") is True:
            if isinstance(model_calls, int):
                calls += model_calls
            if isinstance(serialized_tokens, int):
                tokens += serialized_tokens
        sources = stage.get("sources")
        if not isinstance(sources, list) or not sources:
            failures.append(f"{stage_id}: sources must be a nonempty list")
            continue
        for source in sources:
            if not isinstance(source, dict):
                failures.append(f"{stage_id}: source must be an object")
                continue
            repository = source.get("repository")
            commit = source.get("result_commit")
            if not isinstance(repository, str) or "/" not in repository:
                failures.append(f"{stage_id}: invalid repository")
            if not isinstance(commit, str) or len(commit) != 40 or any(ch not in "0123456789abcdef" for ch in commit):
                failures.append(f"{stage_id}: invalid result_commit {commit!r}")
            if source.get("count_as_experiment_commit") is True and isinstance(repository, str) and isinstance(commit, str):
                experiment_commits.add((repository, commit))

    declared = aggregate.get("declared_totals", {})
    derived = {
        "successor_stages": len(stages),
        "follow_on_model_calls": calls,
        "follow_on_serialized_tokens": tokens,
        "unique_cited_experiment_commits": len(experiment_commits),
    }
    for key, value in derived.items():
        if declared.get(key) != value:
            failures.append(f"declared {key}={declared.get(key)!r}, derived={value}")

    parent = aggregate.get("parent_bank", {})
    if parent.get("exact_replayed_requests") != 42:
        failures.append("parent exact replay count must be 42")
    if parent.get("included_in_follow_on_totals") is not False:
        failures.append("parent bank must be excluded from follow-on totals")

    return {
        "schema_version": "program-stage-aggregate-receipt-v1",
        "passed": not failures,
        "failures": failures,
        "aggregate_sha256": hashlib.sha256(canonical_bytes(aggregate)).hexdigest(),
        "parent_exact_replayed_requests": parent.get("exact_replayed_requests"),
        **derived,
    }


def main() -> int:
    aggregate = json.loads(AGGREGATE_PATH.read_text(encoding="utf-8"))
    receipt = verify(aggregate)
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
