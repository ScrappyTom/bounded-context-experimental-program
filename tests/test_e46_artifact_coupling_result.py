from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ArtifactCouplingResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(
            (ROOT / "E46_ARTIFACT_COUPLING_INTERACTION_RESULT.json").read_text(
                encoding="utf-8"
            )
        )
        cls.aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )

    def test_totals_and_result_binding(self):
        cells = self.result["cells"]
        self.assertEqual(self.result["actor_calls"], sum(row["actor_calls"] for row in cells))
        self.assertEqual(
            self.result["maintenance_calls"],
            sum(row["maintenance_calls"] for row in cells),
        )
        self.assertEqual(
            self.result["provider_calls"],
            sum(row["provider_calls"] for row in cells),
        )
        self.assertEqual(
            self.result["serialized_tokens"],
            sum(row["serialized_tokens"] for row in cells),
        )
        stage = next(row for row in self.aggregate["stages"] if row["stage_id"] == "S38")
        self.assertEqual(self.result["provider_calls"], stage["model_calls"])
        self.assertEqual(self.result["serialized_tokens"], stage["serialized_tokens"])
        self.assertEqual(self.result["result_commit"], stage["sources"][0]["result_commit"])

    def test_quality_and_interaction_disposition(self):
        self.assertEqual(0, self.result["useful_completions"])
        self.assertEqual("none", self.result["semantic_dominance"])
        self.assertTrue(self.result["mechanical_audit_passed"])
        self.assertEqual("closed", self.result["same_boundary_successor"])
        for cell in self.result["cells"]:
            self.assertEqual("strong_partial", cell["quality_class"])
            self.assertEqual("not_ready", cell["closure_readiness"])
            self.assertFalse(cell["submitted"])

    def test_coupling_changed_timing_without_completion(self):
        by_id = {row["configuration_id"]: row for row in self.result["cells"]}
        self.assertLess(
            by_id["A1_COUPLED"]["first_check_actor_call"],
            by_id["D0_DETACHED"]["first_check_actor_call"],
        )
        self.assertGreater(
            by_id["A1_COUPLED"]["decision_distinct_source_citations"],
            by_id["D0_DETACHED"]["decision_distinct_source_citations"],
        )
        self.assertEqual(
            "actor_call_budget_exhausted",
            by_id["A1_COUPLED"]["terminal_disposition"],
        )


if __name__ == "__main__":
    unittest.main()
