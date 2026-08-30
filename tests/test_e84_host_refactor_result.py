from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e84_is_an_offline_apparatus_fact_with_no_gpu_claim() -> None:
    result = json.loads(
        (ROOT / "E84_HOST_RUNTIME_REFACTOR_RESULT.json").read_text(encoding="utf-8")
    )
    assert result["stage_type"] == "apparatus"
    assert result["disposition"] == "offline_host_refactor_qualified"
    assert result["model_calls"] == 0
    assert result["serialized_tokens"] == 0
    assert result["gpu_operation_selected"] is False
    assert result["verification"]["full_tests_passed"] == 266
    assert result["e83_replay"]["delivered_source_count"] == 6
    assert result["e83_replay"]["pending_source_ids"] == ["COMMS", "TRANSIT"]
    assert result["e83_replay"]["synthetic_next_invocation_delivered_source_count"] == 8


def test_governing_contract_records_refactor_and_keeps_interaction_unit() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    refactor = contract["active_host_runtime_refactor"]
    assert contract["unit_of_analysis"] == "whole_configuration_trajectory"
    assert refactor["status"] == "one_call_live_qualified_checkpoint_pause"
    assert refactor["verification"]["e84_full_tests_passed"] == 266
    assert refactor["verification"]["e85_full_compatible_regression_passed"] == 277
    assert refactor["exact_provider_free_qualification"] is True
    assert refactor["live_gpu_provider_qualification"] is True
    assert refactor["gpu_operation_selected"] is True
    assert refactor["gpu_operation_authorized"] is False
    assert refactor["next_operation"] == (
        "trellis_clean_whole_lifecycle_exact_checkpoint_continuation"
    )


def test_narrative_preserves_claim_limits_and_host_model_investigator_split() -> None:
    result = (ROOT / "E84_HOST_RUNTIME_REFACTOR_RESULT.md").read_text(encoding="utf-8")
    handoff = (ROOT / "HOST_RUNTIME_REFACTOR_HANDOFF.md").read_text(encoding="utf-8")
    assert "apparatus fact" in result
    assert "no behavioral" in result.lower()
    assert "No GPU operation is selected" in result
    assert "Host owns only mechanical execution" in handoff
    assert "Model owns task behavior" in handoff
    assert "Investigator owns checkpoint judgment" in handoff
