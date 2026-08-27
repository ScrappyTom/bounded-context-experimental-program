from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class E74OrchardPressureScreenTests(unittest.TestCase):
    def test_aggregate_records_exact_measured_result(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S66")
        self.assertEqual(6, stage["model_calls"])
        self.assertEqual(62_106, stage["serialized_tokens"])
        self.assertEqual(
            "a681f52acd750176065b6ed5d5418f5f5ae6e9b8",
            stage["sources"][0]["result_commit"],
        )

    def test_result_preserves_literal_boundary_and_claim_limit(self) -> None:
        text = (ROOT / "E74_ORCHARD_PRESSURE_SCREEN_RESULT.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("21,152", text)
        self.assertIn("18,509", text)
        self.assertIn("62,106", text)
        self.assertIn("No F0/P1 behavior or utility is measured", text)


if __name__ == "__main__":
    unittest.main()
