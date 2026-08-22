"""Check candidate-bound artifact adjudications without model inference."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


HASH_LENGTH = 64
QUALITY_CLASSES = {"complete", "strong_partial", "partial", "incomplete", "not_evaluated"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_objects(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_objects(child)


def validate_hash(value: str, field: str, failures: list[str], lengths: tuple[int, ...] = (HASH_LENGTH,)) -> None:
    if len(value) not in lengths or any(char not in "0123456789abcdef" for char in value):
        failures.append(f"{field} is not a lowercase hexadecimal identity of length {lengths}: {value!r}")


def check_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    records = ledger.get("records", [])
    by_id: dict[str, dict[str, Any]] = {}

    required = {
        "record_id",
        "candidate_hash",
        "task_id",
        "evaluation_basis_id",
        "evidence_coverage",
        "quality_class",
        "status",
        "source_repository",
        "source_commit",
        "source_path",
        "source_blob_oid",
    }
    for record in records:
        missing = sorted(required - set(record))
        if missing:
            failures.append(f"record missing fields {missing}: {record.get('record_id', '<unknown>')}")
            continue
        record_id = record["record_id"]
        if record_id in by_id:
            failures.append(f"duplicate record_id: {record_id}")
        by_id[record_id] = record
        validate_hash(record["candidate_hash"], f"{record_id}.candidate_hash", failures)
        validate_hash(record["source_commit"], f"{record_id}.source_commit", failures, (40, 64))
        validate_hash(record["source_blob_oid"], f"{record_id}.source_blob_oid", failures, (40, 64))
        for name, value in record.get("artifact_file_hashes", {}).items():
            validate_hash(value, f"{record_id}.artifact_file_hashes[{name}]", failures)
        if record["quality_class"] not in QUALITY_CLASSES:
            failures.append(f"unknown quality_class in {record_id}: {record['quality_class']}")
        if record["status"] not in {"active", "superseded"}:
            failures.append(f"unknown status in {record_id}: {record['status']}")

    for record in records:
        if record.get("status") == "superseded":
            target = record.get("superseded_by")
            if not target or target not in by_id:
                failures.append(f"superseded record lacks valid target: {record.get('record_id')}")
            elif by_id[target].get("status") != "active":
                failures.append(f"supersession target is not active: {target}")

    active_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("status") == "active":
            active_groups[(record["candidate_hash"], record["task_id"])].append(record)

    conflicts: list[dict[str, Any]] = []
    for (candidate_hash, task_id), group in sorted(active_groups.items()):
        classes = sorted({record["quality_class"] for record in group})
        if len(classes) > 1:
            conflicts.append(
                {
                    "candidate_hash": candidate_hash,
                    "task_id": task_id,
                    "quality_classes": classes,
                    "record_ids": sorted(record["record_id"] for record in group),
                }
            )
            failures.append(f"unreconciled active quality conflict: {candidate_hash} {task_id} {classes}")
        bases = sorted({record["evaluation_basis_id"] for record in group})
        if len(bases) > 1:
            warnings.append(f"multiple active evaluation bases: {candidate_hash} {task_id} {bases}")

    return {
        "record_count": len(records),
        "active_record_count": sum(record.get("status") == "active" for record in records),
        "superseded_record_count": sum(record.get("status") == "superseded" for record in records),
        "candidate_task_groups": len(active_groups),
        "conflicts": conflicts,
        "warnings": warnings,
        "failures": failures,
    }


def git_head(repository: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def verify_ledger_sources(ledger: dict[str, Any]) -> dict[str, Any]:
    root = Path(ledger["source_repository_root"])
    failures: list[str] = []
    verified: list[dict[str, str]] = []
    for record in ledger.get("records", []):
        repository = root / record["source_repository"]
        if not repository.is_dir():
            failures.append(f"missing source repository: {repository}")
            continue
        spec = f"{record['source_commit']}:{record['source_path']}"
        completed = subprocess.run(
            ["git", "-C", str(repository), "rev-parse", spec],
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            failures.append(f"missing source object: {repository} {spec}")
            continue
        observed = completed.stdout.strip()
        if observed != record["source_blob_oid"]:
            failures.append(
                f"source blob mismatch for {record['record_id']}: "
                f"expected {record['source_blob_oid']} observed {observed}"
            )
            continue
        verified.append(
            {
                "record_id": record["record_id"],
                "repository": str(repository),
                "commit": record["source_commit"],
                "path": record["source_path"],
                "blob_oid": observed,
            }
        )
    return {"verified": verified, "failures": failures}


def scan_older_bank(repository: Path, relative_root: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    parse_failures: list[str] = []
    root = repository / relative_root
    for path in sorted(root.rglob("*.json")):
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if '"terminal_candidate_id"' not in raw:
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            parse_failures.append(f"{path}: {exc}")
            continue
        for obj in iter_objects(value):
            required = {"terminal_candidate_id", "terminal_passed_count", "case_count", "task"}
            if not required.issubset(obj):
                continue
            candidate = str(obj["terminal_candidate_id"])
            if len(candidate) != HASH_LENGTH or any(c not in "0123456789abcdef" for c in candidate):
                continue
            rows.append(
                {
                    "candidate_hash": candidate,
                    "task_id": str(obj["task"]),
                    "passed": int(obj["terminal_passed_count"]),
                    "total": int(obj["case_count"]),
                    "source_path": str(path.relative_to(repository)).replace("\\", "/"),
                }
            )

    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(row["candidate_hash"], row["task_id"])].append(row)

    conflicts: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    for (candidate_hash, task_id), group in sorted(groups.items()):
        scores = sorted({(row["passed"], row["total"]) for row in group})
        if len(scores) > 1:
            conflicts.append(
                {
                    "candidate_hash": candidate_hash,
                    "task_id": task_id,
                    "scores": [f"{passed}/{total}" for passed, total in scores],
                }
            )
        candidates.append(
            {
                "candidate_hash": candidate_hash,
                "task_id": task_id,
                "score": f"{scores[0][0]}/{scores[0][1]}" if len(scores) == 1 else None,
                "record_occurrences": len(group),
                "source_file_count": len({row["source_path"] for row in group}),
            }
        )

    return {
        "scored_record_occurrences": len(rows),
        "unique_candidate_task_groups": len(groups),
        "conflicts": conflicts,
        "parse_failures": parse_failures,
        "candidates": candidates,
    }


def build_receipt(ledger_path: Path) -> dict[str, Any]:
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger_result = check_ledger(ledger)
    source_result = verify_ledger_sources(ledger)
    older = ledger["older_bank_scan"]
    repository = Path(older["repository"])
    observed_commit = git_head(repository)
    bank_result = scan_older_bank(repository, older["root"])
    failures = list(ledger_result["failures"])
    failures.extend(source_result["failures"])
    if observed_commit != older["expected_commit"]:
        failures.append(
            f"older bank commit mismatch: expected {older['expected_commit']} observed {observed_commit}"
        )
    if bank_result["conflicts"]:
        failures.append(f"older bank has {len(bank_result['conflicts'])} conflicting candidate scores")
    if bank_result["parse_failures"]:
        failures.append(f"older bank has {len(bank_result['parse_failures'])} JSON parse failures")

    return {
        "schema_version": "artifact-adjudication-consistency-receipt-v0",
        "ledger_path": str(ledger_path).replace("\\", "/"),
        "ledger_sha256": sha256_file(ledger_path),
        "ledger_result": ledger_result,
        "source_custody": source_result,
        "older_bank": {
            "repository": str(repository),
            "expected_commit": older["expected_commit"],
            "observed_commit": observed_commit,
            **bank_result,
        },
        "unresolved_conflict_count": len(failures),
        "failures": failures,
        "passed": not failures,
        "gpu_calls": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = build_receipt(args.ledger)
    payload = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8", newline="\n")
    else:
        print(payload, end="")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
