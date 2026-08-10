# Contributing

Thanks for improving the Embodied AI Research Index. The project maintains two evidence layers: an accepted-conference census and a separately labeled recent-arXiv census. The goal is systematic coverage under defensible, reproducible boundaries—not an untraceable paper dump.

## Before adding a paper

A core paper must meet every requirement:

- conference year is within the active 2022–2026 window;
- formally accepted by RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, or ECCV;
- directly relevant to embodied perception, reasoning, action, control, evaluation, or robot systems;
- supported by an official, publisher, or explicitly labeled bibliographic source;
- linked through HTTPS in both `paper_url` and `official_url`;
- labeled with `source_type` and `discovery_source`;
- assigned to exactly one venue and one auditable `track → subcategory → specialty` path;
- not already present under another spelling.

Do not add workshop-only, withdrawn, under-review, or arXiv-only papers to the conference catalog. Preprints belong only in `data/arxiv_recent.json`; the interface never presents them as conference acceptances.

## Catalog workflow

1. For bulk coverage changes, edit the venue/admission rules in `scripts/sync_conference_census.py` or the level-2/level-3 rules in `scripts/taxonomy.py`.
2. Rebuild the conference snapshot:

   ```bash
   python scripts/sync_conference_census.py
   ```

3. Review random samples from every direction and compare venue discovery counts before accepting the generated diff.
4. For a hand-verified exception, edit `data/papers.json`, use the conference year rather than the arXiv upload year, set `discovery_source` to `hand-verified seed`, and cite the best available source tier.
5. Keep every research direction represented in every year from 2022 through 2026. If a direction's framing changes, update its bilingual `track_meta` question and four-stage pipeline as well.
6. Refresh the three-year arXiv layer through the official API. Do not hand-edit bulk preprint records:

   ```bash
   python scripts/sync_arxiv_recent.py
   ```

   The synchronization evaluates every `cs.RO` candidate inside the frozen date window, applies the published title/abstract taxonomy, records admitted and unclassified counts, and uses resumable rate-limited requests.

7. Regenerate the split Markdown catalogs:

   ```bash
   python scripts/render_catalog.py
   ```

   The renderer owns `README.md`, `README.zh-CN.md`, and every page under `papers/taxonomy/`. Do not hand-edit generated homepages or leaf catalogs: both language versions must stay synchronized with the seven-direction taxonomy, each paper must be generated exactly once beneath its level-3 specialty, and oversized leaves are split automatically.

8. Run all repository checks:

   ```bash
   python scripts/apply_taxonomy.py --check
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
- For arXiv changes, report the query window, total candidates, admitted records, unclassified records, and conference-title overlap.
- For taxonomy changes, report how many records move into and out of every affected direction, subfield, and specialty, plus any change to the General / Cross-cutting rate.
- Do not commit downloaded PDFs or large generated assets.
