# Tactile and contact-rich manipulation · 触觉与接触操作

> Verified mini-map: 3 formally accepted papers from RSS 2024, RSS 2025, and CoRL 2025.

This page replaces an earlier speculative list that mixed missing links and unverified future venue labels. The current version only keeps papers whose venue can be checked on official proceedings.

## Evidence map

| Paper | Venue | Primary question | Official source |
|---|---|---|---|
| SpringGrasp: Synthesizing Compliant, Dexterous Grasps under Shape Uncertainty | RSS 2024 | How can a grasp remain compliant and robust under uncertain object shape? | [RSS XX proceedings](https://roboticsproceedings.org/rss20/index.html) |
| Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | RSS 2025 | How can a policy combine long-horizon action generation with fast tactile reaction? | [RSS XXI paper](https://www.roboticsproceedings.org/rss21/p052.html) |
| Tactile Beyond Pixels: Multisensory Touch Representations for Robot Manipulation | CoRL 2025 | How should touch be represented beyond treating tactile observations as ordinary images? | [PMLR 305 proceedings](https://proceedings.mlr.press/v305/) |

## What the three papers cover

### 1. Grasp synthesis under uncertainty

SpringGrasp belongs to grasp planning rather than end-to-end policy learning. Read it for how compliance, uncertainty, and geometric feasibility are represented. Its evidence should not be generalized into a claim about arbitrary downstream manipulation tasks.

### 2. Fast feedback inside a learned policy

Reactive Diffusion Policy focuses on visual-tactile control for contact-rich manipulation. Its slow-fast structure is relevant when a long-horizon policy must still react at a higher feedback rate. Reported experiments remain task- and sensor-dependent.

### 3. Reusable tactile representations

Tactile Beyond Pixels studies multisensory touch representation for robot manipulation. It addresses representation learning, not a universal proof that any tactile encoder improves every policy or hardware stack.

## Comparison checklist

When comparing contact-rich systems, keep these evidence layers separate:

1. **Sensing** — modality, calibration, sampling rate, latency, and spatial coverage.
2. **Representation** — raw signals, images, tokens, geometry, force, or learned latent state.
3. **Control** — open-loop chunks, closed-loop feedback, model predictive control, or policy hierarchy.
4. **Evaluation** — simulation, offline prediction, fixed task suite, real robot, and hardware transfer.
5. **Failure boundary** — slip, occlusion, saturation, contact loss, collision, and distribution shift.

## Scope boundary

This is a compact reading guide, not a survey. Papers without a verified official venue link are not listed as accepted work. Additions must follow [`CONTRIBUTING.md`](../CONTRIBUTING.md) and the repository's five-year catalog policy.
