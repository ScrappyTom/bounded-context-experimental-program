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
        self.assertEqual(
            "e64_aster_stage0_qualified_authentic_pressure_unmeasured",
            self.contract["status"],
        )
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

        successor = self.contract["completed_artifact_coupling_interaction"]
        self.assertEqual(
            "measured_local_mixed_no_useful_completion_advantage",
            successor["status"],
        )
        self.assertTrue(successor["implementation"]["live_expression_qualified"])
        self.assertTrue(successor["implementation"]["activation_qualified"])
        self.assertTrue(successor["implementation"]["measured_offline_preflight_passed"])
        self.assertEqual(27, successor["implementation"]["offline_tests_passed"])
        self.assertEqual(4, successor["implementation"]["expression_model_calls"])
        self.assertEqual(
            "7423d214d5d2a5b77514b0acff43d547743b422e",
            successor["implementation"]["pressure_screen_freeze_commit"],
        )
        self.assertEqual(
            "84037853555362380125a244619894535768056f",
            successor["implementation"]["pressure_screen_result_commit"],
        )
        self.assertEqual(
            "4937083f29df3247a84b3b399c0a7ae922ddb020",
            successor["implementation"]["measured_freeze_commit"],
        )
        self.assertEqual(
            "c11d55a7f143747156831de0b189523ee1bcd776",
            successor["implementation"]["measured_result_commit"],
        )
        self.assertEqual(967, successor["implementation"]["pressure_screen_deficit_tokens"])
        self.assertEqual(40, successor["implementation"]["measured_maximum_actor_calls"])
        self.assertEqual(24, successor["implementation"]["measured_maximum_maintenance_calls"])
        self.assertEqual(64, successor["implementation"]["measured_maximum_provider_calls"])
        self.assertTrue(successor["implementation"]["gpu_authorized"])
        self.assertTrue(successor["implementation"]["measured_completed"])
        self.assertEqual(59, successor["implementation"]["actual_provider_calls"])
        self.assertEqual(0, successor["result"]["useful_completion_count"])
        self.assertEqual("none", successor["result"]["semantic_dominance"])
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
        transfer = self.contract["completed_cedar_transfer_interaction"]
        self.assertEqual(
            "measured_fresh_task_quality_signal_without_useful_completion",
            transfer["status"],
        )
        self.assertEqual(
            "fresh_task_measured_interaction_complete",
            transfer["implementation"],
        )
        self.assertFalse(transfer["gpu_authorized"])
        self.assertEqual(
            "a48d67a8cd888fd54b9c7a59a7e8f1dcd094241f",
            transfer["stage0_commit"],
        )
        self.assertEqual(
            "union_of_exact_source_lines_delivered_across_prior_actor_boundaries",
            transfer["activation"]["unit"],
        )
        self.assertEqual(4, transfer["activation"]["minimum_qualifying_sources"])
        self.assertEqual(3, transfer["activation"]["minimum_evidence_domains"])
        self.assertFalse(transfer["activation"]["host_metadata_actor_visible"])
        self.assertTrue(transfer["permitted_ingress"]["all_full_pairs_admissible"])
        self.assertEqual(11712, transfer["prospective_geometry"]["maturity_prompt_tokens"])
        self.assertEqual(1827, transfer["prospective_geometry"]["pressure_overflow_tokens"])
        self.assertEqual(
            "reachability_not_authentic_activation",
            transfer["prospective_geometry"]["claim_limit"],
        )
        self.assertTrue(transfer["measured_run"]["gpu_authorized"])
        self.assertTrue(transfer["measured_run"]["completed"])
        self.assertEqual(
            "f1610d1bf90b5847dbdbe0d981f4b1676abf4279",
            transfer["measured_run"]["freeze_commit"],
        )
        self.assertEqual(
            "2026-08-25-cedar-artifact-coupling-transfer-measured-v0",
            transfer["measured_run"]["run_id"],
        )
        self.assertEqual(74, transfer["measured_run"]["actual_provider_calls"])
        self.assertEqual(0, transfer["result"]["useful_completion_count"])
        self.assertEqual("weak_partial", transfer["result"]["D0_quality"])
        self.assertEqual("strong_partial", transfer["result"]["A1_quality"])
        self.assertEqual(
            "maintenance_call_budget",
            transfer["result"]["terminal_resource"],
        )
        self.assertEqual(5, transfer["live_activation_result"]["actor_calls"])
        self.assertEqual(2384, transfer["live_activation_result"]["overflow_tokens"])
        self.assertTrue(transfer["live_activation_result"]["pressure_qualified"])
        self.assertIn(
            "prospective_budget_after_first_construction_for_effect_uptake_check_repair_recheck_and_closure",
            transfer["required_properties"],
        )
        self.assertIn(
            "northstar_retry_or_regrade",
            transfer["forbidden_successors"],
        )
        selected = self.contract["next_system_interaction"]
        self.assertEqual(
            "closed_after_expression_transport_failure_material_safety_passed_utility_unmeasured",
            selected["status"],
        )
        self.assertEqual(
            "ScrappyTom/qwen38-artifact-coupled-integration-scout-v0@467ccc0d032af217b969a31315ee41005dbe2167",
            selected["standalone_freeze"],
        )
        self.assertEqual("none_selected", selected["next_live_operation"]["status"])
        self.assertEqual(6, selected["live_activation_result"]["actor_calls"])
        self.assertEqual(2636, selected["live_activation_result"]["overflow_tokens"])
        self.assertTrue(selected["live_activation_result"]["pressure_qualified"])
        self.assertEqual(
            ["RESULT-001"],
            selected["expression_gate_freeze"]["input_result_ids"],
        )
        self.assertFalse(
            selected["expression_gate_freeze"]["measured_continuation_authorized"]
        )
        self.assertEqual(1, selected["expression_gate_freeze"]["maximum_model_calls"])
        self.assertFalse(selected["expression_gate_result"]["transport_passed"])
        self.assertTrue(selected["expression_gate_result"]["material_safety_passed"])
        self.assertFalse(selected["expression_gate_result"]["qualification_passed"])
        self.assertEqual(
            ["DRIFT", "EMBER", "HEATH", "NORTH"],
            selected["expression_gate_result"]["rejected_relationship_object_ids"],
        )
        self.assertEqual(16, selected["topology_audit"]["exact_sources"])
        self.assertEqual(
            16,
            selected["topology_audit"]["sources_with_cross_source_identity_reference"],
        )
        self.assertEqual(
            66,
            selected["topology_audit"]["directed_cross_source_reference_edges"],
        )
        self.assertTrue(
            selected["topology_audit"][
                "bramble_neighbors_equal_expression_gate_rejections"
            ]
        )
        self.assertFalse(selected["topology_audit"]["qualification_regraded"])
        provenance = selected["provenance_semantics_audit"]
        self.assertTrue(provenance["passed"])
        self.assertEqual(10, provenance["historical_fixture_cases"])
        self.assertTrue(
            provenance["e61_grounded_relationship_mechanically_representable"]
        )
        self.assertTrue(provenance["absent_source_slot_mutation_blocked"])
        self.assertTrue(provenance["bluehaven_unsupported_completion_blocked"])
        self.assertTrue(
            provenance["derived_multi_source_claim_requires_separate_work_record"]
        )
        self.assertFalse(provenance["live_expression_qualified"])
        self.assertFalse(provenance["whole_system_utility_measured"])
        self.assertFalse(selected["next_live_operation"]["authorized"])
        self.assertIn("source-local semantic transformation", selected["question"])
        self.assertIn(
            "W0_direct_actor_authored_exact_evidence_and_artifact_work",
            selected["candidate_configuration_families"],
        )
        self.assertIn(
            "L1_source_local_semantic_delta_mechanically_merged_into_exact_source_version_slots",
            selected["candidate_configuration_families"],
        )
        self.assertIn(
            "source_relationship_fidelity",
            selected["primary_outcomes"],
        )
        self.assertIn(
            "check_repair_recheck_and_closure_surface",
            selected["common_live_functions"],
        )
        self.assertIn(
            "complete_global_ledger_third_arm",
            selected["forbidden_shortcuts"],
        )
        self.assertFalse(selected["gpu_authorized"])
        successor = self.contract["candidate_successor_interaction"]
        self.assertEqual(
            "aster_offline_stage0_qualified_common_pressure_pending",
            successor["status"],
        )
        self.assertEqual(1, successor["maximum_expression_qualification_calls_before_measurement"])
        self.assertTrue(successor["stage0_selected"])
        self.assertTrue(successor["stage0_offline_qualified"])
        self.assertEqual(0, successor["provider_calls"])
        self.assertEqual(
            "f91fdaff28b2c7ad760afa90877b284e26529814",
            successor["standalone_commit"],
        )
        self.assertEqual(
            "2026-08-25-aster-provenance-relational-pressure-screen-v0",
            successor["pressure_screen_run_id"],
        )
        self.assertEqual(28, successor["maximum_pressure_screen_actor_calls"])
        self.assertFalse(successor["pressure_screen_treatment_present"])
        self.assertFalse(successor["pressure_screen_authorized"])
        self.assertFalse(successor["authentic_pressure_qualified"])
        self.assertFalse(successor["live_expression_qualified"])
        self.assertFalse(successor["measured_utility_authorized"])
        self.assertTrue(successor["runner_frozen"])
        self.assertFalse(successor["gpu_authorized"])
        plan = ROOT / successor["governing_document"]
        self.assertTrue(plan.is_file())
        plan_text = plan.read_text(encoding="utf-8")
        self.assertIn("complete operating configuration", plan_text)
        self.assertIn("One expression gate maximum", plan_text)
        self.assertIn("The next eligible live", plan_text)
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
