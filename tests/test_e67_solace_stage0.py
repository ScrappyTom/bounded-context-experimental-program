from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "5af42ca96182ce16dc5aced20f952da9a7c791e4"


class E67SolaceStage0Tests(unittest.TestCase):
    def test_aggregate_records_zero_call_whole_system_stage(self) -> None:
        aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S59")
        self.assertEqual(0, stage["model_calls"])
        self.assertEqual(COMMIT, stage["sources"][0]["result_commit"])
        self.assertIn("partial admission", stage["primary_disposition"])

    def test_machine_route_forbids_expression_gate_and_gpu(self) -> None:
        contract = json.loads((ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8"))
        route = contract["active_system_route"]
        self.assertEqual(COMMIT, route["stage0_commit"])
        self.assertFalse(route["maintenance_failure_lifecycle"]["standalone_expression_gate"])
        self.assertFalse(route["next_live_operation"]["authorized"])
        self.assertFalse(route["gpu_authorized"])

    def test_governing_docs_preserve_e66_and_select_whole_system_route(self) -> None:
        direction = (ROOT / "SYSTEM_INTERACTION_EXPLORATION.md").read_text(encoding="utf-8")
        plan = (ROOT / "NEXT_SYSTEM_INTERACTION_FAULT_TOLERANT_PROVENANCE.md").read_text(encoding="utf-8")
        ledger = (ROOT / "EVIDENCE_LEDGER.md").read_text(encoding="utf-8")
        self.assertIn("The exact E66 result remains frozen", direction)
        self.assertIn("Do not run a third carrier-expression micro-iteration", plan)
        self.assertIn("zero valid claims leave the register", ledger)
        self.assertIn(COMMIT, direction + plan + ledger)


if __name__ == "__main__":
    unittest.main()
