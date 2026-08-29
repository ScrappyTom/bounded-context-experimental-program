from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e98_preserves_original_donor_derived_stage0_record() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    live = contract["active_host_runtime_refactor"]["e99_live_lifecycle_result"]
    assert live["freeze_commit"] == (
        "520d8237e42e313fb014ad146aefb4c51feb8a3e"
    )
    assert live["closure_readiness"] == "not_ready"
    assert live["actor_calls"] == 4
    assert live["sealed_route_resumed"] is False

    stage0 = (ROOT / "E98_TRELLIS_E97_VERIFICATION_LIFECYCLE_STAGE0.md").read_text(
        encoding="utf-8"
    )
    assert "not directly resumed under changed code" in stage0
    assert "selected but not authorized" in stage0
    assert "Provider-free completion proves reachability, not Qwen behavior" in stage0
