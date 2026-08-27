from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class E75OrchardPhaseLifecycleFreezeTests(unittest.TestCase):
    def test_aggregate_records_zero_call_freeze(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S67")
        self.assertEqual(0, stage["model_calls"])
        self.assertEqual(0, stage["serialized_tokens"])
        self.assertEqual(
            "094bbce57407568d1ef0ecd94414ae1a957e3b45",
            stage["sources"][0]["result_commit"],
        )

    def test_freeze_is_compound_and_unauthorized(self) -> None:
        text = (ROOT / "E75_ORCHARD_PHASE_LIFECYCLE_MEASURED_FREEZE.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("deliberately compound", text)
        self.assertIn("Check and submission are verification-only", text)
        self.assertIn("zero new provider calls", text)
        self.assertIn("separately authorized", text)


if __name__ == "__main__":
    unittest.main()
