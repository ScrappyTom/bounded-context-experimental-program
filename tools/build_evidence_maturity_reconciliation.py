"""Reconstruct evidence-maturity maintenance episodes from pinned Git objects."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID_RE = re.compile(r"S\d{2}")
SOURCE_KEY_RE = re.compile(r'"source_id"\s*:\s*"(S\d{2})"')


def git_bytes(repository: Path, *args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        capture_output=True,
    ).stdout


def git_text(repository: Path, *args: str) -> str:
    return git_bytes(repository, *args).decode("utf-8")


def object_bytes(repository: Path, commit: str, path: str) -> bytes:
    return git_bytes(repository, "show", f"{commit}:{path}")


def object_json(repository: Path, commit: str, path: str) -> Any:
    return json.loads(object_bytes(repository, commit, path))


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def list_paths(repository: Path, commit: str, root: str, pattern: str) -> list[str]:
    names = git_text(repository, "ls-tree", "-r", "--name-only", commit, root).splitlines()
    prefix = root.rstrip("/") + "/"
    relative_pattern = pattern.replace("\\", "/")
    return sorted(
        name
        for name in names
        if name.startswith(prefix)
        and fnmatch.fnmatch(name[len(prefix) :], relative_pattern)
    )


def sibling(path: str, name: str) -> str:
    return str(Path(path).with_name(name)).replace("\\", "/")


def extract_prior_and_new_sources(messages: list[dict[str, Any]]) -> dict[str, Any]:
    user_content = "\n".join(
        str(message.get("content", ""))
        for message in messages
        if message.get("role") == "user"
    )
    prior_marker = "# Prior accepted integration ledger"
    exact_markers = (
        "# Exact newly externalized observation",
        "# Mechanically batched exact externalized observations",
    )
    marker_positions = [user_content.find(marker) for marker in exact_markers]
    exact_position = max(marker_positions)
    prior_position = user_content.find(prior_marker)
    prior_text = ""
    if prior_position >= 0:
        prior_start = prior_position + len(prior_marker)
        prior_end = exact_position if exact_position >= 0 else len(user_content)
        prior_text = user_content[prior_start:prior_end].strip()
    exact_text = user_content[exact_position:] if exact_position >= 0 else ""
    return {
        "prior_present": bool(prior_text),
        "prior_state_sha256": sha256(prior_text.encode("utf-8")) if prior_text else None,
        "prior_state_source_ids": sorted(set(SOURCE_ID_RE.findall(prior_text))),
        "new_exact_source_ids": sorted(set(SOURCE_KEY_RE.findall(exact_text))),
    }


def actor_delivery_index(
    repository: Path, commit: str, cell_root: str
) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for path in list_paths(repository, commit, f"{cell_root}/actor", "*/RESULT.json"):
        value = object_json(repository, commit, path)
        for result_id in value.get("delivered_result_ids", []):
            index[result_id] = {
                "actor_call": value.get("actor_call"),
                "logical_call": value.get("logical_call"),
                "action": value.get("parsed_action"),
                "path": path,
            }
    return index


def task_binding(repository: Path, commit: str, donor: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for label, field in (("task", "task_path"), ("task_lock", "task_lock_path")):
        path = donor[field]
        payload = object_bytes(repository, commit, path)
        result[label] = {
            "path": path,
            "blob_oid": git_text(repository, "rev-parse", f"{commit}:{path}").strip(),
            "sha256": sha256(payload),
            "size_bytes": len(payload),
        }
    for label, field in (
        ("semantic_adjudication", "semantic_adjudication_path"),
        ("economics_audit", "economics_audit_path"),
    ):
        if field in donor:
            path = donor[field]
            payload = object_bytes(repository, commit, path)
            result[label] = {
                "path": path,
                "blob_oid": git_text(repository, "rev-parse", f"{commit}:{path}").strip(),
                "sha256": sha256(payload),
                "size_bytes": len(payload),
            }
    return result


def build(config: dict[str, Any]) -> dict[str, Any]:
    repository = Path(config["repository"]["path"])
    annotations = config.get("semantic_annotations", {})
    invocations: list[dict[str, Any]] = []
    donors_out: list[dict[str, Any]] = []

    for donor in config["donors"]:
        commit = donor["commit"]
        resolved = git_text(repository, "rev-parse", f"{commit}^{{commit}}").strip()
        if resolved != commit:
            raise ValueError(f"commit mismatch for {donor['stage_id']}: {resolved}")
        paths = list_paths(repository, commit, donor["root"], donor["result_glob"])
        donors_out.append(
            {
                "stage_id": donor["stage_id"],
                "world_id": donor["world_id"],
                "role": donor["role"],
                "commit": commit,
                "invocation_count": len(paths),
                "bindings": task_binding(repository, commit, donor),
            }
        )

        previous_accepted_by_cell: dict[str, dict[str, Any]] = {}
        delivery_by_cell: dict[str, dict[str, dict[str, Any]]] = {}
        if "/cells" in donor["root"]:
            cell_names = sorted({path.split("/cells/", 1)[1].split("/", 1)[0] for path in paths})
            for cell in cell_names:
                run_prefix = donor["root"].split("/cells", 1)[0]
                cell_root = f"{run_prefix}/cells/{cell}"
                delivery_by_cell[cell] = actor_delivery_index(repository, commit, cell_root)

        for path in paths:
            value = object_json(repository, commit, path)
            output_path = sibling(path, "assistant_content.txt")
            messages_path = sibling(path, "messages.json")
            output = object_bytes(repository, commit, output_path)
            messages = object_json(repository, commit, messages_path)
            output_hash = sha256(output)
            message_facts = extract_prior_and_new_sources(messages)
            validation = value.get("validation", {})
            usage = value.get("usage", {})
            cell = (
                path.split("/cells/", 1)[1].split("/", 1)[0]
                if "/cells/" in path
                else "QUALIFICATION"
            )
            invocation_label = value.get("case_id") or f"maintenance-{value.get('maintenance_call'):03d}"
            previous = previous_accepted_by_cell.get(cell)
            accepted = bool(value.get("accepted"))
            output_source_ids = sorted(validation.get("source_ids", []))
            allowed_source_ids = sorted(value.get("allowed_source_ids", []))
            new_exact_source_ids = message_facts["new_exact_source_ids"]
            effect_id = value.get("effect_result_id")
            delivery = delivery_by_cell.get(cell, {}).get(effect_id) if effect_id else None
            annotation = annotations.get(output_hash, {})
            classifications = list(annotation.get("classifications", []))
            if any(
                issue in {"token_budget_exceeded", "heading_mismatch", "syntax_error"}
                for issue in validation.get("issues", [])
            ) and "carrier_failure" not in classifications:
                classifications.append("carrier_failure")
            if accepted and not classifications:
                classifications.append("provenance_admitted_semantics_not_exhaustively_adjudicated")

            record = {
                "invocation_id": f"{donor['stage_id']}:{cell}:{invocation_label}",
                "stage_id": donor["stage_id"],
                "world_id": donor["world_id"],
                "donor_role": donor["role"],
                "commit": commit,
                "cell": cell,
                "invocation_label": invocation_label,
                "result_path": path,
                "result_blob_oid": git_text(repository, "rev-parse", f"{commit}:{path}").strip(),
                "result_sha256": sha256(object_bytes(repository, commit, path)),
                "messages_path": messages_path,
                "messages_sha256": sha256(object_bytes(repository, commit, messages_path)),
                "output_path": output_path,
                "output_blob_oid": git_text(repository, "rev-parse", f"{commit}:{output_path}").strip(),
                "output_sha256": output_hash,
                "input_result_ids": value.get("input_result_ids")
                or ([value["input_result_id"]] if value.get("input_result_id") else []),
                **message_facts,
                "allowed_source_ids": allowed_source_ids,
                "output_source_ids": output_source_ids,
                "disallowed_source_ids": sorted(validation.get("disallowed_source_ids", [])),
                "new_exact_sources_cited": sorted(set(new_exact_source_ids) & set(output_source_ids)),
                "new_exact_sources_not_cited": sorted(set(new_exact_source_ids) - set(output_source_ids)),
                "requirement_ids": sorted(validation.get("requirement_ids", [])),
                "complete_state_requested": len(validation.get("requirement_ids", [])) == 12,
                "accepted": accepted,
                "validation_code": validation.get("code"),
                "validation_issues": validation.get("issues", []),
                "finish_reason": value.get("finish_reason"),
                "prompt_tokens": usage.get("prompt_tokens", value.get("prompt_tokens", 0)),
                "completion_tokens": usage.get("completion_tokens", 0),
                "output_tokens": validation.get("output_tokens"),
                "byte_identical_to_prior_accepted_output": bool(
                    previous and previous["output_sha256"] == output_hash
                ),
                "effect_kind": value.get("effect_kind"),
                "effect_result_id": effect_id,
                "effect_crossed_actor_boundary": delivery is not None,
                "next_actor_observation": delivery,
                "classifications": sorted(set(classifications)),
                "classification_basis": annotation.get("basis"),
            }
            if (
                record["byte_identical_to_prior_accepted_output"]
                and record["new_exact_source_ids"]
                and record["new_exact_sources_not_cited"]
            ):
                record["classifications"] = sorted(
                    set(record["classifications"])
                    | {"failed_new_evidence_capitalization"}
                )
            invocations.append(record)
            if accepted:
                previous_accepted_by_cell[cell] = record

    trajectory = [item for item in invocations if item["donor_role"] == "trajectory_evidence"]
    accepted = [item for item in trajectory if item["accepted"]]
    rejected = [item for item in trajectory if not item["accepted"]]
    unsupported_worlds = sorted(
        {
            item["world_id"]
            for item in trajectory
            if "unsupported_semantic_completion" in item["classifications"]
        }
    )
    no_op_worlds = sorted(
        {
            item["world_id"]
            for item in accepted
            if item["byte_identical_to_prior_accepted_output"]
            and item["new_exact_source_ids"]
        }
    )
    route = config["routing_rule"]
    recurring_complete_replacement_worlds = sorted(
        {
            item["world_id"]
            for item in trajectory
            if any(
                label
                in {
                    "unsupported_semantic_completion",
                    "stale_semantic_selection",
                    "failed_new_evidence_capitalization",
                    "carrier_failure",
                }
                for label in item["classifications"]
            )
        }
    )
    return {
        "schema_version": "evidence-maturity-reconciliation-v0",
        "created": config["created"],
        "source_mode": "pinned_git_objects",
        "repository": config["repository"],
        "donors": donors_out,
        "summary": {
            "all_invocations": len(invocations),
            "trajectory_invocations": len(trajectory),
            "transport_reference_invocations": len(invocations) - len(trajectory),
            "accepted_trajectory_invocations": len(accepted),
            "rejected_trajectory_invocations": len(rejected),
            "trajectory_prompt_tokens": sum(item["prompt_tokens"] for item in trajectory),
            "trajectory_completion_tokens": sum(item["completion_tokens"] for item in trajectory),
            "byte_identical_accepted_replacements": sum(
                item["byte_identical_to_prior_accepted_output"] for item in accepted
            ),
            "accepted_replacements_omitting_new_exact_source_citation": sum(
                bool(item["new_exact_sources_not_cited"]) for item in accepted
            ),
            "effect_results_crossing_actor_boundary": sum(
                item["effect_crossed_actor_boundary"] for item in trajectory
            ),
            "validation_code_counts": dict(
                sorted(Counter(item["validation_code"] for item in trajectory).items())
            ),
            "classification_counts": dict(
                sorted(Counter(label for item in trajectory for label in item["classifications"]).items())
            ),
            "unsupported_completion_worlds": unsupported_worlds,
            "byte_identical_no_op_worlds": no_op_worlds,
            "complete_replacement_failure_worlds": recurring_complete_replacement_worlds,
        },
        "routing_disposition": {
            "unsupported_completion_recurrence_threshold": route[
                "unsupported_completion_minimum_independent_worlds"
            ],
            "unsupported_completion_recurrence_met": len(unsupported_worlds)
            >= route["unsupported_completion_minimum_independent_worlds"],
            "selected_route": route["if_recurrent"]
            if len(unsupported_worlds)
            >= route["unsupported_completion_minimum_independent_worlds"]
            else route["if_not_recurrent"],
            "system_finding": "Complete semantic replacement is the recurring interaction risk: partial-evidence invention is Bluehaven-local, while stale selection, no-op replacement, carrier pressure, and downstream capitalization recur across independent worlds.",
            "next_experiment_family": "fresh_source_local_evidence_delta_by_direct_exact_work_whole_system_scout",
        },
        "invocations": invocations,
    }


def verify(
    config: dict[str, Any],
    materialized: dict[str, Any],
    rebuilt: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rebuilt = rebuilt if rebuilt is not None else build(config)
    failures: list[str] = []
    if rebuilt != materialized:
        failures.append("materialized audit differs from pinned-source reconstruction")
    summary = rebuilt["summary"]
    if summary["trajectory_invocations"] != 57:
        failures.append("expected 57 trajectory maintenance invocations")
    if summary["transport_reference_invocations"] != 4:
        failures.append("expected four E42 expression-reference invocations")
    if summary["unsupported_completion_worlds"] != ["bluehaven"]:
        failures.append("unsupported semantic completion should remain Bluehaven-local")
    if summary["byte_identical_no_op_worlds"] != ["architecture_program", "cedar_valley"]:
        failures.append("byte-identical no-op replacement should recur in two worlds")
    if materialized["routing_disposition"]["unsupported_completion_recurrence_met"]:
        failures.append("evidence-maturity controller must not be promoted")
    return {
        "passed": not failures,
        "failures": failures,
        "all_invocations": summary["all_invocations"],
        "trajectory_invocations": summary["trajectory_invocations"],
        "accepted_trajectory_invocations": summary["accepted_trajectory_invocations"],
        "rejected_trajectory_invocations": summary["rejected_trajectory_invocations"],
        "byte_identical_accepted_replacements": summary[
            "byte_identical_accepted_replacements"
        ],
        "unsupported_completion_worlds": summary["unsupported_completion_worlds"],
        "byte_identical_no_op_worlds": summary["byte_identical_no_op_worlds"],
        "selected_route": materialized["routing_disposition"]["selected_route"],
        "gpu_calls": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "analysis" / "EVIDENCE_MATURITY_RECONCILIATION_CONFIG.json",
    )
    parser.add_argument(
        "--audit",
        type=Path,
        default=ROOT / "analysis" / "EVIDENCE_MATURITY_RECONCILIATION.json",
    )
    parser.add_argument("--materialize", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if args.materialize:
        materialized = build(config)
        args.audit.write_text(
            json.dumps(materialized, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        materialized = json.loads(args.audit.read_text(encoding="utf-8"))
    result = verify(config, materialized, rebuilt=materialized if args.materialize else None)
    receipt = {
        "schema_version": "evidence-maturity-reconciliation-receipt-v0",
        "config_sha256": sha256(args.config.read_bytes()),
        "audit_sha256": sha256(args.audit.read_bytes()),
        "checker_sha256": sha256(Path(__file__).resolve().read_bytes()),
        **result,
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
