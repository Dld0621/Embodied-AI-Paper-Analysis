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
# Unknown dexterity is not evidence of human-to-hand retargeting.
DEFAULT_SUBCATEGORY[TRACKS[2]] = "Multifinger Grasping & Control"
# Parent cues locate a subfield even when its specific level-3 method is unknown.
SUBFIELD_CUES = {
    "Imitation Learning": ("imitation learning", "learning from demonstration", "learning from demonstrations", "behavior cloning"),
    "Reinforcement Learning": ("reinforcement learning", "online rl", "offline rl"),
    "Generative Action Policies": ("diffusion policy", "diffusion policies", "flow matching", "action token"),
    "VLA & Generalist Robot Policies": ("vision language action", "generalist robot", "vla", "robot foundation"),
    "Generalization & Adaptation": ("policy adaptation", "cross robot", "cross embodiment", "test time adaptation"),
    "Grasping & Pick-place": ("grasp", "grasping", "pick place", "rearrangement"),
    "Contact-rich Manipulation": ("insertion", "assembly", "pushing", "pulling", "tool use", "articulated", "contact rich"),
    "Deformable Object Manipulation": ("deformable", "cloth", "garment", "rope", "fabric"),
    "Coordinated & Complex Manipulation": ("bimanual", "dual arm", "mobile manipulation", "task and motion planning", "long horizon manipulation"),
    "Multifinger Grasping & Control": ("dexterous grasping", "dexterous grasp", "multifinger", "multi finger", "grasp force", "hand control", "grip force"),
    "In-hand Manipulation": ("in hand", "object reorientation", "finger gaiting", "pen spinning"),
    "Teleoperation & Shared Control": ("teleoperation", "telemanipulation", "telepresence", "shared autonomy", "shared control", "bilateral"),
    "Human Demonstrations to Dexterous Skills": ("human video", "human videos", "human demonstration", "human demonstrations", "dexterous imitation", "skill transfer"),
    "Localization & Mapping": ("slam", "odometry", "localization", "mapping", "relocalization"),
    "Goal & Language Navigation": ("goal navigation", "objectnav", "vision language navigation", "language navigation", "vln", "semantic navigation"),
    "Motion Planning & Exploration": ("path planning", "motion planning", "exploration", "obstacle avoidance", "trajectory optimization"),
    "Multi-robot & Social Navigation": ("multi robot", "social navigation", "swarm", "formation", "human aware navigation"),
    "Bipedal & Humanoid Locomotion": ("humanoid walking", "bipedal", "biped", "walking", "footstep"),
    "Quadruped & Multilegged Locomotion": ("quadruped", "quadrupedal", "hexapod", "multilegged"),
    "Whole-body Coordination & Balance": ("whole body control", "balance", "fall recovery", "push recovery", "humanoid control"),
    "Whole-body Motion Transfer": ("motion retargeting", "humanoid retargeting", "whole body retargeting", "motion imitation", "human motion", "motion generation"),
    "Locomotion-Manipulation Coordination": ("loco manipulation", "humanoid manipulation", "leg arm", "whole body interaction"),
    "3D Environment Perception": ("3d reconstruction", "point cloud", "depth estimation", "occupancy", "gaussian splatting", "nerf"),
    "Object & Interaction Perception": ("object detection", "segmentation", "object tracking", "object pose", "6d pose", "affordance"),
    "Human & Hand-object Perception": ("hand pose", "hand tracking", "human pose", "human body", "hand object reconstruction"),
    "Tactile & Multimodal Perception": ("tactile", "visuotactile", "visual tactile", "sensor fusion", "proprioception"),
    "State Estimation & Active Perception": ("state estimation", "calibration", "active perception", "view selection", "synchronization"),
    "World & Dynamics Modeling": ("world model", "world models", "dynamics model", "video prediction", "contact dynamics"),
    "Model-based Decision Making": ("model predictive control", "mpc", "model based planning", "model based rl", "imagination", "world model planning"),
    "Task Reasoning & Planning": ("task planning", "task decomposition", "symbolic planning", "llm planning", "embodied reasoning", "question answering"),
    "Memory & Autonomous Execution": ("episodic memory", "replanning", "autonomous execution", "memory augmented", "failure recovery"),
    "Datasets & Data Engineering": ("dataset", "datasets", "data curation", "data quality", "annotation", "data collection"),
    "Synthetic & Augmented Data": ("data engine", "data generation", "synthetic data", "data augmentation", "data synthesis", "data conversion"),
    "Simulation & Digital Twins": ("simulator", "simulators", "simulation framework", "simulation platform", "digital twin", "differentiable simulation"),
    "Sim-to-real Transfer": ("sim to real", "sim2real", "domain randomization", "system identification", "reality gap"),
    "Benchmarks & Experimental Methods": ("benchmark", "benchmarks", "benchmarking", "evaluation protocol", "evaluation metric"),
    "Safety & Reliability Evaluation": ("safety verification", "safety evaluation", "formal verification", "fault diagnosis", "failure analysis"),
    "Mechanisms & Actuation": ("hand design", "gripper design", "robot design", "dexterous hand", "robotic hand", "robot hand", "actuator", "actuation", "transmission", "motor"),
    "Sensors & Human Interfaces": ("tactile sensor", "force sensor", "sensor design", "wearable", "haptic device", "exoskeleton", "data glove", "force feedback glove", "tactile finger", "sensorized soft skin"),
    "Soft & Specialized Robots": ("soft robot", "soft gripper", "continuum robot", "biomimetic", "bio inspired", "underwater robot"),
    "Computing & Deployment Systems": ("software framework", "toolkit", "on device", "policy compression", "middleware", "inference latency", "communication architecture"),
}
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
        for location, text, weight in (("title", title, 1000), ("abstract", abstract, 1)):
            if term_present(text, term):
                value = weight + min(len(normalize_term(term).split()), 4)
                matches.append((value, normalize_term(term), location))
    if not matches:
        return 0, "fallback"
    best = max(matches)
    # A pile of background abstract terms cannot outweigh a title contribution.
    title_matches = [match for match in matches if match[2] == "title"]
    selected = title_matches or matches
    return sum(match[0] for match in selected), f"{best[2]}:{best[1]}"


