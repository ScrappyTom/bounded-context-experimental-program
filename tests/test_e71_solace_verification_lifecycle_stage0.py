from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "a2c9270c676e2d0d8427b119f81ec39b3f21b2d1"


class E71SolaceVerificationLifecycleStage0Tests(unittest.TestCase):
    def test_aggregate_records_zero_call_stage0(self):
        aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S63")
        self.assertEqual(0, stage["model_calls"])
        self.assertEqual(0, stage["serialized_tokens"])
        self.assertEqual(COMMIT, stage["sources"][0]["result_commit"])

    def test_machine_route_freezes_complete_interaction_not_component_gate(self):
        contract = json.loads((ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8"))
        route = contract["active_system_route"]
        stage0 = route["postconstruction_lifecycle_stage0"]
        self.assertEqual(COMMIT, stage0["result_commit"])
        self.assertEqual(0, stage0["provider_calls"])
        self.assertTrue(stage0["provider_free_complete_lifecycle_qualified"])
        self.assertFalse(stage0["behavioral_utility_measured"])
        self.assertEqual(6646, stage0["register_prompt_increment_tokens"])
        measured = route["verification_lifecycle_result"]
        self.assertEqual(14, measured["provider_calls"])
        self.assertEqual(243_637, measured["serialized_tokens"])
        self.assertEqual(6646, measured["register_prompt_increment_tokens"])
        self.assertFalse(measured["useful_completion"])

    def test_docs_preserve_scope_and_no_gpu_authorization(self):
        plan = (ROOT / "NEXT_SYSTEM_INTERACTION_CONSTRUCTION_VERIFICATION_LIFECYCLE.md").read_text(encoding="utf-8")
        ledger = (ROOT / "EVIDENCE_LEDGER.md").read_text(encoding="utf-8")
        self.assertIn("Stage 0 disposition", plan)
        self.assertIn("does **not** isolate", plan)
        self.assertIn("The authorized two-cell run completed", plan)
        self.assertIn("E71", ledger)
        self.assertIn("AF/NQ", ledger)


if __name__ == "__main__":
    unittest.main()
