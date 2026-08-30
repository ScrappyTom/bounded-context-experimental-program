from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_e106_checkpoint_and_e107_continuation_are_recorded() -> None:
    contract = load(ROOT / "SYSTEM_INTERACTION_EXPLORATION.json")
    route = contract["active_host_runtime_refactor"]
    checkpoint = route["e106_clean_whole_lifecycle_checkpoint"]
    continuation = route["e107_clean_whole_lifecycle_continuation_stage0"]

    assert checkpoint["stage"] == "E106"
    assert checkpoint["actor_calls"] == 12
    assert checkpoint["accepted_read_batch_actions"] == 12
    assert checkpoint["candidate_mutations"] == 0
    assert checkpoint["exact_reopens"] == 0
    assert checkpoint["pending_result_id"] == "RESULT-012"
    assert checkpoint["scaffold_selection_loss_observed"] is True
    assert continuation["stage"] == "E107"
    assert continuation["policy_change"] is False
    assert continuation["parent_result_commit"] == checkpoint["apparatus_commit"]
    assert continuation["provider_free_final_readiness"] == "ready"
    assert continuation["live_authorized"] is False


def test_current_boundary_selects_only_unauthorized_exact_continuation() -> None:
    contract = load(ROOT / "SYSTEM_INTERACTION_EXPLORATION.json")
    route = contract["active_host_runtime_refactor"]
    boundary = contract["current_program_boundary"]

    assert boundary["stage"] == "E107"
    assert boundary["result_commit"] == (
        "d62a7594e4703453bd990e1e7df06daf3422c04c"
    )
    assert boundary["next_document"] == (
        "E107_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CONTINUATION_STAGE0.md"
    )
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False
    assert route["next_operation"] == (
        "trellis_clean_whole_lifecycle_exact_checkpoint_continuation"
    )
    assert route["automatic_continuation"] is False


def test_narrative_preserves_checkpoint_limits() -> None:
    result = (ROOT / "E106_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CHECKPOINT_RESULT.md").read_text(
        encoding="utf-8"
    )
    stage0 = (ROOT / "E107_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CONTINUATION_STAGE0.md").read_text(
        encoding="utf-8"
    )

    assert "not a no-progress loop" in result
    assert "same-source replacement" in result
    assert "No further continuation" not in result
    assert "12 additional actor calls" in stage0
    assert "zero retries" in stage0.lower()
    assert "not GPU-authorized" in stage0
