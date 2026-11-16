"""Title/abstract-only contribution review for the 2026-10-30 catalog refresh."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import GENERAL_SPECIALTY, HIERARCHY, OVERRIDES, TRACKS, annotate_paper, normalize_text


CASES = {
    "2610.39582": (
        "Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment",
        (TRACKS[2], "Dexterous Hand Retargeting", "Physics & Dynamics Retargeting"),
        ("Hand Retargeting", "Retargeting", "Contact-rich"),
    ),
    "2610.40349": (
        "TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Video-to-robot Demonstrations"),
        ("Hand Retargeting", "Retargeting", "Contact-rich"),
    ),
    "2610.40210": (
        "AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Demonstration Refinement & Skill Transfer"),
        ("Dexterous Manipulation", "Bimanual"),
    ),
    "2610.40646": (
        "SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing",
        (TRACKS[8], "Mechanisms & Actuation", "Hands, Grippers & Arms"),
        ("Contact-rich", "Teleoperation"),
    ),
    "2610.39367": (
        "Utility-WAM: Correcting Future-Induced Action Changes",
        (TRACKS[0], "VLA & Generalist Robot Policies", GENERAL_SPECIALTY),
        ("World Models",),
    ),
    "2610.40016": (
        "LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks",
        (TRACKS[6], "Memory & Autonomous Execution", "Failure Detection & Replanning"),
        ("World Models",),
    ),
    "2610.40026": (
        "RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence",
        (TRACKS[7], "Benchmarks & Experimental Methods", "Reproducibility & Statistical Comparison"),
        ("World Models",),
    ),
    "2610.40356": (
        "JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning",
        (TRACKS[0], "Imitation Learning", "Behavior Cloning & Sequence Modeling"),
        (),
    ),
    "2610.39528": (
        "PRIME W0: Physical Priors from World Models for Embodied Manipulation",
        (TRACKS[0], "VLA & Generalist Robot Policies", "Hierarchical & Mixture Policies"),
        ("World Models",),
    ),
    "2610.39385": (
        "UMI-Live for In-The-Wild Bimanual Robotics Data Collection",
        (TRACKS[7], "Datasets & Data Engineering", "Robot Demonstration Datasets"),
        ("Bimanual", "Teleoperation"),
    ),
}

# Source identities of the 49 reviewed records in baseline fc44c1e. These
# fixtures do not require Git history, so shallow CI checkouts remain supported.
PREVIOUS_REVIEWED_ARXIV_IDS = {
    "2402.04820", "2503.07541", "2505.01083", "2505.24853", "2506.09384", "2507.03227",
    "2509.16871", "2511.09484", "2601.07284", "2602.00915", "2603.29213", "2605.12182",
    "2606.16272", "2606.17385", "2607.03828", "2607.05883", "2607.07491", "2607.08341",
    "2607.11874", "2608.07045", "2608.15560", "2609.24093", "2609.28660", "2610.01849",
    "2610.02338", "2610.06331", "2610.07681", "2610.08425", "2610.10528", "2610.12026",
    "2610.12440", "2610.13024", "2610.13119", "2610.17572", "2610.17789", "2610.18443",
    "2610.20904", "2610.26762", "2610.27998", "2610.28628", "2610.29997", "2610.31334",
    "2610.31474", "2610.31613", "2610.31617", "2610.31661",
}
PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES = {
    ("DexTele: A Dual-Arm Dexterous Teleoperation System Based on Motion Retargeting and Adaptive Force Control", "ICRA"),
    ("Pose Retargeting from a Single RGB Camera: Optimization-Based Hand Pose Retargeting and Wrist Pose Estimation", "ICRA"),
    ("Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm", "IROS"),
}


class October30TaxonomyReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arxiv = json.loads((ROOT / "data/arxiv_recent.json").read_text())
        cls.records = {p["arxiv_id"]: p for p in cls.arxiv["papers"]}
        cls.conference = json.loads((ROOT / "data/papers.json").read_text())["papers"]

    def test_ten_exact_titles_ids_and_paths_use_only_declared_schema(self):
        keys = {normalize_text(case[0]) for case in CASES.values()}
        matches = [p for p in self.arxiv["papers"] if normalize_text(p["title"]) in keys]
        self.assertEqual(len(matches), len(CASES))
        self.assertEqual({p["arxiv_id"] for p in matches}, set(CASES))
        self.assertTrue(all(normalize_text(p["title"]) not in keys for p in self.conference))
        for identifier, (title, path, _) in CASES.items():
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                self.assertEqual(original["title"], title)
                self.assertGreater(original["published"], "2026-10-24")
                entry = OVERRIDES[normalize_text(title)]
                self.assertEqual(entry["title"], title)
                self.assertEqual(tuple(entry["path"]), path)
                track, subcategory, specialty = path
                self.assertIn(subcategory, HIERARCHY[track])
                if specialty != GENERAL_SPECIALTY:
                    self.assertIn(specialty, [item[0] for item in HIERARCHY[track][subcategory]["specialties"]])

    def test_core_paths_topics_and_evidence_do_not_claim_full_paper_review(self):
        for identifier, (_, path, topics) in CASES.items():
            with self.subTest(identifier=identifier):
                annotated = annotate_paper(deepcopy(self.records[identifier]))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                status = "needs-review" if path[2] == GENERAL_SPECIALTY else "reviewed"
                self.assertEqual(annotated["classification_status"], status)
                self.assertTrue(set(topics).issubset(annotated["related_topics"]))
                reason = annotated["taxonomy_evidence"]
                self.assertIn("Title/abstract-only classification review", reason)
                self.assertIn("not full-paper reading or experiment reproduction", reason)
                self.assertIn(f"https://arxiv.org/abs/{identifier}", reason)

    def test_annotation_preserves_source_fields_and_is_idempotent(self):
        fields = ("arxiv_id", "title", "authors", "abstract", "published", "year", "venue",
                  "paper_url", "pdf_url", "official_url", "source_type", "discovery_source",
                  "primary_category", "admission_track")
        for identifier in CASES:
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                annotated = annotate_paper(deepcopy(original))
                for field in fields:
                    self.assertEqual(annotated[field], original[field])
                self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))

    def test_extended_titles_do_not_inherit_reviewed_exceptions(self):
        for identifier, (title, _, _) in CASES.items():
            for changed in ("A Review of " + title, title + ": A New Benchmark"):
                with self.subTest(identifier=identifier, changed=changed):
                    record = deepcopy(self.records[identifier])
                    record["title"] = changed
                    self.assertNotIn(normalize_text(changed), OVERRIDES)
                    self.assertNotEqual(annotate_paper(record)["classification_status"], "reviewed")

    def test_tactile_transfer_association_does_not_replace_primary_skill_path(self):
        bridge = annotate_paper(deepcopy(self.records["2610.40349"]))
        self.assertNotEqual(bridge["subcategory"], "Dexterous Hand Retargeting")
        self.assertIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"},
                      bridge["related_taxonomy_paths"])
        across = annotate_paper(deepcopy(self.records["2610.40210"]))
        self.assertEqual(across["subcategory"], "Human Demonstrations to Dexterous Skills")
        self.assertNotIn("Hand Retargeting", across["related_topics"])
        self.assertNotIn("Whole-body Retargeting", across["related_topics"])

    def test_policy_correction_keeps_precise_leaf_uncertainty_visible(self):
        utility = annotate_paper(deepcopy(self.records["2610.39367"]))
        self.assertEqual(utility["specialty"], GENERAL_SPECIALTY)
        self.assertEqual(utility["classification_status"], "needs-review")
        self.assertEqual(utility["subcategory"], "VLA & Generalist Robot Policies")
        self.assertIn("World Models", utility["related_topics"])
        self.assertIn("schema lacks an exact specialty", utility["taxonomy_evidence"])
        jedi = annotate_paper(deepcopy(self.records["2610.40356"]))
        self.assertEqual(jedi["track"], TRACKS[0])
        self.assertIn("does not assert", jedi["taxonomy_evidence"])

    def test_previous_49_reviewed_source_records_remain_reviewed(self):
        self.assertEqual(len(PREVIOUS_REVIEWED_ARXIV_IDS) + len(PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES), 49)
        for identifier in PREVIOUS_REVIEWED_ARXIV_IDS:
            with self.subTest(arxiv_id=identifier):
                self.assertIn(identifier, self.records)
                self.assertEqual(annotate_paper(deepcopy(self.records[identifier]))["classification_status"], "reviewed")
        conference = {(p["title"], p["venue"]): p for p in self.conference}
        for identity in PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES:
            with self.subTest(conference=identity):
                self.assertIn(identity, conference)
                self.assertEqual(annotate_paper(deepcopy(conference[identity]))["classification_status"], "reviewed")

    def test_defensible_world_model_and_pending_device_paths_are_not_forced(self):
        paths = {
            "2610.40401": (TRACKS[6], "World & Dynamics Modeling", "Latent Dynamics"),
            "2610.35462": (TRACKS[7], "Datasets & Data Engineering", GENERAL_SPECIALTY),
            "2610.36539": (TRACKS[2], "Dexterous Hand Retargeting", "Contact & Functional Retargeting"),
        }
        for identifier, path in paths.items():
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                self.assertNotIn(normalize_text(original["title"]), OVERRIDES)
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertNotEqual(annotated["classification_status"], "reviewed")


if __name__ == "__main__":
    unittest.main()
