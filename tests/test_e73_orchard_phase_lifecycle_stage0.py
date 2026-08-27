from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "444ab65a745f1d5cbadbd30e1ed07c99a88ee173"


class E73OrchardPhaseLifecycleStage0Tests(unittest.TestCase):
    def test_aggregate_records_zero_call_stage(self):
        aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S65")
        self.assertEqual(0, stage["model_calls"])
        self.assertEqual(0, stage["serialized_tokens"])
        self.assertEqual(COMMIT, stage["sources"][0]["result_commit"])

    def test_machine_route_requires_treatment_free_screen_first(self):
        contract = json.loads((ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8"))
        route = contract["active_system_route"]
        stage0 = route["phase_conditional_transfer_stage0"]
        self.assertEqual(COMMIT, stage0["result_commit"])
        self.assertEqual(0, stage0["provider_calls"])
        self.assertEqual(178, stage0["standalone_tests_passed"])
        self.assertFalse(stage0["behavioral_utility_measured"])
        next_operation = route["next_live_operation"]
        self.assertEqual("treatment_free_orchard_pressure_screen", next_operation["kind"])
        self.assertEqual(30, next_operation["maximum_provider_calls"])
        self.assertFalse(next_operation["semantic_maintenance_present"])
        self.assertFalse(next_operation["treatment_present"])
        self.assertFalse(next_operation["measured_runner_frozen"])
        self.assertFalse(next_operation["authorized"])
        self.assertFalse(route["gpu_authorized"])

    def test_docs_preserve_whole_system_scope_and_claim_limits(self):
        result = (ROOT / "E73_ORCHARD_PHASE_LIFECYCLE_STAGE0.md").read_text(encoding="utf-8")
        plan = (ROOT / "NEXT_SYSTEM_INTERACTION_PHASE_CONDITIONAL_LIFECYCLE_TRANSFER.md").read_text(encoding="utf-8")
        self.assertIn("not component isolation", result.lower())
        self.assertIn("zero model", result.lower())
        self.assertIn("treatment-free pressure screen", plan)
        self.assertIn("F0/P1 measurement", plan)
        self.assertIn("not yet frozen or authorized", plan)


if __name__ == "__main__":
    unittest.main()
