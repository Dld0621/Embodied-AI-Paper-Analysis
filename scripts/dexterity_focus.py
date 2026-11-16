"""Reproducible, evidence-bearing view of dexterous retargeting and contact papers.

This module never edits either source catalog or its primary taxonomy. The
candidate view favors recall, while its tiers keep metadata matches separate
from explicitly reviewed contributions. Reading identities are normalized
titles; all conference/preprint source variants remain attached.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import re


GROUPS = [
    {"slug": "retargeting", "name_zh": "手部重定向与示教迁移", "description_zh": "手部运动、接触或功能迁移；参考跟踪和示教迁移候选保留其实际贡献边界。"},
    {"slug": "contact-control", "name_zh": "接触控制与灵巧任务", "description_zh": "多指抓取、手内操作、力／阻抗、滑移与接触维持；候选不等于已核实控制成果。"},
    {"slug": "contact-perception", "name_zh": "触觉、接触感知与交互重建", "description_zh": "手物接触、力估计、触觉表示与交互重建；感知和器件支撑不冒充机器人策略。"},
    {"slug": "datasets-simulation", "name_zh": "数据集、仿真与数据生成", "description_zh": "人手／机器人手交互数据、仿真重放与示教生成；与实机迁移证据分开。"},
    {"slug": "contact-mechanics", "name_zh": "接触力学与物理可行性", "description_zh": "接触动力学、摩擦、力闭合、接触扳手与稳定性；一般抓取关键词不自动等于接触力学。"},
    {"slug": "residual", "name_zh": "残差方法与执行修正", "description_zh": "标明残差实际作用位置；动作／控制残差与特征适配器、模型误差或规划代价分开。"},
]
GROUP_NAMES = {group["slug"]: group["name_zh"] for group in GROUPS}
TIERS = {"reviewed": "已核查", "strong-candidate": "明确元数据候选", "broad-candidate": "外延待审候选"}
TIER_ORDER = {name: i for i, name in enumerate(TIERS)}
PAGE_SIZE = 100

HAND_TERMS = (
    "dexterous", "in hand manipulation", "in hand rotation", "in hand reorientation",
    "multi finger", "multi fingered", "multifinger", "multifingered", "robot hand",
    "robotic hand", "robot hands", "robotic hands", "human hand", "human hands",
    "hand object", "finger gaiting", "fingertip", "fingertips", "anthropomorphic hand",
    "shadow hand", "allegro hand", "leap hand", "inspire hand", "ability hand",
    "barrett hand", "trifinger", "adroit hand",
)
EXPLICIT_ROBOT_HAND = (
    "dexterous hand", "dexterous hands", "in hand manipulation", "in hand rotation",
    "in hand reorientation", "multi finger", "multi fingered", "multifinger",
    "multifingered", "robot hand", "robotic hand", "robot hands", "robotic hands",
    "finger gaiting", "anthropomorphic hand", "shadow hand", "allegro hand",
    "leap hand", "inspire hand", "ability hand", "barrett hand", "trifinger", "adroit hand",
)
RETARGET_TERMS = ("retargeting", "retarget", "retargeted", "retargets")
TRANSFER_TERMS = ("human demonstrations", "human demonstration", "human references", "human reference", "video to robot", "demonstration transfer", "motion transfer", "cross embodiment transfer")
CONTACT_TERMS = (
    "contact", "contacts", "friction", "frictional", "tactile", "haptic",
    "force closure", "form closure", "grasp force", "finger force", "wrench",
    "slip", "slipping", "impedance", "compliance", "compliant",
)
MECHANICS_TERMS = (
    "contact dynamics", "contact mechanics", "contact force", "contact forces",
    "friction cone", "friction cones", "frictional contact", "contact wrench",
    "wrench space", "force closure", "form closure", "grasp force", "finger force",
    "slip detection", "slip recovery", "contact stability", "contact maintenance",
    "impedance control", "compliant control", "physical feasibility", "dynamically feasible",
)
RESIDUAL_ACTION_TERMS = (
    "residual policy", "residual policies", "residual action", "residual actions",
    "residual control", "residual reinforcement learning", "residual learning",
    "residual correction", "residual flow steering",
)
RESIDUAL_OTHER_TERMS = (
    "residual adapter", "residual adapters", "residual network", "residual networks",
    "resnet", "residual vector quantization", "reconstruction residual", "prediction residual",
)
SUPPORT_TERMS = (
    "dataset", "datasets", "benchmark", "benchmarks", "data engine", "data generation",
    "data collection", "demonstration generation", "motion capture", "simulator",
    "simulation", "simulation framework", "simulation platform", "synthetic data",
)
PERCEPTION_TERMS = (
    "tactile", "haptic", "force estimation", "contact estimation", "contact sensing",
    "contact detection", "contact reconstruction", "hand object reconstruction",
    "hand object interaction reconstruction", "interaction reconstruction", "tactile sensor",
    "tactile sensors", "glove", "gloves", "contact perception", "touch sensing",
)
ADJACENT_TITLE_TERMS = (
    "whole body", "humanoid", "quadruped", "locomotion", "parallel jaw",
    "parallel gripper", "parallel jaw gripper", "aerial", "continuum robot",
    "surgical", "rehabilitation", "sign language",
)
NEGATIVE_RETARGET = ("retargeting free", "without retargeting", "no retargeting")
NEGATIVE_CONTACT = ("contactless", "contact free", "non contact")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").casefold().replace("π", "pi")).strip()


def title_key(title: str) -> str:
    return normalize(title) or str(title).casefold().strip()


def matches(text: str, terms) -> list[str]:
    haystack = " " + normalize(text) + " "
    return [term for term in terms if " " + normalize(term) + " " in haystack]


def _arxiv_id(paper: dict) -> str:
    if paper.get("arxiv_id"):
        return re.sub(r"v\d+$", "", str(paper["arxiv_id"]))
    for field in ("paper_url", "pdf_url", "official_url"):
        found = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", paper.get(field, ""))
        if found:
            return found.group(1)
    return ""


def _evidence(paper: dict) -> list[dict]:
    evidence = []
    families = {"hand": HAND_TERMS, "retargeting": RETARGET_TERMS, "transfer": TRANSFER_TERMS,
                "contact": CONTACT_TERMS, "mechanics": MECHANICS_TERMS,
                "residual-action-phrase": RESIDUAL_ACTION_TERMS, "residual-other": RESIDUAL_OTHER_TERMS,
                "support": SUPPORT_TERMS, "perception": PERCEPTION_TERMS}
    for field in ("title", "abstract"):
        text = paper.get(field, "")
        normalized = normalize(text)
        for kind, terms in families.items():
            for term in matches(text, terms):
                # Snippets use normalized text so hyphenation and boundaries are reproducible.
                at = normalized.find(normalize(term))
                evidence.append({"kind": kind, "field": field, "term": term,
                                 "snippet": normalized[max(0, at - 65): at + len(normalize(term)) + 100]})
    if "Hand Retargeting" in paper.get("related_topics", []) or paper.get("subcategory") == "Dexterous Hand Retargeting":
        evidence.append({"kind": "taxonomy-anchor", "field": "taxonomy", "term": "Hand Retargeting", "snippet": "Existing hand-retargeting classification/tag; not independent full-paper verification."})
    return evidence


def _selection(paper: dict) -> dict | None:
    title, abstract = paper.get("title", ""), paper.get("abstract", "")
    text = title + " " + abstract
    hand = bool(matches(text, HAND_TERMS))
    retarget = bool(matches(text, RETARGET_TERMS))
    contact = bool(matches(text, CONTACT_TERMS))
    residual_action = bool(matches(text, RESIDUAL_ACTION_TERMS))
    residual_other = bool(matches(text, RESIDUAL_OTHER_TERMS))
    anchor = "Hand Retargeting" in paper.get("related_topics", []) or paper.get("subcategory") == "Dexterous Hand Retargeting"
    if not (anchor or hand and (retarget or contact or residual_action or residual_other)):
        return None
    negative_retarget = bool(matches(title, NEGATIVE_RETARGET))
    negative_contact = bool(matches(title, NEGATIVE_CONTACT))
    adjacent = bool(matches(title, ADJACENT_TITLE_TERMS)) and not matches(title, EXPLICIT_ROBOT_HAND)
    support_title = bool(matches(title, SUPPORT_TERMS))
    groups = []
    if anchor or retarget and not negative_retarget or matches(text, TRANSFER_TERMS):
        groups.append("retargeting")
    if contact:
        if matches(text, PERCEPTION_TERMS):
            groups.append("contact-perception")
        if not support_title or matches(title, ("control", "manipulation", "grasping", "retargeting")):
            groups.append("contact-control")
    if support_title or matches(text, SUPPORT_TERMS) and paper.get("track") == "Data, Simulation & Evaluation":
        groups.append("datasets-simulation")
    if matches(text, MECHANICS_TERMS):
        groups.append("contact-mechanics")
    if residual_action or residual_other:
        groups.append("residual")
    if not groups:
        # Retargeting-free / contact-free title matches are retained only as explicit broad candidates.
        groups.append("retargeting" if retarget else "contact-perception")
    title_domain = bool(matches(title, HAND_TERMS))
    title_target = bool(matches(title, RETARGET_TERMS + CONTACT_TERMS + RESIDUAL_ACTION_TERMS))
    strong = (anchor or title_domain and (retarget or contact or residual_action)
              or title_target and bool(matches(text, EXPLICIT_ROBOT_HAND)))
    if adjacent or negative_retarget or negative_contact:
        strong = False
    if residual_other and not residual_action:
        residual_role = "representation-or-model; not action residual"
    elif residual_action:
        residual_role = "action/control phrase; locus needs source review"
    else:
        residual_role = "not established"
    boundary = "机器筛选基于标题、摘要和已有分类，不证明该主题就是论文主要贡献，也不代表全文审阅或实机验证。"
    if adjacent:
        boundary += " 标题含全身／夹爪／其他本体线索，仅列外延候选；不能作为多指手核心成果。"
    if negative_retarget or negative_contact:
        boundary += " 标题含否定式关键词，相关机制不能仅凭字面命中认定。"
    if support_title:
        boundary += " 数据、仿真或评测支撑不等于已完成机器人重定向或控制。"
    if residual_other and not residual_action:
        boundary += " 残差位于表征或模型，不能称为动作残差控制。"
    return {"tier": "strong-candidate" if strong else "broad-candidate", "groups": groups,
            "why_zh": "规范词组匹配到手部语境与目标主题；具体证据见标题／摘要命中。",
            "residual_role": residual_role, "boundary_zh": boundary, "evidence": _evidence(paper)}


def _variant(paper: dict, layer: str) -> dict:
    fields = ("title", "year", "venue", "source_type", "paper_url", "official_url", "published", "track", "subcategory", "specialty")
    return {"source_layer": layer, "arxiv_id": _arxiv_id(paper), **{key: paper.get(key, "") for key in fields}}


def _check_groups(entries):
    for entry in entries:
        unknown = set(entry.get("groups", [])) - set(GROUP_NAMES)
        if unknown:
            raise ValueError(f"Unknown focus groups: {sorted(unknown)}")


def build_focus(catalog: dict, arxiv: dict, curation: dict, status: dict) -> dict:
    """Build an isolated reading view; do not mutate supplied catalogs or taxonomy."""
    curated = curation.get("curated_in_catalog", [])
    foundations = curation.get("external_foundations", [])
    _check_groups(curated + foundations)
    by_title, by_id = defaultdict(list), defaultdict(list)
    for item in curated:
        if item.get("title"):
            by_title[title_key(item["title"])].append(item)
        if item.get("arxiv_id"):
            by_id[re.sub(r"v\d+$", "", str(item["arxiv_id"]))].append(item)
    all_rows = []
    buckets = defaultdict(list)
    selected = {}
    matched_source_records = 0
    hand_retargeting_anchor_sources = 0
    hand_retargeting_anchor_titles = set()
    for layer, payload in (("conference", catalog), ("arxiv", arxiv)):
        for paper in payload.get("papers", []):
            key = title_key(paper["title"])
            buckets[key].append((layer, paper))
            if ("Hand Retargeting" in paper.get("related_topics", [])
                    or paper.get("subcategory") == "Dexterous Hand Retargeting"):
                hand_retargeting_anchor_sources += 1
                hand_retargeting_anchor_titles.add(key)
            review = by_title.get(key) or by_id.get(_arxiv_id(paper), [])
            selection = _selection(paper)
            if selection or review:
                matched_source_records += 1
                selected.setdefault(key, []).append((paper, selection, review))
    for key, matches_for_title in selected.items():
        variants = buckets[key]
        preferred = next((paper for layer, paper in variants if layer == "conference"), variants[0][1])
        reviews = []
        evidence = []
        groups = set()
        for paper, selection, review in matches_for_title:
            if selection:
                evidence.extend(selection["evidence"])
                groups.update(selection["groups"])
            for item in review:
                if item not in reviews:
                    reviews.append(item)
        # Explicit reviewed groups describe the actual contribution; they override
        # background word hits rather than acquiring every automated group.
        if reviews:
            groups = {group for review in reviews for group in review.get("groups", [])}
        if not groups:
            raise ValueError(f"Selected paper has no focus group: {preferred['title']}")
        selection = next((selection for _, selection, _ in matches_for_title if selection and selection["tier"] == "strong-candidate"), None)
        selection = selection or next((selection for _, selection, _ in matches_for_title if selection), {})
        review = reviews[0] if reviews else {}
        tier = "reviewed" if reviews else selection["tier"]
        dedup_evidence = list({(e["kind"], e["field"], e["term"], e["snippet"]): e for e in evidence}.values())
        variant_rows = [_variant(paper, layer) for layer, paper in variants]
        arxiv_dates = [row["published"] for row in variant_rows if row["source_layer"] == "arxiv" and row["published"]]
        all_rows.append({
            "id": "focus-" + hashlib.sha256(key.encode()).hexdigest()[:14],
            **{field: preferred.get(field, "") for field in ("title", "year", "venue", "source_type", "paper_url", "official_url", "track", "subcategory", "specialty")},
            "first_arxiv_published": min(arxiv_dates, default=""),
            "tier": tier, "groups": [g["slug"] for g in GROUPS if g["slug"] in groups],
            "why_zh": review.get("why_zh", selection.get("why_zh", "")),
            "residual_role": review.get("residual_role", selection.get("residual_role", "not established")),
            "boundary_zh": review.get("boundary_zh", selection.get("boundary_zh", "")),
            "review_basis": review.get("review_basis", "automated metadata phrase matching; not full-paper review"),
            "review_urls": list(dict.fromkeys(url for item in reviews for url in item.get("urls", []))),
            "evidence": dedup_evidence, "source_variants": variant_rows,
        })
    all_rows.sort(key=lambda p: (TIER_ORDER[p["tier"]], -int(p.get("year") or 0), p["title"].casefold()))
    group_counts = {group["slug"]: sum(group["slug"] in row["groups"] for row in all_rows) for group in GROUPS}
    return {
        "schema_version": 1,
        "generated_on": status.get("documents_updated_on", curation.get("checked_on", "")),
        "curation_checked_on": curation.get("checked_on", ""),
        "curation_review_scope": curation.get("review_scope", ""),
        "discovery_notes": curation.get("discovery_notes", []),
        "source_snapshots": {"conference": catalog.get("as_of", ""), "arxiv": arxiv.get("as_of", "")},
        "scope": "Current conference and arXiv catalog metadata only; not all global literature or universal paper identities.",
        "selection_policy": {
            "candidate_union": "Hand-domain phrases AND retarget/contact/residual phrases, existing hand-retargeting anchors, or exact reviewed title/arXiv identities.",
            "matching": "Casefolded, punctuation-normalized whole phrases; no naked acronym substring matching.",
            "identity": "Normalized-title reading deduplication; all original source variants retained. Different titles may still describe one work.",
            "tiers": TIERS,
            "group_counts_overlap": True,
            "review_boundary": "Reviewed means the supplied title/abstract/selected-source review basis, not universal full-paper reading or reproduction.",
        },
        "counts": {"source_records": sum(len(p["source_variants"]) for p in all_rows),
                   "matched_source_records": matched_source_records,
                   "reading_records": len(all_rows),
                   "hand_retargeting_anchor_source_records": hand_retargeting_anchor_sources,
                   "hand_retargeting_anchor_reading_records": len(hand_retargeting_anchor_titles),
                   "tier_counts": {tier: sum(p["tier"] == tier for p in all_rows) for tier in TIERS},
                   "group_counts": group_counts, "external_foundations": len(foundations)},
        "groups": GROUPS, "papers": all_rows,
        "external_foundations": foundations,
    }


def _cell(value) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def _paper_table(papers, url_prefix="") -> list[str]:
    lines = ["| 论文 | 年份／优先来源 | 层级 | 关联专题 |", "|---|---|---|---|"]
    for paper in papers:
        lines.append(f"| [{_cell(paper['title'])}]({paper['paper_url']}) | {paper['year']} · {_cell(paper['venue'])} | {TIERS[paper['tier']]} | {'、'.join(GROUP_NAMES[g] for g in paper['groups'])} |")
    return lines


def _detail(paper) -> list[str]:
    sources = " · ".join(f"[{_cell(v['venue'])} / {v['source_layer']}]({v['official_url'] or v['paper_url']})" for v in paper["source_variants"])
    lines = [f"### {paper['title']}", "", f"- 阅读层级：**{TIERS[paper['tier']]}**；分组：{'、'.join(GROUP_NAMES[g] for g in paper['groups'])}。",
             f"- 来源记录：{sources}。", f"- 纳入理由：{paper['why_zh']}",
             f"- 证据边界：{paper['boundary_zh']}", f"- 审核基础：{paper['review_basis']}。"]
    if "residual" in paper["groups"]:
        lines.append(f"- 残差作用位置：{paper['residual_role']}。")
    if paper["review_urls"]:
        lines.append("- 核查来源：" + " · ".join(f"[来源 {i + 1}]({url})" for i, url in enumerate(paper["review_urls"])) + "。")
    # Compact page evidence; complete match occurrences stay in JSON/CSV export.
    ev = paper["evidence"]
    summarized = []
    for field in ("title", "abstract", "taxonomy"):
        terms = list(dict.fromkeys(e["term"] for e in ev if e["field"] == field))
        if terms:
            summarized.append(f"{field}: {', '.join(terms)}")
    if summarized:
        lines.append("- 元数据命中：" + "；".join(summarized) + "。")
    lines.append("")
    return lines


def render_markdown(focus: dict, root: Path) -> dict[Path, str]:
    base = root / "papers" / "focus" / "dexterous-retargeting-contact"
    outputs = {}
    papers = focus["papers"]
    counts = focus["counts"]
    lines = ["# 灵巧操作：重定向与接触专题", "",
             "从当前论文库筛出手部重定向、接触控制、触觉／交互重建、数据与仿真、接触力学和残差方法。", "",
             f"范围：会议快照 **{focus['source_snapshots']['conference']}**，arXiv 快照 **{focus['source_snapshots']['arxiv']}**；人工来源核查日期 **{focus['curation_checked_on']}**。", "",
             f"当前共 **{counts['reading_records']:,} 条规范标题去重阅读记录**，保留 **{counts['source_records']:,} 条会议／预印本来源记录**。这不是全网论文总数；不同标题仍可能属于同一工作。", "",
             "[下载完整 JSON](../../../data/dexterous-retargeting-contact.json) · [下载完整 CSV](../../../data/dexterous-retargeting-contact.csv) · [回到全库分类](../../taxonomy/README.md)", "",
             "## 阅读层级", "", "| 层级 | 阅读记录 | 含义 |", "|---|---:|---|"]
    explanations = {"reviewed": "有明确的一手来源核查记录；仍须查看其审核基础与实验边界。",
                    "strong-candidate": "标题或已有手部分类明确命中，尚不等于人工确认主要贡献。",
                    "broad-candidate": "摘要语境或外延本体命中，可能只是背景／可迁移方法，需进一步复核。"}
    for tier, name in TIERS.items():
        lines.append(f"| {name} | {counts['tier_counts'][tier]:,} | {explanations[tier]} |")
    lines.extend(["", "分组允许交叉，下面数量不可相加。一般抓取不自动等于接触力学；触觉不自动等于多指手；人手交互数据不自动等于机器人重定向。", "",
                  "## 按问题进入", "",
                  f"**口径区别：**原有手部重定向索引（既有 Hand Retargeting 标签或手部重定向主类）为 **{counts['hand_retargeting_anchor_source_records']:,} 条来源记录／{counts['hand_retargeting_anchor_reading_records']:,} 条规范标题去重记录**。本专题“手部重定向与示教迁移”分组的 **{counts['group_counts']['retargeting']:,} 条**包含示教迁移和外延候选，**不等于 {counts['group_counts']['retargeting']:,} 篇已核实手部重定向论文**；原有索引数量也不是语义完整性或全文审阅证明。", "",
                  "| 专题 | 阅读记录 | 范围 |", "|---|---:|---|"])
    for group in GROUPS:
        lines.append(f"| [{group['name_zh']}]({group['slug']}/README.md) | {counts['group_counts'][group['slug']]:,} | {group['description_zh']} |")
    lines.extend(["", "## 优先阅读：已核查条目", ""])
    reviewed = [p for p in papers if p["tier"] == "reviewed"]
    lines.extend(_paper_table(reviewed) if reviewed else ["本次没有独立核查条目；请勿将自动候选称作已审核。"])
    lines.extend(["", "## 完整候选目录", "", "以下分页不删去外延待审候选；每页最多 100 条，JSON 和 CSV 提供逐条证据与全部来源。", ""])
    for index in range(0, len(papers), PAGE_SIZE):
        name = f"all-{index // PAGE_SIZE + 1:03}.md"
        batch = papers[index:index + PAGE_SIZE]
        lines.append(f"- [完整清单 {index // PAGE_SIZE + 1}：{index + 1}–{index + len(batch)}]({name})")
        page = [f"# 完整候选清单 {index // PAGE_SIZE + 1}", "", "[← 专题总览](README.md)", ""]
        page.extend(_paper_table(batch))
        page.extend(["", "## 逐条纳入证据", ""])
        for paper in batch:
            page.extend(_detail(paper))
        outputs[base / name] = "\n".join(page).rstrip() + "\n"
    lines.extend(["", "## 库外经典与补充来源", "", "下面是独立补充表，不进入上述库内候选、来源或分组数量；原始发表年份保留，不冒充本次窗口新增。", ""])
    if focus["external_foundations"]:
        lines.extend(["| 论文 | 原始年份 | 用途与边界 |", "|---|---:|---|"])
        for item in focus["external_foundations"]:
            url = next(iter(item.get("urls", [])), "")
            title = f"[{_cell(item['title'])}]({url})" if url else _cell(item["title"])
            lines.append(f"| {title} | {item.get('year', '')} | {_cell(item.get('why_zh', ''))} {_cell(item.get('boundary_zh', ''))} |")
    else:
        lines.append("当前没有库外补充。")
    lines.extend(["", "## 筛选与证据边界", "",
                  "- 仅在当前会议与 arXiv 两层元数据中按规范完整词组筛选，或按确切标题／arXiv ID 纳入有来源的人工例外；不按 SPIDER、TACO 等裸缩写子串匹配。",
                  "- 同一规范标题合并为阅读条目，但会议与预印本来源记录全部保留。标题去重不是严格论文实体识别，也不证明 arXiv 版本获得会议录用。",
                  "- 全身／四足、双指夹爪、一般机械臂插入、连续体接触模型等不能自动成为多指手核心成果；若作为外延候选出现，必须查看层级与边界。",
                  "- 残差适配器／网络、规划代价和动作残差属于不同作用位置；未核查条目不能仅因 residual 一词认定为动作残差。",
                  "- 自动候选可能漏检或误检；已核查只对应各条所列的标题／摘要、局部全文或其他来源核对，不代表全库全文精读、成功复现或实机验证。", ""])
    outputs[base / "README.md"] = "\n".join(lines).rstrip() + "\n"
    for group in GROUPS:
        group_rows = [p for p in papers if group["slug"] in p["groups"]]
        page = [f"# {group['name_zh']}", "", "[← 专题总览](../README.md)", "", group["description_zh"], "",
                f"本组 **{len(group_rows):,}** 条标题去重阅读记录；与其他分组可交叉，不可相加。", ""]
        for index in range(0, len(group_rows), PAGE_SIZE):
            batch = group_rows[index:index + PAGE_SIZE]
            name = f"part-{index // PAGE_SIZE + 1:03}.md"
            page.append(f"- [完整分组清单 {index // PAGE_SIZE + 1}：{index + 1}–{index + len(batch)}]({name})")
            part = [f"# {group['name_zh']} · {index // PAGE_SIZE + 1}", "", "[← 分组入口](README.md) · [专题总览](../README.md)", ""]
            part.extend(_paper_table(batch))
            part.extend(["", "## 逐条纳入证据", ""])
            for paper in batch:
                part.extend(_detail(paper))
            outputs[base / group["slug"] / name] = "\n".join(part).rstrip() + "\n"
        if not group_rows:
            page.append("当前没有符合本组筛选条件的库内条目。")
        outputs[base / group["slug"] / "README.md"] = "\n".join(page).rstrip() + "\n"
    return outputs


def render_exports(focus: dict, root: Path) -> dict[Path, str]:
    buffer = io.StringIO(newline="")
    columns = ["id", "title", "year", "venue", "tier", "groups", "paper_url", "why_zh", "residual_role", "boundary_zh", "review_basis", "review_urls", "source_variants", "evidence"]
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for paper in focus["papers"]:
        row = {key: paper.get(key, "") for key in columns}
        for key in ("groups", "review_urls", "source_variants", "evidence"):
            row[key] = json.dumps(row[key], ensure_ascii=False, separators=(",", ":"))
        for key, value in row.items():
            if isinstance(value, str) and value.lstrip(" \t\r\n").startswith(("=", "+", "-", "@")):
                row[key] = "'" + value
        writer.writerow(row)
    return {root / "data" / "dexterous-retargeting-contact.json": json.dumps(focus, ensure_ascii=False, indent=2) + "\n",
            root / "data" / "dexterous-retargeting-contact.csv": "\ufeff" + buffer.getvalue()}
