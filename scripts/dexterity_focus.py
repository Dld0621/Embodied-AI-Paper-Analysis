"""Reproducible, evidence-bearing view of contact, dexterity and retargeting papers.

This module never edits either source catalog or its primary taxonomy. The
candidate view favors recall, while its tiers keep metadata matches separate
from explicitly reviewed contributions. Reading identities are normalized
titles; all conference/preprint source variants remain attached.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
from functools import lru_cache
import hashlib
import io
import json
from pathlib import Path
import re


GROUPS = [
    {"slug": "retargeting", "name_zh": "重定向与示教迁移", "description_zh": "手部、全身与跨本体运动／接触／功能迁移；参考跟踪与示教迁移候选按实际贡献区分。"},
    {"slug": "contact-control", "name_zh": "接触、力与阻抗控制", "description_zh": "接触维持、力／阻抗／导纳、柔顺与滑移控制候选；一般力／力矩线索也保留为待审，不能自动认定接触机制。"},
    {"slug": "contact-perception", "name_zh": "触觉、接触感知与交互重建", "description_zh": "触觉、接触／力估计、传感器、手物及机器人环境交互重建；感知支撑与策略证据分开。"},
    {"slug": "datasets-simulation", "name_zh": "数据集、仿真与数据生成", "description_zh": "接触与交互数据、接触仿真、仿真重放及示教生成；与实机迁移证据分开。"},
    {"slug": "contact-mechanics", "name_zh": "接触力学与物理可行性", "description_zh": "接触动力学、摩擦、力闭合、接触扳手与稳定性；一般抓取关键词不自动等于接触力学。"},
    {"slug": "residual", "name_zh": "残差方法与执行修正", "description_zh": "标明残差实际作用位置；动作／控制残差与特征适配器、模型误差或规划代价分开。"},
    {"slug": "arm-contact", "name_zh": "机械臂接触操作与装配", "description_zh": "机械臂／夹爪接触操作、插入装配、打磨擦拭、工具使用和柔顺操作；不自动等于多指手实验。"},
    {"slug": "contact-planning", "name_zh": "接触规划、优化与 MPC", "description_zh": "接触隐式规划、模式／序列选择、轨迹优化与接触感知预测控制。"},
    {"slug": "legged-contact", "name_zh": "足式与全身多接触", "description_zh": "步行、足地接触、落足规划、全身及多接触协调；保留本体与任务边界。"},
    {"slug": "physical-hri", "name_zh": "物理人机交互与触觉交互", "description_zh": "物理协作、交接、可穿戴／康复、触觉反馈与人机接触安全。"},
    {"slug": "dexterous-manipulation", "name_zh": "灵巧操作与手内任务", "description_zh": "多指手、手内旋转／重定向、指步、灵巧抓取及其他明确灵巧操作；非手本体的灵巧任务不能冒充多指手成果。"},
    {"slug": "related-comparisons", "name_zh": "相关对照与范围待定", "description_zh": "否定式对照、仅一般力／力矩或旧索引关联；未确认具体接触机制、重定向贡献或多指手任务。"},
]
GROUP_NAMES = {group["slug"]: group["name_zh"] for group in GROUPS}
TIERS = {"reviewed": "已核查", "strong-candidate": "明确元数据候选", "broad-candidate": "宽范围待审候选"}
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
MIGRATION_TERMS = ("video to robot", "human to robot", "human2robot", "demonstration transfer", "motion transfer",
                   "cross embodiment", "cross morphology", "cross morphological", "embodiment transfer")
DEXTEROUS_TASK_TERMS = ("manipulation", "manipulating", "grasp", "grasping", "hand", "hands", "finger", "fingers",
                       "fingertip", "fingertips", "regrasping", "in hand", "object reorientation")
CONTACT_TERMS = (
    "contact", "contacts", "friction", "frictional", "tactile", "haptic",
    "force closure", "form closure", "grasp force", "finger force", "wrench",
    "slip", "slipping", "impedance", "admittance", "compliance", "compliant",
    "force control", "force tracking", "force feedback", "force sensing",
    "force torque", "hybrid position force", "touch sensing", "touch perception",
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
ARM_TERMS = ("robot arm", "robotic arm", "manipulator", "manipulators", "gripper", "grippers",
             "parallel jaw", "parallel gripper", "insertion", "peg in hole", "assembly", "polishing",
             "grinding", "wiping", "screwing", "screwdriving", "surface following", "tool use")
PLANNING_TERMS = ("planning", "planner", "planners", "trajectory optimization", "trajectory optimisation",
                  "contact implicit", "model predictive control", "mpc", "contact sequence", "contact mode")
LEGGED_TERMS = ("whole body", "quadruped", "bipedal", "biped", "legged", "locomotion",
                "walking", "footstep", "foothold", "foot ground")
HRI_TERMS = ("physical human robot", "human robot interaction", "human robot collaboration", "human robot cooperation",
             "human robot contact", "human robot handover", "handover", "handovers", "exoskeleton", "prosthetic",
             "rehabilitation", "haptic feedback", "haptic interface", "wearable haptic")
WEAK_FORCE_TERMS = ("force", "forces", "torque", "torques")
ROBOT_TERMS = ("robot", "robots", "robotic", "robotics", "manipulator", "manipulation", "gripper", "grippers",
               "locomotion", "humanoid", "quadruped", "bipedal", "exoskeleton", "prosthetic", "haptic", "tactile")
NONPHYSICAL_PHRASES = ("contact tracing", "contact email", "contact us", "contact author",
                       "regulatory compliance", "legal compliance", "policy compliance", "standards compliance",
                       "instruction compliance", "compliance with regulations", "colregs compliant",
                       "rule compliant", "rules compliant", "regulation compliant", "regulations compliant")
NEGATIVE_RETARGET = ("retargeting free", "without retargeting", "no retargeting")
NEGATIVE_CONTACT = ("contactless", "contact free", "non contact")


@lru_cache(maxsize=8192)
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
                "support": SUPPORT_TERMS, "perception": PERCEPTION_TERMS,
                "force-torque-context": WEAK_FORCE_TERMS, "arm-task": ARM_TERMS,
                "planning": PLANNING_TERMS, "legged-body": LEGGED_TERMS,
                "physical-hri": HRI_TERMS, "nonphysical-sense": NONPHYSICAL_PHRASES}
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


def _physical_text(text: str) -> str:
    """Remove known nonphysical senses without erasing independent physical cues."""
    cleaned = " " + normalize(text) + " "
    for phrase in NONPHYSICAL_PHRASES:
        cleaned = cleaned.replace(" " + normalize(phrase) + " ", " ")
    return cleaned.strip()


def _selection(paper: dict) -> dict | None:
    title, abstract = paper.get("title", ""), paper.get("abstract", "")
    text = title + " " + abstract
    physical = _physical_text(text)
    nonphysical = bool(matches(text, NONPHYSICAL_PHRASES))
    hand = bool(matches(text, HAND_TERMS))
    retarget = bool(matches(text, RETARGET_TERMS))
    contact = bool(matches(physical, CONTACT_TERMS))
    if nonphysical:
        independent_contact_terms = tuple(term for term in CONTACT_TERMS if term not in ("compliance", "compliant"))
        # Regulatory compliance and compliant robots are different senses;
        # disease contact tracing also leaves plural "contacts" in abstracts.
        if matches(text, ("contact tracing",)):
            independent_contact_terms = tuple(term for term in independent_contact_terms if term not in ("contact", "contacts"))
        contact = bool(matches(physical, independent_contact_terms))
    residual_action = bool(matches(text, RESIDUAL_ACTION_TERMS))
    residual_other = bool(matches(text, RESIDUAL_OTHER_TERMS))
    anchor = "Hand Retargeting" in paper.get("related_topics", []) or paper.get("subcategory") == "Dexterous Hand Retargeting"
    # This rule-based legacy union preserves the old hand/contact/residual view;
    # it is not a stored list of paper identities and never restricts new scope.
    legacy = anchor or hand and (retarget or matches(text, CONTACT_TERMS) or residual_action or residual_other)
    dexterity = bool(matches(text, EXPLICIT_ROBOT_HAND) or matches(text, ("dexterous",)) and matches(text, DEXTEROUS_TASK_TERMS))
    nonhand_title = bool(matches(title, ADJACENT_TITLE_TERMS)) and not matches(title, EXPLICIT_ROBOT_HAND)
    title_dexterity = bool(matches(title, EXPLICIT_ROBOT_HAND) or matches(title, ("dexterous",)) and matches(title, DEXTEROUS_TASK_TERMS))
    future_hand = bool(re.search(r"\b(?:future|later|could|may)\b.{0,55}\b(?:support|enable|extend|inform)\b.{0,55}\b(?:hand|hands|dexterous)\b", normalize(abstract)))
    dexterity = dexterity and (not nonhand_title or title_dexterity) and (not future_hand or title_dexterity)
    robot = bool(matches(text, ROBOT_TERMS + HAND_TERMS))
    transfer = bool(matches(text, MIGRATION_TERMS)) and robot
    weak_force = bool(matches(physical, WEAK_FORCE_TERMS)) and robot
    if not (legacy or contact or dexterity or retarget and robot or transfer or weak_force):
        return None
    negative_retarget = bool(matches(title, NEGATIVE_RETARGET))
    negative_contact = bool(matches(title, NEGATIVE_CONTACT))
    constraint_contact = (bool(matches(title, ("collision free",)))
                          and bool(matches(text, ("minimum allowed separation", "minimum separation", "separation violations")))
                          and not matches(text, ("contact force", "contact forces", "tactile", "haptic", "friction", "grasping", "manipulation", "impedance")))
    if negative_contact and not (legacy or dexterity or retarget and robot or transfer or weak_force):
        return None
    # A negated title is related literature, not positive evidence for the denied
    # method. Keep it discoverable but do not infer the denied contribution.
    positive_contact = contact and not (negative_contact or constraint_contact)
    positive_retarget = (anchor or retarget or transfer) and not negative_retarget
    support_title = bool(matches(title, SUPPORT_TERMS))
    groups = []
    if positive_retarget:
        groups.append("retargeting")
    if positive_contact:
        if matches(physical, PERCEPTION_TERMS):
            groups.append("contact-perception")
        if not support_title or matches(title, ("control", "manipulation", "grasping", "retargeting")):
            groups.append("contact-control")
    if support_title or matches(text, SUPPORT_TERMS) and paper.get("track") == "Data, Simulation & Evaluation":
        groups.append("datasets-simulation")
    if positive_contact and matches(physical, MECHANICS_TERMS):
        groups.append("contact-mechanics")
    if residual_action or residual_other:
        groups.append("residual")
    if positive_contact and (matches(text, ARM_TERMS) or paper.get("track") == "Arm & General Object Manipulation"):
        groups.append("arm-contact")
    if positive_contact and matches(text, PLANNING_TERMS):
        groups.append("contact-planning")
    if positive_contact and matches(text, LEGGED_TERMS):
        groups.append("legged-contact")
    if positive_contact and matches(text, HRI_TERMS):
        groups.append("physical-hri")
    if dexterity:
        groups.append("dexterous-manipulation")
    if not groups:
        # Negative comparisons and bare force/torque cues remain discoverable
        # without assigning the contribution that the paper explicitly denies.
        groups.append("related-comparisons")
    strong = (anchor or bool(matches(title, CONTACT_TERMS)) and not nonphysical
              or title_dexterity
              or bool(matches(title, RETARGET_TERMS)) and robot)
    if negative_retarget or negative_contact or nonphysical or constraint_contact:
        strong = False
    if residual_other and not residual_action:
        residual_role = "representation-or-model; not action residual"
    elif residual_action:
        residual_role = "action/control phrase; locus needs source review"
    else:
        residual_role = "not established"
    boundary = "机器筛选基于标题、摘要和已有分类，不证明该主题就是论文主要贡献，也不代表全文审阅或实机验证。"
    if nonhand_title:
        boundary += " 本体含全身／夹爪／其他机器人线索，是接触领域相关方法；不能自动作为多指手成果。"
    elif dexterity and not title_dexterity:
        boundary += " 灵巧手线索来自摘要语境，不能直接认定已完成多指手任务或实机验证。"
    if dexterity and not matches(text, EXPLICIT_ROBOT_HAND):
        boundary += " 灵巧任务未明确多指机器人手本体；不能将一般灵巧操作等同于手内或多指手实验。"
    if negative_retarget or negative_contact:
        boundary += " 标题含否定式关键词，仅作相关领域索引；不能据此认定论文采用被否定的重定向或接触机制。"
    if constraint_contact:
        boundary += " contact 描述最小间距约束的激活点，未确认物理触碰；仅列相关规划对照。"
    if nonphysical:
        boundary += " 含追踪／联络／合规等非物理词义，已忽略这些短语；保留的其他命中仍需人工复核。"
    if weak_force and not positive_contact:
        boundary += " 仅有力／力矩线索时也可能是驱动或其他物理力，并未确认接触机制或接触力学贡献。"
    if support_title:
        boundary += " 数据、仿真或评测支撑不等于已完成机器人重定向或控制。"
    if residual_other and not residual_action:
        boundary += " 残差位于表征或模型，不能称为动作残差控制。"
    return {"tier": "strong-candidate" if strong else "broad-candidate", "groups": groups,
            "why_zh": "接触／力触觉、灵巧操作或重定向／示教迁移词组命中；具体依据见标题／摘要证据。",
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
    source_counts = Counter(v["source_layer"] for row in all_rows for v in row["source_variants"])
    source_reading_counts = {layer: sum(any(v["source_layer"] == layer for v in row["source_variants"]) for row in all_rows)
                             for layer in ("conference", "arxiv")}
    source_overlap = sum({v["source_layer"] for v in row["source_variants"]} == {"conference", "arxiv"} for row in all_rows)
    conference_venues = Counter(v["venue"] for row in all_rows for v in row["source_variants"] if v["source_layer"] == "conference")
    return {
        "schema_version": 2,
        "generated_on": status.get("documents_updated_on", curation.get("checked_on", "")),
        "curation_checked_on": curation.get("checked_on", ""),
        "curation_review_scope": curation.get("review_scope", ""),
        "discovery_notes": curation.get("discovery_notes", []),
        "source_snapshots": {"conference": catalog.get("as_of", ""), "arxiv": arxiv.get("as_of", "")},
        "source_metadata": {"conference": {key: catalog.get(key, []) if key == "venues" else catalog.get(key, {}) for key in ("window", "venues")},
                            "arxiv": {"window": arxiv.get("window", {})}},
        "scope": "Current conference and arXiv catalog metadata only; not all global literature or universal paper identities.",
        "selection_policy": {
            "candidate_union": "Physical contact/force/tactile methods across embodiments, dexterous manipulation, robot retargeting/demonstration transfer, legacy hand/contact/residual rules, or exact reviewed title/arXiv identities.",
            "matching": "Casefolded, punctuation-normalized whole phrases; no naked acronym substring matching.",
            "identity": "Normalized-title reading deduplication; all original source variants retained. Different titles may still describe one work.",
            "tiers": TIERS,
            "group_counts_overlap": True,
            "review_boundary": "Reviewed means the supplied title/abstract/selected-source review basis, not universal full-paper reading or reproduction.",
        },
        "counts": {"source_records": sum(len(p["source_variants"]) for p in all_rows),
                   "matched_source_records": matched_source_records,
                   "reading_records": len(all_rows),
                   "conference_source_records": source_counts["conference"],
                   "arxiv_source_records": source_counts["arxiv"],
                   "source_reading_counts": source_reading_counts,
                   "conference_arxiv_overlap_reading_records": source_overlap,
                   "conference_venue_source_counts": dict(sorted(conference_venues.items())),
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
    lines = ["# 接触方法、灵巧操作与重定向", "",
             "按可交叉的研究方向整理所有本体的接触方法，以及灵巧操作、重定向与示教迁移；覆盖机械臂、夹爪、多指手、足式／全身、物理人机交互、感知、仿真与规划，并单设相关对照／范围待定附录。", "",
             f"范围：会议快照 **{focus['source_snapshots']['conference']}**，arXiv 快照 **{focus['source_snapshots']['arxiv']}**；人工来源核查日期 **{focus['curation_checked_on']}**。", "",
             f"当前共 **{counts['reading_records']:,} 条规范标题去重阅读记录**，保留 **{counts['source_records']:,} 条会议／预印本来源记录**。这不是全网论文总数；不同标题仍可能属于同一工作。", "",
             f"其中会议层 **{counts['conference_source_records']:,} 条来源记录**，arXiv 层 **{counts['arxiv_source_records']:,} 条来源记录**；**{counts['conference_arxiv_overlap_reading_records']:,} 条规范标题**同时出现在两层。两层来源数量可相加，标题阅读数量不可直接相加。", "",
             "[完整会议目录](conference/README.md) · [完整 arXiv 目录](arxiv/README.md) · [在线筛选](https://dld0621.github.io/Embodied-AI-Paper-Analysis/dexterous-retargeting-contact.html)", "",
             "[下载完整 JSON](../../../data/dexterous-retargeting-contact.json) · [下载完整 CSV](../../../data/dexterous-retargeting-contact.csv) · [回到全库分类](../../taxonomy/README.md)", "",
             "## 阅读层级", "", "| 层级 | 阅读记录 | 含义 |", "|---|---:|---|"]
    explanations = {"reviewed": "有明确的一手来源核查记录；仍须查看其审核基础与实验边界。",
                    "strong-candidate": "标题或已有分类明确命中相应领域，尚不等于人工确认主要贡献。",
                    "broad-candidate": "摘要、一般力／力矩或关联语境命中，可能只是背景／比较，需进一步复核。"}
    for tier, name in TIERS.items():
        lines.append(f"| {name} | {counts['tier_counts'][tier]:,} | {explanations[tier]} |")
    lines.extend(["", "分组允许交叉，下面数量不可相加。一般抓取不自动等于接触力学；触觉不自动等于多指手；人手交互数据不自动等于机器人重定向。", "",
                  "## 按问题进入", "",
                  f"**口径区别：**原有手部重定向索引（既有 Hand Retargeting 标签或手部重定向主类）为 **{counts['hand_retargeting_anchor_source_records']:,} 条来源记录／{counts['hand_retargeting_anchor_reading_records']:,} 条规范标题去重记录**。本专题“重定向与示教迁移”分组的 **{counts['group_counts']['retargeting']:,} 条**还包含全身／跨本体示教迁移和待审候选，**不等于 {counts['group_counts']['retargeting']:,} 篇已核实手部重定向论文**；原有索引数量也不是语义完整性或全文审阅证明。", "",
                  "| 专题 | 阅读记录 | 范围 |", "|---|---:|---|"])
    for group in GROUPS:
        lines.append(f"| [{group['name_zh']}]({group['slug']}/README.md) | {counts['group_counts'][group['slug']]:,} | {group['description_zh']} |")
    lines.extend(["", "## 优先阅读：已核查条目", ""])
    reviewed = [p for p in papers if p["tier"] == "reviewed"]
    lines.extend(_paper_table(reviewed) if reviewed else ["本次没有独立核查条目；请勿将自动候选称作已审核。"])
    lines.extend(["", "## 完整候选目录", "", "以下分页保留全部宽范围待审候选；每页最多 100 条，JSON 和 CSV 提供逐条证据与全部来源。", ""])
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
                  "- 全身／四足、双指夹爪、机械臂装配、连续体接触模型等属于接触研究覆盖范围，但不能自动成为多指手实验成果；本体与技术贡献分别核查。",
                  "- 力／力矩词组不自动证明接触力学贡献；否定式或比较语境仍可能作为待审相关文献保留，不能据此认定论文采用被否定的机制。",
                  "- 残差适配器／网络、规划代价和动作残差属于不同作用位置；未核查条目不能仅因 residual 一词认定为动作残差。",
                  "- 自动候选可能漏检或误检；已核查只对应各条所列的标题／摘要、局部全文或其他来源核对，不代表全库全文精读、成功复现或实机验证。", ""])
    outputs[base / "README.md"] = "\n".join(lines).rstrip() + "\n"
    for layer, label in (("conference", "会议来源"), ("arxiv", "arXiv 来源")):
        layer_rows = []
        for paper in papers:
            variants = [v for v in paper["source_variants"] if v["source_layer"] == layer]
            if variants:
                # Show this layer in the summary table; retain every variant in
                # the detailed provenance so no source record disappears.
                layer_rows.append({**paper, **{key: variants[0][key] for key in ("year", "venue", "paper_url", "official_url")}})
        metadata = focus.get("source_metadata", {}).get(layer, {})
        window = metadata.get("window", {})
        window_text = f"{window.get('start', '未声明')} 至 {window.get('end', '未声明')}"
        page = [f"# 接触、灵巧操作与重定向 · {label}完整目录", "", "[← 专题总览](../README.md)", "",
                f"来源快照：**{focus['source_snapshots'][layer]}**；原库收录窗口：**{window_text}**。", "",
                f"本层 **{counts[f'{layer}_source_records']:,} 条来源记录／{len(layer_rows):,} 条规范标题去重阅读记录**；全部分页保留，每页最多 {PAGE_SIZE} 条。", "",
                "目录沿用总表的已核查／明确元数据候选／宽范围待审候选层级；同一标题的其他来源仍可在逐条证据中查看。", ""]
        if layer == "conference":
            page.extend(["收录会议范围：" + "、".join(metadata.get("venues", [])) + "。", "",
                         "会议层包含原库已核查条目和书目元数据来源；请查看各条官方来源。书目标签及与 arXiv 的标题重合，不单独构成录用核实证明。", "",
                         "| 会议书目来源 | 本专题来源记录 |", "|---|---:|"])
            for venue, count in counts["conference_venue_source_counts"].items():
                page.append(f"| {_cell(venue)} | {count:,} |")
            page.append("")
        else:
            page.extend(["本层来自原库收录的 arXiv cs.RO 记录；预印本身份不代表已获会议录用，库外经典见专题总览独立补充表。", ""])
        for index in range(0, len(layer_rows), PAGE_SIZE):
            batch = layer_rows[index:index + PAGE_SIZE]
            name = f"part-{index // PAGE_SIZE + 1:03}.md"
            page.append(f"- [完整{label}清单 {index // PAGE_SIZE + 1}：{index + 1}–{index + len(batch)}]({name})")
            part = [f"# {label} · {index // PAGE_SIZE + 1}", "", "[← 来源目录](README.md) · [专题总览](../README.md)", ""]
            part.extend(_paper_table(batch))
            part.extend(["", "## 逐条纳入证据", ""])
            for paper in batch:
                part.extend(_detail(paper))
            outputs[base / layer / name] = "\n".join(part).rstrip() + "\n"
        outputs[base / layer / "README.md"] = "\n".join(page).rstrip() + "\n"
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
