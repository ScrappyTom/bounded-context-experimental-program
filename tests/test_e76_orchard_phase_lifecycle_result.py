from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "5bfd615d58a97a3d8c83b5bf3c4fc713c5e62e9a"


class E76OrchardPhaseLifecycleResultTests(unittest.TestCase):
    def test_aggregate_records_measured_result(self) -> None:
        aggregate = json.loads(
            (ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8")
        )
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S68")
        self.assertEqual(54, stage["model_calls"])
        self.assertEqual(736_332, stage["serialized_tokens"])
        self.assertEqual(RESULT_COMMIT, stage["sources"][0]["result_commit"])

    def test_result_preserves_compound_interpretation_and_failure_migration(self) -> None:
        text = (ROOT / "E76_ORCHARD_PHASE_LIFECYCLE_INTERACTION_RESULT.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("identical through actor call 12", text)
        self.assertIn("repair effect uptake", text)
        self.assertIn("four byte-identical CURRENT reads", text)
        self.assertIn("not a useful completion", text)
        self.assertIn(
            "Do not run a causal-tail-only prompt ablation",
            " ".join(text.split()),
        )

    def test_machine_route_records_completed_orchard_result(self) -> None:
        contract = json.loads(
            (ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8")
        )
        route = contract["active_system_route"]
        result = route["orchard_phase_lifecycle_result"]
        self.assertEqual(RESULT_COMMIT, result["result_commit"])
        self.assertEqual(54, result["provider_calls"])
        self.assertFalse(result["useful_completion"])
        self.assertFalse(route["gpu_authorized"])

    def test_governing_documents_move_to_bounded_causal_interaction(self) -> None:
        reconciliation = (ROOT / "PROGRAM_RECONCILIATION.md").read_text(
            encoding="utf-8"
        )
        system = (ROOT / "SYSTEM_INTERACTION_EXPLORATION.md").read_text(
            encoding="utf-8"
        )
        roadmap = (ROOT / "STRUCTURED_EXPLORATION_ROADMAP.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("current program synthesis through E77", reconciliation)
        self.assertIn("bounded exact causal tail", reconciliation)
        self.assertIn("governing direction through E77", system)
        self.assertIn("Do not tune Orchard", system)
        self.assertIn("updated through E77", roadmap)


if __name__ == "__main__":
    unittest.main()
