#!/usr/bin/env python3
"""Check repository-local Markdown and HTML links without network access."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_LINK = re.compile(r"\b(?:href|src)=['\"]([^'\"]+)['\"]", re.IGNORECASE)
IGNORED_PARTS = {".git", ".pytest_cache", "__pycache__"}


def source_files() -> list[Path]:
    files: list[Path] = []
    for suffix in ("*.md", "*.html"):
        files.extend(
            path
            for path in ROOT.rglob(suffix)
            if not any(part in IGNORED_PARTS for part in path.parts)
        )
    return sorted(files)


def markdown_targets(text: str) -> list[str]:
    """Extract simple inline Markdown destinations without parsing prose parentheses."""
    targets: list[str] = []
    cursor = 0
    while True:
        marker = text.find("](", cursor)
        if marker == -1:
            return targets
        end = text.find(")", marker + 2)
        if end == -1:
            return targets
        destination = text[marker + 2 : end].strip()
        if destination:
            targets.append(destination.split(maxsplit=1)[0].strip("<>"))
        cursor = end + 1


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    parsed = urlsplit(target)
    if (
        not target
        or target.startswith("#")
        or target.startswith("//")
        or parsed.scheme
        or parsed.netloc
    ):
        return None

    path_text = unquote(parsed.path)
    if not path_text:
        return None
    if path_text.startswith("/"):
        return ROOT / path_text.lstrip("/")
    return source.parent / path_text


def find_broken_links() -> list[str]:
    broken: list[str] = []
    for source in source_files():
        text = source.read_text(encoding="utf-8")
        targets = markdown_targets(text) if source.suffix == ".md" else HTML_LINK.findall(text)
        for raw_target in targets:
            target = local_target(source, raw_target)
            if target is None:
                continue
            try:
                resolved = target.resolve()
                resolved.relative_to(ROOT.resolve())
            except (OSError, ValueError):
                broken.append(f"{source.relative_to(ROOT)}: path escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                broken.append(f"{source.relative_to(ROOT)}: missing {raw_target}")
    return broken


def main() -> int:
    broken = find_broken_links()
    if broken:
        print("Local link audit: FAILED")
        for error in broken:
            print(f"- {error}")
        return 1
    print(f"Local link audit: OK ({len(source_files())} documents)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
