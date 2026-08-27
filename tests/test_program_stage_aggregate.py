from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_program_stage_aggregate",
    ROOT / "tools" / "check_program_stage_aggregate.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ProgramStageAggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))

    def test_declared_aggregate_passes(self):
        result = MODULE.verify(self.aggregate)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual(63, result["successor_stages"])
        self.assertEqual(614, result["follow_on_model_calls"])
        self.assertEqual(7_907_644, result["follow_on_serialized_tokens"])
        self.assertEqual(58, result["unique_cited_experiment_commits"])
        self.assertEqual(42, result["parent_exact_replayed_requests"])

    def test_frozen_receipt_matches_recomputation(self):
        expected = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE_RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(expected, MODULE.verify(self.aggregate))

    def test_changed_call_total_fails(self):
        value = copy.deepcopy(self.aggregate)
        value["stages"][0]["model_calls"] += 1
        result = MODULE.verify(value)
        self.assertFalse(result["passed"])
        self.assertTrue(any("follow_on_model_calls" in failure for failure in result["failures"]))

    def test_duplicate_stage_id_fails(self):
        value = copy.deepcopy(self.aggregate)
        value["stages"][1]["stage_id"] = "S01"
        result = MODULE.verify(value)
        self.assertFalse(result["passed"])
        self.assertTrue(any("stage IDs differ" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
