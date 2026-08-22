import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_artifact_adjudications", ROOT / "tools" / "check_artifact_adjudications.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ArtifactAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads(
            (ROOT / "audits" / "ARTIFACT_ADJUDICATION_LEDGER.json").read_text(encoding="utf-8")
        )

    def test_current_ledger_has_no_active_conflict(self):
        result = MODULE.check_ledger(self.ledger)
        self.assertEqual([], result["failures"])
        self.assertEqual(1, result["superseded_record_count"])

    def test_locked_source_blobs_resolve(self):
        result = MODULE.verify_ledger_sources(self.ledger)
        self.assertEqual([], result["failures"])
        self.assertEqual(4, len(result["verified"]))

    def test_active_quality_upgrade_is_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        original = next(
            record for record in ledger["records"] if record["record_id"] == "navigation-h05-original-coarse-review"
        )
        original["status"] = "active"
        original.pop("superseded_by")
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("unreconciled active quality conflict" in item for item in result["failures"]))

    def test_superseded_record_requires_active_target(self):
        ledger = copy.deepcopy(self.ledger)
        record = next(record for record in ledger["records"] if record["status"] == "superseded")
        record["superseded_by"] = "missing-record"
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("lacks valid target" in item for item in result["failures"]))


if __name__ == "__main__":
    unittest.main()
