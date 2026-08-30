from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e99_records_live_phase_entry_and_apparatus_censor() -> None:
    value = json.loads(
        (ROOT / "E99_TRELLIS_E97_VERIFICATION_LIFECYCLE_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["corrected_result_commit"] == (
        "554bf496f0ea6a12881d0ab730e800d045cb36b2"
    )
    assert value["actual_additional"]["actor_calls"] == 4
    assert value["actual_additional"]["serialized_tokens"] == 82_646
    assert value["behavior"]["pending_result_delivered"] is True
    assert value["behavior"]["verification_phase_entered"] is True
    assert value["behavior"]["current_check_run"] is False
    assert value["apparatus_censor"][
        "verification_actions_allowed_by_response_schema"
    ] is True
    assert value["apparatus_censor"]["readable_verification_contract_present"] is False
    assert value["terminal"]["prospective_prompt_tokens"] == 23_811
    assert value["candidate"]["closure_readiness"] == "not_ready"


def test_e100_freezes_only_the_repaired_route_without_live_authorization() -> None:
    value = json.loads(
        (ROOT / "E100_TRELLIS_REPAIRED_VERIFICATION_LIFECYCLE_STAGE0.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["apparatus_commit"] == (
        "76091fc5885d25d31becccbb0edb8fc6a3681bac"
    )
    assert value["provider_calls"] == 0
    assert value["repairs"]["readable_phase_contract_aligned_with_response_schema"] is True
    assert value["repairs"]["rejected_response_raw_custody_preserved"] is True
    assert value["repairs"]["rejected_response_prompt_receipt_bounded"] is True
    assert value["repairs"]["semantic_summary_or_retry_added"] is False
    assert value["sealed_failure_replay"]["prospective_prompt_tokens"] == 16_335
    assert value["sealed_failure_replay"]["raw_rejected_bodies_model_resident"] is False
    assert value["provider_free_lifecycle"]["terminal"] == "completed"
    assert value["qualification"]["full_repository_tests_passed"] == 315
    assert value["live_authorized"] is False


def test_current_boundary_preserves_e100_and_e99_as_history() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    boundary = contract["current_program_boundary"]
    assert boundary["stage"] == "E107"
    assert boundary["result_document"] == (
        "E107_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CONTINUATION_STAGE0.md"
    )
    assert boundary["live_predecessor_result"] == (
        "E106_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CHECKPOINT_RESULT.md"
    )
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False

    live = contract["active_host_runtime_refactor"]["e99_live_lifecycle_result"]
    assert live["sealed_route_resumed"] is False
    selected = contract["active_host_runtime_refactor"]["selected_lifecycle_scout"]
    assert selected["stage"] == "E102"
    assert selected["run_id"] == (
        "2026-08-30-trellis-e99-verification-lifecycle-continuation-v1"
    )
