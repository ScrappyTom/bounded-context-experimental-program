from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPARATUS = Path(r"E:\qwen38-artifact-coupled-integration-scout-v0")
COMMIT = "a7c7686977661dcd7adebc1da78a78aa2b423ff5"


def test_e86_records_exact_provider_free_qualification() -> None:
    result = json.loads(
        (ROOT / "E86_HOST_LOCKED_ASSET_RESTORATION_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert result["apparatus_commit"] == COMMIT
    assert result["locked_full_model"]["verified"] is True
    assert result["verification"]["direct_e83_ordinary_prompt_tokens"] == 21_401
    assert result["verification"]["direct_e83_relief_prompt_tokens"] == 18_785
    assert result["verification"]["full_exact_regression_passed"] == 280
    assert result["model_calls"] == 0


def test_e86_apparatus_commit_resolves_and_contains_restoration_result() -> None:
    subprocess.run(
        ["git", "cat-file", "-e", f"{COMMIT}^{{commit}}"],
        cwd=APPARATUS,
        check=True,
        capture_output=True,
        text=True,
    )
    tracked = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", COMMIT],
        cwd=APPARATUS,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    assert "host_refactor/HOST_ASSET_RESTORATION_RESULT.md" in tracked
    assert "tests/test_offline_tokenizer_asset_resolution.py" in tracked


def test_governing_contract_marks_only_provider_free_exact_qualification() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    refactor = contract["active_host_runtime_refactor"]
    assert refactor["asset_restoration_commit"] == COMMIT
    assert refactor["exact_tokenizer_projection_present"] is False
    assert refactor["exact_locked_full_model_present"] is True
    assert refactor["exact_provider_free_qualification"] is True
    assert refactor["live_gpu_provider_qualification"] is True
    assert refactor["gpu_operation_selected"] is True
    assert refactor["gpu_operation_authorized"] is False
