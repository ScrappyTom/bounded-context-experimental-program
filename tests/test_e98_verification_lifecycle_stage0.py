from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e98_freezes_donor_derived_lifecycle_without_authorization() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    boundary = contract["current_program_boundary"]
    assert boundary["stage"] == "E98"
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False

    scout = contract["active_host_runtime_refactor"]["selected_lifecycle_scout"]
    assert scout["apparatus_commit"] == (
        "520d8237e42e313fb014ad146aefb4c51feb8a3e"
    )
    assert scout["donor_closure_readiness"] == "not_ready"
    assert scout["inherited_provider_attempts"] == 29
    assert scout["inherited_serialized_tokens"] == 350_510
    assert scout["offline_prompt_tokens"] == 19_116
    assert scout["maximum_additional_actor_calls"] == 18
    assert scout["mandatory_review_after_actor_calls"] == 6
    assert scout["provider_free_complete_lifecycle_qualified"] is True
    assert scout["live_authorized"] is False

    stage0 = (ROOT / "E98_TRELLIS_E97_VERIFICATION_LIFECYCLE_STAGE0.md").read_text(
        encoding="utf-8"
    )
    assert "not directly resumed under changed code" in stage0
    assert "selected but not authorized" in stage0
    assert "Provider-free completion proves reachability, not Qwen behavior" in stage0
