from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPARATUS_COMMIT = "fbc1db052051b23cfb8667780eab0a9939dee11a"


def test_e87_binds_exact_apparatus_and_one_call_limits() -> None:
    stage = json.loads(
        (ROOT / "E87_HOST_LIVE_SMOKE_STAGE0.json").read_text(encoding="utf-8")
    )
    assert stage["apparatus_commit"] == APPARATUS_COMMIT
    assert stage["maximum_model_calls"] == 1
    assert stage["maximum_serialized_tokens"] == 30_000
    assert stage["attempts_per_call"] == 1
    assert stage["retries"] == 0
    assert stage["parent_boundary"]["pending_result_id"] == "RESULT-007"


def test_e87_remains_nonbehavioral_and_authorization_gated() -> None:
    stage = json.loads(
        (ROOT / "E87_HOST_LIVE_SMOKE_STAGE0.json").read_text(encoding="utf-8")
    )
    assert stage["status"] == "completed_by_e88_pre_provider_environment_block"
    assert "not_behavioral_or_utility_evidence" in stage["claim_limit"]
    system = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    host = system["active_host_runtime_refactor"]
    assert host["live_smoke_commit"] == "3afd9e269abb437512ea961772b43f4a12ea0f30"
    assert host["gpu_operation_selected"] is True
    assert host["gpu_operation_authorized"] is False
    assert host["automatic_continuation"] is False
