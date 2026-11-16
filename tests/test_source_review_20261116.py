"""Contribution and evidence boundaries from the November 16 source review.

These local tests exercise classification without claiming an online harvest or
depending on a future catalog snapshot containing every reviewed identity.
"""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import HIERARCHY, OVERRIDES, TAG_RULES, annotate_paper, normalize_text


class November16SourceReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = json.loads(
            (ROOT / "data/catalog-refresh-2026-11-16-source-review.json").read_text()
        )
        cls.records = {r["arxiv_id"]: r for r in cls.review["classification_reviews"]}

    def classify(self, arxiv_id, abstract=""):
        evidence = self.records[arxiv_id]
        paper = {
            "arxiv_id": arxiv_id,
            "title": evidence["title"],
            "published": evidence["arxiv_first_submission_on"],
            "year": int(evidence["arxiv_first_submission_on"][:4]),
            "venue": "arXiv",
            "track": "Manipulation & Imitation",
            "abstract": abstract,
        }
        return annotate_paper(deepcopy(paper))

    def test_review_is_targeted_and_does_not_certify_harvest_or_acceptance(self):
        review = self.review
        self.assertEqual(review["checked_on"], "2026-11-16")
        self.assertEqual(review["refresh_scope"], "targeted-source-review-only")
        self.assertFalse(review["harvest_completion_claimed"])
        self.assertEqual(review["conference_promotions"], [])
        self.assertIn("not full-paper review", review["scope"])
        self.assertIn("independent reproduction", review["scope"])
        self.assertEqual(len(review["baseline_commit"]), 40)

    def test_reviewed_overrides_use_real_paths_and_existing_topic_facets(self):
        self.assertEqual(len(self.records), 11)
        for arxiv_id, evidence in self.records.items():
            with self.subTest(arxiv_id=arxiv_id):
                override = OVERRIDES[normalize_text(evidence["title"])]
                self.assertEqual(override["title"], evidence["title"])
                self.assertEqual(override["path"], evidence["classification_path"])
                track, subcategory, specialty = override["path"]
                self.assertIn(specialty, {r[0] for r in HIERARCHY[track][subcategory]["specialties"]})
                self.assertEqual(evidence["arxiv_url"], "https://arxiv.org/abs/" + arxiv_id)
                self.assertIn(evidence["arxiv_url"], override["reason"])
                self.assertTrue(set(override.get("related_topics", [])) <= set(TAG_RULES["related_topics"]))
                self.assertTrue(set(override.get("excluded_topics", [])) <= set(TAG_RULES["related_topics"]))

    def test_touch_grounded_human_data_is_not_claimed_as_robot_retargeting(self):
        paper = self.classify(
            "2611.17619",
            "TouchScale tactile glove recordings ground simulated human hand-object replays. "
            "Related work uses dexterous hand retargeting and whole-body retargeting.",
        )
        self.assertEqual((paper["track"], paper["subcategory"], paper["specialty"]), (
            "Data, Simulation & Evaluation", "Synthetic & Augmented Data", "Simulated Trajectory Generation"
        ))
        self.assertIn("Contact-rich", paper["related_topics"])
        self.assertIn("Dexterous Manipulation", paper["related_topics"])
        self.assertFalse(set(paper["related_topics"]) & {"Retargeting", "Hand Retargeting", "Whole-body Retargeting"})
        self.assertEqual(paper["classification_status"], "reviewed")
        self.assertIn("not evidence of robot-hand retargeting", self.records["2611.17619"]["evidence_boundary"])

    def test_restricted_actuation_is_a_grasp_constraint_not_hardware_contribution(self):
        paper = self.classify(
            "2610.30969",
            "Support-aware grasp synthesis for irregular objects and low-DoF coupled hands. "
            "Graph matches and physical rollouts test contact feasibility and disturbance resistance.",
        )
        self.assertEqual((paper["track"], paper["subcategory"], paper["specialty"]), (
            "Dexterous Hands, Retargeting & Teleoperation", "Multifinger Grasping & Control",
            "Multifinger Coordination & Grasp Generation",
        ))
        self.assertNotIn("Hand Retargeting", paper["related_topics"])
        self.assertEqual(paper["published"], "2026-10-22")

    def test_residual_latents_are_not_additive_dexterous_action_control(self):
        expected = {
            "2611.17529": ("World Models, Planning & Embodied Reasoning", "Model-based Decision Making", "World-model Planning"),
            "2611.17775": ("Data, Simulation & Evaluation", "Benchmarks & Experimental Methods", "Reproducibility & Statistical Comparison"),
        }
        for arxiv_id, path in expected.items():
            with self.subTest(arxiv_id=arxiv_id):
                paper = self.classify(arxiv_id, "A lightweight residual representation adapter supports world-model planning or evaluation.")
                self.assertEqual((paper["track"], paper["subcategory"], paper["specialty"]), path)
                self.assertIn("World Models", paper["related_topics"])
                self.assertFalse(set(paper["related_topics"]) & {"Dexterous Manipulation", "Hand Retargeting", "Whole-body Retargeting"})

    def test_vlm_mpc_data_engine_modular_agent_and_rl_remain_distinct(self):
        expected = {
            "2611.18298": ("Model-based Decision Making", "Model Predictive Control"),
            "2611.17394": ("Synthetic & Augmented Data", "Simulated Trajectory Generation"),
            "2611.18176": ("VLA & Generalist Robot Policies", "Hierarchical & Mixture Policies"),
            "2611.18562": ("Reinforcement Learning", "Online Reinforcement Learning"),
        }
        for arxiv_id, path in expected.items():
            with self.subTest(arxiv_id=arxiv_id):
                paper = self.classify(arxiv_id)
                self.assertEqual((paper["subcategory"], paper["specialty"]), path)
                self.assertEqual(paper["venue"], "arXiv")

    def test_revision_and_listing_dates_do_not_rewrite_original_submission(self):
        iora = self.records["2610.30969"]
        voke = self.review["version_checks"][0]
        for evidence in (iora, voke):
            self.assertEqual(evidence["observed_version"], 2)
            self.assertEqual(evidence["version_submitted_on"], "2026-11-13")
            self.assertLess(evidence["arxiv_first_submission_on"], evidence["version_submitted_on"])
        for arxiv_id in ("2611.17394", "2611.17529"):
            paper = self.classify(arxiv_id)
            self.assertEqual(paper["published"], "2026-11-12")
            self.assertNotEqual(paper["published"], self.review["checked_on"])
        self.assertEqual(voke["classification_path"], [
            "Perception, Representation & State Estimation", "Object & Interaction Perception", "6D Pose & Tracking"
        ])

    def test_continuum_contact_and_journal_comments_do_not_create_hand_or_conference_evidence(self):
        paper = self.classify("2611.18546", "A continuum robot friction model under complementarity constraints.")
        self.assertEqual(paper["specialty"], "Object & Contact Dynamics")
        self.assertNotIn("Dexterous Manipulation", paper["related_topics"])
        self.assertNotIn("Hand Retargeting", paper["related_topics"])
        claims = self.review["publication_claim_reviews"]
        self.assertEqual({r["arxiv_id"] for r in claims}, {"2611.18546", "2611.15981"})
        for claim in claims:
            self.assertIn("author_stated", claim["action"])
            self.assertIn("not", claim["boundary"])
        self.assertEqual(paper["venue"], "arXiv")


if __name__ == "__main__":
    unittest.main()
