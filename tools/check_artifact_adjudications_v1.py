"""Exact candidate/task/rubric/readiness adjudication consistency checker."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


SHA256_LENGTH = 64
HEX = set("0123456789abcdef")
QUALITY_CLASSES = {"complete", "strong_partial", "partial", "incomplete", "not_evaluated"}
READINESS = {"ready", "not_ready", "not_adjudicated"}
CRITERION_STATUSES = {"met", "partial", "failed", "not_adjudicated"}
PROVENANCE_ROLES = {"independent", "inherited", "reconciliation", "superseded"}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate_hex(value: Any, field: str, failures: list[str], lengths: tuple[int, ...]) -> None:
    if not isinstance(value, str) or len(value) not in lengths or any(char not in HEX for char in value):
        failures.append(f"{field} is not lowercase hexadecimal of length {lengths}: {value!r}")


def index_unique(items: list[dict[str, Any]], key: str, failures: list[str]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        identity = item.get(key)
        if not isinstance(identity, str) or not identity:
            failures.append(f"missing {key}: {item!r}")
            continue
        if identity in result:
            failures.append(f"duplicate {key}: {identity}")
        result[identity] = item
    return result


def payload_projection(payload: dict[str, Any]) -> dict[str, Any]:
    criteria = sorted(payload.get("criteria", []), key=lambda item: item.get("name", ""))
    return {
        "quality_class": payload.get("quality_class"),
        "score": payload.get("score"),
        "closure_readiness": payload.get("closure_readiness"),
        "blocking_requirements": sorted(payload.get("blocking_requirements", [])),
        "criterion_detail_status": payload.get("criterion_detail_status"),
        "criteria": criteria,
    }


def check_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    if ledger.get("schema_version") != "artifact-adjudication-ledger-v1":
        failures.append(f"unexpected ledger schema: {ledger.get('schema_version')}")

    tasks = index_unique(ledger.get("task_specs", []), "task_spec_id", failures)
    evidence = index_unique(ledger.get("evidence_manifests", []), "evidence_manifest_id", failures)
    bases = index_unique(ledger.get("evaluation_bases", []), "evaluation_basis_id", failures)
    payloads = index_unique(ledger.get("adjudication_payloads", []), "payload_id", failures)
    records = index_unique(ledger.get("records", []), "record_id", failures)

    for task_id, task in tasks.items():
        validate_hex(task.get("sha256", ""), f"task_specs[{task_id}].sha256", failures, (64,))
        if not isinstance(task.get("size_bytes"), int) or task["size_bytes"] < 1:
            failures.append(f"invalid task size: {task_id}")

    for manifest_id, manifest in evidence.items():
        validate_hex(manifest.get("sha256", ""), f"evidence_manifests[{manifest_id}].sha256", failures, (64,))
        seen_paths: set[str] = set()
        for item in manifest.get("items", []):
            path = item.get("path")
            if path in seen_paths:
                failures.append(f"duplicate evidence path in {manifest_id}: {path}")
            seen_paths.add(path)
            validate_hex(item.get("sha256", ""), f"{manifest_id}:{path}.sha256", failures, (64,))
            validate_hex(item.get("blob_oid", ""), f"{manifest_id}:{path}.blob_oid", failures, (40, 64))

    for basis_id, basis in bases.items():
        status = basis.get("identity_status")
        value = basis.get("sha256")
        if status == "available":
            validate_hex(value or "", f"evaluation_bases[{basis_id}].sha256", failures, (64,))
        elif status == "not_separately_materialized":
            if value is not None:
                failures.append(f"unavailable evaluation basis has a hash: {basis_id}")
            warnings.append(f"evaluation basis has no separately materialized hash: {basis_id}")
        else:
            failures.append(f"unknown evaluation basis identity_status: {basis_id} {status}")

    for payload_id, payload in payloads.items():
        if payload.get("quality_class") not in QUALITY_CLASSES:
            failures.append(f"unknown quality_class: {payload_id} {payload.get('quality_class')}")
        if payload.get("closure_readiness") not in READINESS:
            failures.append(f"unknown closure_readiness: {payload_id} {payload.get('closure_readiness')}")
        blockers = payload.get("blocking_requirements", [])
        if not isinstance(blockers, list) or any(not isinstance(item, str) or not item for item in blockers):
            failures.append(f"invalid blocking_requirements: {payload_id}")
            blockers = []
        if payload.get("closure_readiness") == "ready" and blockers:
            failures.append(f"ready payload has blocking requirements: {payload_id}")
        if payload.get("closure_readiness") == "not_ready" and not blockers:
            failures.append(f"not-ready payload lacks blocking requirements: {payload_id}")
        detail_status = payload.get("criterion_detail_status")
        if detail_status not in {"complete", "unavailable_in_structured_record"}:
            failures.append(f"unknown criterion_detail_status: {payload_id} {detail_status}")
        criteria = payload.get("criteria", [])
        names = [criterion.get("name") for criterion in criteria]
        if len(names) != len(set(names)):
            failures.append(f"duplicate criterion names: {payload_id}")
        for criterion in criteria:
            if criterion.get("status") not in CRITERION_STATUSES:
                failures.append(
                    f"unknown criterion status: {payload_id} {criterion.get('name')} {criterion.get('status')}"
                )
        if detail_status == "complete":
            counts = Counter(criterion.get("status") for criterion in criteria)
            score = payload.get("score", {})
            expected = {
                "met": counts["met"],
                "partial": counts["partial"],
                "failed": counts["failed"],
                "total": len(criteria),
            }
            if score != expected:
                failures.append(f"criterion/score mismatch in {payload_id}: expected {expected}, got {score}")
            blockers = set(blockers)
            nonmet = {criterion["name"] for criterion in criteria if criterion["status"] != "met"}
            if not blockers.issubset(nonmet):
                failures.append(f"blockers are not non-met criteria in {payload_id}: {sorted(blockers - nonmet)}")
        elif criteria:
            failures.append(f"payload with unavailable criterion detail includes criteria: {payload_id}")

    relationship_pairs = {
        (item.get("from_record_id"), item.get("to_record_id"))
        for item in ledger.get("basis_relationships", [])
        if item.get("relationship") and item.get("explanation")
    }

    required_record_fields = {
        "candidate_hash",
        "artifact_file_hash_manifest",
        "task_spec_id",
        "evaluation_basis_id",
        "evidence_manifest_id",
        "payload_id",
        "status",
        "provenance_role",
        "semantic_independence_group",
        "source_repository",
        "source_commit",
        "source_path",
        "source_blob_oid",
    }
    for record_id, record in records.items():
        missing = sorted(required_record_fields - set(record))
        if missing:
            failures.append(f"record {record_id} missing fields: {missing}")
            continue
        validate_hex(record["candidate_hash"], f"{record_id}.candidate_hash", failures, (64,))
        validate_hex(record["source_commit"], f"{record_id}.source_commit", failures, (40, 64))
        validate_hex(record["source_blob_oid"], f"{record_id}.source_blob_oid", failures, (40, 64))
        for name, value in record["artifact_file_hash_manifest"].items():
            validate_hex(value, f"{record_id}.artifact_file_hash_manifest[{name}]", failures, (64,))
        if record["task_spec_id"] not in tasks:
            failures.append(f"unknown task spec in {record_id}: {record['task_spec_id']}")
        if record["evaluation_basis_id"] not in bases:
            failures.append(f"unknown evaluation basis in {record_id}: {record['evaluation_basis_id']}")
        if record["evidence_manifest_id"] not in evidence:
            failures.append(f"unknown evidence manifest in {record_id}: {record['evidence_manifest_id']}")
        if record["payload_id"] not in payloads:
            failures.append(f"unknown payload in {record_id}: {record['payload_id']}")
        if record["status"] not in {"active", "superseded"}:
            failures.append(f"unknown record status: {record_id} {record['status']}")
        if record["provenance_role"] not in PROVENANCE_ROLES:
            failures.append(f"unknown provenance role: {record_id} {record['provenance_role']}")
        if record["provenance_role"] in {"inherited", "reconciliation"}:
            parent = record.get("derived_from")
            if parent not in records:
                failures.append(f"{record_id} lacks valid derived_from record")
            elif record["semantic_independence_group"] != records[parent].get("semantic_independence_group"):
                failures.append(f"{record_id} changes semantic independence group from {parent}")

    for record_id, record in records.items():
        if record.get("status") != "superseded":
            continue
        target = record.get("superseded_by")
        if target not in records:
            failures.append(f"superseded record lacks valid target: {record_id}")
        elif records[target].get("status") != "active":
            failures.append(f"supersession target is not active: {record_id} -> {target}")
        if (record_id, target) not in relationship_pairs:
            failures.append(f"supersession lacks typed explained relationship: {record_id} -> {target}")

    def canonical_basis(record: dict[str, Any]) -> tuple[str, ...]:
        task = tasks[record["task_spec_id"]]
        basis = bases[record["evaluation_basis_id"]]
        manifest = evidence[record["evidence_manifest_id"]]
        basis_hash = basis.get("sha256") or f"unavailable:{basis['identity_status']}"
        return (
            record["candidate_hash"],
            canonical_json(record["artifact_file_hash_manifest"]),
            task["sha256"],
            record["evaluation_basis_id"],
            basis_hash,
            manifest["sha256"],
        )

    active = [record for record in records.values() if record.get("status") == "active"]
    same_basis: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    candidate_task: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in active:
        references_resolve = (
            record.get("task_spec_id") in tasks
            and record.get("evaluation_basis_id") in bases
            and record.get("evidence_manifest_id") in evidence
            and record.get("payload_id") in payloads
        )
        if not references_resolve:
            continue
        same_basis[canonical_basis(record)].append(record)
        candidate_task[(record["candidate_hash"], tasks[record["task_spec_id"]]["sha256"])].append(record)

    same_basis_conflicts: list[dict[str, Any]] = []
    for basis_key, group in same_basis.items():
        projections = {canonical_json(payload_projection(payloads[record["payload_id"]])) for record in group}
        if len(projections) > 1:
            item = {"basis_key": list(basis_key), "record_ids": sorted(record["record_id"] for record in group)}
            same_basis_conflicts.append(item)
            failures.append(f"same-basis adjudication mismatch: {item['record_ids']}")

    cross_basis_conflicts: list[dict[str, Any]] = []
    for group in candidate_task.values():
        for index, left in enumerate(group):
            for right in group[index + 1 :]:
                if canonical_basis(left) == canonical_basis(right):
                    continue
                left_projection = payload_projection(payloads[left["payload_id"]])
                right_projection = payload_projection(payloads[right["payload_id"]])
                if left_projection == right_projection:
                    continue
                pair = (left["record_id"], right["record_id"])
                reverse = (right["record_id"], left["record_id"])
                if pair not in relationship_pairs and reverse not in relationship_pairs:
                    item = {"record_ids": sorted(pair)}
                    cross_basis_conflicts.append(item)
                    failures.append(f"unexplained cross-basis adjudication divergence: {item['record_ids']}")

    active_independence_groups = sorted({record["semantic_independence_group"] for record in active})
    return {
        "record_count": len(records),
        "active_record_count": len(active),
        "superseded_record_count": sum(record.get("status") == "superseded" for record in records.values()),
        "active_semantic_independence_group_count": len(active_independence_groups),
        "active_semantic_independence_groups": active_independence_groups,
        "same_basis_group_count": len(same_basis),
        "same_basis_conflicts": same_basis_conflicts,
        "cross_basis_conflicts": cross_basis_conflicts,
        "warnings": warnings,
        "failures": failures,
    }


def git_bytes(repository: Path, commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(repository), "show", f"{commit}:{path}"],
        check=True,
        capture_output=True,
    )
    return completed.stdout


def git_text(repository: Path, commit: str, path: str) -> str:
    return git_bytes(repository, commit, path).decode("utf-8")


def git_blob_oid(repository: Path, commit: str, path: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", f"{commit}:{path}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def git_head(repository: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def git_status(repository: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def verify_identity_custody(ledger: dict[str, Any]) -> dict[str, Any]:
    root = Path(ledger["source_repository_root"])
    failures: list[str] = []
    source_records: list[dict[str, str]] = []

    for record in ledger.get("records", []):
        repository = root / record["source_repository"]
        try:
            observed = git_blob_oid(repository, record["source_commit"], record["source_path"])
        except (OSError, subprocess.CalledProcessError) as exc:
            failures.append(f"cannot resolve adjudication source for {record['record_id']}: {exc}")
            continue
        if observed != record["source_blob_oid"]:
            failures.append(
                f"adjudication source blob mismatch for {record['record_id']}: "
                f"expected {record['source_blob_oid']} observed {observed}"
            )
        source_records.append({"record_id": record["record_id"], "blob_oid": observed})

    task_records: list[dict[str, Any]] = []
    for task in ledger.get("task_specs", []):
        source = task["source"]
        repository = root / source["repository"]
        try:
            observed_oid = git_blob_oid(repository, source["commit"], source["path"])
            request = json.loads(git_text(repository, source["commit"], source["path"]))
            extraction = source["extraction"]
            content = request["messages"][extraction["message_index"]]["content"]
            prefix = content.split(extraction["end_marker"], 1)[0].rstrip() + "\n"
            payload = prefix.encode("utf-8")
        except (OSError, subprocess.CalledProcessError, KeyError, IndexError, ValueError) as exc:
            failures.append(f"cannot reconstruct task spec {task['task_spec_id']}: {exc}")
            continue
        if observed_oid != source["blob_oid"]:
            failures.append(f"task source blob mismatch: {task['task_spec_id']}")
        if sha256_bytes(payload) != task["sha256"] or len(payload) != task["size_bytes"]:
            failures.append(f"task payload mismatch: {task['task_spec_id']}")
        task_records.append(
            {"task_spec_id": task["task_spec_id"], "sha256": sha256_bytes(payload), "size_bytes": len(payload)}
        )

    evidence_records: list[dict[str, Any]] = []
    for manifest in ledger.get("evidence_manifests", []):
        repository = root / manifest["source_repository"]
        prefix = manifest.get("canonical_path_prefix", "parent_evidence/source/")
        lines: list[str] = []
        verified_items = 0
        for item in manifest.get("items", []):
            try:
                observed_oid = git_blob_oid(repository, manifest["source_commit"], item["path"])
                payload = git_bytes(repository, manifest["source_commit"], item["path"])
            except (OSError, subprocess.CalledProcessError) as exc:
                failures.append(f"cannot reconstruct evidence item {item['path']}: {exc}")
                continue
            if observed_oid != item["blob_oid"]:
                failures.append(f"evidence blob mismatch: {item['path']}")
            if sha256_bytes(payload) != item["sha256"] or len(payload) != item["size_bytes"]:
                failures.append(f"evidence payload mismatch: {item['path']}")
            canonical_path = item["path"]
            if canonical_path.startswith(prefix):
                canonical_path = canonical_path[len(prefix) :]
            lines.append(f"{canonical_path}\t{item['sha256']}\t{item['size_bytes']}")
            verified_items += 1
        canonical = ("\n".join(sorted(lines)) + "\n").encode("utf-8")
        observed_manifest_hash = sha256_bytes(canonical)
        if observed_manifest_hash != manifest["sha256"]:
            failures.append(
                f"evidence manifest mismatch {manifest['evidence_manifest_id']}: "
                f"expected {manifest['sha256']} observed {observed_manifest_hash}"
            )
        evidence_records.append(
            {
                "evidence_manifest_id": manifest["evidence_manifest_id"],
                "sha256": observed_manifest_hash,
                "verified_items": verified_items,
            }
        )

    return {
        "adjudication_source_records": source_records,
        "task_specs": task_records,
        "evidence_manifests": evidence_records,
        "failures": failures,
    }


def iter_objects(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_objects(child)


def pinned_json_paths(repository: Path, commit: str, root: str) -> list[str]:
    completed = subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "grep",
            "-l",
            "-e",
            '"terminal_candidate_id"',
            commit,
            "--",
            f":(glob){root}/**/*.json",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    prefix = f"{commit}:"
    paths = []
    for line in completed.stdout.splitlines():
        paths.append(line[len(prefix) :] if line.startswith(prefix) else line)
    return sorted(paths)


def scan_older_bank_pinned(repository: Path, commit: str, root: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    parse_failures: list[str] = []
    try:
        paths = pinned_json_paths(repository, commit, root)
    except (OSError, subprocess.CalledProcessError) as exc:
        return {
            "pinned_json_file_count": 0,
            "scored_record_occurrences": 0,
            "unique_candidate_task_groups": 0,
            "conflicts": [],
            "parse_failures": [str(exc)],
            "candidates": [],
        }
    for path in paths:
        try:
            value = json.loads(git_text(repository, commit, path))
        except (UnicodeDecodeError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
            parse_failures.append(f"{path}: {exc}")
            continue
        for obj in iter_objects(value):
            required = {"terminal_candidate_id", "terminal_passed_count", "case_count", "task"}
            if not required.issubset(obj):
                continue
            candidate = str(obj["terminal_candidate_id"])
            if len(candidate) != SHA256_LENGTH or any(char not in HEX for char in candidate):
                continue
            try:
                passed = int(obj["terminal_passed_count"])
                total = int(obj["case_count"])
            except (TypeError, ValueError) as exc:
                parse_failures.append(f"{path}: invalid terminal score: {exc}")
                continue
            rows.append(
                {
                    "candidate_hash": candidate,
                    "task_id": str(obj["task"]),
                    "passed": passed,
                    "total": total,
                    "source_path": path,
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
        "pinned_json_file_count": len(paths),
        "scored_record_occurrences": len(rows),
        "unique_candidate_task_groups": len(groups),
        "conflicts": conflicts,
        "parse_failures": parse_failures,
        "candidates": candidates,
    }


def build_receipt(ledger_path: Path) -> dict[str, Any]:
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger_result = check_ledger(ledger)
    custody = verify_identity_custody(ledger)
    bank = ledger["older_bank_scan"]
    repository = Path(bank["repository"])
    bank_result = scan_older_bank_pinned(repository, bank["commit"], bank["root"])
    failures = list(ledger_result["failures"]) + list(custody["failures"])
    if bank_result["conflicts"]:
        failures.append(f"older bank has {len(bank_result['conflicts'])} conflicting candidate scores")
    if bank_result["parse_failures"]:
        failures.append(f"older bank has {len(bank_result['parse_failures'])} pinned JSON parse failures")
    try:
        observed_head = git_head(repository)
        worktree_status = git_status(repository)
    except (OSError, subprocess.CalledProcessError) as exc:
        observed_head = None
        worktree_status = None
        failures.append(f"cannot inspect older bank repository: {exc}")
    return {
        "schema_version": "artifact-adjudication-consistency-receipt-v1",
        "checker_path": "tools/check_artifact_adjudications_v1.py",
        "checker_sha256": sha256_file(Path(__file__).resolve()),
        "ledger_path": str(ledger_path).replace("\\", "/"),
        "ledger_sha256": sha256_file(ledger_path),
        "ledger_result": ledger_result,
        "identity_custody": custody,
        "older_bank": {
            "repository": str(repository),
            "scanned_commit": bank["commit"],
            "source_mode": "pinned_git_objects",
            "working_tree_head_observation": observed_head,
            "working_tree_clean_observation": worktree_status == "" if worktree_status is not None else None,
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
