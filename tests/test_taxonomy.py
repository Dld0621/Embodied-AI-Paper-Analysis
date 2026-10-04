from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from taxonomy import GENERAL_SPECIALTY, HIERARCHY, OVERRIDES, TRACKS, annotate_paper, classify_hierarchy, taxonomy_metadata


def paper(title, abstract="", old_track="Dexterity & Teleoperation"):
    return {"title": title, "track": old_track, "abstract": abstract,
            "paper_url": "https://example.org/paper", "year": 2025}


class TaxonomyClassifierTests(unittest.TestCase):
    def test_approved_nine_direction_structure(self):
        meta = taxonomy_metadata()
        self.assertEqual(len(meta["tracks"]), 9)
        self.assertEqual(meta["subcategory_count"], 42)
        self.assertEqual(meta["specialty_count"], 126)
        self.assertEqual(meta["fallback_specialty_count"], 42)
        self.assertEqual(meta["version"], 4)

    def test_three_retargeting_families_share_one_parent(self):
        cases = {
            "DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation": "Contact & Functional Retargeting",
            "SPIDER: Scalable Physics-Informed Dexterous Retargeting": "Physics & Dynamics Retargeting",
            "Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm": "Kinematic & Pose Retargeting",
        }
        for title, expected in cases.items():
            with self.subTest(title=title):
                p = annotate_paper(paper(title))
                self.assertEqual(p["track"], TRACKS[2])
                self.assertEqual(p["subcategory"], "Dexterous Hand Retargeting")
                self.assertEqual(p["specialty"], expected)
                self.assertEqual(p["classification_status"], "reviewed")

    def test_reviewed_exceptions_use_only_declared_paths(self):
        for entry in OVERRIDES.values():
            track, sub, spec = entry["path"]
            self.assertIn(sub, HIERARCHY[track])
            self.assertIn(spec, [item[0] for item in HIERARCHY[track][sub]["specialties"]])
            self.assertTrue(entry["reason"])

    def test_annotation_is_idempotent_and_preserves_provenance(self):
        original = paper("SPIDER: Scalable Physics-Informed Dexterous Retargeting")
        p = annotate_paper(deepcopy(original))
        self.assertEqual(deepcopy(p), annotate_paper(p))
        self.assertEqual(p["admission_track"], original["track"])
        for field in ("paper_url", "year", "abstract"):
            self.assertEqual(p[field], original[field])

    def test_spider_is_found_from_hand_and_whole_body_views(self):
        p = annotate_paper(paper("SPIDER: Scalable Physics-Informed Dexterous Retargeting"))
        self.assertIn("Hand Retargeting", p["related_topics"])
        self.assertIn("Whole-body Retargeting", p["related_topics"])
        self.assertIn({"track": TRACKS[4], "subcategory": "Whole-body Motion Transfer"}, p["related_taxonomy_paths"])

    def test_parallel_jaw_grasp_transfer_is_not_hand_retargeting(self):
        title = "HOGraspFlow: Taxonomy-Aware Hand-Object Retargeting for Multi-Modal SE(3) Grasp Generation"
        p = annotate_paper(paper(title, "We generate parallel jaw grasps."))
        self.assertEqual(p["track"], TRACKS[1])
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_data_engine_has_primary_and_related_entries(self):
        title = "EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning"
        p = annotate_paper(paper(title))
        self.assertEqual(p["track"], TRACKS[7])
        self.assertIn("Hand Retargeting", p["related_topics"])
        self.assertIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"}, p["related_taxonomy_paths"])

    def test_generic_policy_world_model_and_hardware_have_distinct_entries(self):
        for title, expected in [
            ("Diffusion Policies for Robot Control", TRACKS[0]),
            ("Action-conditioned Video Prediction with World Models", TRACKS[6]),
            ("A New Tactile Sensor for Robot Hands", TRACKS[8]),
            ("LiDAR-Inertial Odometry for Mobile Robots", TRACKS[3]),
        ]:
            with self.subTest(title=title):
                self.assertEqual(annotate_paper(paper(title))["track"], expected)

    def test_whole_body_does_not_default_to_hand_retargeting(self):
        p = annotate_paper(paper("Motion Retargeting for Humanoid Whole-Body Control",
                                "We compare to robot hand retargeting in related work."))
        self.assertEqual(p["track"], TRACKS[4])
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_unknown_evidence_remains_in_review(self):
        p = annotate_paper(paper("A Study of Embodied Intelligence"))
        self.assertEqual(p["specialty"], GENERAL_SPECIALTY)
        self.assertEqual(p["classification_status"], "needs-review")

    def test_no_substring_matching_for_acronyms(self):
        p = annotate_paper(paper("A Scalar Algorithm for Robotics", old_track="Foundation Models & VLA"))
        self.assertNotIn("Reinforcement Learning", p["method_tags"])

    def test_diffusion_and_flow_are_separate_specialties(self):
        sub, spec, _ = classify_hierarchy(TRACKS[0], "Diffusion Policy for Robot Control")
        self.assertEqual(sub, "Generative Action Policies")
        self.assertEqual(spec, "Diffusion Policies")
        _, spec, _ = classify_hierarchy(TRACKS[0], "Flow Matching for Robot Control")
        self.assertEqual(spec, "Flow-matching Policies")

    def test_generic_dexterity_does_not_become_hand_retargeting(self):
        p = annotate_paper(paper("Learning Dexterous Manipulation with Quantized Hand State"))
        self.assertEqual(p["subcategory"], "Multifinger Grasping & Control")
        self.assertEqual(p["subcategory_status"], "provisional")
        self.assertEqual(p["classification_status"], "needs-review")
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_title_parent_controls_abstract_background_matches(self):
        cases = [
            ("Learning In-Hand Translation Using Tactile Skin with Shear and Normal Force Sensing", "In-hand Manipulation"),
            ("Learning Universal Dexterous Grasping with Synthetic Data", "Multifinger Grasping & Control"),
            ("A Shared Autonomy System for Dexterous Teleoperation", "Teleoperation & Shared Control"),
        ]
        for title, parent in cases:
            with self.subTest(title=title):
                p = annotate_paper(paper(title, "We compare baselines using hand retargeting, geometric retargeting and physics based retargeting."))
                self.assertEqual(p["subcategory"], parent)
                self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_abstract_terms_cannot_outvote_explicit_diffusion_title(self):
        p = annotate_paper(paper("Diffusion Policy for Robot Control",
                                "Baselines use flow matching, flow policy, flow policies, action token and action tokenizer."))
        self.assertEqual(p["specialty"], "Diffusion Policies")

    def test_hand_design_is_hardware_not_hand_retargeting(self):
        p = annotate_paper(paper("MultiHand: Design and Verification of a Dexterous Hand with Multi-modal Grasping Capabilities"))
        self.assertEqual(p["track"], TRACKS[8])
        self.assertEqual(p["subcategory"], "Mechanisms & Actuation")
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_simulation_framework_is_infrastructure_not_retargeting(self):
        p = annotate_paper(paper("ETac: A Lightweight and Efficient Tactile Simulation Framework for Learning Dexterous Manipulation"))
        self.assertEqual(p["track"], TRACKS[7])
        self.assertEqual(p["subcategory"], "Simulation & Digital Twins")
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_sensor_fusion_is_perception_not_sensor_hardware(self):
        p = annotate_paper(paper("Sensor Fusion for State Estimation in Humanoid Robots"))
        self.assertEqual(p["track"], TRACKS[5])

    def test_retargeting_topics_are_hierarchically_consistent(self):
        for title in ("SPIDER: Scalable Physics-Informed Dexterous Retargeting",
                      "Motion Retargeting for Humanoid Whole-Body Control"):
            p = annotate_paper(paper(title))
            self.assertIn("Retargeting", p["related_topics"])
            self.assertTrue(set(p["related_topics"]) & {"Hand Retargeting", "Whole-body Retargeting"})

    def test_negative_title_cannot_support_demonstration_transfer(self):
        p = annotate_paper(paper("CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations",
                                "Other approaches learn from human demonstrations and human videos."))
        self.assertNotEqual(p["subcategory"], "Human Demonstrations to Dexterous Skills")

    def test_retargeting_free_title_does_not_acquire_hand_retargeting(self):
        p = annotate_paper(paper("Dexterous Hand Control without Retargeting"))
        self.assertNotEqual(p["subcategory"], "Dexterous Hand Retargeting")
        self.assertNotIn("Hand Retargeting", p["related_topics"])

    def test_force_feedback_glove_is_a_device_contribution(self):
        p = annotate_paper(paper("CDF-Glove: A Cable-Driven Force Feedback Glove for Dexterous Teleoperation"))
        self.assertEqual(p["track"], TRACKS[8])
        self.assertEqual(p["subcategory"], "Sensors & Human Interfaces")


if __name__ == "__main__":
    unittest.main()
