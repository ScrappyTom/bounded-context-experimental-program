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
    assert stage["status"] == "completed_by_e90_pre_provider_live_tokenizer_projection_mismatch"


def test_v1_result_preserves_exact_pre_provider_projection_stop() -> None:
    result = json.loads(
        (ROOT / "E90_HOST_LIVE_SMOKE_V1_RESULT.json").read_text(encoding="utf-8")
    )
    assert result["apparatus_commit"] == "a92577d64612a6a5f7c623e02de89eb527b47017"
    assert result["offline_relief_prompt_tokens"] == 18_785
    assert result["live_relief_prompt_tokens"] == 18_786
    assert result["provider_attempts"] == 0
    assert result["model_calls"] == 0
    assert result["retries"] == 0


def test_v2_freezes_distinct_exact_offline_and_live_projections() -> None:
    stage = json.loads(
        (ROOT / "E91_HOST_LIVE_SMOKE_V2_STAGE0.json").read_text(encoding="utf-8")
    )
    assert stage["apparatus_commit"] == "3afd9e269abb437512ea961772b43f4a12ea0f30"
    assert stage["run_id"] == "2026-08-28-host-refactor-live-smoke-v2"
    assert stage["scope"] == "host_refactor_live_smoke_v2"
    assert stage["parent_boundary"]["offline_relief_prompt_tokens"] == 18_785
    assert stage["parent_boundary"]["live_relief_prompt_tokens"] == 18_786
    assert stage["maximum_model_calls"] == 1
    assert stage["maximum_serialized_tokens"] == 30_000
    assert stage["attempts_per_call"] == 1
    assert stage["retries"] == 0
    assert stage["status"] == "completed_by_e92_qualified_checkpoint_pause"


def test_v2_result_records_qualified_single_call_live_path() -> None:
    result = json.loads(
        (ROOT / "E92_HOST_LIVE_SMOKE_V2_RESULT.json").read_text(encoding="utf-8")
    )
    assert result["apparatus_freeze_commit"] == "3afd9e269abb437512ea961772b43f4a12ea0f30"
    assert result["apparatus_result_commit"] == "eddb5d6f8095a931701642542d94face46b7057b"
    assert result["qualified"] is True
    assert result["model_calls"] == 1
    assert result["provider_attempts"] == 1
    assert result["retries"] == 0
    assert result["live_prompt_tokens"] == 18_786
    assert result["completion_tokens"] == 74
    assert result["pending_result_first_delivered_call"] == 8
    assert result["next_pending_result_id"] == "RESULT-008"
    assert result["candidate_changed"] is False
    assert result["runtime_released"] is True
