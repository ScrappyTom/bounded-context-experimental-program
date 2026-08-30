from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e97_records_bounded_applied_causal_history_without_utility_claim() -> None:
    value = json.loads(
        (ROOT / "E97_TRELLIS_CANDIDATE_EFFECT_LIFECYCLE_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["result_commit"] == (
        "15b7f57e1042194d3cdf859b2650a213c8a93a77"
    )
    assert value["stage_type"] == "offline_apparatus_qualification"
    assert value["bounded_projection"]["offline_prompt_tokens"] == 19_116
    assert value["bounded_projection"]["headroom_tokens"] == 1_876
    assert value["bounded_projection"]["pending_exact_result_id"] == "RESULT-018"
    assert value["bounded_projection"]["exact_effect_hashes_preserved"] is True
    assert value["bounded_projection"]["semantic_uptake_inferred"] is False
    assert value["qualification"]["focused_tests_passed"] == 5
    assert value["qualification"]["full_repository_tests_passed"] == 303
    assert value["qualification"]["gpu_provider_calls"] == 0
    assert value["live_actor_utility"] == "untested"
    assert value["automatic_successor"] is False


def test_e97_remains_qualified_infrastructure_under_selected_repaired_scout() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(
            encoding="utf-8"
        )
    )
    lifecycle = contract["active_host_runtime_refactor"]["candidate_causal_history"]
    assert lifecycle["stage"] == "E97"
    assert lifecycle["status"] == "offline_future_path_qualified"
    boundary = contract["current_program_boundary"]
    assert boundary["stage"] == "E103"
    assert boundary["gpu_operation_selected"] is False
    assert boundary["gpu_operation_authorized"] is False
    assert boundary["next_document"] == (
        "NEXT_OFFLINE_VERIFICATION_RESIDENCY_RECONCILIATION.md"
    )
    result = (ROOT / "E97_TRELLIS_CANDIDATE_EFFECT_LIFECYCLE_RESULT.md").read_text(
        encoding="utf-8"
    )
    assert "newly emitted complete-document\nmutation and its pending effect" in result
    assert "does not infer semantic uptake" in result
