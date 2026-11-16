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
    def test_spider_is_not_spiderbot_or_an_acronym_substring(self):
        rows = [paper("SPIDER: Scalable Physics-Informed Dexterous Retargeting", "Robot hand contact trajectories."),
                paper("Spiderbot: Energy-Efficient Hexapod", "Legged contact and whole-body retargeting."),
                paper("TACO: Task-Aware Contact Optimization", "A robot arm inserts a peg."),
                paper("TacoNet: Visual Meal Recognition", "A handheld tactile device.")]
        result = focus(rows)
        self.assertEqual([p["title"] for p in result["papers"]], [rows[0]["title"]])
        self.assertTrue(result["papers"][0]["evidence"])

    def test_tactile_is_not_a_hand_and_grasp_is_not_contact_mechanics(self):
        result = focus([paper("Tactile insertion", "A parallel-jaw gripper uses tactile sensing."),
                        paper("Dexterous grasp learning", "A multi-finger robot hand learns grasp poses.")])
        self.assertEqual(result["counts"]["reading_records"], 0)

    def test_wholebody_and_paralleljaw_background_only_cannot_be_strong(self):
        result = focus([paper("Humanoid whole-body contact planning", "Can later support dexterous robot hand applications."),
                        paper("Parallel-jaw contact planner", "Unlike a dexterous robot hand, the gripper has two jaws.")])
        self.assertEqual(result["counts"]["reading_records"], 2)
        self.assertTrue(all(p["tier"] == "broad-candidate" for p in result["papers"]))
        self.assertTrue(all("外延" in p["boundary_zh"] for p in result["papers"]))

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
                paper("Dexterous contact transfer", "Human demonstrations transfer to robot hand contact tasks.")]
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
