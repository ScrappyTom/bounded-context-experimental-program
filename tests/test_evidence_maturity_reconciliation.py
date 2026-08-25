from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_evidence_maturity_reconciliation",
    ROOT / "tools" / "build_evidence_maturity_reconciliation.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class EvidenceMaturityReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(
            (ROOT / "analysis" / "EVIDENCE_MATURITY_RECONCILIATION_CONFIG.json").read_text(
                encoding="utf-8"
            )
        )
        cls.audit = json.loads(
            (ROOT / "analysis" / "EVIDENCE_MATURITY_RECONCILIATION.json").read_text(
                encoding="utf-8"
            )
        )

    def test_pinned_reconstruction_matches(self):
        result = MODULE.verify(self.config, self.audit)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual(57, result["trajectory_invocations"])
        self.assertEqual(0, result["gpu_calls"])

    def test_partial_evidence_invention_is_not_promoted_as_recurrent(self):
        summary = self.audit["summary"]
        self.assertEqual(["bluehaven"], summary["unsupported_completion_worlds"])
        self.assertFalse(
            self.audit["routing_disposition"]["unsupported_completion_recurrence_met"]
        )

    def test_complete_replacement_no_op_recurs_across_worlds(self):
        self.assertEqual(
            ["architecture_program", "cedar_valley"],
            self.audit["summary"]["byte_identical_no_op_worlds"],
        )
        self.assertGreaterEqual(
            self.audit["summary"]["byte_identical_accepted_replacements"], 8
        )


if __name__ == "__main__":
    unittest.main()
