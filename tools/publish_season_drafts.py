#!/usr/bin/env python3
"""Publish structured wiki article drafts into content/blogs.

This extracts the YAML block under "Publication Frontmatter" and the public
story body from "Story Draft" through "Teaching Tie-In", stopping before private
continuity notes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "bl4ck4t-wiki" / "drafts"
BLOG_DIR = ROOT / "content" / "blogs"


def extract_public_article(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")

    frontmatter_match = re.search(
        r"## Publication Frontmatter\s+```yaml\s+(.*?)\s+```",
        text,
        flags=re.S,
    )
    if not frontmatter_match:
        raise ValueError(f"{path}: missing Publication Frontmatter YAML block")

    story_match = re.search(
        r"## Story Draft\s+(.*?)(?=\n## Continuity Checks|\Z)",
        text,
        flags=re.S,
    )
    if not story_match:
        raise ValueError(f"{path}: missing Story Draft section")

    yaml = frontmatter_match.group(1).strip()
    body = story_match.group(1).strip()
    slug_match = re.search(r'^slug:\s+"?([^"\n]+)"?$', yaml, flags=re.M)
    if not slug_match:
        raise ValueError(f"{path}: publication YAML missing slug")

    return slug_match.group(1), f"---\n{yaml}\n---\n\n{body}\n"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: publish_season_drafts.py <draft.md> [<draft.md> ...]", file=sys.stderr)
        return 2

    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[1:]:
        draft = (ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
        if not draft.exists():
            print(f"missing draft: {draft}", file=sys.stderr)
            return 1

        slug, article = extract_public_article(draft)
        target = BLOG_DIR / f"{slug}.md"
        target.write_text(article, encoding="utf-8")
        print(target.relative_to(ROOT))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
