"""Verify the dedicated-maintenance eligibility artifacts and pinned donor."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def git_bytes(repository: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repository), *args], check=True, capture_output=True).stdout


def git_text(repository: Path, *args: str) -> str:
    return git_bytes(repository, *args).decode("utf-8").strip()


def verify(lock: dict[str, Any], audit: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    repository = Path(lock["donor_repository"])
    commit = lock["donor_commit"]
    try:
        resolved = git_text(repository, "rev-parse", f"{commit}^{{commit}}")
    except (OSError, subprocess.CalledProcessError) as exc:
        return {"passed": False, "failures": [f"cannot resolve donor: {exc}"]}
    if resolved != commit:
        failures.append("donor commit mismatch")

    observed_sources: list[dict[str, Any]] = []
    for source in lock["sources"]:
        try:
            blob = git_text(repository, "rev-parse", f"{commit}:{source['path']}")
            payload = git_bytes(repository, "show", f"{commit}:{source['path']}")
        except (OSError, subprocess.CalledProcessError) as exc:
            failures.append(f"cannot read {source['path']}: {exc}")
            continue
        sha256 = hashlib.sha256(payload).hexdigest()
        if blob != source["blob_oid"]:
            failures.append(f"blob mismatch: {source['path']}")
        if sha256 != source["sha256"]:
            failures.append(f"SHA-256 mismatch: {source['path']}")
        if len(payload) != source["size_bytes"]:
            failures.append(f"size mismatch: {source['path']}")
        observed_sources.append({"path": source["path"], "blob_oid": blob, "sha256": sha256, "size_bytes": len(payload)})

    if audit.get("donor_commit") != commit:
        failures.append("audit donor commit mismatch")
    if audit.get("chat_completions_called") is not False:
        failures.append("eligibility audit must make zero chat completions")
    if audit.get("endpoint_calls", {}).get("chat_completions") != 0:
        failures.append("endpoint receipt reports chat completions")
    if audit.get("maintenance_reserve_tokens") != 512 or audit.get("ordinary_reserve_tokens") != 4096:
        failures.append("reserve mismatch")
    if audit.get("eligible") is not True:
        failures.append("audit is not eligible")

    expected_prefixes = {
        "s42-s1": (
            "evidence/parent/s42-s1/data/s42-s1/turns/turn-012/request.json",
            "evidence/parent/s42-s1/data/s42-s1/turns/turn-012/assistant-message.json",
            "evidence/parent/s42-s1/data/s42-s1/turns/turn-012/result-message.json",
        ),
        "s314159-s1": (
            "evidence/parent/s314159-s1/data/s314159-s1/turns/turn-010/request.json",
            "evidence/parent/s314159-s1/data/s314159-s1/turns/turn-010/assistant-message.json",
            "evidence/parent/s314159-s1/data/s314159-s1/turns/turn-010/result-message.json",
        ),
    }
    for cell in audit.get("cells", []):
        cell_id = cell["cell"]
        if cell_id not in expected_prefixes:
            failures.append(f"unexpected cell: {cell_id}")
            continue
        request_path = ROOT / cell["manager_request"]["path"]
        if not request_path.is_file():
            failures.append(f"missing manager request: {request_path}")
            continue
        raw = request_path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != cell["manager_request"]["sha256"]:
            failures.append(f"manager request hash mismatch: {cell_id}")
        if len(raw) != cell["manager_request"]["size_bytes"]:
            failures.append(f"manager request size mismatch: {cell_id}")
        request = json.loads(raw)
        donor_request_path, assistant_path, pending_path = expected_prefixes[cell_id]
        donor_request = json.loads(git_bytes(repository, "show", f"{commit}:{donor_request_path}"))
        assistant = json.loads(git_bytes(repository, "show", f"{commit}:{assistant_path}"))
        pending = json.loads(git_bytes(repository, "show", f"{commit}:{pending_path}"))
        if request["messages"][:-2] != donor_request["messages"]:
            failures.append(f"historical manager prefix differs: {cell_id}")
        if request["messages"][-2] != assistant:
            failures.append(f"accepted action differs: {cell_id}")
        maintenance = request["messages"][-1]
        if maintenance.get("role") != "user" or "DEDICATED EXACT-WORKSPACE MAINTENANCE MODE" not in maintenance.get("content", ""):
            failures.append(f"maintenance message missing: {cell_id}")
        if pending["content"] in maintenance.get("content", ""):
            failures.append(f"pending exact result body leaked into manager metadata: {cell_id}")
        schema = request.get("response_format", {}).get("json_schema", {}).get("schema", {})
        if set(schema.get("properties", {})) != {"release_result_ids"}:
            failures.append(f"manager schema exposes non-selection output: {cell_id}")
        if request.get("max_tokens") != 512:
            failures.append(f"manager response allowance mismatch: {cell_id}")
        if not cell["manager_request"]["fits"] or cell["manager_request"]["headroom_after_reserve"] < 0:
            failures.append(f"manager does not fit: {cell_id}")
        if cell["feasible_single_choice_count"] < 2 or not cell["selection_is_nontrivial"]:
            failures.append(f"selection is mechanically trivial: {cell_id}")
        if not cell["incumbent"]["decision_preserved_in_measured_run"] or not cell["incumbent"]["result_absorbed_in_measured_run"]:
            failures.append(f"incumbent is not qualified: {cell_id}")

    return {
        "passed": not failures,
        "failures": failures,
        "donor_commit": resolved,
        "source_mode": "pinned_git_objects",
        "source_count": len(observed_sources),
        "source_size_bytes": sum(item["size_bytes"] for item in observed_sources),
        "manager_request_count": len(audit.get("cells", [])),
        "manager_prompt_tokens": {cell["cell"]: cell["manager_request"]["prompt_tokens"] for cell in audit.get("cells", [])},
        "manager_headroom": {cell["cell"]: cell["manager_request"]["headroom_after_reserve"] for cell in audit.get("cells", [])},
        "feasible_single_choices": {cell["cell"]: cell["feasible_single_choice_count"] for cell in audit.get("cells", [])},
        "chat_completions": 0,
        "gpu_calls": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, default=ROOT / "audits" / "DEDICATED_MAINTENANCE_SOURCE_LOCK.json")
    parser.add_argument("--audit", type=Path, default=ROOT / "audits" / "DEDICATED_MAINTENANCE_ELIGIBILITY.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    result = verify(lock, audit)
    receipt = {
        "schema_version": "dedicated-maintenance-eligibility-receipt-v0",
        "lock_sha256": hashlib.sha256(args.lock.read_bytes()).hexdigest(),
        "audit_sha256": hashlib.sha256(args.audit.read_bytes()).hexdigest(),
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
