from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "eacafe5e4b46fcb3ffbadd90e9823d16796f6f4e"


def test_aggregate_records_nonqualifying_live_screen() -> None:
    aggregate = json.loads(
        (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
    )
    stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S71")
    assert stage["stage_type"] == "measured"
    assert stage["model_calls"] == 9
    assert stage["serialized_tokens"] == 102_009
    assert stage["sources"][0]["result_commit"] == RESULT_COMMIT


def test_machine_route_records_pressure_without_interaction_qualification() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    route = contract["active_system_route"]
    result = route["keystone_pressure_screen_result"]
    assert result["result_commit"] == RESULT_COMMIT
    assert result["provider_calls"] == 9
    assert result["delivered_source_count"] == 8
    assert result["delivered_evidence_domain_count"] == 8
    assert result["ordinary_prospective_prompt_tokens"] == 22_267
    assert result["first_fit_relief_prompt_tokens"] == 20_648
    assert result["interaction_trigger_qualified"] is False
    assert result["measured_continuation_ran"] is False
    qualification = route["keystone_event_triggered_continuation_qualification"]
    assert qualification["result_commit"] == "c443f39fca414303c6f3b4efdfa94ba0b06a37b7"
    assert qualification["provider_free_runner_qualification_passed"] is True
    operation = route["next_live_operation"]
    assert operation["kind"] == "none_selected"
    assert operation["authorized"] is False
    assert route["gpu_authorized"] is False


def test_docs_preserve_whole_interaction_and_claim_limit() -> None:
    result = (ROOT / "E79_KEYSTONE_PRESSURE_SCREEN_RESULT.md").read_text(
        encoding="utf-8"
    )
    reconciliation = (ROOT / "PROGRAM_RECONCILIATION.md").read_text(
        encoding="utf-8"
    )
    exploration = (ROOT / "SYSTEM_INTERACTION_EXPLORATION.md").read_text(
        encoding="utf-8"
    )
    assert "activation-geometry" in result
    assert "No bounded-causal behavior" in reconciliation
    assert "common pre-treatment infrastructure" in reconciliation
    assert "whole system's activation semantics" in exploration
    assert "no GPU operation is authorized" in result
