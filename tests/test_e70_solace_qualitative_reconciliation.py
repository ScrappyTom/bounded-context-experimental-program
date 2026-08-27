from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class E70SolaceQualitativeReconciliationTests(unittest.TestCase):
    def test_aggregate_records_zero_call_audit_and_exact_commit(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S62")
        self.assertEqual("offline_audit", stage["stage_type"])
        self.assertEqual(0, stage["model_calls"])
        self.assertEqual(0, stage["serialized_tokens"])
        self.assertEqual(
            "891bb0d46b757313781a8c40e6084c24d3d064bd",
            stage["sources"][0]["result_commit"],
        )

    def test_reconciliation_corrects_shorthand_without_regrading(self) -> None:
        text = (ROOT / "E70_SOLACE_QUALITATIVE_TRANSCRIPT_RECONCILIATION.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Both visible drafts contained substantial cross-domain synthesis", text)
        self.assertIn("zero admitted decision mutations", text)
        self.assertIn("Q02, Q03, Q04, Q09", text)
        self.assertIn("Q10 is **met**", text)
        self.assertIn("No new GPU run is authorized", text)

    def test_machine_route_records_compound_interaction_and_scope(self) -> None:
        contract = json.loads(
            (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
        )
        route = contract["active_system_route"]
        measured = route["measured_interaction_result"]
        audit = route["qualitative_transcript_reconciliation"]
        self.assertEqual(2, measured["W0_unadmitted_global_decision_attempts"])
        self.assertEqual(8192, measured["W0_unadmitted_global_decision_completion_tokens"])
        self.assertEqual(34, audit["provider_turns_reconstructed"])
        self.assertEqual(0, audit["new_model_calls"])
        self.assertFalse(audit["sealed_outcomes_changed"])
        self.assertEqual(["Q02", "Q03", "Q04", "Q09"], audit["direct_partial_requirements"])
        self.assertIn("marginal_register_value_only", audit["post_construction_ablation_scope"])

    def test_e69_and_lifecycle_plan_do_not_repeat_no_construction_story(self) -> None:
        e69 = (ROOT / "E69_SOLACE_ANCHORED_PROVENANCE_INTERACTION_RESULT.md").read_text(
            encoding="utf-8"
        )
        plan = (
            ROOT / "NEXT_SYSTEM_INTERACTION_CONSTRUCTION_VERIFICATION_LIFECYCLE.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("no decision construction", e69)
        self.assertIn("two broad global decision attempts", e69)
        self.assertIn("does **not** isolate", plan)
        self.assertIn("construction granularity", plan)


if __name__ == "__main__":
    unittest.main()
