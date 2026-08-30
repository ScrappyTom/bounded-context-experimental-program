from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e103_records_closed_corrupted_route_and_offline_successor() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    result = contract["active_host_runtime_refactor"][
        "e103_live_continuation_result"
    ]
    boundary = contract["current_program_boundary"]

    assert result["freeze_commit"] == "97d84493ef72d271410ae590f6ead7e86c2b551a"
    assert result["actor_calls"] == 2
    assert result["serialized_tokens"] == 39_865
    assert result["next_prompt_tokens"] == 21_318
    assert result["prompt_allowance"] == 20_992
    assert result["artifact_boundary_corrupted"] is True
    assert result["route_closed"] is True
    assert boundary["stage"] == "E103"
    assert boundary["gpu_operation_selected"] is False
    assert boundary["next_document"] == (
        "NEXT_OFFLINE_VERIFICATION_RESIDENCY_RECONCILIATION.md"
    )


def test_e103_narrative_preserves_behavior_quality_and_claim_limits() -> None:
    narrative = (
        ROOT / "E103_TRELLIS_VERIFICATION_CONTINUATION_RESULT.md"
    ).read_text(encoding="utf-8")
    plan = (
        ROOT / "NEXT_OFFLINE_VERIFICATION_RESIDENCY_RECONCILIATION.md"
    ).read_text(encoding="utf-8")

    assert "Qwen was not looping" in narrative
    assert "This is a host fault" in narrative
    assert "not_ready" in narrative
    assert "must not resume from the corrupted candidate" in narrative
    assert "The host may not infer that Qwen understood" in plan
    assert "No GPU use is part of this stage" in plan
