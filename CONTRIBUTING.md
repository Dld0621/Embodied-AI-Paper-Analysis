# Contributing

Thanks for improving the Embodied AI research map. The goal is a small, defensible catalog—not the largest possible list.

## Before adding a paper

A core paper must meet every requirement:

- conference year is within the active 2022–2026 window;
- formally accepted by RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, or ECCV;
- directly relevant to embodied perception, reasoning, action, control, evaluation, or robot systems;
- supported by an official venue source;
- assigned to exactly one venue, one research track, and one concise topic;
- not already present under another spelling.

Do not add workshop-only, withdrawn, under-review, or arXiv-only papers to the core catalog. Important preprints can be discussed in `notes/` with their status stated explicitly.

## Catalog workflow

1. Edit `data/papers.json`.
2. Use the conference year, not the arXiv upload year.
3. Put the reading link in `paper_url` and the acceptance evidence in `official_url`.
4. Regenerate the Markdown catalog:

   ```bash
   python scripts/render_catalog.py
   ```

5. Run all repository checks:

   ```bash
   python scripts/audit_catalog.py
   python scripts/render_catalog.py --check
   python -m unittest discover -s tests -v
   ```

## Analysis notes

Use [`docs/paper-analysis-template.md`](docs/paper-analysis-template.md). Separate:

- claims made by the paper;
- evidence shown in experiments;
- limitations acknowledged by the authors;
- your own inference or recommendation.

Do not convert simulation, offline metrics, or visualization results into real-robot success claims.

## Pull requests

- Keep each pull request focused.
- Explain why the paper belongs in the curated map.
- Include the official acceptance source.
- Do not commit downloaded PDFs or large generated assets.
