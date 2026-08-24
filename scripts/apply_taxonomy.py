#!/usr/bin/env python3
"""Apply the published three-level taxonomy to both catalog layers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from taxonomy import annotate_paper, hierarchy_counts, taxonomy_metadata


ROOT = Path(__file__).resolve().parents[1]
CONFERENCE_PATH = ROOT / "data" / "papers.json"
ARXIV_PATH = ROOT / "data" / "arxiv_recent.json"


def annotate_records(records: list[dict]) -> None:
    for paper in records:
        annotate_paper(paper, paper.get("abstract", ""))


def build_outputs() -> dict[Path, str]:
    conference = json.loads(CONFERENCE_PATH.read_text(encoding="utf-8"))
    arxiv = json.loads(ARXIV_PATH.read_text(encoding="utf-8"))
    metadata = taxonomy_metadata()

    annotate_records(conference["papers"])
    conference["schema_version"] = 4
    conference["taxonomy"] = metadata
    conference["taxonomy_counts"] = hierarchy_counts(conference["papers"])
    conference["census"]["taxonomy_version"] = metadata["version"]
    conference["census"]["classification"] = (
        "Level 1 is assigned by the conference admission rules in "
        "scripts/sync_conference_census.py. Levels 2 and 3 use the stored title, "
        "topic, and abstract evidence in scripts/taxonomy.py."
    )

    annotate_records(arxiv["papers"])
    arxiv["schema_version"] = 2
    arxiv["taxonomy"] = metadata
    arxiv["taxonomy_counts"] = hierarchy_counts(arxiv["papers"])
    arxiv["source"]["taxonomy_version"] = metadata["version"]
    arxiv["source"]["classification"] = (
        "Level 1 uses the title/abstract admission rules in "
        "scripts/sync_arxiv_recent.py. Levels 2 and 3 use the stored title, "
        "topic, and abstract evidence in scripts/taxonomy.py."
    )

    return {
        CONFERENCE_PATH: json.dumps(conference, ensure_ascii=False, indent=2) + "\n",
        ARXIV_PATH: json.dumps(arxiv, ensure_ascii=False, separators=(",", ":")) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs()
    stale = [
        path
        for path, rendered in outputs.items()
        if not path.exists() or path.read_text(encoding="utf-8") != rendered
    ]
    if args.check:
        if stale:
            print("Taxonomy annotations are stale:")
            for path in stale:
                print(f"- {path.relative_to(ROOT)}")
            return 1
        print("Three-level taxonomy annotations are current.")
        return 0
    for path, rendered in outputs.items():
        path.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Annotated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
