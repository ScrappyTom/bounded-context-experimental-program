from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "c443f39fca414303c6f3b4efdfa94ba0b06a37b7"


def test_aggregate_records_zero_call_event_trigger_qualification() -> None:
    aggregate = json.loads(
        (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
    )
    stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S72")
    assert stage["stage_type"] == "eligibility"
    assert stage["model_calls"] == 0
    assert stage["serialized_tokens"] == 0
    assert stage["sources"][0]["result_commit"] == RESULT_COMMIT


def test_machine_route_records_event_not_count_activation() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    route = contract["active_system_route"]
    result = route["keystone_event_triggered_continuation_qualification"]
    assert result["result_commit"] == RESULT_COMMIT
    assert result["provider_calls"] == 0
    assert result["count_based_activation_retired"] is True
    assert result["activation_unit"] == "exact_lifecycle_event_sequence"
    assert result["first_fit_selected_result_ids"] == ["RESULT-001"]
    assert result["ordinary_pending_prompt_tokens"] == 22_267
    assert result["relieved_pending_prompt_tokens"] == 20_648
    assert result["provider_free_runner_qualification_passed"] is True
    assert result["behavioral_activation_measured"] is False
    assert result["authorized"] is False


def test_docs_keep_event_trigger_inside_the_whole_lifecycle() -> None:
    stage = (ROOT / "E80_KEYSTONE_EVENT_TRIGGERED_CONTINUATION_PREFLIGHT.md").read_text(
        encoding="utf-8"
    )
    plan = (
        ROOT / "NEXT_SYSTEM_INTERACTION_BOUNDED_CAUSAL_VERIFICATION_TRANSFER.md"
    ).read_text(encoding="utf-8")
    assert "ten-source/ten-domain gate therefore mixed" in stage
    assert "It is retired rather than lowered" in stage
    assert "later exact source or reopen observation acquired" in stage
    assert "Both branch prompts deliver that pending observation" in plan
    assert "No GPU run is authorized" in plan
