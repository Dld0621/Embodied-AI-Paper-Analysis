from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from taxonomy import GENERAL_SPECIALTY, HIERARCHY, OVERRIDES, TRACKS, annotate_paper, classify_hierarchy, normalize_text, taxonomy_metadata

ROOT = Path(__file__).resolve().parents[1]
NEW_ARXIV_REVIEW_CASES = {
    "2610.06331": ("DexForge: High-Fidelity Physics-Informed Dexterous Retargeting",
                   (TRACKS[2], "Dexterous Hand Retargeting", "Physics & Dynamics Retargeting"),
                   "A differentiable simulator combines contact-aware kinematic retargeting with force-aware dynamics refinement."),
    "2610.07681": ("EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors",
                   (TRACKS[0], "Reinforcement Learning", "Online Reinforcement Learning"),
                   "Human-derived eigenvectors structure correlated exploration in dexterous reinforcement learning without changing the action representation."),
    "2610.08425": ("MIM-VLA: Learning Physical Interaction Representations from Gripper Motor Feedback",
                   (TRACKS[0], "VLA & Generalist Robot Policies", "Vision-Language-Action Modeling"),
                   "A learned interaction token from existing motor feedback conditions only the gripper-action pathway of SmolVLA."),
    "2610.02338": ("SoTa: Soft Tactile Skins for Dexterous Manipulation",
                   (TRACKS[8], "Sensors & Human Interfaces", "Tactile & Force Sensors"),
                   "A low-cost capacitive tactile skin supplies corresponding taxel layouts on human and robot hands, evaluated in demonstration co-training."),
    "2610.10528": ("Long-WAM: Scaling the Context of World-Action Models",
                   (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
                   "Causal world-action models use autoregressive video pretraining and streaming future-video prediction for real-time control."),
}
WEEKLY_ARXIV_REVIEW_CASES = {
    "2610.12440": (
        "Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation",
        (TRACKS[2], "Dexterous Hand Retargeting", "Physics & Dynamics Retargeting"),
        ("Hand Retargeting",),
    ),
    "2610.18443": (
        "PACT: Posture-Aligned Co-Design Technique for Hand Configuration and Retargeting in Multi-Finger Imitation Learning",
        (TRACKS[8], "Mechanisms & Actuation", "Hands, Grippers & Arms"),
        ("Hand Retargeting",),
    ),
    "2610.12026": (
        "HWAM: Humanoid World Action Model With Joint State--Action Generation",
        (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
        ("World Models",),
    ),
    "2610.13024": (
        "What Visual Representations Do World Action Models Need?",
        (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
        ("World Models",),
    ),
    "2610.17572": (
        "EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization",
        (TRACKS[2], "Dexterous Hand Retargeting", "Contact & Functional Retargeting"),
        ("Hand Retargeting",),
    ),
    "2610.13119": (
        "Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Video-to-robot Demonstrations"),
        ("Hand Retargeting",),
    ),
    "2610.17789": (
        "DexStitch: Learning and Composing Dexterous Skills from Human Videos via Contact-Aware Robotic Inpainting",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Video-to-robot Demonstrations"),
        ("Hand Retargeting",),
    ),
}
UPDATED_SOURCE_REVIEW_CASES = {
    "https://arxiv.org/abs/2601.07284": (
        "SHARE: Sharing Human Actions across Robot Embodiments through Unified Retargeting and Tracking",
        (TRACKS[4], "Whole-body Motion Transfer", "Motion Imitation & Generation"),
        "reviewed",
        ("Whole-body Retargeting", "Retargeting"),
    ),
    "https://arxiv.org/abs/2602.00915": (
        "DiffMorphGrasp: A Diffusion Framework Conditioned on Hand Morphology for Cross-Embodiment Grasp Generation",
        (TRACKS[2], "Multifinger Grasping & Control", "Multifinger Coordination & Grasp Generation"),
        "reviewed",
        ("Dexterous Manipulation",),
    ),
    "https://doi.org/10.1109/ICRA57385.2026.11696443": (
        "Contributing Factors in Human-Robot Handshake: Compliance, Hand Grip, and Synchrony",
        (TRACKS[2], "Multifinger Grasping & Control", GENERAL_SPECIALTY),
        "needs-review",
        (),
    ),
}


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
        declared = taxonomy_metadata()["tracks"]
        for entry in OVERRIDES.values():
            track, sub, spec = entry["path"]
            self.assertIn(sub, HIERARCHY[track])
            self.assertIn(spec, declared[track]["subcategories"][sub]["specialties"])
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

    def test_five_new_arxiv_exceptions_follow_core_contribution_not_background(self):
        for identifier, (title, path, abstract) in NEW_ARXIV_REVIEW_CASES.items():
            with self.subTest(identifier=identifier):
                original = paper(title, abstract)
                original.update(arxiv_id=identifier, source_type="arxiv", year=2026,
                                paper_url=f"https://arxiv.org/abs/{identifier}")
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[key] for key in ("track", "subcategory", "specialty")), path)
                self.assertEqual(annotated["classification_status"], "reviewed")
                self.assertIn("Title/abstract-only", annotated["taxonomy_evidence"])
                self.assertIn("not full-paper reading", annotated["taxonomy_evidence"])
                self.assertIn(original["paper_url"], annotated["taxonomy_evidence"])
                for field in ("arxiv_id", "source_type", "year", "paper_url", "abstract"):
                    self.assertEqual(annotated[field], original[field])
                self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))

    def test_new_exceptions_match_exact_titles_not_incidental_method_terms(self):
        for identifier, (title, _, abstract) in NEW_ARXIV_REVIEW_CASES.items():
            with self.subTest(identifier=identifier):
                key = normalize_text(title)
                self.assertIn(key, OVERRIDES)
                self.assertIn(f"https://arxiv.org/abs/{identifier}", OVERRIDES[key]["reason"])
                self.assertNotEqual(annotate_paper(paper("A Review of " + title, abstract))["classification_status"], "reviewed")

    def test_new_exception_titles_hit_only_the_five_declared_arxiv_records(self):
        keys = {normalize_text(case[0]) for case in NEW_ARXIV_REVIEW_CASES.values()}
        arxiv = json.loads((ROOT / "data" / "arxiv_recent.json").read_text())
        matched = [p for p in arxiv["papers"] if normalize_text(p["title"]) in keys]
        self.assertEqual(len(matched), len(NEW_ARXIV_REVIEW_CASES))
        self.assertEqual({p["arxiv_id"] for p in matched}, set(NEW_ARXIV_REVIEW_CASES))
        for p in matched:
            title, expected_path, _ = NEW_ARXIV_REVIEW_CASES[p["arxiv_id"]]
            self.assertEqual(p["title"], title)
            self.assertEqual(p["source_type"], "arxiv")
            annotated = annotate_paper(deepcopy(p))
            self.assertEqual(tuple(annotated[key] for key in ("track", "subcategory", "specialty")), expected_path)

    def test_reviewed_arxiv_titles_do_not_match_conference_records(self):
        conference = json.loads((ROOT / "data" / "papers.json").read_text())
        cases = {**NEW_ARXIV_REVIEW_CASES, **WEEKLY_ARXIV_REVIEW_CASES}
        keys = {normalize_text(case[0]) for case in cases.values()}
        for original in conference["papers"]:
            self.assertNotIn(normalize_text(original["title"]), keys)

    def test_weekly_reviewed_paths_topics_and_provenance_are_idempotent(self):
        arxiv = json.loads((ROOT / "data" / "arxiv_recent.json").read_text())
        records = {p["arxiv_id"]: p for p in arxiv["papers"]}
        for identifier, (title, path, expected_topics) in WEEKLY_ARXIV_REVIEW_CASES.items():
            with self.subTest(identifier=identifier):
                self.assertIn(identifier, records)
                original = records[identifier]
                self.assertEqual(original["title"], title)
                self.assertEqual(original["source_type"], "arxiv")
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertEqual(annotated["classification_status"], "reviewed")
                self.assertTrue(set(expected_topics).issubset(annotated["related_topics"]))
                reason = annotated["taxonomy_evidence"]
                self.assertIn("Title/abstract-only", reason)
                self.assertIn("not full-paper reading or experiment reproduction", reason)
                self.assertIn(f"https://arxiv.org/abs/{identifier}", reason)
                for field in ("arxiv_id", "source_type", "year", "published", "paper_url",
                              "official_url", "abstract", "admission_track"):
                    self.assertEqual(annotated[field], original[field])
                if "Hand Retargeting" in expected_topics:
                    self.assertIn("Retargeting", annotated["related_topics"])
                    if path[1] != "Dexterous Hand Retargeting":
                        self.assertIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"},
                                      annotated["related_taxonomy_paths"])
                else:
                    self.assertNotIn("Hand Retargeting", annotated["related_topics"])
                self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))

    def test_weekly_exceptions_match_only_the_seven_exact_arxiv_titles(self):
        arxiv = json.loads((ROOT / "data" / "arxiv_recent.json").read_text())
        keys = {normalize_text(case[0]) for case in WEEKLY_ARXIV_REVIEW_CASES.values()}
        matches = [p for p in arxiv["papers"] if normalize_text(p["title"]) in keys]
        self.assertEqual(len(matches), len(WEEKLY_ARXIV_REVIEW_CASES))
        self.assertEqual({p["arxiv_id"] for p in matches}, set(WEEKLY_ARXIV_REVIEW_CASES))
        for identifier, (title, path, _) in WEEKLY_ARXIV_REVIEW_CASES.items():
            with self.subTest(identifier=identifier):
                entry = OVERRIDES[normalize_text(title)]
                self.assertEqual(entry["title"], title)
                self.assertEqual(tuple(entry["path"]), path)
                track, sub, spec = path
                self.assertIn(sub, HIERARCHY[track])
                self.assertIn(spec, [item[0] for item in HIERARCHY[track][sub]["specialties"]])
                for extended_title in ("A Review of " + title, title + ": A New Benchmark"):
                    extended = annotate_paper(paper(extended_title))
                    self.assertNotEqual(extended["classification_status"], "reviewed")
                    self.assertNotIn(normalize_text(extended_title), OVERRIDES)

    def test_weekly_demonstration_papers_keep_primary_paths_and_gain_related_view(self):
        for identifier in ("2610.13119", "2610.17789"):
            title, path, _ = WEEKLY_ARXIV_REVIEW_CASES[identifier]
            annotated = annotate_paper(paper(title))
            self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
            self.assertNotEqual(annotated["subcategory"], "Dexterous Hand Retargeting")
            self.assertIn("Hand Retargeting", annotated["related_topics"])
            self.assertIn("Retargeting", annotated["related_topics"])
            self.assertIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"},
                          annotated["related_taxonomy_paths"])

    def test_updated_source_reviews_preserve_source_metadata_and_are_idempotent(self):
        arxiv = json.loads((ROOT / "data" / "arxiv_recent.json").read_text())["papers"]
        conference = json.loads((ROOT / "data" / "papers.json").read_text())["papers"]
        for url, (title, path, status, topics) in UPDATED_SOURCE_REVIEW_CASES.items():
            with self.subTest(url=url):
                source = arxiv if url.startswith("https://arxiv.org/") else conference
                matches = [p for p in source if p["title"] == title and p["official_url"] == url]
                self.assertEqual(len(matches), 1)
                original = matches[0]
                if url.startswith("https://arxiv.org/"):
                    self.assertEqual(original["arxiv_id"], url.rsplit("/", 1)[-1])
                    self.assertLess(original["published"], "2026-10-08")
                    self.assertEqual(original["source_type"], "arxiv")
                else:
                    self.assertEqual(original["venue"], "ICRA")
                    self.assertEqual(original["source_type"], "publisher")
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertEqual(annotated["classification_status"], status)
                self.assertTrue(set(topics).issubset(annotated["related_topics"]))
                self.assertNotIn("Hand Retargeting", annotated["related_topics"])
                self.assertNotIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"},
                                 annotated["related_taxonomy_paths"])
                self.assertIn("Title/abstract-only", annotated["taxonomy_evidence"])
                self.assertIn("not full-paper reading or experiment reproduction", annotated["taxonomy_evidence"])
                self.assertIn(url, annotated["taxonomy_evidence"])
                for field in ("arxiv_id", "source_type", "year", "published", "paper_url",
                              "official_url", "abstract", "admission_track", "venue"):
                    self.assertEqual(annotated.get(field), original.get(field))
                self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))

    def test_updated_source_exceptions_do_not_match_extended_titles(self):
        for title, _, _, _ in UPDATED_SOURCE_REVIEW_CASES.values():
            for extended_title in ("A Review of " + title, title + ": A New Benchmark"):
                with self.subTest(title=extended_title):
                    self.assertNotIn(normalize_text(extended_title), OVERRIDES)
                    annotated = annotate_paper(paper(extended_title))
                    self.assertFalse(annotated["taxonomy_evidence"].startswith("reviewed:"))

    def test_pending_override_keeps_uncertainty_without_changing_resolved_exceptions(self):
        pending = {}
        for entry in OVERRIDES.values():
            with self.subTest(title=entry["title"]):
                annotated = annotate_paper(paper(entry["title"]))
                if entry["path"][2] == GENERAL_SPECIALTY:
                    pending[entry["title"]] = annotated
                    self.assertEqual(annotated["classification_status"], "needs-review")
                    self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")),
                                     tuple(entry["path"]))
                    self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))
                else:
                    self.assertEqual(annotated["classification_status"], "reviewed")
        handshake = UPDATED_SOURCE_REVIEW_CASES[
            "https://doi.org/10.1109/ICRA57385.2026.11696443"][0]
        utility = "Utility-WAM: Correcting Future-Induced Action Changes"
        self.assertEqual(set(pending), {handshake, utility})
        self.assertIn("lacks a precise physical-HRI specialty", pending[handshake]["taxonomy_evidence"])
        self.assertIn("schema lacks an exact specialty", pending[utility]["taxonomy_evidence"])

    def test_updated_whole_body_transfer_and_grasp_generation_are_not_hand_retargeting(self):
        share = annotate_paper(paper(UPDATED_SOURCE_REVIEW_CASES["https://arxiv.org/abs/2601.07284"][0]))
        self.assertIn("Whole-body Retargeting", share["related_topics"])
        self.assertIn("Retargeting", share["related_topics"])
        self.assertNotIn("Hand Retargeting", share["related_topics"])
        grasp = annotate_paper(paper(UPDATED_SOURCE_REVIEW_CASES["https://arxiv.org/abs/2602.00915"][0]))
        self.assertNotIn("Hand Retargeting", grasp["related_topics"])
        self.assertNotIn("Whole-body Retargeting", grasp["related_topics"])


if __name__ == "__main__":
    unittest.main()
