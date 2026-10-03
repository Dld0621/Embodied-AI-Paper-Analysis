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
        self.assertEqual(meta["version"], 3)

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


if __name__ == "__main__":
    unittest.main()
