"""Title/abstract-only review boundaries for the 2026-11-04 arXiv refresh."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import GENERAL_SPECIALTY, HIERARCHY, OVERRIDES, TRACKS, annotate_paper, normalize_text


CASES = {
    "2611.05023": (
        "HiLo-WAM: Decoupling Long-Horizon Task Evolution and Local Dynamics in World Action Models",
        (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
        ("World Models",),
    ),
    "2611.04870": (
        "PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations",
        (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
        ("World Models",),
    ),
    "2611.05080": (
        "CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation",
        (TRACKS[7], "Benchmarks & Experimental Methods", "Task & Capability Benchmarks"),
        (),
    ),
    "2611.05093": (
        "LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models",
        (TRACKS[7], "Benchmarks & Experimental Methods", "Reproducibility & Statistical Comparison"),
        (),
    ),
    "2611.04226": (
        "DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution",
        (TRACKS[6], "Memory & Autonomous Execution", "Failure Detection & Replanning"),
        (),
    ),
    "2611.04083": (
        "MABEL: An Open Anthropomorphic Mobile Bimanual Platform for Teleoperation and Learning",
        (TRACKS[8], "Mechanisms & Actuation", "Hands, Grippers & Arms"),
        ("Bimanual", "Teleoperation"),
    ),
    "2611.02968": (
        "ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation",
        (TRACKS[4], "Whole-body Motion Transfer", "Contact & Dynamic Retargeting"),
        ("Retargeting", "Whole-body Retargeting", "Contact-rich"),
    ),
    "2611.05163": (
        "RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Video-to-robot Demonstrations"),
        ("Bimanual",),
    ),
    "2611.04527": (
        "Future Representation Distillation for Imagination-Free World Action Models",
        (TRACKS[0], "VLA & Generalist Robot Policies", GENERAL_SPECIALTY),
        ("World Models",),
    ),
    "2611.05368": (
        "GUILD: Guided Iterative Data Collection for Imitation Learning",
        (TRACKS[7], "Datasets & Data Engineering", "Data Curation & Quality"),
        ("Teleoperation",),
    ),
}

# The 58 reviewed source identities in baseline 31288a7. Keep fixtures local so
# shallow CI checkouts do not need the historical Git objects to run the tests.
PREVIOUS_REVIEWED_ARXIV_IDS = {
    "2402.04820", "2503.07541", "2505.01083", "2505.24853", "2506.09384", "2507.03227",
    "2509.16871", "2511.09484", "2601.07284", "2602.00915", "2603.29213", "2605.12182",
    "2606.16272", "2606.17385", "2607.03828", "2607.05883", "2607.07491", "2607.08341",
    "2607.11874", "2608.07045", "2608.15560", "2609.24093", "2609.28660", "2610.01849",
    "2610.02338", "2610.06331", "2610.07681", "2610.08425", "2610.10528", "2610.12026",
    "2610.12440", "2610.13024", "2610.13119", "2610.17572", "2610.17789", "2610.18443",
    "2610.20904", "2610.26762", "2610.27998", "2610.28628", "2610.29997", "2610.31334",
    "2610.31474", "2610.31613", "2610.31617", "2610.31661", "2610.39385", "2610.39528",
    "2610.39582", "2610.40016", "2610.40026", "2610.40210", "2610.40349", "2610.40356",
    "2610.40646",
}
PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES = {
    ("DexTele: A Dual-Arm Dexterous Teleoperation System Based on Motion Retargeting and Adaptive Force Control", "ICRA"),
    ("Pose Retargeting from a Single RGB Camera: Optimization-Based Hand Pose Retargeting and Wrist Pose Estimation", "ICRA"),
    ("Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm", "IROS"),
}


class November4TaxonomyReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arxiv = json.loads((ROOT / "data/arxiv_recent.json").read_text())
        cls.records = {p["arxiv_id"]: p for p in cls.arxiv["papers"]}
        cls.conference = json.loads((ROOT / "data/papers.json").read_text())["papers"]

    def test_ten_exact_arxiv_titles_have_legal_paths_and_no_conference_title_collision(self):
        keys = {normalize_text(case[0]) for case in CASES.values()}
        matches = [p for p in self.arxiv["papers"] if normalize_text(p["title"]) in keys]
        self.assertEqual(len(matches), len(CASES))
        self.assertEqual({p["arxiv_id"] for p in matches}, set(CASES))
        self.assertTrue(all(normalize_text(p["title"]) not in keys for p in self.conference))
        for identifier, (title, path, _) in CASES.items():
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                self.assertEqual(original["title"], title)
                self.assertGreater(original["published"], "2026-10-30")
                entry = OVERRIDES[normalize_text(title)]
                self.assertEqual(entry["title"], title)
                self.assertEqual(tuple(entry["path"]), path)
                track, subcategory, specialty = path
                self.assertIn(subcategory, HIERARCHY[track])
                if specialty != GENERAL_SPECIALTY:
                    self.assertIn(specialty, [item[0] for item in HIERARCHY[track][subcategory]["specialties"]])

    def test_reviewed_paths_topics_and_evidence_keep_full_paper_claims_out(self):
        for identifier, (_, path, topics) in CASES.items():
            with self.subTest(identifier=identifier):
                annotated = annotate_paper(deepcopy(self.records[identifier]))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertEqual(annotated["classification_status"],
                                 "needs-review" if path[2] == GENERAL_SPECIALTY else "reviewed")
                self.assertTrue(set(topics).issubset(annotated["related_topics"]))
                evidence = annotated["taxonomy_evidence"]
                self.assertIn("Title/abstract-only classification review", evidence)
                self.assertIn("not full-paper reading or experiment reproduction", evidence)
                self.assertIn(f"https://arxiv.org/abs/{identifier}", evidence)

    def test_annotation_preserves_source_metadata_and_is_idempotent(self):
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

    def test_extended_titles_do_not_inherit_exact_reviewed_exceptions(self):
        for identifier, (title, _, _) in CASES.items():
            for changed in ("A Review of " + title, title + ": A New Benchmark"):
                with self.subTest(identifier=identifier, changed=changed):
                    record = deepcopy(self.records[identifier])
                    record["title"] = changed
                    self.assertNotIn(normalize_text(changed), OVERRIDES)
                    self.assertNotEqual(annotate_paper(record)["classification_status"], "reviewed")

    def test_whole_body_retargeting_and_video_synthesis_do_not_pollute_hand_retargeting(self):
        whole_body = annotate_paper(deepcopy(self.records["2611.02968"]))
        self.assertIn("Whole-body Retargeting", whole_body["related_topics"])
        self.assertNotIn("Hand Retargeting", whole_body["related_topics"])
        self.assertNotEqual(whole_body["subcategory"], "Dexterous Hand Retargeting")
        video = annotate_paper(deepcopy(self.records["2611.05163"]))
        self.assertEqual(video["subcategory"], "Human Demonstrations to Dexterous Skills")
        self.assertTrue({"Retargeting", "Hand Retargeting", "Whole-body Retargeting"}.isdisjoint(video["related_topics"]))
        self.assertFalse(any(p["subcategory"] == "Dexterous Hand Retargeting"
                             for p in whole_body["related_taxonomy_paths"] + video["related_taxonomy_paths"]))

    def test_dreamfree_and_existing_pending_overrides_remain_uncertain(self):
        dreamfree = annotate_paper(deepcopy(self.records["2611.04527"]))
        self.assertEqual(dreamfree["specialty"], GENERAL_SPECIALTY)
        self.assertEqual(dreamfree["classification_status"], "needs-review")
        self.assertEqual(dreamfree["subcategory"], "VLA & Generalist Robot Policies")
        self.assertIn("schema lacks an exact specialty", dreamfree["taxonomy_evidence"])
        self.assertIn("neither reinforcement learning nor", dreamfree["taxonomy_evidence"])
        utility = annotate_paper(deepcopy(self.records["2610.39367"]))
        self.assertEqual(utility["specialty"], GENERAL_SPECIALTY)
        self.assertEqual(utility["classification_status"], "needs-review")
        handshake = next(p for p in self.conference if p["title"] ==
                         "Contributing Factors in Human-Robot Handshake: Compliance, Hand Grip, and Synchrony")
        self.assertEqual(annotate_paper(deepcopy(handshake))["classification_status"], "needs-review")

    def test_previous_58_reviewed_source_identities_remain_reviewed(self):
        self.assertEqual(len(PREVIOUS_REVIEWED_ARXIV_IDS) + len(PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES), 58)
        for identifier in PREVIOUS_REVIEWED_ARXIV_IDS:
            with self.subTest(arxiv_id=identifier):
                self.assertIn(identifier, self.records)
                self.assertEqual(annotate_paper(deepcopy(self.records[identifier]))["classification_status"], "reviewed")
        conference = {(p["title"], p["venue"]): p for p in self.conference}
        for identity in PREVIOUS_REVIEWED_CONFERENCE_IDENTITIES:
            with self.subTest(conference=identity):
                self.assertIn(identity, conference)
                self.assertEqual(annotate_paper(deepcopy(conference[identity]))["classification_status"], "reviewed")

    def test_defensible_automatic_paths_and_distinct_pact_title_are_not_forced(self):
        paths = {
            "2611.05119": (TRACKS[2], "Multifinger Grasping & Control", GENERAL_SPECIALTY),
            "2611.05302": (TRACKS[8], "Mechanisms & Actuation", "Actuators & Transmission"),
            "2611.03520": (TRACKS[8], "Sensors & Human Interfaces", "Tactile & Force Sensors"),
            "2611.04424": (TRACKS[4], "Whole-body Coordination & Balance", "Whole-body Optimization & Control"),
        }
        for identifier, path in paths.items():
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                self.assertNotIn(normalize_text(original["title"]), OVERRIDES)
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertNotEqual(annotated["classification_status"], "reviewed")
        dexhot = annotate_paper(deepcopy(self.records["2611.05119"]))
        self.assertNotIn("Hand Retargeting", dexhot["related_topics"])
        self.assertIn("without human reference motions", self.records["2611.05119"]["abstract"])
        self.assertNotEqual(self.records["2611.05302"]["title"], self.records["2610.18443"]["title"])


if __name__ == "__main__":
    unittest.main()
