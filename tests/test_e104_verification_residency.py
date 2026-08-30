from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e104_records_exact_check_turnover_without_live_claim() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    result = contract["active_host_runtime_refactor"][
        "e104_verification_residency_reconciliation"
    ]
    boundary = contract["current_program_boundary"]

    assert result["result_commit"] == (
        "b548a4d246e3261da69d913a00c73c5171eefc78"
    )
    assert result["gpu_model_calls"] == 0
    assert result["externalized_check_result_ids"] == ["RESULT-021", "RESULT-024"]
    assert result["pending_exact_result_id"] == "RESULT-026"
    assert result["prospective_prompt_tokens"] == 20_548
    assert result["prospective_offline_headroom_tokens"] == 444
    assert result["prospective_conservative_headroom_tokens"] == 427
    assert result["exact_reopen_preserved"] is True
    assert result["provider_free_complete_lifecycle_qualified"] is True
    assert result["donor_checkpoint_eligible"] is False
    assert result["live_behavioral_utility_measured"] is False

    assert boundary["stage"] == "E105"
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False
    assert boundary["next_document"] == "E105_TRELLIS_CLEAN_WHOLE_LIFECYCLE_STAGE0.md"


def test_e104_narrative_preserves_scope_and_donor_stop_rule() -> None:
    narrative = (ROOT / "E104_VERIFICATION_RESIDENCY_RECONCILIATION.md").read_text(
        encoding="utf-8"
    )
    assert "remains an exact pending body" in narrative
    assert "No checkpoint was invented" in narrative
    assert "This qualifies mechanics, not live Qwen" in narrative
    assert "No GPU run is selected by E104" in narrative
