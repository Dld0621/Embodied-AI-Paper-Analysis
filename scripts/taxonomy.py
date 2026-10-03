"""Contribution-oriented nine-direction taxonomy and cross-topic tags.

Admission to the source census is independent of this organization step.
Automatic assignments are reproducible suggestions, not semantic certification.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import re
from typing import Any

SCHEMA = json.loads(Path(__file__).with_name("taxonomy_schema.json").read_text())
GENERAL_SPECIALTY = "Pending specialty review"
GENERAL_SPECIALTY_ZH = "待审专题"
HIERARCHY = {
    track["name"]: {
        sub["name"]: {
            "name_zh": sub["name_zh"],
            "terms": (),
            "specialties": tuple(
                (spec["name"], spec["name_zh"], tuple(spec["terms"]))
                for spec in sub["specialties"]
            ),
        }
        for sub in track["subcategories"]
    }
    for track in SCHEMA["tracks"]
}
TRACKS = list(HIERARCHY)
TRACK_META = {
    track["name"]: {key: track[key] for key in
                    ("name_zh", "question", "question_zh", "pipeline", "pipeline_zh")}
    for track in SCHEMA["tracks"]
}
DEFAULT_SUBCATEGORY = {track: next(iter(subs)) for track, subs in HIERARCHY.items()}
LEGACY_TRACKS = {
    "Foundation Models & VLA": TRACKS[0],
    "Manipulation & Imitation": TRACKS[1],
    "Dexterity & Teleoperation": TRACKS[2],
    "Navigation & Embodied Agents": TRACKS[3],
    "Humanoids & Locomotion": TRACKS[4],
    "Perception & World Models": TRACKS[5],
    "Simulation, Data & Evaluation": TRACKS[7],
}
OVERRIDES = json.loads(Path(__file__).with_name("taxonomy_overrides.json").read_text())

# Search facets supplement the mutually exclusive primary directory.
TAG_RULES = {
    "method_tags": {
        "Reinforcement Learning": ("强化学习", ("reinforcement learning", "rl", "policy gradient", "actor critic")),
        "Imitation Learning": ("模仿学习", ("imitation learning", "behavior cloning", "learning from demonstration")),
        "Optimization": ("优化", ("optimization", "inverse kinematics", "quadratic program")),
        "Diffusion": ("扩散", ("diffusion", "denoising")),
        "Flow Matching": ("Flow Matching", ("flow matching",)),
        "MPC": ("模型预测控制", ("model predictive control", "mpc")),
        "Physics Constraints": ("物理约束", ("physics based", "physics informed", "dynamic feasibility")),
    },
    "embodiment_tags": {
        "Dexterous Hands": ("灵巧手", ("dexterous", "multifinger", "multi finger", "robot hand", "robot hands")),
        "Humanoids": ("人形机器人", ("humanoid", "humanoids", "bipedal")),
        "Quadrupeds": ("四足机器人", ("quadruped", "quadrupedal")),
        "Arms & Grippers": ("机械臂与夹爪", ("manipulator", "robot arm", "gripper", "parallel jaw")),
        "Aerial Robots": ("空中机器人", ("uav", "aerial", "drone")),
        "Marine Robots": ("水下机器人", ("underwater", "marine")),
        "Ground Vehicles": ("地面车辆", ("autonomous driving", "ground vehicle", "mobile robot")),
    },
    "data_tags": {
        "Human Video": ("人类视频", ("human video", "human videos", "monocular video", "video demonstration")),
        "Motion Capture": ("动作捕捉", ("motion capture", "mocap", "motion recordings")),
        "Teleoperation Data": ("遥操作数据", ("teleoperation", "teleoperated", "teleoperating")),
        "Simulation": ("仿真", ("simulation", "simulated", "simulator")),
        "Real Robot": ("真实机器人", ("real robot", "real robots", "hardware experiments", "physical hardware")),
        "Tactile Data": ("触觉数据", ("tactile", "touch sensing")),
    },
    "related_topics": {
        "Retargeting": ("全部重定向", ("retargeting", "retarget")),
        "Hand Retargeting": ("灵巧手重定向", ()),
        "Whole-body Retargeting": ("全身重定向", ()),
        "Dexterous Manipulation": ("灵巧操作", ("dexterous manipulation", "in hand manipulation")),
        "Bimanual": ("双手／双臂", ("bimanual", "dual arm", "dual hand")),
        "Contact-rich": ("接触丰富交互", ("contact rich", "hand object", "contact structure")),
        "Teleoperation": ("遥操作", ("teleoperation", "teleoperated")),
        "World Models": ("世界模型", ("world model", "world models", "world action model")),
    },
}


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).strip()


@lru_cache(maxsize=None)
def normalize_term(value: str) -> str:
    return normalize_text(value)


def term_present(text: str, term: str) -> bool:
    term = normalize_term(term)
    return bool(term) and f" {term} " in f" {text} "


def score_terms(terms, title, topic, abstract):
    # Legacy admission topics do not determine the new organization.
    matches = []
    for term in set(terms):
        for location, text, weight in (("title", title, 12), ("abstract", abstract, 1)):
            if term_present(text, term):
                value = weight + min(len(normalize_term(term).split()), 4)
                matches.append((value, normalize_term(term), location))
    if not matches:
        return 0, "fallback"
    best = max(matches)
    return sum(match[0] for match in matches), f"{best[2]}:{best[1]}"


def _contains(text, terms):
    return any(term_present(text, term) for term in terms)


def _hand_retargeting(title, abstract):
    hand = _contains(title, ("hand", "hand pose", "hand object", "dexterous", "finger"))
    retarget = "retarget" in title
    # Hand-object contact can be central even without 'hand' in the title.
    hand_context = _contains(abstract, ("human hand", "robot hand", "target hands", "robot hands"))
    body_title = _contains(title, ("humanoid", "whole body", "quadruped", "upper body"))
    return retarget and (hand or (hand_context and not body_title))


def _primary_track(title, abstract, old_track):
    """Use explicit contribution cues before generic keyword ranking."""
    if _contains(title, ("dataset", "benchmark", "data engine", "simulator", "simulation platform")):
        return TRACKS[7], "title:data or evaluation contribution"
    if _contains(title, ("sensor", "actuator", "motor", "mechanism", "robot design", "hand design",
                         "gripper design", "hand based on", "on device", "policy compression")):
        return TRACKS[8], "title:hardware or deployment contribution"
    if _hand_retargeting(title, abstract):
        return TRACKS[2], "title/abstract:hand retargeting"
    if _contains(title, ("world model", "world models", "video prediction", "latent dynamics",
                         "task planning", "embodied reasoning", "question answering", "episodic memory")):
        return TRACKS[6], "title:prediction or reasoning"
    if _contains(title, ("humanoid", "humanoids", "quadruped", "bipedal", "locomotion",
                         "whole body", "gait", "legged", "motion retargeting")):
        return TRACKS[4], "title:locomotion or whole body"
    if _contains(title, ("navigation", "slam", "odometry", "localization", "path planning",
                         "exploration", "swarm", "formation control")):
        return TRACKS[3], "title:navigation or localization"
    if _contains(title, ("dexterous", "in hand", "finger gaiting", "multifinger", "multi finger",
                         "teleoperation", "shared autonomy", "hand retargeting")):
        return TRACKS[2], "title:dexterous hands or teleoperation"
    if _contains(title, ("vision language action", "vla", "diffusion policy", "flow policy",
                         "behavior cloning", "offline reinforcement", "generalist robot",
                         "robot pretraining")):
        return TRACKS[0], "title:general policy learning"
    if _contains(title, ("manipulation", "grasp", "grasping", "insertion", "assembly",
                         "pick and place", "rearrangement", "cloth", "rope", "handover")):
        return TRACKS[1], "title:object manipulation"
    if _contains(title, ("reconstruction", "perception", "pose estimation", "segmentation",
                         "depth estimation", "tracking", "tactile", "sensor fusion")):
        return TRACKS[5], "title:perception or state"
    ranked = []
    for index, (track, subfields) in enumerate(HIERARCHY.items()):
        # Maximum leaf score avoids favoring directions with more vocabulary.
        score = max(
            score_terms(terms, title, "", abstract)[0]
            for meta in subfields.values() for _, _, terms in meta["specialties"]
        )
        ranked.append((score, -index, track))
    score, _, track = max(ranked)
    if score:
        return track, "rule:contribution vocabulary"
    return LEGACY_TRACKS.get(old_track, old_track if old_track in HIERARCHY else TRACKS[0]), "fallback"


def classify_hierarchy(track, title, topic="", abstract=""):
    if track not in HIERARCHY:
        raise ValueError(f"Unsupported research track: {track}")
    title_text, abstract_text = normalize_text(title), normalize_text(abstract)
    ranked = []
    for sub_index, (name, meta) in enumerate(HIERARCHY[track].items()):
        for spec_index, (spec, _, terms) in enumerate(meta["specialties"]):
            score, evidence = score_terms(terms, title_text, "", abstract_text)
            if score:
                ranked.append((score, -sub_index, -spec_index, name, spec, evidence))
    if track == TRACKS[2] and _hand_retargeting(title_text, abstract_text):
        name = "Dexterous Hand Retargeting"
        selected = [row for row in ranked if row[3] == name]
        if selected:
            _, _, _, sub, spec, evidence = max(selected)
            return sub, spec, evidence
        return name, GENERAL_SPECIALTY, "title:retargeting"
    if not ranked:
        return DEFAULT_SUBCATEGORY[track], GENERAL_SPECIALTY, "fallback"
    _, _, _, sub, spec, evidence = max(ranked)
    return sub, spec, evidence


def annotate_paper(paper: dict[str, Any], abstract: str = "") -> dict[str, Any]:
    abstract = abstract or paper.get("abstract", "")
    title_text, abstract_text = normalize_text(paper["title"]), normalize_text(abstract)
    paper.setdefault("admission_track", paper["track"])
    override = OVERRIDES.get(title_text)
    track, primary_evidence = _primary_track(title_text, abstract_text, paper["admission_track"])
    if override:
        track, sub, spec = override["path"]
        evidence = "reviewed:" + override["reason"]
        primary_evidence = evidence
    else:
        sub, spec, evidence = classify_hierarchy(track, paper["title"], "", abstract)
    paper.update(track=track, subcategory=sub, specialty=spec, taxonomy_evidence=evidence,
                 primary_evidence=primary_evidence,
                 classification_status="reviewed" if override else
                 ("needs-review" if evidence == "fallback" or primary_evidence == "fallback"
                  or spec == GENERAL_SPECIALTY else "rule-assigned"))
    combined = title_text + " " + abstract_text
    for field, rules in TAG_RULES.items():
        paper[field] = [name for name, (_, terms) in rules.items() if _contains(combined, terms)]
    if _hand_retargeting(title_text, abstract_text) or sub == "Dexterous Hand Retargeting":
        paper["related_topics"].append("Hand Retargeting")
    if "retarget" in combined and _contains(combined, ("humanoid", "whole body", "quadruped")):
        paper["related_topics"].append("Whole-body Retargeting")
    if override:
        paper["related_topics"].extend(override.get("related_topics", []))
        paper["related_topics"] = [
            topic for topic in paper["related_topics"]
            if topic not in override.get("excluded_topics", [])
        ]
    for field in TAG_RULES:
        paper[field] = sorted(set(paper[field]))
    paper["related_taxonomy_paths"] = []
    # These links are associations, not extra primary directory attachments.
    if "Hand Retargeting" in paper["related_topics"] and sub != "Dexterous Hand Retargeting":
        paper["related_taxonomy_paths"].append(
            {"track": TRACKS[2], "subcategory": "Dexterous Hand Retargeting"})
    if "Whole-body Retargeting" in paper["related_topics"] and sub != "Whole-body Motion Transfer":
        paper["related_taxonomy_paths"].append(
            {"track": TRACKS[4], "subcategory": "Whole-body Motion Transfer"})
    if "Reinforcement Learning" in paper["method_tags"] and sub != "Reinforcement Learning":
        paper["related_taxonomy_paths"].append(
            {"track": TRACKS[0], "subcategory": "Reinforcement Learning"})
    return paper


def taxonomy_metadata():
    tracks = {}
    for track, subfields in HIERARCHY.items():
        tracks[track] = {"subcategories": {
            name: {"name_zh": meta["name_zh"], "specialties": {
                **{spec: {"name_zh": zh} for spec, zh, _ in meta["specialties"]},
                GENERAL_SPECIALTY: {"name_zh": GENERAL_SPECIALTY_ZH},
            }} for name, meta in subfields.items()
        }}
    return {
        "version": 3,
        "levels": {
            "level_1": {"field": "track", "name": "Research direction", "name_zh": "一级研究方向"},
            "level_2": {"field": "subcategory", "name": "Subfield", "name_zh": "二级子领域"},
            "level_3": {"field": "specialty", "name": "Specialty", "name_zh": "三级专题"},
        },
        "classification": "Primary contribution rules and title/abstract evidence; reviewed exceptions take precedence. One primary path, additional method/embodiment/data/topic facets. Unsupported assignments are marked needs-review.",
        "tracks": tracks,
        "subcategory_count": sum(len(subs) for subs in HIERARCHY.values()),
        "specialty_count": sum(len(meta["specialties"]) for subs in HIERARCHY.values() for meta in subs.values()),
        "fallback_specialty_count": sum(len(subs) for subs in HIERARCHY.values()),
        "facets": {field: {name: {"name_zh": zh} for name, (zh, _) in rules.items()}
                   for field, rules in TAG_RULES.items()},
        "review_statuses": ["reviewed", "rule-assigned", "needs-review"],
    }


def hierarchy_counts(papers):
    return {
        "level_1": dict(sorted(Counter(p["track"] for p in papers).items())),
        "level_2": dict(sorted(Counter(f'{p["track"]} / {p["subcategory"]}' for p in papers).items())),
        "level_3": dict(sorted(Counter(f'{p["track"]} / {p["subcategory"]} / {p["specialty"]}' for p in papers).items())),
        "classification_evidence": dict(sorted(Counter(p["taxonomy_evidence"].split(":", 1)[0] for p in papers).items())),
        "review_status": dict(sorted(Counter(p.get("classification_status", "needs-review") for p in papers).items())),
    }
