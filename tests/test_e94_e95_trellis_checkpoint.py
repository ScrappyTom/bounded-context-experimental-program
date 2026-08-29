from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e94_records_literal_checkpoint_and_claim_limits() -> None:
    value = json.loads(
        (ROOT / "E94_TRELLIS_REFACTORED_INTERACTION_TRANCHE_RESULT.json").read_text(
            encoding="utf-8"
        )
    )
    assert value["actual"] == {
        "actor_calls": 24,
        "maintenance_calls": 6,
        "provider_calls": 30,
        "serialized_tokens": 379972,
        "retries": 0,
    }
    assert value["common_behavior"]["pending_result_id"] == "RESULT-012"
    assert value["common_behavior"]["candidate_mutations"] == 0
    assert value["disposition"]["same_source_replacement"] == (
        "semantically_lossy_local_negative"
    )
    assert value["disposition"]["downstream_utility"] == "untested"


def test_e95_continues_exact_system_without_repair() -> None:
    stage = json.loads(
        (ROOT / "E95_TRELLIS_REFACTORED_INTERACTION_CONTINUATION_STAGE0.json").read_text(
            encoding="utf-8"
        )
    )
    assert stage["apparatus_commit"] == (
        "18e17806e906d57943ab9b7461def708084d69b1"
    )
    assert stage["policy_change"] is False
    assert stage["live_authorized"] is False
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    selected = contract["selected_whole_system_interaction"]
    continuation = selected["selected_continuation"]
    assert selected["stage"] == "E95"
    assert continuation["apparatus_commit"] == (
        "18e17806e906d57943ab9b7461def708084d69b1"
    )
    assert continuation["policy_change"] is False
    assert continuation["maximum_additional_actor_calls"] == 24
    assert continuation["maximum_additional_maintenance_calls"] == 6
    assert continuation["maximum_additional_provider_calls"] == 30
    assert continuation["maximum_additional_serialized_tokens"] == 520028
    assert continuation["live_authorized"] is False
