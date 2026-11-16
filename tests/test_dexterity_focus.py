"""Focus-view regression cases: evidence and boundaries, not token snapshots."""
import copy
import csv
import io
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from dexterity_focus import build_focus, render_exports, render_markdown


def paper(title, abstract="", **extra):
    return {"title": title, "abstract": abstract, "year": 2026, "venue": "arXiv",
            "paper_url": "https://arxiv.org/abs/2601.00001", "official_url": "https://arxiv.org/abs/2601.00001",
            "source_type": "arxiv", "track": "", "subcategory": "", "specialty": "", **extra}


def focus(rows, conference=None, curation=None):
    return build_focus({"as_of": "2026-11-16", "papers": conference or []},
                       {"as_of": "2026-11-16", "papers": rows},
                       curation or {"checked_on": "2026-11-16"},
                       {"documents_updated_on": "2026-11-16"})


class DexterityFocusTests(unittest.TestCase):
    def test_spider_not_acronym_substrings_and_other_contact_fields_remain(self):
        rows = [paper("SPIDER: Scalable Physics-Informed Dexterous Retargeting", "Robot hand contact trajectories."),
                paper("Spiderbot: Energy-Efficient Hexapod", "Legged contact and whole-body retargeting."),
                paper("TACO: Task-Aware Contact Optimization", "A robot arm inserts a peg."),
                paper("TacoNet: Visual Meal Recognition", "A handheld device classifies food.")]
        result = focus(rows)
        by_title = {p["title"]: p for p in result["papers"]}
        self.assertEqual(set(by_title), {p["title"] for p in rows[:3]})
        self.assertIn("dexterous-manipulation", by_title[rows[0]["title"]]["groups"])
        self.assertIn("legged-contact", by_title[rows[1]["title"]]["groups"])
        self.assertNotIn("dexterous-manipulation", by_title[rows[1]["title"]]["groups"])
        self.assertIn("arm-contact", by_title[rows[2]["title"]]["groups"])
        self.assertTrue(by_title[rows[0]["title"]]["evidence"])

    def test_tactile_arm_and_dexterous_grasp_are_in_scope_without_inventing_mechanics(self):
        result = focus([paper("Tactile insertion", "A parallel-jaw gripper uses tactile sensing."),
                        paper("Dexterous grasp learning", "A multi-finger robot hand learns grasp poses.")])
        self.assertEqual(result["counts"]["reading_records"], 2)
        by_title = {p["title"]: p for p in result["papers"]}
        self.assertIn("arm-contact", by_title["Tactile insertion"]["groups"])
        self.assertNotIn("dexterous-manipulation", by_title["Tactile insertion"]["groups"])
        self.assertIn("dexterous-manipulation", by_title["Dexterous grasp learning"]["groups"])
        self.assertTrue(all("contact-mechanics" not in p["groups"] for p in result["papers"]))

    def test_wholebody_and_paralleljaw_are_central_contact_fields_not_multifinger_claims(self):
        result = focus([paper("Humanoid whole-body contact planning", "Can later support dexterous robot hand applications."),
                        paper("Parallel-jaw contact planner", "Unlike a dexterous robot hand, the gripper has two jaws.")])
        self.assertEqual(result["counts"]["reading_records"], 2)
        self.assertTrue(all(p["tier"] == "strong-candidate" for p in result["papers"]))
        self.assertTrue(all("dexterous-manipulation" not in p["groups"] for p in result["papers"]))
        self.assertTrue(all("多指手成果" in p["boundary_zh"] for p in result["papers"]))
        self.assertTrue(all("contact-planning" in p["groups"] for p in result["papers"]))

    def test_face_is_selected_by_contact_rules_without_hand_or_manual_override(self):
        result = focus([paper("Contact-Aware Imitation Learning Through Contact Factorization",
                              "A robot arm adapts force observations using contact normals and friction.", arxiv_id="2610.09533")])
        selected = result["papers"][0]
        self.assertEqual(selected["tier"], "strong-candidate")
        self.assertIn("arm-contact", selected["groups"])
        self.assertIn("contact-control", selected["groups"])
        self.assertNotIn("retargeting", selected["groups"])
        self.assertNotIn("dexterous-manipulation", selected["groups"])

    def test_nonphysical_contact_and_compliance_are_not_physics_contributions(self):
        rows = [paper("Contact tracing for robot fleets", "A robot tracks infectious disease contacts."),
                paper("Regulatory compliance for robots", "Legal compliance with regulations."),
                paper("Robot force tracking with compliant control", "The robot arm measures forces.")]
        result = focus(rows)
        self.assertEqual([p["title"] for p in result["papers"]], [rows[2]["title"]])
        self.assertIn("contact-control", result["papers"][0]["groups"])
        self.assertEqual(focus([paper("COLREGs-Compliant Collision Avoidance", "A dynamically feasible robot planner is compliant with regulations.")])["papers"], [])
        selected = focus([paper("ContactKernels: Learning Contact Information", "A robot learns physical contact information and tactile geometry.")])["papers"][0]
        self.assertEqual(selected["tier"], "strong-candidate")

    def test_generic_torque_is_only_broad_and_not_contact_mechanics(self):
        selected = focus([paper("Robot motor torque optimization", "A robotic actuator reduces torque variation.")])["papers"][0]
        self.assertEqual(selected["tier"], "broad-candidate")
        self.assertNotIn("contact-mechanics", selected["groups"])
        self.assertEqual(selected["groups"], ["related-comparisons"])
        self.assertIn("并未确认接触机制", selected["boundary_zh"])

    def test_negative_titles_stay_related_without_denied_method_claim(self):
        rows = [paper("Retargeting-free dexterous manipulation", "A robot hand learns from contact observations."),
                paper("Contact-free robot hand reconstruction", "Human hand geometry is reconstructed without touch.")]
        result = focus(rows)
        by_title = {p["title"]: p for p in result["papers"]}
        self.assertNotIn("retargeting", by_title[rows[0]["title"]]["groups"])
        self.assertNotIn("contact-control", by_title[rows[1]["title"]]["groups"])
        self.assertNotIn("contact-mechanics", by_title[rows[1]["title"]]["groups"])
        self.assertTrue(all(p["tier"] == "broad-candidate" for p in result["papers"]))
        self.assertTrue(all("被否定" in p["boundary_zh"] for p in result["papers"]))
        self.assertEqual(focus([paper("Contact-free navigation", "A mobile robot uses wireless localization.")])["papers"], [])

    def test_humanoid_dexterous_title_can_be_an_actual_hand_task(self):
        selected = focus([paper("Humanoid Dexterous Manipulation", "A humanoid manipulates objects with a multi-finger hand.")])["papers"][0]
        self.assertIn("dexterous-manipulation", selected["groups"])

    def test_generic_imitation_demonstrations_are_not_retargeting(self):
        result = focus([paper("Robot imitation from human demonstrations", "A robot arm learns behavior cloning from human demonstrations.")])
        self.assertEqual(result["papers"], [])
        selected = focus([paper("Dexterous contact learning", "A robot hand learns from human demonstrations.")])["papers"][0]
        self.assertNotIn("retargeting", selected["groups"])
        transferred = focus([paper("Human-to-robot motion transfer", "A robot arm transfers human motion.")])["papers"][0]
        self.assertIn("retargeting", transferred["groups"])

    def test_dexterous_flight_and_future_hand_background_do_not_claim_hand_tasks(self):
        result = focus([paper("Dexterous flapping flight", "An aerial robot generates large torques."),
                        paper("General contact planning", "This could later support dexterous robot hand applications.")])
        self.assertTrue(all("dexterous-manipulation" not in p["groups"] for p in result["papers"]))

    def test_multi_contact_grasping_and_humanoid_hand_do_not_imply_legs(self):
        result = focus([paper("Multi-contact Grasp Optimization", "A robot hand coordinates multi-contact grasps."),
                        paper("Humanoid Hand Tactile Sensing", "Contact sensors on a humanoid hand support grasping.")])
        self.assertTrue(all("legged-contact" not in p["groups"] for p in result["papers"]))

    def test_retargeting_free_locomotion_is_related_comparison_not_retargeting(self):
        selected = focus([paper("Retargeting-free Humanoid Control", "A humanoid robot uses a motion latent policy.")])["papers"][0]
        self.assertEqual(selected["groups"], ["related-comparisons"])
        self.assertNotIn("retargeting", selected["groups"])

    def test_collision_constraint_contacts_are_not_physical_touch(self):
        selected = focus([paper("Contact-based optimization for collision-free motion planning",
                                "Robot trajectories meet contacts at the minimum allowed separation.")])["papers"][0]
        self.assertEqual(selected["groups"], ["related-comparisons"])
        self.assertEqual(selected["tier"], "broad-candidate")
        self.assertIn("未确认物理触碰", selected["boundary_zh"])
        physical = focus([paper("Contact-based collision-free grasping",
                                "A robot optimizes contact forces and minimum allowed separation during manipulation.")])["papers"][0]
        self.assertIn("contact-mechanics", physical["groups"])

    def test_residual_adapter_is_not_labeled_action_residual(self):
        result = focus([paper("Dexterous visual policy adaptation", "A residual adapter improves robot hand representations.")])
        selected = result["papers"][0]
        self.assertIn("residual", selected["groups"])
        self.assertEqual(selected["residual_role"], "representation-or-model; not action residual")
        self.assertIn("不能称为动作残差控制", selected["boundary_zh"])

    def test_title_dedup_preserves_both_evidence_layers_and_inputs(self):
        arxiv = paper("Hand Contact Control", "A robot hand senses contact forces.", arxiv_id="2601.00001")
        conference = paper("Hand Contact Control", "", venue="CoRL", source_type="publisher", official_url="https://doi.org/10.1/test")
        original = copy.deepcopy((arxiv, conference))
        result = focus([arxiv], [conference])
        self.assertEqual(result["counts"]["reading_records"], 1)
        self.assertEqual(result["counts"]["source_records"], 2)
        self.assertEqual(result["counts"]["conference_source_records"], 1)
        self.assertEqual(result["counts"]["arxiv_source_records"], 1)
        self.assertEqual(result["counts"]["conference_arxiv_overlap_reading_records"], 1)
        self.assertEqual(result["papers"][0]["venue"], "CoRL")
        self.assertEqual({v["source_layer"] for v in result["papers"][0]["source_variants"]}, {"conference", "arxiv"})
        self.assertEqual((arxiv, conference), original)

    def test_reviewed_identity_overrides_background_groups_and_external_is_separate(self):
        title = "TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real"
        curation = {"checked_on": "2026-11-16", "curated_in_catalog": [{"title": title,
                    "groups": ["datasets-simulation"], "why_zh": "触觉数据生成", "boundary_zh": "不是已验证的跨机器人手重定向。", "review_basis": "selected full text", "urls": ["https://arxiv.org/abs/2611.17619"]}],
                    "external_foundations": [{"title": "GRAB", "year": 2020, "groups": ["datasets-simulation"], "urls": ["https://grab.is.tue.mpg.de/"]}]}
        result = focus([paper(title, "Human hand contact and retargeting can inform tactile datasets.")], curation=curation)
        selected = result["papers"][0]
        self.assertEqual(selected["tier"], "reviewed")
        self.assertEqual(selected["groups"], ["datasets-simulation"])
        self.assertEqual(result["counts"]["reading_records"], 1)
        self.assertEqual(result["counts"]["external_foundations"], 1)
        self.assertEqual(result["counts"]["group_counts"]["retargeting"], 0)

    def test_pages_and_exports_cover_every_selected_title_without_truncation(self):
        rows = [paper(f"Dexterous contact controller {i}", "A robot hand senses contact forces.", arxiv_id=f"2601.{i:05}") for i in range(205)]
        result = focus(rows)
        root = Path("/tmp/focus-test")
        markdown = render_markdown(result, root)
        all_pages = {p: text for p, text in markdown.items() if p.name.startswith("all-")}
        self.assertEqual(len(all_pages), 3)
        for text in all_pages.values():
            self.assertLessEqual(text.count("\n### "), 100)
        self.assertEqual(sum(text.count("\n### ") for text in all_pages.values()), 205)
        exported = render_exports(result, root)
        data = json.loads(exported[root / "data/dexterous-retargeting-contact.json"])
        csv_text = exported[root / "data/dexterous-retargeting-contact.csv"]
        self.assertTrue(csv_text.startswith("\ufeff"))
        csv_rows = list(csv.DictReader(io.StringIO(csv_text.lstrip("\ufeff"))))
        self.assertEqual(len(data["papers"]), 205)
        self.assertEqual({p["id"] for p in data["papers"]}, {p["id"] for p in csv_rows})
        self.assertEqual(result["counts"]["group_counts"]["contact-control"], 205)

    def test_both_source_directories_are_complete_and_keep_source_provenance(self):
        rows = [paper(f"Contact control {i}", "A robot arm performs force control.", arxiv_id=f"2601.{i:05}") for i in range(205)]
        conferences = [paper(f"Contact control {i}", "", venue="RSS", source_type="publisher") for i in range(101)]
        result = focus(rows, conferences)
        self.assertEqual(result["counts"]["source_reading_counts"], {"conference": 101, "arxiv": 205})
        self.assertEqual(result["counts"]["conference_arxiv_overlap_reading_records"], 101)
        root = Path("/tmp/focus-test")
        output = render_markdown(result, root)
        base = root / "papers/focus/dexterous-retargeting-contact"
        for layer, expected in (("conference", 101), ("arxiv", 205)):
            pages = {p: text for p, text in output.items() if p.parent == base / layer and p.name.startswith("part-")}
            self.assertEqual(sum(t.count("\n### ") for t in pages.values()), expected)
            self.assertTrue(all(t.count("\n### ") <= 100 for t in pages.values()))
            self.assertIn(base / layer / "README.md", output)
        arxiv_part = output[base / "arxiv/part-001.md"]
        self.assertIn("RSS / conference", arxiv_part)
        self.assertIn("arXiv / arxiv", arxiv_part)

    def test_invalid_curated_group_is_rejected_instead_of_silently_lost(self):
        with self.assertRaises(ValueError):
            focus([], curation={"curated_in_catalog": [{"title": "X", "groups": ["invented-group"]}]})

    def test_csv_quotes_text_and_does_not_execute_formula_shaped_titles(self):
        title = '=HYPERLINK("https://example.com", "Dexterous contact control")'
        result = focus([paper(title, "A robot hand senses contact forces.")])
        root = Path("/tmp/focus-test")
        exports = render_exports(result, root)
        rows = list(csv.DictReader(io.StringIO(exports[root / "data/dexterous-retargeting-contact.csv"].lstrip("\ufeff"))))
        self.assertEqual(rows[0]["title"], "'" + title)
        self.assertEqual(json.loads(exports[root / "data/dexterous-retargeting-contact.json"])["papers"][0]["title"], title)

    def test_existing_hand_anchor_counts_are_not_the_broader_transfer_group_count(self):
        rows = [paper("Exact Hand Retargeting", related_topics=["Hand Retargeting"]),
                paper("Another hand mapping", subcategory="Dexterous Hand Retargeting"),
                paper("Dexterous contact transfer", "Human-to-robot motion transfer provides robot hand contact tasks.")]
        conference = paper("Exact Hand Retargeting", venue="CoRL", related_topics=["Hand Retargeting"])
        result = focus(rows, [conference])
        self.assertEqual(result["counts"]["hand_retargeting_anchor_source_records"], 3)
        self.assertEqual(result["counts"]["hand_retargeting_anchor_reading_records"], 2)
        self.assertEqual(result["counts"]["group_counts"]["retargeting"], 3)
        root = Path("/tmp/focus-test")
        overview = render_markdown(result, root)[root / "papers/focus/dexterous-retargeting-contact/README.md"]
        self.assertIn("3 条来源记录／2 条规范标题去重记录", overview)
        self.assertIn("不等于 3 篇已核实手部重定向论文", overview)


if __name__ == "__main__":
    unittest.main()
