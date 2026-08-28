from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPARATUS = Path(r"E:\qwen38-artifact-coupled-integration-scout-v0")
COMMIT = "cc78d3b4c7162c6d3615696defd68e9790ee04ea"


def test_e85_records_provider_free_success_and_exact_asset_blocker() -> None:
    result = json.loads(
        (ROOT / "E85_HOST_LIVE_HARDENING_RESULT.json").read_text(encoding="utf-8")
    )
    assert result["stage_type"] == "apparatus"
    assert result["apparatus_commit"] == COMMIT
    assert result["model_calls"] == 0
    assert result["gpu_operation_selected"] is False
    assert result["verification"]["adversarial_tests_passed"] == 11
    assert result["verification"]["full_compatible_regression_passed"] == 277
    assert result["exact_asset_blocker"]["exists"] is False


def test_e85_apparatus_commit_resolves_and_contains_hardening_result() -> None:
    resolved = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=APPARATUS,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    assert resolved == COMMIT
    tracked = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", COMMIT],
        cwd=APPARATUS,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    assert "host_refactor/HOST_LIVE_HARDENING_RESULT.md" in tracked
    assert "host_refactor/binding.py" in tracked
    assert "tests/test_host_refactor_live_hardening.py" in tracked


def test_governing_documents_do_not_promote_exact_live_or_gpu_readiness() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    refactor = contract["active_host_runtime_refactor"]
    narrative = (ROOT / "E85_HOST_LIVE_HARDENING_RESULT.md").read_text(
        encoding="utf-8"
    )
    assert refactor["live_hardening_commit"] == COMMIT
    assert refactor["exact_tokenizer_projection_present"] is False
    assert refactor["exact_live_qualification"] is False
    assert refactor["gpu_operation_selected"] is False
    assert "not yet exactly live-" in narrative
    assert "qualified" in narrative
    assert "does not authorize GPU use" in narrative
