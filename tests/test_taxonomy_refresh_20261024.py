"""Exact-title, title/abstract-only classification checks for the 2026-10-24 refresh."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import HIERARCHY, OVERRIDES, TRACKS, annotate_paper, normalize_text


CASES = {
    "2610.26762": (
        "DexOAK: Object-Aware Kinematic Retargeting",
        (TRACKS[2], "Dexterous Hand Retargeting", "Contact & Functional Retargeting"),
        ("Hand Retargeting", "Retargeting", "Contact-rich"),
        (),
    ),
    "2610.29997": (
        "DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations",
        (TRACKS[2], "Human Demonstrations to Dexterous Skills", "Demonstration Refinement & Skill Transfer"),
        ("Hand Retargeting", "Retargeting", "Bimanual"),
        (),
    ),
    "2610.28628": (
        "Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking",
        (TRACKS[0], "Reinforcement Learning", "Combining Imitation & Reinforcement"),
        ("Dexterous Manipulation",),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.27998": (
        "LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning",
        (TRACKS[2], "Teleoperation & Shared Control", "Bilateral Feedback & Delay"),
        ("Teleoperation",),
        ("Retargeting", "Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.31661": (
        "OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing",
        (TRACKS[8], "Sensors & Human Interfaces", "Tactile & Force Sensors"),
        (),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.31334": (
        "GelSlim 5.0: Unifying Vision and Touch with a Single Fingertip Camera",
        (TRACKS[5], "Tactile & Multimodal Perception", "Visuotactile & Proprioceptive Fusion"),
        (),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.31617": (
        "DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control",
        (TRACKS[6], "Model-based Decision Making", "Imagination & Model-based RL"),
        ("World Models",),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.31474": (
        "Skeleton-Grounded Latent Action Model for Robot World Models",
        (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
        ("World Models",),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.31613": (
        "Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models",
        (TRACKS[6], "Memory & Autonomous Execution", "Failure Detection & Replanning"),
        (),
        ("Hand Retargeting", "Whole-body Retargeting"),
    ),
    "2610.20904": (
        "EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos",
        (TRACKS[6], "World & Dynamics Modeling", "Latent Dynamics"),
        ("World Models", "Dexterous Manipulation"),
        ("Retargeting", "Hand Retargeting", "Whole-body Retargeting"),
    ),
}


class October24TaxonomyReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arxiv = json.loads((ROOT / "data/arxiv_recent.json").read_text())
        cls.records = {p["arxiv_id"]: p for p in cls.arxiv["papers"]}
        cls.conference = json.loads((ROOT / "data/papers.json").read_text())["papers"]

    def test_reviewed_titles_match_exactly_the_ten_declared_arxiv_records(self):
        keys = {normalize_text(case[0]) for case in CASES.values()}
        matches = [p for p in self.arxiv["papers"] if normalize_text(p["title"]) in keys]
        self.assertEqual({p["arxiv_id"] for p in matches}, set(CASES))
        self.assertEqual(len(matches), len(CASES))
        self.assertTrue(all(normalize_text(p["title"]) not in keys for p in self.conference))
        for identifier, (title, path, _, _) in CASES.items():
            with self.subTest(identifier=identifier):
                self.assertEqual(self.records[identifier]["title"], title)
                if identifier == "2610.20904":
                    # Newly admitted is not synonymous with newly published.
                    self.assertEqual(self.records[identifier]["published"], "2026-10-14")
                else:
                    self.assertGreater(self.records[identifier]["published"], "2026-10-15")
                entry = OVERRIDES[normalize_text(title)]
                self.assertEqual(entry["title"], title)
                self.assertEqual(tuple(entry["path"]), path)
                track, sub, specialty = path
                self.assertIn(sub, HIERARCHY[track])
                self.assertIn(specialty, [item[0] for item in HIERARCHY[track][sub]["specialties"]])

    def test_core_contribution_paths_topics_and_scope_are_preserved(self):
        for identifier, (_, path, included, excluded) in CASES.items():
            with self.subTest(identifier=identifier):
                annotated = annotate_paper(deepcopy(self.records[identifier]))
                self.assertEqual(tuple(annotated[key] for key in ("track", "subcategory", "specialty")), path)
                self.assertEqual(annotated["classification_status"], "reviewed")
                self.assertTrue(set(included).issubset(annotated["related_topics"]))
                self.assertTrue(set(excluded).isdisjoint(annotated["related_topics"]))
                reason = annotated["taxonomy_evidence"]
                self.assertIn("Title/abstract-only classification review", reason)
                self.assertIn("not full-paper reading or experiment reproduction", reason)
                self.assertIn(f"https://arxiv.org/abs/{identifier}", reason)

    def test_source_identity_and_metadata_are_unchanged_and_annotation_is_idempotent(self):
        source_fields = ("arxiv_id", "title", "authors", "abstract", "published", "year", "venue",
                         "paper_url", "pdf_url", "official_url", "source_type", "discovery_source",
                         "primary_category", "admission_track")
        for identifier in CASES:
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                annotated = annotate_paper(deepcopy(original))
                for field in source_fields:
                    self.assertEqual(annotated[field], original[field])
                self.assertEqual(annotated, annotate_paper(deepcopy(annotated)))

    def test_title_extensions_do_not_inherit_reviewed_exceptions(self):
        for identifier, (title, _, _, _) in CASES.items():
            for changed in ("A Review of " + title, title + ": A New Benchmark"):
                with self.subTest(identifier=identifier, changed=changed):
                    record = deepcopy(self.records[identifier])
                    record["title"] = changed
                    self.assertNotIn(normalize_text(changed), OVERRIDES)
                    self.assertNotEqual(annotate_paper(record)["classification_status"], "reviewed")

    def test_tracking_association_does_not_reclassify_learning_as_retargeting(self):
        tracker = annotate_paper(deepcopy(self.records["2610.29997"]))
        self.assertNotEqual(tracker["subcategory"], "Dexterous Hand Retargeting")
        self.assertIn({"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"},
                      tracker["related_taxonomy_paths"])
        learner = annotate_paper(deepcopy(self.records["2610.28628"]))
        self.assertEqual(learner["subcategory"], "Reinforcement Learning")
        self.assertNotIn("Hand Retargeting", learner["related_topics"])
        teleoperator = annotate_paper(deepcopy(self.records["2610.27998"]))
        self.assertNotIn("Retargeting", teleoperator["related_topics"])
        self.assertFalse(any(p["subcategory"] == "Dexterous Hand Retargeting"
                             for p in teleoperator["related_taxonomy_paths"]))

    def test_three_already_supported_vla_world_action_paths_do_not_get_overrides(self):
        paths = {
            "2610.30991": (TRACKS[6], "World & Dynamics Modeling", "Action-conditioned Video Prediction"),
            "2610.31569": (TRACKS[0], "VLA & Generalist Robot Policies", "Vision-Language-Action Modeling"),
            "2610.31423": (TRACKS[0], "VLA & Generalist Robot Policies", "Vision-Language-Action Modeling"),
        }
        for identifier, path in paths.items():
            with self.subTest(identifier=identifier):
                original = self.records[identifier]
                self.assertNotIn(normalize_text(original["title"]), OVERRIDES)
                annotated = annotate_paper(deepcopy(original))
                self.assertEqual(tuple(annotated[k] for k in ("track", "subcategory", "specialty")), path)
                self.assertNotEqual(annotated["classification_status"], "reviewed")

    def test_beyond_retargeting_does_not_classify_latent_world_model_as_retargeting(self):
        original = self.records["2610.20904"]
        self.assertIn("without rule-based human-to-robot retargeting", original["abstract"])
        annotated = annotate_paper(deepcopy(original))
        self.assertEqual(annotated["track"], TRACKS[6])
        self.assertEqual(annotated["subcategory"], "World & Dynamics Modeling")
        self.assertEqual(annotated["specialty"], "Latent Dynamics")
        self.assertTrue({"World Models", "Dexterous Manipulation"}.issubset(annotated["related_topics"]))
        self.assertTrue({"Retargeting", "Hand Retargeting", "Whole-body Retargeting"}.isdisjoint(
            annotated["related_topics"]))
        self.assertFalse(any(path["subcategory"] == "Dexterous Hand Retargeting"
                             for path in annotated["related_taxonomy_paths"]))


if __name__ == "__main__":
    unittest.main()
