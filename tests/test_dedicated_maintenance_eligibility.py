import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_dedicated_maintenance_eligibility",
    ROOT / "tools" / "check_dedicated_maintenance_eligibility.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class DedicatedMaintenanceEligibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock = json.loads((ROOT / "audits" / "DEDICATED_MAINTENANCE_SOURCE_LOCK.json").read_text(encoding="utf-8"))
        cls.audit = json.loads((ROOT / "audits" / "DEDICATED_MAINTENANCE_ELIGIBILITY.json").read_text(encoding="utf-8"))

    def test_pinned_donor_and_manager_packets_pass(self):
        result = MODULE.verify(self.lock, self.audit)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual(11, result["source_count"])
        self.assertEqual(2, result["manager_request_count"])
        self.assertEqual(0, result["chat_completions"])
        self.assertEqual(0, result["gpu_calls"])

    def test_tampered_donor_hash_fails(self):
        lock = copy.deepcopy(self.lock)
        lock["sources"][0]["sha256"] = "0" * 64
        result = MODULE.verify(lock, self.audit)
        self.assertFalse(result["passed"])
        self.assertTrue(any("SHA-256 mismatch" in failure for failure in result["failures"]))

    def test_infeasible_manager_fails(self):
        audit = copy.deepcopy(self.audit)
        audit["cells"][0]["manager_request"]["fits"] = False
        result = MODULE.verify(self.lock, audit)
        self.assertFalse(result["passed"])
        self.assertTrue(any("manager does not fit" in failure for failure in result["failures"]))

    def test_trivial_choice_fails(self):
        audit = copy.deepcopy(self.audit)
        audit["cells"][1]["feasible_single_choice_count"] = 1
        result = MODULE.verify(self.lock, audit)
        self.assertFalse(result["passed"])
        self.assertTrue(any("mechanically trivial" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
