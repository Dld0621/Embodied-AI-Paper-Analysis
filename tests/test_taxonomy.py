from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from taxonomy import GENERAL_SPECIALTY, classify_hierarchy, taxonomy_metadata


class TaxonomyClassifierTests(unittest.TestCase):
    def test_published_taxonomy_shape(self) -> None:
        metadata = taxonomy_metadata()
        self.assertEqual(len(metadata["tracks"]), 7)
        self.assertEqual(metadata["subcategory_count"], 40)
        self.assertEqual(metadata["specialty_count"], 160)

    def test_vla_diffusion_path(self) -> None:
        subfield, specialty, evidence = classify_hierarchy(
            "Foundation Models & VLA",
            "Fast Diffusion Policies for Vision-Language-Action Robot Control",
        )
        self.assertEqual(subfield, "VLA Architectures")
        self.assertEqual(specialty, "Diffusion & Flow Policies")
        self.assertTrue(evidence.startswith("title:"))

    def test_hand_retargeting_path(self) -> None:
        subfield, specialty, _ = classify_hierarchy(
            "Dexterity & Teleoperation",
            "Hand Pose Retargeting Across Anthropomorphic Robot Hands",
        )
        self.assertEqual(subfield, "Retargeting & Human Motion")
        self.assertEqual(specialty, "Hand-pose Retargeting")

    def test_navigation_localization_path(self) -> None:
        subfield, specialty, _ = classify_hierarchy(
            "Navigation & Embodied Agents",
            "LiDAR-Inertial Odometry for GNSS-Denied Mobile Robots",
        )
        self.assertEqual(subfield, "Mapping & Localization")
        self.assertEqual(specialty, "Visual-inertial & LiDAR Odometry")

    def test_unsupported_precision_remains_general(self) -> None:
        subfield, specialty, evidence = classify_hierarchy(
            "Foundation Models & VLA",
            "A Study of Embodied Intelligence",
        )
        self.assertEqual(subfield, "VLA Architectures")
        self.assertEqual(specialty, GENERAL_SPECIALTY)
        self.assertEqual(evidence, "fallback")


if __name__ == "__main__":
    unittest.main()
