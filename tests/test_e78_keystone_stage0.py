from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "d13582a9371512ee6d279ade461a88f05096f9f9"


def test_aggregate_records_zero_call_keystone_stage0() -> None:
    aggregate = json.loads(
        (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
    )
    stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S70")
    assert stage["stage_type"] == "eligibility"
    assert stage["model_calls"] == 0
    assert stage["serialized_tokens"] == 0
    assert stage["sources"][0]["result_commit"] == RESULT_COMMIT


def test_machine_route_preserves_keystone_stage0_after_pressure_screen() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    route = contract["active_system_route"]
    stage0 = route["keystone_bounded_causal_stage0"]
    assert stage0["result_commit"] == RESULT_COMMIT
    assert stage0["provider_calls"] == 0
    assert stage0["source_count"] == 14
    assert stage0["prospective_pressure_prompt_tokens"] == 23_021
    assert stage0["prospective_relief_prompt_tokens"] == 19_495
    assert stage0["V0_recurrence_after_newer_observation"] is False
    assert stage0["V1_recurrence_count"] == 2
    assert stage0["behavioral_utility_measured"] is False
    assert stage0["measured_runner_frozen"] is False
    assert route["keystone_pressure_screen_result"]["interaction_trigger_qualified"] is False
    assert route["next_live_operation"]["authorized"] is False
    assert route["gpu_authorized"] is False


def test_docs_preserve_whole_lifecycle_and_claim_limits() -> None:
    result = (ROOT / "E78_KEYSTONE_BOUNDED_CAUSAL_STAGE0.md").read_text(
        encoding="utf-8"
    )
    plan = (
        ROOT / "NEXT_SYSTEM_INTERACTION_BOUNDED_CAUSAL_VERIFICATION_TRANSFER.md"
    ).read_text(encoding="utf-8")
    reconciliation = (ROOT / "PROGRAM_RECONCILIATION.md").read_text(
        encoding="utf-8"
    )
    assert "fourteen interacting regional-rail evidence" in result
    assert "does not establish" in result
    assert "valid alternative repair" in plan
    assert "apparatus reachability, not behavioral utility" in reconciliation
    assert "not authorized" in result
