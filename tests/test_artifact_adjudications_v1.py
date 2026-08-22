import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_artifact_adjudications_v1",
    ROOT / "tools" / "check_artifact_adjudications_v1.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ArtifactAdjudicationV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads(
            (ROOT / "audits" / "ARTIFACT_ADJUDICATION_LEDGER_V1.json").read_text(encoding="utf-8")
        )

    def test_current_ledger_has_one_active_semantic_judgment(self):
        result = MODULE.check_ledger(self.ledger)
        self.assertEqual([], result["failures"])
        self.assertEqual(3, result["active_record_count"])
        self.assertEqual(1, result["active_semantic_independence_group_count"])

    def test_exact_task_evidence_and_adjudication_sources_reconstruct(self):
        result = MODULE.verify_identity_custody(self.ledger)
        self.assertEqual([], result["failures"])
        self.assertEqual(4, len(result["adjudication_source_records"]))
        self.assertEqual(1, len(result["task_specs"]))
        self.assertEqual(1, len(result["evidence_manifests"]))
        self.assertEqual(4, result["evidence_manifests"][0]["verified_items"])

    def test_score_must_equal_criterion_dispositions(self):
        ledger = copy.deepcopy(self.ledger)
        payload = next(item for item in ledger["adjudication_payloads"] if item["payload_id"] == "navigation-strong-partial-v0")
        payload["score"] = {"met": 11, "partial": 1, "failed": 0, "total": 12}
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("criterion/score mismatch" in item for item in result["failures"]))

    def test_same_basis_criterion_difference_is_a_conflict(self):
        ledger = copy.deepcopy(self.ledger)
        original = next(item for item in ledger["adjudication_payloads"] if item["payload_id"] == "navigation-strong-partial-v0")
        variant = copy.deepcopy(original)
        variant["payload_id"] = "navigation-strong-partial-variant"
        criterion = next(item for item in variant["criteria"] if item["name"] == "factual_precision")
        criterion["finding"] = "A different asserted defect under the same canonical basis."
        ledger["adjudication_payloads"].append(variant)
        ledger["records"][1]["payload_id"] = variant["payload_id"]
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("same-basis adjudication mismatch" in item for item in result["failures"]))

    def test_same_basis_readiness_difference_is_a_conflict(self):
        ledger = copy.deepcopy(self.ledger)
        original = next(item for item in ledger["adjudication_payloads"] if item["payload_id"] == "navigation-strong-partial-v0")
        variant = copy.deepcopy(original)
        variant["payload_id"] = "navigation-readiness-variant"
        variant["closure_readiness"] = "ready"
        variant["blocking_requirements"] = []
        ledger["adjudication_payloads"].append(variant)
        ledger["records"][1]["payload_id"] = variant["payload_id"]
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("same-basis adjudication mismatch" in item for item in result["failures"]))

    def test_not_ready_payload_requires_explicit_blockers(self):
        ledger = copy.deepcopy(self.ledger)
        payload = next(item for item in ledger["adjudication_payloads"] if item["payload_id"] == "navigation-strong-partial-v0")
        payload["blocking_requirements"] = []
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("not-ready payload lacks blocking requirements" in item for item in result["failures"]))

    def test_supersession_requires_typed_explained_relationship(self):
        ledger = copy.deepcopy(self.ledger)
        ledger["basis_relationships"] = []
        result = MODULE.check_ledger(ledger)
        self.assertTrue(any("supersession lacks typed explained relationship" in item for item in result["failures"]))

    def test_older_bank_scan_reads_pinned_commit_not_worktree(self):
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            subprocess.run(["git", "init", "-q", str(repository)], check=True)
            subprocess.run(["git", "-C", str(repository), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(repository), "config", "user.name", "Test"], check=True)
            path = repository / "experiments" / "case" / "summary.json"
            path.parent.mkdir(parents=True)
            committed = {
                "task": "task-v0",
                "terminal_candidate_id": "a" * 64,
                "terminal_passed_count": 7,
                "case_count": 9,
            }
            path.write_text(json.dumps(committed), encoding="utf-8")
            subprocess.run(["git", "-C", str(repository), "add", "."], check=True)
            subprocess.run(["git", "-C", str(repository), "commit", "-q", "-m", "fixture"], check=True)
            commit = subprocess.run(
                ["git", "-C", str(repository), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            modified = dict(committed)
            modified["terminal_passed_count"] = 1
            path.write_text(json.dumps(modified), encoding="utf-8")

            result = MODULE.scan_older_bank_pinned(repository, commit, "experiments")
            self.assertEqual([], result["parse_failures"])
            self.assertEqual([], result["conflicts"])
            self.assertEqual("7/9", result["candidates"][0]["score"])


if __name__ == "__main__":
    unittest.main()
