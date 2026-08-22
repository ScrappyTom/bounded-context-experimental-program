import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_information_economics_ledger",
    ROOT / "tools" / "check_information_economics_ledger.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class InformationEconomicsLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock = json.loads((ROOT / "analysis" / "INFORMATION_ECONOMICS_SOURCE_LOCK.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "analysis" / "INFORMATION_ECONOMICS_EPISODE_SCHEMA.json").read_text(encoding="utf-8"))
        cls.ledger = json.loads((ROOT / "analysis" / "INFORMATION_ECONOMICS_EPISODES.json").read_text(encoding="utf-8"))

    def test_pinned_sources_and_episode_ledger_pass(self):
        result = MODULE.verify(self.lock, self.schema, self.ledger)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual(12, result["source_count"])
        self.assertEqual(29, result["episode_count"])
        self.assertEqual(11, result["comparison_group_count"])
        self.assertEqual(0, result["gpu_calls"])

    def test_tampered_source_hash_fails(self):
        lock = copy.deepcopy(self.lock)
        lock["sources"][0]["sha256"] = "0" * 64
        result = MODULE.verify(lock, self.schema, self.ledger)
        self.assertFalse(result["passed"])
        self.assertTrue(any("SHA-256 mismatch" in failure for failure in result["failures"]))

    def test_duplicate_boundary_fails(self):
        ledger = copy.deepcopy(self.ledger)
        duplicate = copy.deepcopy(ledger["episodes"][0])
        duplicate["episode_id"] = "IEE-999"
        ledger["episodes"].append(duplicate)
        result = MODULE.verify(self.lock, self.schema, ledger)
        self.assertFalse(result["passed"])
        self.assertTrue(any("duplicate canonical boundary" in failure for failure in result["failures"]))

    def test_unexplained_null_fails(self):
        ledger = copy.deepcopy(self.ledger)
        ledger["episodes"][0]["outcome"]["first_action"] = None
        result = MODULE.verify(self.lock, self.schema, ledger)
        self.assertFalse(result["passed"])
        self.assertTrue(any("outcome.first_action" in failure for failure in result["failures"]))

    def test_cross_basis_comparison_fails(self):
        ledger = copy.deepcopy(self.ledger)
        ledger["episodes"][12]["evaluation"]["basis_id"] = "wrong-basis"
        result = MODULE.verify(self.lock, self.schema, ledger)
        self.assertFalse(result["passed"])
        self.assertTrue(any("common evaluation basis" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
