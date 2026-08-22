"""Verify the next-route overlap audit against pinned Git objects."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


def git_output(repository: Path, *args: str, text: bool = False) -> bytes | str:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        capture_output=True,
        text=text,
    ).stdout


def verify(lock: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    repository = Path(lock["donor_repository"])
    commit = lock["donor_commit"]
    try:
        resolved_commit = str(git_output(repository, "rev-parse", f"{commit}^{{commit}}", text=True)).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        return {"passed": False, "failures": [f"cannot resolve donor commit: {exc}"], "sources": []}
    if resolved_commit != commit:
        failures.append(f"donor commit mismatch: expected {commit}, observed {resolved_commit}")

    observed: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for source in lock.get("sources", []):
        path = source["path"]
        if path in seen_paths:
            failures.append(f"duplicate source path: {path}")
        seen_paths.add(path)
        try:
            blob_oid = str(git_output(repository, "rev-parse", f"{commit}:{path}", text=True)).strip()
            payload = bytes(git_output(repository, "show", f"{commit}:{path}"))
        except (OSError, subprocess.CalledProcessError) as exc:
            failures.append(f"cannot read pinned source {path}: {exc}")
            continue
        sha256 = hashlib.sha256(payload).hexdigest()
        size_bytes = len(payload)
        if blob_oid != source["blob_oid"]:
            failures.append(f"blob mismatch for {path}")
        if sha256 != source["sha256"]:
            failures.append(f"SHA-256 mismatch for {path}")
        if size_bytes != source["size_bytes"]:
            failures.append(f"size mismatch for {path}")
        observed.append(
            {
                "category": source["category"],
                "path": path,
                "blob_oid": blob_oid,
                "sha256": sha256,
                "size_bytes": size_bytes,
            }
        )

    return {
        "passed": not failures,
        "failures": failures,
        "donor_commit": resolved_commit,
        "source_mode": "pinned_git_objects",
        "source_count": len(observed),
        "total_size_bytes": sum(item["size_bytes"] for item in observed),
        "category_counts": dict(sorted(Counter(item["category"] for item in observed).items())),
        "sources": observed,
        "gpu_calls": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    result = verify(lock)
    receipt = {
        "schema_version": "next-route-prior-evidence-receipt-v0",
        "lock_path": str(args.lock).replace("\\", "/"),
        "lock_sha256": hashlib.sha256(args.lock.read_bytes()).hexdigest(),
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
