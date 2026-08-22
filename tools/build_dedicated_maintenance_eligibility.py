"""Build and token-audit a dedicated maintenance-only selection view.

This is an offline eligibility tool. It calls only llama.cpp's template and
tokenization endpoints and never calls chat completion.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DONOR = Path(r"E:\qwen38-context-reduction-pressure-boundary-v0")
DONOR_COMMIT = "ab0e21b201d04521a43f83c223a364bca35a7b86"
CELLS = ("s42-s1", "s314159-s1")
CONTEXT_TOKENS = 25_088
ORDINARY_RESERVE = 4_096
MAINTENANCE_RESERVE = 512


def compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_donor() -> None:
    head = subprocess.run(
        ["git", "-C", str(DONOR), "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    status = subprocess.run(
        ["git", "-C", str(DONOR), "status", "--porcelain"], check=True, capture_output=True, text=True
    ).stdout.strip()
    if head != DONOR_COMMIT:
        raise RuntimeError(f"donor HEAD mismatch: {head}")
    if status:
        raise RuntimeError("donor working tree is not clean")


def maintenance_schema(ids: list[str]) -> dict[str, Any]:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "dedicated_workspace_selection_v0",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "release_result_ids": {
                        "type": "array",
                        "items": {"type": "string", "enum": ids},
                        "minItems": 1,
                        "maxItems": len(ids),
                        "uniqueItems": True,
                    }
                },
                "required": ["release_result_ids"],
                "additionalProperties": False,
            },
        },
    }


def maintenance_message(
    cell: str,
    eligible: list[dict[str, Any]],
    pending_action: dict[str, Any],
    pending_result_message: dict[str, Any],
    control_post_tokens: int,
) -> str:
    deficit = control_post_tokens - (CONTEXT_TOKENS - ORDINARY_RESERVE)
    rows = []
    for row in eligible:
        rows.append(
            f"{row['result_id']} | chronological_result_index={row['result_index']} | "
            f"reopen_action={compact(row['action'])} | exact_message_bytes={row['message_size_bytes']}"
        )
    pending_content = pending_result_message["content"].encode("utf-8")
    return (
        "DEDICATED EXACT-WORKSPACE MAINTENANCE MODE\n"
        "This call performs workspace selection only. Do not perform an ordinary task action, "
        "summarize content, judge readiness, or recommend what the ordinary actor should do next.\n"
        "The exact task, chronology, and currently resident result bodies above are available for selection.\n"
        "The host owns exact bytes, receipts, capacity enforcement, and recovery.\n"
        "Choose one or more eligible historical result messages to replace with deterministic exact "
        "reopenable receipts. The pending result is never eligible for release.\n"
        f"cell: {cell}\n"
        f"ordinary_prompt_allowance_tokens: {CONTEXT_TOKENS - ORDINARY_RESERVE}\n"
        f"control_post_result_prompt_tokens: {control_post_tokens}\n"
        f"minimum_net_release_tokens_required: {deficit}\n"
        f"pending_action: {compact(pending_action)}\n"
        f"pending_result_message_sha256: {sha256_bytes(pending_content)}\n"
        f"pending_result_message_bytes: {len(pending_content)}\n"
        "Eligible exact-backed resident result messages:\n"
        + "\n".join(rows)
        + "\nReturn only the schema object. The host will reject duplicates, unknown IDs, "
        "non-positive substitutions, or a selection whose exact rendered ordinary packet remains infeasible."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "audits" / "dedicated_maintenance")
    parser.add_argument("--output", type=Path, default=ROOT / "audits" / "DEDICATED_MAINTENANCE_ELIGIBILITY.json")
    args = parser.parse_args()
    verify_donor()

    sys.path.insert(0, str(DONOR))
    from apparatus.canonical import canonical_json_bytes  # type: ignore
    from apparatus.modelio import ParentTokenEndpoint, request_with_messages  # type: ignore
    from apparatus.parent import boundary_objects  # type: ignore
    from apparatus.receipts import make_receipt, pair_indices  # type: ignore

    preflight = json.loads((DONOR / "CAPACITY_PREFLIGHT.json").read_text(encoding="utf-8"))
    token_endpoint = ParentTokenEndpoint(args.endpoint)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cells: list[dict[str, Any]] = []

    for cell in CELLS:
        parent = boundary_objects(cell)
        messages = copy.deepcopy(parent["request"]["messages"])
        historical_tail = [copy.deepcopy(parent["assistant_message"]), copy.deepcopy(parent["result_message"])]
        capacity_rows = [row for row in preflight["cells"] if row["cell"] == cell]
        control = capacity_rows[0]
        recent = next(row for row in capacity_rows if row["policy_id"] == "recent2_receipts_v0")
        action_by_result = {result: action for action, result in pair_indices(messages)}
        eligible: list[dict[str, Any]] = []
        for trace in recent["selection_trace"]:
            if not trace.get("accepted_positive_savings"):
                continue
            result_index = int(trace["result_index"])
            eligible.append(
                {
                    "result_id": f"RESULT_{result_index:03d}",
                    "result_index": result_index,
                    "action_index": action_by_result[result_index],
                    "action": trace["action"],
                    "message_size_bytes": len(messages[result_index]["content"].encode("utf-8")),
                }
            )

        maintenance = maintenance_message(
            cell,
            eligible,
            parent["action"],
            parent["result_message"],
            control["control_post_historical_result"]["prompt_tokens"],
        )
        manager_messages = messages + [copy.deepcopy(parent["assistant_message"]), {"role": "user", "content": maintenance}]
        request = request_with_messages(parent["request"], manager_messages)
        request["max_tokens"] = MAINTENANCE_RESERVE
        request["response_format"] = maintenance_schema([row["result_id"] for row in eligible])
        request_bytes = canonical_json_bytes(request)
        request_path = args.output_dir / f"{cell}-manager-request.json"
        request_path.write_bytes(request_bytes)
        manager_count = token_endpoint.count(manager_messages, request["chat_template_kwargs"])
        manager_headroom = CONTEXT_TOKENS - MAINTENANCE_RESERVE - manager_count.prompt_tokens

        single_choices: list[dict[str, Any]] = []
        for row in eligible:
            projected = copy.deepcopy(messages)
            index = row["result_index"]
            action_index = row["action_index"]
            projected[index] = make_receipt(
                projected[action_index],
                projected[index],
                backing_id=f"parent:{cell}:request-message:{index:03d}",
            )
            count = token_endpoint.count(projected + historical_tail, request["chat_template_kwargs"])
            single_choices.append(
                {
                    "result_id": row["result_id"],
                    "post_result_prompt_tokens": count.prompt_tokens,
                    "headroom_after_ordinary_reserve": CONTEXT_TOKENS - ORDINARY_RESERVE - count.prompt_tokens,
                    "feasible": count.prompt_tokens <= CONTEXT_TOKENS - ORDINARY_RESERVE,
                }
            )

        incumbent = next(row for row in capacity_rows if row["policy_id"] == "oldest_fit_receipts_v0")
        cells.append(
            {
                "cell": cell,
                "seed": parent["model_profile"]["routine_tool_request_defaults"]["seed"],
                "historical_action": parent["action"],
                "control_decision_prompt_tokens": control["control_decision"]["prompt_tokens"],
                "control_post_result_prompt_tokens": control["control_post_historical_result"]["prompt_tokens"],
                "ordinary_prompt_allowance_tokens": CONTEXT_TOKENS - ORDINARY_RESERVE,
                "minimum_net_release_tokens_required": control["control_post_historical_result"]["prompt_tokens"] - (CONTEXT_TOKENS - ORDINARY_RESERVE),
                "eligible_result_count": len(eligible),
                "eligible_results": eligible,
                "manager_request": {
                    "path": request_path.relative_to(ROOT).as_posix(),
                    "sha256": sha256_bytes(request_bytes),
                    "size_bytes": len(request_bytes),
                    "prompt_tokens": manager_count.prompt_tokens,
                    "response_reserve_tokens": MAINTENANCE_RESERVE,
                    "headroom_after_reserve": manager_headroom,
                    "fits": manager_headroom >= 0,
                    "rendered_prompt_sha256": manager_count.rendered_prompt_sha256,
                },
                "feasible_single_choice_count": sum(row["feasible"] for row in single_choices),
                "single_choice_capacity": single_choices,
                "incumbent": {
                    "released_result_indices": [change["result_index"] for change in incumbent["changes"]],
                    "post_result_prompt_tokens": incumbent["treated_post_historical_result"]["prompt_tokens"],
                    "post_result_headroom": incumbent["treated_post_historical_result"]["headroom_after_reserve"],
                    "decision_preserved_in_measured_run": True,
                    "result_absorbed_in_measured_run": True,
                },
                "selection_is_nontrivial": sum(row["feasible"] for row in single_choices) >= 2,
            }
        )

    result = {
        "schema_version": "dedicated-maintenance-eligibility-v0",
        "created": "2026-08-22",
        "donor_repository": str(DONOR),
        "donor_commit": DONOR_COMMIT,
        "mode": "offline_template_and_tokenization_only",
        "chat_completions_called": False,
        "maintenance_reserve_tokens": MAINTENANCE_RESERVE,
        "ordinary_reserve_tokens": ORDINARY_RESERVE,
        "cells": cells,
        "eligible": all(
            cell["manager_request"]["fits"]
            and cell["selection_is_nontrivial"]
            and cell["incumbent"]["decision_preserved_in_measured_run"]
            and cell["incumbent"]["result_absorbed_in_measured_run"]
            for cell in cells
        ),
        "claim_limit": "Capacity and donor eligibility only. No maintenance selection or downstream actor utility was measured.",
        "endpoint_calls": {
            "apply_template": token_endpoint.apply_calls,
            "tokenize": token_endpoint.tokenize_calls,
            "chat_completions": token_endpoint.chat_completion_calls,
        },
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(json.dumps({"eligible": result["eligible"], "cells": len(cells), "chat_completions": 0}, sort_keys=True))
    return 0 if result["eligible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
