from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_e105_selects_clean_unauthorized_review_tranche() -> None:
    contract = json.loads(
        (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
    )
    result = contract["active_host_runtime_refactor"][
        "e105_clean_whole_lifecycle_stage0"
    ]
    boundary = contract["current_program_boundary"]

    assert result["apparatus_commit"] == (
        "fc5acada791bc53dc3562e3f3e2e0b62c1f367a0"
    )
    assert result["historical_checkpoint_imported"] is False
    assert result["provider_free_actor_calls"] == 19
    assert result["provider_free_maintenance_calls"] == 7
    assert result["provider_free_check_sequence"] == [False, True]
    assert result["provider_free_final_readiness"] == "ready"
    assert result["provider_free_submitted"] is True
    assert result["full_repository_tests_passed"] == 333
    assert result["first_live_maximum_actor_calls"] == 12
    assert result["first_live_maximum_maintenance_calls"] == 6
    assert result["mandatory_review"] is True
    assert result["automatic_continuation"] is False
    assert result["live_authorized"] is False

    assert boundary["stage"] == "E107"
    assert boundary["gpu_operation_selected"] is True
    assert boundary["gpu_operation_authorized"] is False


def test_e105_narrative_separates_fixture_reachability_from_live_utility() -> None:
    narrative = (ROOT / "E105_TRELLIS_CLEAN_WHOLE_LIFECYCLE_STAGE0.md").read_text(
        encoding="utf-8"
    )
    assert "imports no E103 candidate" in narrative
    assert "fail → pass" in narrative
    assert "do not establish\nreadiness" in narrative
    assert "mechanical reachability, not Qwen task utility" in narrative
    assert "selected but not authorized" in narrative
