from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e96_records_joint_signal_and_terminal_effect_lifecycle() -> None:
    value = json.loads(
        (ROOT / "E96_TRELLIS_REFACTORED_INTERACTION_CONTINUATION_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["freeze_commit"] == "18e17806e906d57943ab9b7461def708084d69b1"
    assert value["result_commit"] == (
        "ef90d6d7f80b838fd03fb54e57d61f20f98a00d0"
    )
    assert value["actual_additional"]["provider_calls"] == 23
    assert value["actual_additional"]["serialized_tokens"] == 383176
    assert value["V0"]["catalog_replay_actions"] == 12
    assert value["V0"]["candidate_transitions"] == 0
    assert value["V1"]["candidate_transitions"] == 6
    assert value["V1"]["closure_readiness"] == "not_ready"
    assert value["V1"]["next_prompt_tokens"] == 21041
    assert value["V1"]["positive_relief_candidates"] == 0
    assert value["causal_unit"] == "whole_evolving_configuration"
    assert value["automatic_gpu_successor"] is False


def test_selected_offline_work_completed_without_another_continuation() -> None:
    plan = (ROOT / "NEXT_OFFLINE_CANDIDATE_EFFECT_LIFECYCLE.md").read_text(
        encoding="utf-8"
    )
    assert "no GPU/provider call occurred" in plan
    assert "construction-to-verification interaction" in plan
    assert "pending effect remains exact and non-droppable" in plan
    assert "Do not continue E96" in plan
    assert "completed at E97" in plan
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    lifecycle = contract["active_host_runtime_refactor"]["candidate_causal_history"]
    assert lifecycle["stage"] == "E97"
    assert lifecycle["status"] == "offline_future_path_qualified"
    boundary = contract["current_program_boundary"]
    assert boundary["stage"] == "E105"
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False
