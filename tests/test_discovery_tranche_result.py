from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DiscoveryTrancheResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads((ROOT / "DISCOVERY_TRANCHE_RESULT.json").read_text(encoding="utf-8"))
        cls.aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))

    def test_mechanical_totals_are_internally_consistent(self):
        self.assertTrue(self.result["mechanically_qualified"])
        self.assertEqual(self.result["actor_calls"], self.result["provider_attempts"])
        self.assertEqual(0, self.result["retries"])
        self.assertEqual(
            self.result["serialized_tokens"],
            self.result["prompt_tokens"] + self.result["completion_tokens"],
        )
        self.assertEqual(39, self.result["actor_calls"])
        self.assertEqual(101_657, self.result["serialized_tokens"])

    def test_e37_aggregate_binding_matches_result(self):
        stage = next(stage for stage in self.aggregate["stages"] if stage["stage_id"] == "S29")
        self.assertEqual(self.result["actor_calls"], stage["model_calls"])
        self.assertEqual(self.result["serialized_tokens"], stage["serialized_tokens"])
        self.assertEqual(self.result["result_commit"], stage["sources"][0]["result_commit"])
        self.assertEqual(self.result["experiment_repository"], stage["sources"][0]["repository"])

    def test_closure_and_pressure_disposition_is_explicit(self):
        self.assertEqual(0, self.result["pressure_events"])
        self.assertEqual(0, self.result["pressure_substitutions"])
        self.assertEqual(0, self.result["exact_reopens"])
        self.assertEqual(0, self.result["correct_useful_completions"])
        self.assertEqual(["D2", "D5", "D6"], self.result["submitted_cells"])
        self.assertFalse(self.result["interaction_question_adjudicated"])
        self.assertEqual("low_pressure_reference_regime", self.result["program_role"])


if __name__ == "__main__":
    unittest.main()