def _contains(text, terms):
    return any(term_present(text, term) for term in terms)


def _hand_retargeting(title, abstract):
    if _contains(title, ("without retargeting", "retargeting free", "no retargeting")):
        return False
    hand = _contains(title, ("hand", "hand pose", "hand object", "dexterous", "finger"))
    retarget = "retarget" in title
    # Hand-object contact can be central even without 'hand' in the title.
    hand_context = _contains(abstract, ("human hand", "robot hand", "target hands", "robot hands"))
    body_title = _contains(title, ("humanoid", "whole body", "quadruped", "upper body"))
    return retarget and (hand or (hand_context and not body_title))


def _primary_track(title, abstract, old_track):
    """Use explicit contribution cues before generic keyword ranking."""
    if _contains(title, ("dataset", "datasets", "benchmark", "benchmarks", "data engine",
                         "data generation", "data collection", "simulator", "simulators", "simulation platform", "simulation framework")):
        return TRACKS[7], "title:data or evaluation contribution"
    if _contains(title, ("sensor fusion", "sensor calibration", "tactile representation",
                         "hand pose estimation", "hand tracking", "human pose estimation",
                         "force estimation", "object pose", "contact estimation")):
        return TRACKS[5], "title:perception or estimation contribution"
    design = _contains(title, ("design", "designed", "development", "fabrication", "modular",
                              "underactuated", "tendon driven", "cable driven", "low cost"))
    device = _contains(title, ("hand", "gripper", "arm", "robot", "robots", "sensor", "sensors", "glove", "finger"))
    if (design and device) or _contains(title, ("tactile sensor", "tactile sensors", "force sensor",
                         "actuator", "motor", "mechanism", "robot design", "hand design",
                         "gripper design", "hand based on", "force feedback glove", "tactile finger",
                         "sensorized soft skin", "exoskeleton", "on device", "policy compression")):
        return TRACKS[8], "title:hardware or deployment contribution"
    if _hand_retargeting(title, abstract):
        return TRACKS[2], "title/abstract:hand retargeting"
    if _contains(title, ("world model", "world models", "video prediction", "latent dynamics",
                         "task planning", "embodied reasoning", "question answering", "episodic memory")):
        return TRACKS[6], "title:prediction or reasoning"
    if _contains(title, ("vision language action", "vla", "robot foundation model", "generalist robot")):
        return TRACKS[0], "title:foundation policy contribution"
    if _contains(title, ("humanoid", "humanoids", "quadruped", "bipedal", "locomotion",
                         "whole body", "gait", "legged", "motion retargeting")):
        return TRACKS[4], "title:locomotion or whole body"
    if _contains(title, ("navigation", "slam", "odometry", "localization", "path planning",
                         "exploration", "swarm", "formation control")):
        return TRACKS[3], "title:navigation or localization"
    if _contains(title, ("dexterous", "in hand", "finger gaiting", "multifinger", "multi finger",
                         "teleoperation", "telemanipulation", "shared autonomy", "hand retargeting")):
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
    is_hand_retargeting = _hand_retargeting(title_text, abstract_text)
    # Explicit title-level parent cues constrain abstract-level leaf ranking.
    parent_matches = []
    for index, name in enumerate(HIERARCHY[track]):
        terms = SUBFIELD_CUES.get(name, ())
        found = [normalize_term(term) for term in terms if term_present(title_text, term)]
        if found:
            best = max(found, key=lambda term: (len(term.split()), len(term), term))
            parent_matches.append((len(best.split()), len(best), -index, name, best))
    selected_parent = max(parent_matches)[3] if parent_matches else None
    if track == TRACKS[2] and is_hand_retargeting:
        selected_parent = "Dexterous Hand Retargeting"
    ranked = []
    for sub_index, (name, meta) in enumerate(HIERARCHY[track].items()):
        if name == "Dexterous Hand Retargeting" and not is_hand_retargeting:
            continue
        if selected_parent and name != selected_parent:
            continue
        if name == "Human Demonstrations to Dexterous Skills" and _contains(title_text, ("without demonstrations", "without human demonstrations", "demonstration free")):
            continue
        for spec_index, (spec, _, terms) in enumerate(meta["specialties"]):
            score, evidence = score_terms(terms, title_text, "", abstract_text)
            if score:
                ranked.append((score, -sub_index, -spec_index, name, spec, evidence))
    if track == TRACKS[2] and is_hand_retargeting:
        name = "Dexterous Hand Retargeting"
        selected = [row for row in ranked if row[3] == name]
        if selected:
            _, _, _, sub, spec, evidence = max(selected)
            return sub, spec, evidence
        return name, GENERAL_SPECIALTY, "title:retargeting"
    if not ranked:
        if selected_parent:
            matched = next(row[4] for row in parent_matches if row[3] == selected_parent)
            return selected_parent, GENERAL_SPECIALTY, f"title:{matched}"
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
                 subcategory_status="provisional" if evidence == "fallback" else "rule-supported",
                 classification_status="reviewed" if override else
                 ("needs-review" if evidence == "fallback" or primary_evidence == "fallback"
                  or spec == GENERAL_SPECIALTY else "rule-assigned"))
    combined = title_text + " " + abstract_text
    for field, rules in TAG_RULES.items():
        paper[field] = [name for name, (_, terms) in rules.items() if _contains(combined, terms)]
    if _hand_retargeting(title_text, abstract_text):
        paper["related_topics"].append("Hand Retargeting")
    if "retarget" in title_text and _contains(title_text, ("humanoid", "whole body", "quadruped", "motion retargeting")) and not _hand_retargeting(title_text, abstract_text):
        paper["related_topics"].append("Whole-body Retargeting")
    if override:
        paper["related_topics"].extend(override.get("related_topics", []))
        paper["related_topics"] = [
            topic for topic in paper["related_topics"]
            if topic not in override.get("excluded_topics", [])
        ]
    # A generic fallback must never manufacture a specific retargeting association.
    if sub == "Dexterous Hand Retargeting" and override:
        paper["related_topics"].append("Hand Retargeting")
    if any(tag in paper["related_topics"] for tag in ("Hand Retargeting", "Whole-body Retargeting")):
        paper["related_topics"].append("Retargeting")
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
        "version": 4,
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
        "assignment_rules": "Title-level parent cues precede abstract leaf matches; hand-retargeting requires explicit hand-transfer evidence, not fallback placement. Unresolved subfields remain provisional.",
    }


def hierarchy_counts(papers):
    return {
        "level_1": dict(sorted(Counter(p["track"] for p in papers).items())),
        "level_2": dict(sorted(Counter(f'{p["track"]} / {p["subcategory"]}' for p in papers).items())),
        "level_3": dict(sorted(Counter(f'{p["track"]} / {p["subcategory"]} / {p["specialty"]}' for p in papers).items())),
        "classification_evidence": dict(sorted(Counter(p["taxonomy_evidence"].split(":", 1)[0] for p in papers).items())),
        "review_status": dict(sorted(Counter(p.get("classification_status", "needs-review") for p in papers).items())),
    }
