from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "381e44c9eb3c3c10a793903155c2482f5f8c570f"


def test_e93_stage0_is_provider_free_and_live_unauthorized() -> None:
    stage = json.loads(
        (ROOT / "E93_TRELLIS_REFACTORED_INTERACTION_STAGE0.json").read_text(
            encoding="utf-8"
        )
    )
    assert stage["apparatus_commit"] == COMMIT
    assert stage["status"] == "provider_free_qualified_live_unauthorized"
    assert stage["model_calls"] == 0
    assert stage["regression_tests_passed"] == 290
    assert stage["live_authorization_limits"] == {
        "maximum_actor_calls": 24,
        "maximum_maintenance_calls": 12,
        "maximum_provider_calls": 36,
        "maximum_serialized_tokens": 900000,
        "attempts_per_call": 1,
        "retries": 0,
    }


def test_e93_keeps_host_and_semantic_layer_ownership_separate() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    host = contract["active_host_runtime_refactor"]
    selected = contract["selected_whole_system_interaction"]
    assert host["gpu_operation_selected"] is False
    assert selected["configurations"] == [
        "V0_EXACT_ARTIFACT",
        "V1_TEMPORARY_PROVENANCE_SCAFFOLD",
    ]
    assert "deterministic_first_fit_relief" in selected["common_functions"]
    assert (
        "charged_fallible_anchored_maintenance_during_construction"
        in selected["treatment_only_functions"]
    )
    assert selected["live_authorized"] is False
