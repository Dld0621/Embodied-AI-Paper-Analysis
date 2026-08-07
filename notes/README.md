# Deep-dive notes · 深度笔记

The core catalog is intentionally compact. This directory holds longer analyses for a small number of papers and systems.

## Published core papers

| Paper | Venue | Note |
|---|---|---|
| R3M | CoRL 2022 | [Visual representation](perception/foundation-models/2022-r3m.md) |
| Diffusion Policy | RSS 2023 | [Policy formulation](policy/diffusion-policy/2023-diffusion-policy.md) |
| GELLO | IROS 2024 | [Low-cost teleoperation](locomotion/teleoperation/2023-gello.md) |
| ReKep | CoRL 2024 | [Relational keypoint constraints](manipulation/manipulation/2024-rekep.md) |
| Open-TeleVision | CoRL 2024 | [Immersive teleoperation](locomotion/teleoperation/2024-open-television.md) |

The GELLO filename retains the 2023 preprint date for link stability; its formal venue year is **IROS 2024**.

## Research notes outside the core catalog

| Paper | Status | Note |
|---|---|---|
| π0 | arXiv / technical report; superseded in the core map by the formally accepted π0.5 paper | [π0 note](policy/vla/2024-pi0.md) |
| HIL-SERL | Science Robotics 2025; outside the conference-only core | [Human-in-the-loop RL](manipulation/manipulation/2024-hil-serl.md) |

These notes are valuable context but are not counted as top-conference core entries unless an official acceptance source from one of the selected venues is added to `data/papers.json`. Every deep dive now separates paper-reported evidence from interpretation and avoids unsupported task-level numbers.

## Writing standard

Use [`docs/paper-analysis-template.md`](../docs/paper-analysis-template.md) and label statements as paper claim, reported evidence, inference, limitation, or recommendation.
