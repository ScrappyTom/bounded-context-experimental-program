from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CedarTransferResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(
            (ROOT / "E52_CEDAR_ARTIFACT_COUPLING_TRANSFER_RESULT.json").read_text(
                encoding="utf-8"
            )
        )

    def test_exact_run_totals_and_binding(self):
        self.assertEqual("E52", self.result["stage_id"])
        self.assertEqual(
            "eec64f42564ebd014e048e6897485b095c634aa3",
            self.result["result_commit"],
        )
        self.assertEqual(38, self.result["actor_calls"])
        self.assertEqual(36, self.result["maintenance_calls"])
        self.assertEqual(74, self.result["provider_calls"])
        self.assertEqual(1_026_000, self.result["serialized_tokens"])
        self.assertEqual(1, self.result["attempts_per_call"])
        self.assertEqual(0, self.result["retries"])

    def test_quality_signal_is_not_promoted_to_completion(self):
        by_configuration = {
            cell["configuration_id"]: cell for cell in self.result["cells"]
        }
        self.assertEqual("weak_partial", by_configuration["D0_DETACHED"]["quality_class"])
        self.assertEqual("strong_partial", by_configuration["A1_COUPLED"]["quality_class"])
        self.assertFalse(by_configuration["D0_DETACHED"]["useful_completion"])
        self.assertFalse(by_configuration["A1_COUPLED"]["useful_completion"])
        self.assertEqual(0, self.result["useful_completions"])
        self.assertEqual("closed", self.result["same_boundary_successor"])


if __name__ == "__main__":
    unittest.main()
