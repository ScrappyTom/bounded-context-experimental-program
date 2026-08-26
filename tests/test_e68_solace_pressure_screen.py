from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "6059797681e2591737476417148952c844043b7f"


class E68SolacePressureScreenTests(unittest.TestCase):
    def test_aggregate_records_exact_live_result(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S60")
        self.assertEqual(6, stage["model_calls"])
        self.assertEqual(63_731, stage["serialized_tokens"])
        self.assertEqual(COMMIT, stage["sources"][0]["result_commit"])
        self.assertIn("2397 tokens", stage["primary_disposition"])

    def test_docs_route_to_complete_interaction_without_expression_gate(self) -> None:
        result = (ROOT / "E68_SOLACE_PRESSURE_SCREEN_RESULT.md").read_text(
            encoding="utf-8"
        )
        plan = (
            ROOT / "NEXT_SYSTEM_INTERACTION_FAULT_TOLERANT_PROVENANCE.md"
        ).read_text(encoding="utf-8")
        self.assertIn("21,211", result)
        self.assertIn("2,397", result)
        self.assertIn("does not place another expression-only gate", result)
        self.assertIn("Start both cells from the exact audited E68 boundary", plan)
        self.assertIn(COMMIT, result + plan)


if __name__ == "__main__":
    unittest.main()
