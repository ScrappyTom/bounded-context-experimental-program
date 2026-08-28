from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "133bd274e930806634006ed7644b25c4b553dab8"


def test_aggregate_records_measured_nonactivation() -> None:
    aggregate = json.loads(
        (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
    )
    stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S73")
    assert stage["stage_type"] == "measured"
    assert stage["model_calls"] == 18
    assert stage["serialized_tokens"] == 198_745
    assert stage["sources"][0]["result_commit"] == RESULT_COMMIT


def test_machine_route_records_valid_closed_nonactivation() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    route = contract["active_system_route"]
    result = route["keystone_event_triggered_continuation_result"]
    assert result["result_commit"] == RESULT_COMMIT
    assert result["run_valid"] is True
    assert result["new_provider_calls"] == 18
    assert result["common_actor_calls"] == 8
    assert result["common_maintenance_calls"] == 10
    assert result["whole_pre_treatment_calls"] == 27
    assert result["whole_pre_treatment_serialized_tokens"] == 300_754
    assert result["distinct_sources_observed"] == 14
    assert result["maintenance_claims_proposed"] == 48
    assert result["maintenance_claims_admitted"] == 8
    assert result["maintenance_relationship_claims_admitted"] == 0
    assert result["candidate_changed"] is False
    assert result["causal_trigger_observed"] is False
    assert result["treatment_dependent_decisions"] == 0
    assert result["keystone_disposition"] == "non_diagnostic_closed"
    assert route["next_live_operation"]["kind"] == "none_selected"
    assert route["gpu_authorized"] is False


def test_docs_capture_interaction_not_only_trigger_absence() -> None:
    result = (ROOT / "E81_KEYSTONE_EVENT_TRIGGERED_CONTINUATION_RESULT.md").read_text(
        encoding="utf-8"
    )
    reconciliation = (ROOT / "PROGRAM_RECONCILIATION.md").read_text(
        encoding="utf-8"
    )
    roadmap = (ROOT / "STRUCTURED_EXPLORATION_ROADMAP.md").read_text(
        encoding="utf-8"
    )
    assert "Eight entered the register" in result
    assert "carrier-selected" in result
    assert "evidence-to-work conversion" in reconciliation
    assert "not a failed isolated component" in roadmap
    assert "No successor research GPU operation" in result
