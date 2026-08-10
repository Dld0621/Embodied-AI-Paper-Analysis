#!/usr/bin/env python3
"""Deterministic three-level taxonomy for the Embodied AI paper index.

Level 1 is the repository's existing research track. Level 2 identifies a
stable subfield, and level 3 identifies the primary task, method, or systems
problem inside that subfield. The classifier never changes a paper's level-1
track; it refines that already-admitted record using weighted title, topic, and
abstract evidence.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import re
from typing import Any


GENERAL_SPECIALTY = "General / Cross-cutting"
GENERAL_SPECIALTY_ZH = "综合与交叉研究"


def subcategory(
    name_zh: str,
    terms: tuple[str, ...],
    specialties: tuple[tuple[str, str, tuple[str, ...]], ...],
) -> dict[str, Any]:
    return {"name_zh": name_zh, "terms": terms, "specialties": specialties}


HIERARCHY: dict[str, dict[str, dict[str, Any]]] = {
    "Foundation Models & VLA": {
        "VLA Architectures": subcategory(
            "VLA 架构",
            ("vision language action", "vla", "action model", "robot policy", "action generation"),
            (
                ("Action Tokenization & Decoding", "动作标记化与解码", ("action token", "tokenized action", "action tokenizer", "autoregressive action", "action decoding", "action chunk")),
                ("Diffusion & Flow Policies", "扩散与流策略", ("diffusion policy", "diffusion policies", "action diffusion", "flow matching", "flow policy", "flow policies", "denoising policy", "diffusion transformer")),
                ("Hierarchical & Mixture Policies", "分层与混合专家策略", ("hierarchical policy", "mixture of experts", "policy expert", "expert routing", "moe", "high level policy")),
                ("Real-time & On-device VLA", "实时与端侧 VLA", ("real time", "realtime", "on device", "edge deploy", "latency", "efficient vla", "policy compression")),
            ),
        ),
        "Multimodal Grounding": subcategory(
            "多模态具身对齐",
            ("multimodal", "grounding", "vision language", "language conditioned", "language guided", "instruction"),
            (
                ("Vision-Language Grounding", "视觉语言对齐", ("vision language", "visual language", "vlm", "visual grounding", "referring expression", "open vocabulary")),
                ("Language-conditioned Control", "语言条件控制", ("language conditioned", "language guided", "instruction following", "natural language command", "language control", "text conditioned")),
                ("3D & Spatial Grounding", "三维与空间对齐", ("3d grounding", "spatial grounding", "spatial reasoning", "scene graph", "3d scene", "geometric grounding")),
                ("Audio, Touch & Multisensory Models", "音频、触觉与多感官模型", ("audio", "speech", "tactile", "touch", "multisensory", "cross modal", "multimodal fusion")),
            ),
        ),
        "Reasoning, Planning & Agents": subcategory(
            "推理、规划与智能体",
            ("reasoning", "planning", "agentic", "embodied agent", "long horizon", "task decomposition"),
            (
                ("Task & Long-horizon Planning", "任务与长时程规划", ("task planning", "long horizon", "subgoal", "task decomposition", "hierarchical planning", "plan generation")),
                ("Agentic Robot Systems", "智能体机器人系统", ("agentic", "robot agent", "multi agent", "tool use", "code generation", "autonomous agent")),
                ("Embodied Reasoning & Question Answering", "具身推理与问答", ("embodied reasoning", "robot reasoning", "question answering", "chain of thought", "reasoning and action", "decision reasoning")),
                ("Failure Detection & Self-correction", "失败检测与自纠正", ("failure detection", "failure recovery", "self correction", "self correcting", "reflection", "verification", "replanning")),
            ),
        ),
        "Pretraining, Scaling & Transfer": subcategory(
            "预训练、规模化与迁移",
            ("foundation model", "pretrain", "generalist", "scaling", "transfer", "generalization", "cross embodiment"),
            (
                ("Robot Pretraining & Foundation Policies", "机器人预训练与基础策略", ("pretrain", "foundation policy", "robot foundation", "generalist robot", "general purpose robot", "large scale policy")),
                ("Cross-embodiment & Morphology Transfer", "跨本体与形态迁移", ("cross embodiment", "cross robot", "morphology", "embodiment aware", "multi embodiment", "heterogeneous robot")),
                ("Data Scaling & Mixture Design", "数据规模化与混合设计", ("data scaling", "scaling law", "data mixture", "large scale dataset", "data diversity", "mixture dataset")),
                ("Fine-tuning, Few-shot & Adaptation", "微调、少样本与适配", ("fine tuning", "finetuning", "adapter", "lora", "few shot", "in context", "zero shot", "test time adaptation")),
            ),
        ),
        "Memory & World Knowledge": subcategory(
            "记忆与世界知识",
            ("memory", "knowledge", "retrieval", "world action", "predictive action", "world knowledge"),
            (
                ("Episodic & Semantic Memory", "情景与语义记忆", ("episodic memory", "semantic memory", "long term memory", "spatial memory", "memory augmented", "persistent memory")),
                ("World-Action & Predictive Models", "世界动作与预测模型", ("world action model", "world-action model", "predictive action", "action world model", "latent action", "future prediction")),
                ("Retrieval-augmented Robotics", "检索增强机器人", ("retrieval augmented", "retrieval", "rag", "experience retrieval", "skill retrieval", "memory retrieval")),
                ("Knowledge Graphs & Structured Knowledge", "知识图谱与结构化知识", ("knowledge graph", "scene graph", "symbolic knowledge", "structured knowledge", "ontology", "world knowledge")),
            ),
        ),
    },
    "Manipulation & Imitation": {
        "Grasping & Object Interaction": subcategory(
            "抓取与物体交互",
            ("grasp", "pick and place", "pick place", "gripper", "object interaction", "prehension"),
            (
                ("Grasp Detection & Synthesis", "抓取检测与生成", ("grasp detection", "grasp synthesis", "grasp generation", "grasp pose", "grasp planning", "6d grasp")),
                ("Grasp Stability & Force Control", "抓取稳定性与力控制", ("grasp stability", "force closure", "grasp force", "stable grasp", "grip force", "grasp quality")),
                ("Grippers, Suction & End-effectors", "夹爪、吸盘与末端执行器", ("gripper", "suction", "end effector", "soft gripper", "parallel jaw", "vacuum grasp")),
                ("Pick-place & Object Rearrangement", "拾放与物体重排", ("pick and place", "pick place", "rearrangement", "object relocation", "tabletop manipulation", "bin picking")),
            ),
        ),
        "Contact-rich & Deformable Manipulation": subcategory(
            "接触丰富与可变形操作",
            ("contact rich", "insertion", "assembly", "deformable", "cloth", "rope", "tool use", "pushing"),
            (
                ("Insertion, Assembly & Precision Tasks", "插入、装配与精密任务", ("insertion", "assembly", "peg in hole", "connector", "precision manipulation", "mating task")),
                ("Pushing, Sliding & Non-prehensile Skills", "推、滑与非抓取技能", ("pushing", "sliding", "non prehensile", "pivoting", "tossing", "dynamic manipulation")),
                ("Tool Use & Articulated Objects", "工具使用与关节物体", ("tool use", "articulated object", "drawer", "door opening", "cabinet", "mechanism manipulation")),
                ("Cloth, Rope & Soft Objects", "布料、绳索与软体物体", ("cloth", "fabric", "rope", "cable", "deformable object", "soft object", "garment")),
            ),
        ),
        "Imitation & Demonstration Learning": subcategory(
            "模仿与示范学习",
            ("imitation", "demonstration", "behavior cloning", "behaviour cloning", "learning from demonstration", "human demonstration"),
            (
                ("Behavior Cloning & Sequence Modeling", "行为克隆与序列建模", ("behavior cloning", "behaviour cloning", "sequence modeling", "action sequence", "supervised imitation", "bc policy")),
                ("Learning from Demonstration", "从示范中学习", ("learning from demonstration", "learning from demonstrations", "demonstration learning", "robot demonstration", "human demonstration", "lfd")),
                ("One-shot, Few-shot & Skill Transfer", "单样本、少样本与技能迁移", ("one shot", "few shot", "skill transfer", "task transfer", "meta imitation", "cross task")),
                ("Skill Discovery & Demonstration Segmentation", "技能发现与示范分段", ("skill discovery", "skill segmentation", "demonstration segmentation", "latent skill", "skill primitive", "option discovery")),
            ),
        ),
        "Manipulation Policy Learning": subcategory(
            "操作策略学习",
            ("policy learning", "policy", "reinforcement learning", "robot learning", "visuomotor", "visual servoing", "trajectory optimization", "model predictive", "world model", "generative robot", "co training"),
            (
                ("Reinforcement & Offline RL", "强化学习与离线强化学习", ("reinforcement learning", "offline reinforcement", "offline rl", "actor critic", "q learning", "reward learning")),
                ("Visuomotor & Closed-loop Policies", "视觉运动与闭环策略", ("visuomotor", "closed loop", "visual control", "image based policy", "feedback policy", "end to end policy")),
                ("Generative & Diffusion Policies", "生成式与扩散策略", ("diffusion policy", "diffusion policies", "action diffusion", "generative policy", "generative policies", "flow policy", "flow policies", "energy based policy", "trajectory diffusion")),
                ("Model-based Control & Trajectory Optimization", "基于模型的控制与轨迹优化", ("model based", "trajectory optimization", "model predictive", "mpc", "optimal control", "planning and control")),
            ),
        ),
        "Long-horizon & Mobile Manipulation": subcategory(
            "长时程与移动操作",
            ("long horizon", "mobile manipulation", "multi stage", "task and motion", "household", "open world manipulation", "agentic", "workflow", "language guided", "reasoning"),
            (
                ("Long-horizon Task Execution", "长时程任务执行", ("long horizon", "multi stage", "multi step", "task sequence", "long term task", "extended task")),
                ("Mobile Manipulation", "移动操作", ("mobile manipulation", "mobile manipulator", "navigation and manipulation", "whole body manipulation", "base arm", "fetching")),
                ("Task-and-motion Planning", "任务与运动规划", ("task and motion planning", "tamp", "symbolic planning", "geometric planning", "integrated planning", "task motion")),
                ("Household, Industrial & Open-world Tasks", "家居、工业与开放世界任务", ("household", "kitchen", "industrial manipulation", "warehouse", "open world", "unstructured environment")),
            ),
        ),
    },
    "Dexterity & Teleoperation": {
        "Dexterous Hand Control": subcategory(
            "灵巧手控制",
            ("dexterous", "robot hand", "robotic hand", "multifinger", "multi finger", "anthropomorphic hand"),
            (
                ("Multifinger Control & Coordination", "多指控制与协调", ("multifinger", "multi finger", "finger coordination", "multi digit", "finger control", "dexterous control")),
                ("Hand Design, Actuation & Morphology", "手部设计、驱动与形态", ("hand design", "actuation", "tendon driven", "underactuated", "anthropomorphic hand", "hand morphology")),
                ("Dexterous Grasping", "灵巧抓取", ("dexterous grasp", "multifinger grasp", "multi finger grasp", "hand grasp", "grasp taxonomy", "precision grasp")),
                ("Cross-hand Generalization", "跨手型泛化", ("cross hand", "multi hand", "different hands", "hand generalization", "universal hand", "morphology aware")),
            ),
        ),
        "In-hand Manipulation": subcategory(
            "手内操作",
            ("in hand", "in-hand", "reorientation", "finger gait", "within hand", "hand object"),
            (
                ("Object Reorientation & Rotation", "物体重定向与旋转", ("reorientation", "object rotation", "rotate object", "orientation control", "spinning", "in hand rotation")),
                ("Rolling, Sliding & Finger Gaiting", "滚动、滑动与手指步态", ("finger gait", "rolling", "in hand sliding", "hand sliding", "finger reposition", "gaiting")),
                ("Slip, Stability & Contact Maintenance", "滑移、稳定与接触保持", ("slip", "contact stability", "grasp stability", "contact maintenance", "incipient slip", "object stabilization")),
                ("In-hand Sensing & State Estimation", "手内感知与状态估计", ("in hand sensing", "in hand pose", "object pose in hand", "proprioceptive hand", "hand state estimation", "tactile state")),
            ),
        ),
        "Bimanual Coordination": subcategory(
            "双手协同",
            ("bimanual", "dual arm", "two arm", "two hand", "handover", "cooperative manipulation"),
            (
                ("Bimanual Manipulation", "双手操作", ("bimanual manipulation", "two hand manipulation", "bimanual skill", "coordinated hands", "dual hand", "bimanual control")),
                ("Dual-arm Planning & Control", "双臂规划与控制", ("dual arm planning", "dual arm control", "two arm planning", "multi arm", "coordinated arm", "dual manipulator")),
                ("Handovers & Collaborative Tasks", "交接与协作任务", ("handover", "hand off", "collaborative manipulation", "cooperative task", "human robot handover", "object transfer")),
                ("Bimanual Assembly & Deformables", "双手装配与可变形操作", ("bimanual assembly", "bimanual cloth", "bimanual rope", "two handed assembly", "bimanual folding", "bimanual insertion")),
            ),
        ),
        "Teleoperation & Shared Autonomy": subcategory(
            "遥操作与共享自主",
            ("teleoperation", "tele operated", "telepresence", "shared autonomy", "remote operation", "bilateral"),
            (
                ("VR, XR & Immersive Teleoperation", "VR、XR 与沉浸式遥操作", ("virtual reality", "mixed reality", "augmented reality", "vr teleoperation", "xr teleoperation", "immersive")),
                ("Bilateral & Master-slave Control", "双边与主从控制", ("bilateral teleoperation", "master slave", "master salve", "force reflection", "bilateral control", "leader follower")),
                ("Shared Autonomy & Assistance", "共享自主与辅助", ("shared autonomy", "assisted teleoperation", "intent prediction", "autonomy blending", "human in the loop", "operator assistance")),
                ("Remote Presence, Delay & Communication", "远程临场、时延与通信", ("telepresence", "remote operation", "communication delay", "latency", "networked control", "remote manipulation")),
            ),
        ),
        "Retargeting & Human Motion": subcategory(
            "重定向与人体动作",
            ("retargeting", "human motion", "motion capture", "hand pose", "human demonstration", "human to robot"),
            (
                ("Hand-pose Retargeting", "手部姿态重定向", ("hand pose retargeting", "finger retargeting", "pose retargeting", "hand retargeting", "keypoint retargeting", "human hand pose")),
                ("Whole-body & Motion Retargeting", "全身与动作重定向", ("motion retargeting", "whole body retargeting", "body retargeting", "motion mapping", "human motion transfer", "kinematic retargeting")),
                ("Motion Capture & Wearable Input", "动作捕捉与可穿戴输入", ("motion capture", "mocap", "wearable", "data glove", "glove", "body tracking")),
                ("Cross-embodiment Demonstration Transfer", "跨本体示范迁移", ("cross embodiment", "human to robot", "demonstration transfer", "embodiment transfer", "human demonstration", "cross morphology")),
            ),
        ),
        "Tactile & Haptic Interfaces": subcategory(
            "触觉与力觉接口",
            ("tactile", "haptic", "touch sensing", "force feedback", "contact sensing", "vibrotactile"),
            (
                ("Tactile Sensing & Representation", "触觉感知与表征", ("tactile sensing", "tactile sensor", "touch sensing", "tactile representation", "vision based tactile", "gel tactile")),
                ("Haptic Feedback & Rendering", "力触觉反馈与渲染", ("haptic feedback", "haptic rendering", "force feedback", "vibrotactile", "stiffness rendering", "tactile feedback")),
                ("Contact & Force Estimation", "接触与力估计", ("contact estimation", "force estimation", "contact sensing", "wrench estimation", "contact localization", "normal force")),
                ("Wearable & Human Interfaces", "可穿戴与人机接口", ("haptic glove", "wearable interface", "exoskeleton glove", "human interface", "hand interface", "wearable haptic")),
            ),
        ),
    },
    "Navigation & Embodied Agents": {
        "Visual & Language Navigation": subcategory(
            "视觉与语言导航",
            ("visual navigation", "language navigation", "vln", "object goal", "image goal", "embodied question", "instruction navigation"),
            (
                ("Vision-language Navigation", "视觉语言导航", ("vision language navigation", "visual language navigation", "vln", "language navigation", "instruction guided navigation", "instruction following navigation")),
                ("Object-goal & Semantic Navigation", "物体目标与语义导航", ("object goal", "object-goal", "semantic navigation", "category goal", "target object navigation", "semantic goal")),
                ("Image-goal, Point-goal & Retrieval Navigation", "图像目标、点目标与检索导航", ("image goal", "image-goal", "point goal", "point-goal", "instance goal", "visual target")),
                ("Embodied QA & Interactive Navigation", "具身问答与交互导航", ("embodied question answering", "embodied qa", "interactive navigation", "dialog navigation", "question guided", "embodied instruction")),
            ),
        ),
        "Mapping & Localization": subcategory(
            "建图与定位",
            ("slam", "localization", "mapping", "odometry", "place recognition", "loop closure", "map", "lidar inertial", "gps denied", "gnss denied", "inertial navigation", "bundle adjustment", "dvl"),
            (
                ("Visual, LiDAR & Multi-sensor SLAM", "视觉、激光与多传感器 SLAM", ("slam", "visual slam", "lidar slam", "rgb d slam", "multi sensor slam", "semantic slam")),
                ("Visual-inertial & LiDAR Odometry", "视觉惯性与激光里程计", ("visual odometry", "visual inertial", "lidar odometry", "inertial odometry", "lio", "vio")),
                ("Place Recognition & Loop Closure", "地点识别与回环检测", ("place recognition", "loop closure", "relocalization", "global localization", "image retrieval", "topological localization")),
                ("Semantic, Metric & Neural Maps", "语义、度量与神经地图", ("semantic map", "metric map", "neural map", "occupancy map", "topological map", "map representation")),
            ),
        ),
        "Motion & Path Planning": subcategory(
            "运动与路径规划",
            ("motion planning", "path planning", "trajectory planning", "collision avoidance", "local planner", "global planner", "navigation", "mobile robot", "trajectory tracking", "predictive control", "reachability", "guidance"),
            (
                ("Global Search & Path Planning", "全局搜索与路径规划", ("path planning", "global planner", "a star", "dijkstra", "graph search", "route planning")),
                ("Local Planning & Obstacle Avoidance", "局部规划与避障", ("local planner", "obstacle avoidance", "collision avoidance", "reactive navigation", "dynamic obstacle", "local navigation")),
                ("Trajectory Optimization & MPC", "轨迹优化与模型预测控制", ("trajectory optimization", "model predictive", "mpc", "optimal trajectory", "trajectory planner", "receding horizon")),
                ("Sampling, Learning & Safety-aware Planning", "采样、学习与安全感知规划", ("sampling based", "rrt", "learned planner", "neural planner", "control barrier", "safe planning")),
            ),
        ),
        "Exploration & Active Mapping": subcategory(
            "探索与主动建图",
            ("exploration", "active mapping", "next best view", "frontier", "information gain", "coverage planning", "search and rescue"),
            (
                ("Frontier & Coverage Exploration", "前沿与覆盖探索", ("frontier exploration", "frontier based", "coverage planning", "area coverage", "exploration strategy", "coverage path")),
                ("Next-best-view & Information Gain", "下一最佳视角与信息增益", ("next best view", "information gain", "active view", "view planning", "uncertainty exploration", "informative planning")),
                ("Active Mapping & Reconstruction", "主动建图与重建", ("active mapping", "active slam", "active reconstruction", "mapping exploration", "map completion", "exploration mapping")),
                ("Search, Inspection & Discovery", "搜索、巡检与发现", ("search and rescue", "inspection", "target search", "object search", "environment discovery", "reconnaissance")),
            ),
        ),
        "Multi-agent & Social Navigation": subcategory(
            "多智能体与社会导航",
            ("multi robot", "multi agent", "swarm", "social navigation", "human aware", "pedestrian", "crowd", "crowded", "human robot teaming", "group following"),
            (
                ("Multi-robot Coordination", "多机器人协同", ("multi robot", "multi-robot", "robot team", "cooperative robots", "fleet coordination", "decentralized coordination")),
                ("Swarm Navigation & Formation", "集群导航与编队", ("swarm", "formation control", "collective navigation", "flocking", "multi uav", "robot swarm")),
                ("Social & Human-aware Navigation", "社会与人类感知导航", ("social navigation", "human aware", "socially aware", "pedestrian", "crowd navigation", "personal space")),
                ("Multi-agent Collision Avoidance", "多智能体避碰", ("multi agent collision", "reciprocal avoidance", "decentralized avoidance", "agent interaction", "collision coordination", "traffic coordination")),
            ),
        ),
        "Field, Aerial & Marine Robotics": subcategory(
            "野外、空中与海洋机器人",
            ("uav", "drone", "aerial", "underwater", "marine", "maritime", "auv", "uuv", "autonomous driving", "vehicle", "outdoor", "field robot", "agricultural", "delivery", "warehouse", "wheelchair"),
            (
                ("Aerial & UAV Navigation", "空中与无人机导航", ("uav", "drone", "aerial robot", "quadrotor", "flight navigation", "autonomous flight")),
                ("Autonomous Driving & Ground Vehicles", "自动驾驶与地面车辆", ("autonomous driving", "autonomous vehicle", "self driving", "ground vehicle", "road navigation", "off road")),
                ("Marine & Underwater Autonomy", "海洋与水下自主", ("underwater", "marine robot", "subsea", "auv", "usv", "aquatic robot")),
                ("Outdoor, Agricultural & Delivery Robots", "户外、农业与配送机器人", ("outdoor navigation", "agricultural robot", "field robot", "delivery robot", "warehouse robot", "last mile")),
            ),
        ),
    },
    "Humanoids & Locomotion": {
        "Humanoid Whole-body Control": subcategory(
            "人形全身控制",
            ("humanoid", "whole body", "whole-body", "loco manipulation", "humanoid control", "upper body"),
            (
                ("Whole-body Tracking & Control", "全身跟踪与控制", ("whole body tracking", "whole body control", "whole-body tracking", "whole-body control", "full body control", "motion tracking")),
                ("Humanoid Loco-manipulation", "人形移动操作", ("loco manipulation", "loco-manipulation", "humanoid manipulation", "whole body manipulation", "locomotion manipulation", "mobile humanoid")),
                ("Upper-body Skills & Coordination", "上肢技能与协调", ("upper body", "upper-body", "arm coordination", "torso control", "humanoid arm", "whole body reaching")),
                ("Humanoid Teleoperation & Interaction", "人形遥操作与交互", ("humanoid teleoperation", "whole body teleoperation", "humanoid interaction", "avatar control", "human humanoid", "humanoid collaboration")),
            ),
        ),
        "Bipedal & Humanoid Locomotion": subcategory(
            "双足与人形运动",
            ("biped", "bipedal", "humanoid locomotion", "walking", "gait", "running", "jumping", "parkour"),
            (
                ("Walking & Gait Control", "行走与步态控制", ("walking", "gait", "bipedal locomotion", "footstep", "walkability", "stepping")),
                ("Running, Jumping & Agile Skills", "跑跳与敏捷技能", ("running", "jumping", "parkour", "agile", "acrobat", "dynamic locomotion")),
                ("Stairs, Terrain & Rough-ground Traversal", "楼梯、地形与崎岖地面通行", ("stairs", "terrain", "rough ground", "uneven ground", "slope", "stepping stone")),
                ("Footstep & Contact Planning", "落脚点与接触规划", ("footstep planning", "contact planning", "foothold", "step planning", "walking pattern", "zero moment point")),
            ),
        ),
        "Quadruped & Legged Locomotion": subcategory(
            "四足与多足运动",
            ("quadruped", "quadrupedal", "legged", "multi legged", "hexapod", "robot dog"),
            (
                ("Quadruped Locomotion", "四足运动", ("quadruped", "quadrupedal", "robot dog", "four legged", "quadruped locomotion", "quadruped control")),
                ("General Legged & Multi-legged Control", "通用腿式与多足控制", ("legged", "multi legged", "hexapod", "six legged", "legged robot", "legged locomotion")),
                ("Terrain Adaptation & Traversal", "地形适应与通行", ("terrain adaptation", "rough terrain", "terrain traversal", "uneven terrain", "blind locomotion", "proprioceptive locomotion")),
                ("Agility, Recovery & Dynamic Maneuvers", "敏捷、恢复与动态机动", ("agile locomotion", "dynamic maneuver", "jump recovery", "fall recovery", "rapid locomotion", "athletic")),
            ),
        ),
        "Motion Imitation & Generation": subcategory(
            "动作模仿与生成",
            ("motion imitation", "motion tracking", "motion generation", "human motion", "motion style", "reference motion"),
            (
                ("Reference-motion Imitation", "参考动作模仿", ("motion imitation", "reference motion", "motion tracking", "motion retargeting", "imitation control", "motion replay")),
                ("Language-conditioned Motion Generation", "语言条件动作生成", ("language conditioned motion", "text to motion", "motion generation", "motion synthesis", "language motion", "commanded motion")),
                ("Style, Expressive & Human-like Motion", "风格化、表现性与类人动作", ("motion style", "style transfer", "human like", "expressive motion", "natural motion", "dance")),
                ("Motion Priors & Behavioral Models", "动作先验与行为模型", ("motion prior", "behavior model", "behaviour model", "motion manifold", "latent motion", "behavior foundation")),
            ),
        ),
        "Balance, Dynamics & Recovery": subcategory(
            "平衡、动力学与恢复",
            ("balance", "dynamics", "recovery", "state estimation", "stability", "contact force", "centroidal"),
            (
                ("Balance & Stability Control", "平衡与稳定控制", ("balance control", "balancing", "stability", "center of mass", "zero moment", "postural control")),
                ("Dynamics, MPC & Whole-body Optimization", "动力学、MPC 与全身优化", ("centroidal dynamics", "rigid body dynamics", "model predictive", "whole body optimization", "inverse dynamics", "dynamics control")),
                ("Fall Prevention & Recovery", "防跌倒与恢复", ("fall prevention", "fall recovery", "push recovery", "disturbance recovery", "fault recovery", "robust recovery")),
                ("State, Contact & Force Estimation", "状态、接触与力估计", ("state estimation", "contact estimation", "force estimation", "ground reaction", "contact force", "inertial estimation")),
            ),
        ),
        "Hardware & Morphology": subcategory(
            "硬件与机器人形态",
            ("actuator", "joint design", "robot design", "musculoskeletal", "leg design", "mechanism", "hardware"),
            (
                ("Actuators, Joints & Transmission", "驱动器、关节与传动", ("actuator", "joint actuator", "transmission", "gearbox", "series elastic", "tendon driven")),
                ("Feet, Legs & Mechanical Design", "足部、腿部与机械设计", ("foot design", "leg design", "ankle", "mechanical design", "compliant leg", "robot mechanism")),
                ("Musculoskeletal & Bio-inspired Robots", "肌骨与仿生机器人", ("musculoskeletal", "bio inspired", "biomimetic", "artificial muscle", "tendon driven humanoid", "human biomechanics")),
                ("Morphology & Co-design", "形态与协同设计", ("morphology", "co design", "codesign", "body design", "robot morphology", "design optimization")),
            ),
        ),
    },
    "Perception & World Models": {
        "3D Scene Perception": subcategory(
            "三维场景感知",
            ("3d", "point cloud", "depth", "reconstruction", "occupancy", "nerf", "gaussian splatting"),
            (
                ("Point-cloud & LiDAR Perception", "点云与激光感知", ("point cloud", "lidar", "laser scan", "3d point", "range image", "point based")),
                ("Depth, Stereo & RGB-D", "深度、双目与 RGB-D", ("depth estimation", "stereo", "rgb d", "depth completion", "monocular depth", "range sensing")),
                ("3D Reconstruction, NeRF & Gaussian Splatting", "三维重建、NeRF 与高斯泼溅", ("3d reconstruction", "nerf", "neural radiance", "gaussian splatting", "3dgs", "scene reconstruction")),
                ("Occupancy & Scene Representation", "占据与场景表征", ("occupancy", "voxel", "scene representation", "implicit scene", "signed distance", "sdf")),
            ),
        ),
        "Object, Pose & Affordance Perception": subcategory(
            "物体、姿态与可供性感知",
            ("object detection", "segmentation", "pose estimation", "affordance", "object pose", "articulated object"),
            (
                ("Object Detection & Segmentation", "物体检测与分割", ("object detection", "semantic segmentation", "instance segmentation", "open vocabulary detection", "object segmentation", "panoptic")),
                ("6D Pose & Keypoint Estimation", "六维姿态与关键点估计", ("6d pose", "object pose", "pose estimation", "keypoint", "pose tracking", "orientation estimation")),
                ("Affordance & Interaction Prediction", "可供性与交互预测", ("affordance", "interaction prediction", "actionable region", "grasp affordance", "functional part", "object function")),
                ("Articulated & Object-centric Perception", "关节物体与物体中心感知", ("articulated object", "object centric", "part segmentation", "kinematic structure", "object part", "articulation")),
            ),
        ),
        "State Estimation & Tracking": subcategory(
            "状态估计与跟踪",
            ("state estimation", "tracking", "odometry", "calibration", "sensor fusion", "scene flow"),
            (
                ("Object & Multi-target Tracking", "物体与多目标跟踪", ("object tracking", "multi object tracking", "target tracking", "visual tracking", "tracking by detection", "trajectory tracking")),
                ("Robot State & Visual Odometry", "机器人状态与视觉里程计", ("robot state estimation", "visual odometry", "state estimator", "ego motion", "camera motion", "odometry")),
                ("Calibration & Sensor Fusion", "标定与传感器融合", ("calibration", "sensor fusion", "multi sensor", "camera lidar", "extrinsic calibration", "imu fusion")),
                ("Scene Flow & Dynamic-state Estimation", "场景流与动态状态估计", ("scene flow", "motion estimation", "dynamic scene", "velocity estimation", "dynamic object", "temporal perception")),
            ),
        ),
        "Tactile & Multimodal Perception": subcategory(
            "触觉与多模态感知",
            ("tactile", "touch", "force sensing", "contact sensing", "visuotactile", "proprioception"),
            (
                ("Tactile Recognition & Representation", "触觉识别与表征", ("tactile recognition", "tactile representation", "tactile image", "touch recognition", "tactile feature", "tactile learning")),
                ("Force, Contact & Slip Perception", "力、接触与滑移感知", ("force sensing", "contact sensing", "slip detection", "contact perception", "wrench sensing", "pressure sensing")),
                ("Visuotactile & Multisensory Fusion", "视触觉与多感官融合", ("visuotactile", "visual tactile", "multisensory", "multi modal sensing", "sensor fusion", "vision touch")),
                ("Proprioception & Embodied Sensing", "本体感知与具身传感", ("proprioception", "proprioceptive", "joint sensing", "body sensing", "embodied sensing", "internal sensing")),
            ),
        ),
        "World & Dynamics Models": subcategory(
            "世界与动力学模型",
            ("world model", "dynamics model", "predictive model", "video prediction", "neural dynamics", "future prediction"),
            (
                ("Latent World Models", "潜空间世界模型", ("latent world model", "world model", "latent dynamics", "state space model", "predictive representation", "latent state")),
                ("Object-centric & Structured Dynamics", "物体中心与结构化动力学", ("object centric dynamics", "structured dynamics", "graph dynamics", "compositional dynamics", "interaction network", "object dynamics")),
                ("Video & Future Prediction", "视频与未来预测", ("video prediction", "future prediction", "frame prediction", "visual forecasting", "future frame", "predictive video")),
                ("Physics-informed & Neural Dynamics", "物理先验与神经动力学", ("physics informed", "neural dynamics", "dynamics model", "hamiltonian", "lagrangian", "physical prediction")),
            ),
        ),
        "Active & Multiview Perception": subcategory(
            "主动与多视角感知",
            ("active perception", "next best view", "viewpoint", "multi view", "multiview", "occlusion"),
            (
                ("Next-best-view & View Planning", "下一最佳视角与视角规划", ("next best view", "view planning", "viewpoint selection", "camera planning", "active view", "view optimization")),
                ("Active Perception & Information Gathering", "主动感知与信息采集", ("active perception", "information gathering", "uncertainty reduction", "active sensing", "perception action", "sensor planning")),
                ("Multiview Fusion & Consistency", "多视角融合与一致性", ("multi view", "multiview", "view fusion", "cross view", "multi camera", "view consistency")),
                ("Occlusion-aware & Interactive Perception", "遮挡感知与交互式感知", ("occlusion", "occluded object", "interactive perception", "move to see", "active object perception", "visibility")),
            ),
        ),
    },
    "Simulation, Data & Evaluation": {
        "Simulation & Digital Twins": subcategory(
            "仿真与数字孪生",
            ("simulation", "simulator", "digital twin", "physics engine", "differentiable simulation", "neural simulation"),
            (
                ("Physics Engines & Robot Simulators", "物理引擎与机器人仿真器", ("physics engine", "robot simulator", "simulation platform", "mujoco", "isaac", "gazebo")),
                ("Differentiable & Neural Simulation", "可微与神经仿真", ("differentiable simulation", "differentiable physics", "neural simulation", "learned simulator", "differentiable dynamics", "gradient simulation")),
                ("Digital Twins & Real-to-sim Reconstruction", "数字孪生与现实到仿真重建", ("digital twin", "digital twins", "real to sim", "real-to-sim", "scene replica", "environment reconstruction")),
                ("Large-scale Parallel Simulation", "大规模并行仿真", ("parallel simulation", "gpu simulation", "massively parallel", "large scale simulation", "vectorized environment", "batch simulation")),
            ),
        ),
        "Sim-to-real & Domain Adaptation": subcategory(
            "仿真到现实与域适配",
            ("sim to real", "sim2real", "domain adaptation", "domain randomization", "system identification", "reality gap"),
            (
                ("Domain Randomization", "域随机化", ("domain randomization", "visual randomization", "dynamics randomization", "texture randomization", "randomized simulation", "parameter randomization")),
                ("System Identification & Calibration", "系统辨识与校准", ("system identification", "system identification", "sim calibration", "parameter identification", "dynamics calibration", "model calibration")),
                ("Domain Adaptation & Transfer", "域适配与迁移", ("domain adaptation", "domain transfer", "sim to real transfer", "feature adaptation", "adversarial adaptation", "cross domain")),
                ("Reality-gap Evaluation", "现实差距评估", ("reality gap", "sim real gap", "simulation fidelity", "transfer gap", "real world validation", "sim versus real")),
            ),
        ),
        "Datasets & Data Engines": subcategory(
            "数据集与数据引擎",
            ("dataset", "data collection", "data generation", "synthetic data", "demonstration data", "data engine"),
            (
                ("Robot Datasets & Corpora", "机器人数据集与语料库", ("robot dataset", "robotics dataset", "dataset", "data corpus", "large scale data", "benchmark dataset")),
                ("Demonstration & Trajectory Data", "示范与轨迹数据", ("demonstration dataset", "trajectory dataset", "human demonstration", "teleoperation data", "motion dataset", "robot trajectories")),
                ("Synthetic Data Generation", "合成数据生成", ("synthetic data", "data generation", "procedural generation", "synthetic dataset", "rendered data", "generative data")),
                ("Data Curation, Annotation & Quality", "数据整理、标注与质量", ("data curation", "annotation", "data quality", "dataset cleaning", "data filtering", "data selection")),
            ),
        ),
        "Benchmarks & Evaluation": subcategory(
            "基准与评测",
            ("benchmark", "evaluation", "metric", "protocol", "comparison", "challenge"),
            (
                ("Task & Capability Benchmarks", "任务与能力基准", ("task benchmark", "capability benchmark", "benchmarking", "challenge", "evaluation suite", "test suite")),
                ("Metrics & Evaluation Protocols", "指标与评测协议", ("evaluation metric", "evaluation protocol", "metric", "scoring", "measurement protocol", "evaluation framework")),
                ("Robustness & Stress Testing", "稳健性与压力测试", ("stress test", "robustness evaluation", "perturbation", "noise benchmark", "adversarial test", "failure benchmark")),
                ("Real-world & Cross-platform Evaluation", "真实世界与跨平台评测", ("real world evaluation", "cross platform", "cross robot evaluation", "hardware evaluation", "field evaluation", "cross embodiment benchmark")),
            ),
        ),
        "Training Infrastructure & Tools": subcategory(
            "训练基础设施与工具",
            ("framework", "toolkit", "infrastructure", "distributed", "gpu", "middleware", "runtime", "library"),
            (
                ("Training Frameworks & RL Environments", "训练框架与强化学习环境", ("training framework", "rl environment", "learning framework", "training platform", "environment suite", "gym environment")),
                ("Distributed, GPU & Data Systems", "分布式、GPU 与数据系统", ("distributed training", "gpu accelerated", "data pipeline", "parallel training", "distributed system", "compute efficient")),
                ("Open-source Libraries & Toolkits", "开源库与工具包", ("open source", "library", "toolkit", "software framework", "robotics framework", "development kit")),
                ("Deployment, Runtime & Middleware", "部署、运行时与中间件", ("deployment", "runtime", "middleware", "ros", "edge computing", "real time system")),
            ),
        ),
        "Safety, Robustness & Reproducibility": subcategory(
            "安全、稳健与可复现性",
            ("safety", "robustness", "uncertainty", "failure", "reproducibility", "certification", "reliable"),
            (
                ("Safety Constraints & Verification", "安全约束与验证", ("safety constraint", "formal verification", "safe control", "safety filter", "control barrier", "certification")),
                ("Uncertainty & Out-of-distribution Testing", "不确定性与分布外测试", ("uncertainty", "out of distribution", "ood", "distribution shift", "confidence estimation", "unknown environment")),
                ("Failure Analysis & Reliability", "失败分析与可靠性", ("failure analysis", "fault detection", "reliability", "failure mode", "fault tolerant", "system failure")),
                ("Reproducibility & Standardization", "可复现性与标准化", ("reproducibility", "standardization", "standard protocol", "repeatability", "open benchmark", "reporting standard")),
            ),
        ),
    },
}


DEFAULT_SUBCATEGORY = {
    "Foundation Models & VLA": "VLA Architectures",
    "Manipulation & Imitation": "Manipulation Policy Learning",
    "Dexterity & Teleoperation": "Dexterous Hand Control",
    "Navigation & Embodied Agents": "Motion & Path Planning",
    "Humanoids & Locomotion": "Humanoid Whole-body Control",
    "Perception & World Models": "3D Scene Perception",
    "Simulation, Data & Evaluation": "Benchmarks & Evaluation",
}


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).strip()


@lru_cache(maxsize=None)
def normalize_term(value: str) -> str:
    return normalize_text(value)


def term_present(text: str, term: str) -> bool:
    normalized = normalize_term(term)
    if not normalized:
        return False
    return f" {normalized} " in f" {text} "


def score_terms(
    terms: tuple[str, ...], title: str, topic: str, abstract: str
) -> tuple[int, str]:
    score = 0
    evidence: list[tuple[int, int, str, str]] = []
    for term in terms:
        normalized = normalize_term(term)
        specificity = min(len(normalized.split()), 4)
        for location, text, weight in (
            ("title", title, 12),
            ("topic", topic, 5),
            ("abstract", abstract, 1),
        ):
            if term_present(text, normalized):
                value = weight + specificity
                score += value
                evidence.append((value, len(normalized), location, normalized))
    if not evidence:
        return 0, "fallback"
    _, _, location, term = max(evidence)
    return score, f"{location}:{term}"


def classify_hierarchy(
    track: str,
    title: str,
    topic: str = "",
    abstract: str = "",
) -> tuple[str, str, str]:
    """Return level-2 subcategory, level-3 specialty, and best evidence."""
    if track not in HIERARCHY:
        raise ValueError(f"Unsupported research track: {track}")
    title_text = normalize_text(title)
    topic_text = normalize_text(topic)
    abstract_text = normalize_text(abstract)
    ranked_subcategories: list[tuple[int, int, str, str]] = []
    for priority, (name, meta) in enumerate(HIERARCHY[track].items()):
        specialty_terms = tuple(
            term
            for _, _, terms in meta["specialties"]
            for term in terms
        )
        score, evidence = score_terms(
            tuple(dict.fromkeys(tuple(meta["terms"]) + specialty_terms)),
            title_text,
            topic_text,
            abstract_text,
        )
        if score:
            ranked_subcategories.append((score, -priority, name, evidence))
    if ranked_subcategories:
        _, _, subcategory_name, subcategory_evidence = max(ranked_subcategories)
    else:
        subcategory_name = DEFAULT_SUBCATEGORY[track]
        subcategory_evidence = "fallback"

    specialty_ranked: list[tuple[int, int, str, str]] = []
    specialties = HIERARCHY[track][subcategory_name]["specialties"]
    for priority, (name, _, terms) in enumerate(specialties):
        score, evidence = score_terms(terms, title_text, topic_text, abstract_text)
        if score:
            specialty_ranked.append((score, -priority, name, evidence))
    if specialty_ranked:
        _, _, specialty_name, evidence = max(specialty_ranked)
    else:
        specialty_name = GENERAL_SPECIALTY
        evidence = subcategory_evidence
    return subcategory_name, specialty_name, evidence


def annotate_paper(paper: dict[str, Any], abstract: str = "") -> dict[str, Any]:
    subcategory_name, specialty_name, evidence = classify_hierarchy(
        paper["track"], paper["title"], paper.get("topic", ""), abstract
    )
    paper["subcategory"] = subcategory_name
    paper["specialty"] = specialty_name
    paper["taxonomy_evidence"] = evidence
    return paper


def taxonomy_metadata() -> dict[str, Any]:
    tracks: dict[str, Any] = {}
    specialty_count = 0
    for track, subcategories in HIERARCHY.items():
        rendered_subcategories: dict[str, Any] = {}
        for name, meta in subcategories.items():
            specialties = {
                specialty_name: {"name_zh": specialty_zh}
                for specialty_name, specialty_zh, _ in meta["specialties"]
            }
            specialties[GENERAL_SPECIALTY] = {"name_zh": GENERAL_SPECIALTY_ZH}
            specialty_count += len(meta["specialties"])
            rendered_subcategories[name] = {
                "name_zh": meta["name_zh"],
                "specialties": specialties,
            }
        tracks[track] = {"subcategories": rendered_subcategories}
    return {
        "version": 2,
        "levels": {
            "level_1": {"field": "track", "name": "Research direction", "name_zh": "一级研究方向"},
            "level_2": {"field": "subcategory", "name": "Subfield", "name_zh": "二级子领域"},
            "level_3": {"field": "specialty", "name": "Specialty", "name_zh": "三级专题"},
        },
        "classification": "Weighted deterministic title, topic, and abstract taxonomy in scripts/taxonomy.py; one primary path per paper. General / Cross-cutting is retained when the source text does not support a narrower level-3 claim.",
        "tracks": tracks,
        "subcategory_count": sum(len(items) for items in HIERARCHY.values()),
        "specialty_count": specialty_count,
        "fallback_specialty_count": sum(len(items) for items in HIERARCHY.values()),
    }


def hierarchy_counts(papers: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    return {
        "level_1": dict(sorted(Counter(paper["track"] for paper in papers).items())),
        "level_2": dict(sorted(Counter(f'{paper["track"]} / {paper["subcategory"]}' for paper in papers).items())),
        "level_3": dict(sorted(Counter(f'{paper["track"]} / {paper["subcategory"]} / {paper["specialty"]}' for paper in papers).items())),
        "classification_evidence": dict(sorted(Counter(paper["taxonomy_evidence"].split(":", 1)[0] for paper in papers).items())),
    }
