from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class E66AsterRelationalExpressionResultTests(unittest.TestCase):
    def test_aggregate_binds_exact_measured_result(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S58")
        self.assertEqual("measured", stage["stage_type"])
        self.assertEqual(1, stage["model_calls"])
        self.assertEqual(5_136, stage["serialized_tokens"])
        self.assertEqual(
            "d19f45cd4478946f9271e85285df32f7152e8e6c",
            stage["sources"][0]["result_commit"],
        )

    def test_program_disposition_separates_safety_transport_and_utility(self) -> None:
        result = (
            ROOT / "E66_ASTER_RELATIONAL_EXPRESSION_QUALIFICATION_RESULT.md"
        ).read_text(encoding="utf-8")
        self.assertIn("raw semantic material safety          local positive", result)
        self.assertIn("complete-line transport admission     local negative", result)
        self.assertIn("downstream persistence and utility    untested", result)
        self.assertIn("0/4 claims", result)

    def test_exact_route_is_closed_without_repair_or_continuation(self) -> None:
        plan = (
            ROOT / "NEXT_SYSTEM_INTERACTION_PROVENANCE_LOCAL_RELATIONAL_SCOUT.md"
        ).read_text(encoding="utf-8")
        ledger = (ROOT / "EVIDENCE_LEDGER.md").read_text(encoding="utf-8")
        self.assertIn("Status: closed at E66", plan)
        self.assertIn("not repaired, retried, or carried into an actor", plan)
        self.assertIn("| E66 |", ledger)
        self.assertIn("transport admitted 0/4 claims", ledger)


if __name__ == "__main__":
    unittest.main()
