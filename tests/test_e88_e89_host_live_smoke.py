from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_v0_result_preserves_zero_call_environmental_stop() -> None:
    result = json.loads(
        (ROOT / "E88_HOST_LIVE_SMOKE_V0_RESULT.json").read_text(encoding="utf-8")
    )
    assert result["status"] == "sealed_pre_provider_environment_block"
    assert result["provider_attempts"] == 0
    assert result["model_calls"] == 0
    assert result["retries"] == 0


def test_v1_freeze_has_new_identity_and_unchanged_limits() -> None:
    stage = json.loads(
        (ROOT / "E89_HOST_LIVE_SMOKE_V1_STAGE0.json").read_text(encoding="utf-8")
    )
    assert stage["apparatus_commit"] == "a92577d64612a6a5f7c623e02de89eb527b47017"
    assert stage["run_id"] == "2026-08-28-host-refactor-live-smoke-v1"
    assert stage["maximum_model_calls"] == 1
    assert stage["maximum_serialized_tokens"] == 30_000
    assert stage["attempts_per_call"] == 1
    assert stage["retries"] == 0
