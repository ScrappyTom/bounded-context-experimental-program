from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


def resolve_repo(repository: str) -> Path:
    name = repository.split("/", 1)[1]
    path = WORKSPACE / name
    if not (path / ".git").exists():
        raise FileNotFoundError(f"local repository not found: {path}")
    return path


def main() -> int:
    aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))
    bindings: set[tuple[str, str]] = set()
    for stage in aggregate["stages"]:
        for source in stage["sources"]:
            if source.get("count_as_experiment_commit") is True:
                bindings.add((source["repository"], source["result_commit"]))

    failures: list[str] = []
    for repository, commit in sorted(bindings):
        try:
            repo = resolve_repo(repository)
            subprocess.run(
                ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
                cwd=repo,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )
        except (FileNotFoundError, subprocess.CalledProcessError) as exc:
            failures.append(f"{repository}@{commit}: {exc}")

    receipt = {
        "schema_version": "program-stage-commit-binding-receipt-v1",
        "passed": not failures,
        "failures": failures,
        "verified_unique_commit_bindings": len(bindings) - len(failures),
        "declared_unique_commit_bindings": len(bindings),
        "verification_method": "git cat-file -e <commit>^{commit} in named local repository",
    }
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
