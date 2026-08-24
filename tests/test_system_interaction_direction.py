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

    def test_closed_scout_measured_interaction_and_successor_are_explicit(self):
        closed = self.contract["closed_first_interaction"]
        self.assertEqual(4, len(closed["configurations"]))
        self.assertIn("semantic_residue", closed["axis_a"])
        self.assertIn("incremental_exact", closed["axis_b"])
        self.assertEqual(
            "mechanically_triggered_one_attempt_zero_retry",
            closed["maintenance_mode"],
        )
        self.assertEqual(
            "not_qualified_after_declared_final_v2_gate",
            closed["final_disposition"],
        )
        self.assertTrue(closed["same_route_successor_forbidden"])

        completed = self.contract["completed_ingress_work_interaction"]
        self.assertEqual(4, len(completed["configurations"]))
        self.assertIn("multi_range", completed["axis_a"])
        self.assertIn("cumulative", completed["axis_b"])
        self.assertEqual(
            "local_negative_with_apparatus_censoring",
            completed["status"],
        )
        self.assertEqual(
            "1c041e2c55e0cc1f735e056df84a156c15bd8679",
            completed["freeze_commit"],
        )
        self.assertEqual(138, completed["measured_run"]["actual_provider_calls"])
        self.assertTrue(completed["measured_run"]["completed"])
        self.assertEqual("I1", completed["apparatus_qualification"]["affected_configuration"])

        successor = self.contract["next_system_interaction"]
        self.assertEqual(
            "live_expression_qualified_pressure_screen_pending_gpu_not_authorized",
            successor["status"],
        )
        self.assertTrue(successor["implementation"]["live_expression_qualified"])
        self.assertEqual(4, successor["implementation"]["expression_model_calls"])
        self.assertEqual(
            "7423d214d5d2a5b77514b0acff43d547743b422e",
            successor["implementation"]["pressure_screen_freeze_commit"],
        )
        self.assertIn("exact incremental task-artifact", successor["question"])
        self.assertIn(
            "effects_checks_repair_readiness_and_closure_are_in_horizon",
            successor["non_isolation"],
        )
        self.assertIn(
            "positive_savings_relief_regression",
            successor["completed_offline_gates"],
        )
        self.assertIn(
            "fresh_task_and_candidate_lineage_with_E40_as_design_donor_only",
            successor["completed_offline_gates"],
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
        self.assertIn(
            "prospective_positive_savings_relief_eligibility",
            self.contract["common_live_functions"],
        )
        self.assertFalse(self.contract["gpu_authorized"])


if __name__ == "__main__":
    unittest.main()
