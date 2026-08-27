from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class E69SolaceAnchoredInteractionTests(unittest.TestCase):
    def test_aggregate_records_exact_measured_result(self):
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S61")
        self.assertEqual(34, stage["model_calls"])
        self.assertEqual(578_257, stage["serialized_tokens"])
        self.assertEqual(
            "353c059b31c94dc5951e727b1a2cfa0bba51b6b8",
            stage["sources"][0]["result_commit"],
        )

    def test_result_preserves_positive_interaction_without_completion(self):
        result = (ROOT / "E69_SOLACE_ANCHORED_PROVENANCE_INTERACTION_RESULT.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("first locally positive whole-system interaction signal", result)
        self.assertIn("It is not useful completion", result)
        self.assertIn("strong partial, 8 met and 4 partial", result)
        self.assertIn("final L1 mutation effect never crossed another actor decision", result)
        self.assertIn("No GPU run is authorized", result)

    def test_machine_route_records_completed_lifecycle_and_offline_successor(self):
        contract = json.loads(
            (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
        )
        route = contract["active_system_route"]
        measured = route["measured_interaction_result"]
        self.assertEqual(34, measured["provider_calls"])
        self.assertEqual("not_ready_strong_partial_8_met_4_partial", measured["L1_readiness"])
        self.assertFalse(measured["useful_completion"])
        self.assertTrue(measured["independent_audit_passed"])
        lifecycle = route["verification_lifecycle_result"]
        self.assertEqual(14, lifecycle["provider_calls"])
        self.assertFalse(lifecycle["useful_completion"])
        next_operation = route["next_live_operation"]
        self.assertTrue(next_operation["offline_stage0_required"])
        self.assertTrue(next_operation["offline_stage0_passed"])
        self.assertEqual(
            "444ab65a745f1d5cbadbd30e1ed07c99a88ee173",
            next_operation["freeze_commit"],
        )
        self.assertFalse(next_operation["authorized"])
        self.assertFalse(route["gpu_authorized"])
        self.assertEqual(
            "NEXT_SYSTEM_INTERACTION_PHASE_CONDITIONAL_LIFECYCLE_TRANSFER.md",
            route["governing_document"],
        )

    def test_lifecycle_plan_is_a_post_signal_interaction_ablation(self):
        plan = (
            ROOT / "NEXT_SYSTEM_INTERACTION_CONSTRUCTION_VERIFICATION_LIFECYCLE.md"
        ).read_text(encoding="utf-8")
        self.assertIn("This is a lifecycle interaction ablation", plan)
        self.assertIn("A0 — exact artifact only", plan)
        self.assertIn("A1 — exact artifact plus earned register", plan)
        self.assertIn("check, repair, recheck, and closure", plan)
        self.assertIn("No live model call is authorized", plan)


if __name__ == "__main__":
    unittest.main()
