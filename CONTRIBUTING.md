# Contributing

Thanks for improving the Embodied AI conference census. The goal is systematic coverage under a defensible, reproducible boundary—not an untraceable paper dump.

## Before adding a paper

A core paper must meet every requirement:

- conference year is within the active 2022–2026 window;
- formally accepted by RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, or ECCV;
- directly relevant to embodied perception, reasoning, action, control, evaluation, or robot systems;
- supported by an official, publisher, or explicitly labeled bibliographic source;
- linked through HTTPS in both `paper_url` and `official_url`;
- labeled with `source_type` and `discovery_source`;
- assigned to exactly one venue, one research track, and one concise topic;
- not already present under another spelling.

Do not add workshop-only, withdrawn, under-review, or arXiv-only papers to the core catalog. Important preprints can be discussed in `notes/` with their status stated explicitly.

## Catalog workflow

1. For bulk coverage changes, edit the auditable venue, taxonomy, or exclusion rules in `scripts/sync_conference_census.py`.
2. Rebuild the conference snapshot:

   ```bash
   python scripts/sync_conference_census.py
   ```

3. Review random samples from every direction and compare venue discovery counts before accepting the generated diff.
4. For a hand-verified exception, edit `data/papers.json`, use the conference year rather than the arXiv upload year, set `discovery_source` to `hand-verified seed`, and cite the best available source tier.
5. Keep every research direction represented in every year from 2022 through 2026. If a direction's framing changes, update its bilingual `track_meta` question and four-stage pipeline as well.
6. Regenerate the split Markdown catalogs:

   ```bash
   python scripts/render_catalog.py
   ```

7. Run all repository checks:

   ```bash
   python scripts/audit_catalog.py
   python scripts/render_catalog.py --check
   python scripts/check_local_links.py
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
- Explain why the paper belongs inside the published census boundary.
- Explain whether the source is official, publisher, or bibliographic.
- For taxonomy changes, report how many records move into and out of every affected direction.
- Do not commit downloaded PDFs or large generated assets.
