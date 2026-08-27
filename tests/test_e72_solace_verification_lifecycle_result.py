from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_COMMIT = "7620e1b84e1269a2edfbd31112187286d46e3ddc"


class E72SolaceVerificationLifecycleResultTests(unittest.TestCase):
    def test_aggregate_records_measured_lifecycle(self):
        aggregate = json.loads((ROOT / "PROGRAM_STAGE_AGGREGATE.json").read_text(encoding="utf-8"))
        stage = next(row for row in aggregate["stages"] if row["stage_id"] == "S64")
        self.assertEqual(14, stage["model_calls"])
        self.assertEqual(243_637, stage["serialized_tokens"])
        self.assertEqual(RESULT_COMMIT, stage["sources"][0]["result_commit"])

    def test_result_preserves_quality_and_lifecycle_limits(self):
        result = (ROOT / "E72_SOLACE_VERIFICATION_LIFECYCLE_RESULT.md").read_text(encoding="utf-8")
        self.assertIn("eleven substantive groups met", result)
        self.assertIn("ten substantive groups met", result)
        self.assertIn("6,646", result)
        self.assertIn("not_ready", result.lower())
        self.assertIn("effect uptake", result.lower())

    def test_machine_route_selects_phase_conditional_transfer_without_gpu_authority(self):
        contract = json.loads((ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8"))
        route = contract["active_system_route"]
        measured = route["verification_lifecycle_result"]
        self.assertEqual(RESULT_COMMIT, measured["result_commit"])
        self.assertEqual("verification_prompt_pressure_without_feasible_relief", measured["A0_terminal_failure"])
        self.assertEqual("verification_prompt_pressure_without_feasible_relief", measured["A1_terminal_failure"])
        self.assertFalse(measured["final_effect_uptake"])
        successor = route["next_live_operation"]
        self.assertEqual("fresh_world_phase_conditional_lifecycle_transfer_stage0", successor["kind"])
        self.assertFalse(successor["component_isolation_claim"])
        self.assertFalse(successor["authorized"])
        self.assertFalse(route["gpu_authorized"])

    def test_successor_is_explicitly_interaction_level(self):
        plan = (ROOT / "NEXT_SYSTEM_INTERACTION_PHASE_CONDITIONAL_LIFECYCLE_TRANSFER.md").read_text(encoding="utf-8")
        self.assertIn("not a component-isolation study", plan.lower())
        self.assertIn("fresh-world requirement", plan.lower())
        self.assertIn("No live run is authorized", plan)


if __name__ == "__main__":
    unittest.main()
