from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SystemInteractionDirectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads((ROOT / "SYSTEM_INTERACTION_EXPLORATION.json").read_text(encoding="utf-8"))

    def test_unit_is_whole_configuration_not_component(self):
        self.assertEqual("whole_configuration_trajectory", self.contract["unit_of_analysis"])
        self.assertEqual("low_pressure_reference_not_interaction_result", self.contract["e37_role"])
        self.assertIn(
            "capability_labels_are_trajectory_codes_not_component_backlog",
            self.contract["non_isolation_rules"],
        )
        self.assertIn(
            "component_ablation_waits_for_joint_configuration_signal",
            self.contract["non_isolation_rules"],
        )

    def test_first_scout_crosses_two_persistence_functions(self):
        interaction = self.contract["first_interaction"]
        self.assertEqual(4, len(interaction["configurations"]))
        self.assertIn("semantic_residue", interaction["axis_a"])
        self.assertIn("incremental_exact", interaction["axis_b"])
        self.assertEqual(
            "mechanically_triggered_one_attempt_zero_retry",
            interaction["maintenance_mode"],
        )
        self.assertEqual("authentic_prompt_pressure", self.contract["required_activation"])

    def test_feedback_loop_remains_live(self):
        required = {
            "deterministic_first_fit_pressure_relief",
            "exact_reopen",
            "candidate_bound_effects",
            "candidate_bound_feedback",
            "bounded_resumption",
            "independent_artifact_quality_and_readiness",
        }
        self.assertTrue(required.issubset(set(self.contract["common_live_functions"])))
        self.assertFalse(self.contract["gpu_authorized"])


if __name__ == "__main__":
    unittest.main()
