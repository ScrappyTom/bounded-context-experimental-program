from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e101_records_coherent_but_incomplete_live_checkpoint() -> None:
    value = json.loads(
        (ROOT / "E101_TRELLIS_REPAIRED_VERIFICATION_CHECKPOINT_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["result_commit"] == "97d84493ef72d271410ae590f6ead7e86c2b551a"
    assert value["actual"]["actor_calls"] == 6
    assert value["behavior"]["section_version_rejection_recovered"] is True
    assert value["behavior"]["changed_candidate_rechecked"] is True
    assert value["behavior"]["looping_observed"] is False
    assert value["candidate"]["substantive_groups_met"] == 1
    assert value["candidate"]["closure_readiness"] == "not_ready"


def test_e102_freeze_remains_historical_after_e103_execution() -> None:
    value = json.loads(
        (ROOT / "E102_TRELLIS_VERIFICATION_CONTINUATION_STAGE0.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["apparatus_commit"] == "97d84493ef72d271410ae590f6ead7e86c2b551a"
    assert value["provider_free_probe"]["pending_result_delivered"] == "RESULT-024"
    assert value["provider_free_probe"]["prompt_tokens"] == 19_247
    assert value["qualification"]["full_repository_tests_passed"] == 318
    assert value["live_authorized"] is False

    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    assert contract["current_program_boundary"]["stage"] == "E105"
    assert contract["current_program_boundary"]["gpu_operation_selected"] is True
    scout = contract["active_host_runtime_refactor"]["selected_lifecycle_scout"]
    assert scout["stage"] == "E102"
    assert scout["maximum_additional_actor_calls"] == 6
    assert scout["live_authorized"] is True
    result = contract["active_host_runtime_refactor"]["e103_live_continuation_result"]
    assert result["actor_calls"] == 2
    assert result["terminal"] == "capacity_blocked"
