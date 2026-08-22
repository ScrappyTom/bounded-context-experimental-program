import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_next_route_prior_evidence",
    ROOT / "tools" / "check_next_route_prior_evidence.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class NextRoutePriorEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock = json.loads(
            (ROOT / "audits" / "NEXT_ROUTE_PRIOR_EVIDENCE_LOCK.json").read_text(encoding="utf-8")
        )

    def test_all_sources_verify_from_pinned_git_objects(self):
        result = MODULE.verify(self.lock)
        self.assertTrue(result["passed"])
        self.assertEqual([], result["failures"])
        self.assertEqual(13, result["source_count"])

    def test_tampered_hash_fails(self):
        lock = copy.deepcopy(self.lock)
        lock["sources"][0]["sha256"] = "0" * 64
        result = MODULE.verify(lock)
        self.assertFalse(result["passed"])
        self.assertTrue(any("SHA-256 mismatch" in item for item in result["failures"]))


if __name__ == "__main__":
    unittest.main()
