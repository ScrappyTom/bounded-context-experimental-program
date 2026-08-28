from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "2e276cb69106de263516aa4828d30cec0e25e365"


def test_aggregate_records_zero_call_cross_run_audit() -> None:
    aggregate = json.loads(
        (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
    )
    stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S69")
    assert stage["stage_type"] == "reconciliation"
    assert stage["model_calls"] == 0
    assert stage["serialized_tokens"] == 0
    assert stage["sources"][0]["result_commit"] == RESULT_COMMIT


def test_machine_route_preserves_claim_limits_and_records_stage0_successor() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    route = contract["active_system_route"]
    audit = route["cross_run_causal_continuity_audit"]
    assert audit["result_commit"] == RESULT_COMMIT
    assert audit["provider_calls"] == 0
    assert audit["actor_calls_reconstructed"] == 157
    assert audit["rejected_mutation_recurrence_worlds"] == [
        "architecture_decision",
        "orchard",
    ]
    assert audit["maximum_frame_tokens"] == 1297
    assert audit["bound_repair_action_tokens"] == 461
    assert audit["behavioral_utility_measured"] is False
    next_operation = route["next_live_operation"]
    assert next_operation["kind"] == "none_selected"
    assert next_operation["status"] == "keystone_closed_no_research_successor_authorized"
    assert next_operation["fresh_task_selected"] is False
    assert next_operation["measured_runner_frozen"] is False
    assert next_operation["authorized"] is False
    assert route["gpu_authorized"] is False


def test_docs_keep_whole_system_scope_and_no_gpu_authority() -> None:
    result = (ROOT / "E77_CROSS_RUN_CAUSAL_CONTINUITY_AUDIT.md").read_text(
        encoding="utf-8"
    )
    plan = (
        ROOT / "NEXT_SYSTEM_INTERACTION_BOUNDED_CAUSAL_VERIFICATION_TRANSFER.md"
    ).read_text(encoding="utf-8")
    reconciliation = (ROOT / "PROGRAM_RECONCILIATION.md").read_text(
        encoding="utf-8"
    )
    assert "four independent worlds" in result
    assert "Actor utility | untested" in result
    assert "complete system operating over time" in plan
    assert "repair surface is common apparatus" in reconciliation
    assert "No GPU run is authorized" in plan
