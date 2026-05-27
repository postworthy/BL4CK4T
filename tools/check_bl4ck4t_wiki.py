#!/usr/bin/env python3
"""Validate basic BL4CK4T wiki structure and local markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "bl4ck4t-wiki"

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_TYPE_RE = re.compile(r"^type:\s*([A-Za-z0-9_-]+)\s*$", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_external(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def local_target_path(source: Path, target: str) -> Path:
    clean = target.split("#", 1)[0]
    return (source.parent / clean).resolve()


def validate_links(errors: list[str]) -> None:
    for path in sorted(WIKI.rglob("*.md")):
        text = read(path)
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if is_external(target) or not target:
                continue
            resolved = local_target_path(path, target)
            if not resolved.exists():
                rel_source = path.relative_to(ROOT)
                errors.append(f"{rel_source}: missing link target {target}")


def validate_index(errors: list[str]) -> None:
    index = WIKI / "index.md"
    if not index.exists():
        errors.append("bl4ck4t-wiki/index.md is missing")
        return
    for match in LINK_RE.finditer(read(index)):
        target = match.group(1).strip()
        if is_external(target) or not target:
            continue
        resolved = local_target_path(index, target)
        if not resolved.exists():
            errors.append(f"bl4ck4t-wiki/index.md: missing indexed file {target}")


def validate_drafts(errors: list[str]) -> None:
    drafts = WIKI / "drafts"
    if not drafts.exists():
        return
    required = [
        "## Publication Frontmatter",
        "## Story Draft",
        "## Teaching Tie-In",
        "## Continuity Checks",
        "Safety review:",
        "TROPES.md validation:",
    ]
    for path in sorted(drafts.glob("*.md")):
        text = read(path)
        for marker in required:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing draft marker {marker}")


def validate_missions(errors: list[str]) -> None:
    missions = WIKI / "missions"
    if not missions.exists():
        return
    required = [
        "## Lesson Payload",
        "## Public Transformation Notes",
        "## Safety Constraints",
        "## Episode Hook",
    ]
    concept_or_lesson_link = re.compile(r"\]\(\.\./(?:concepts|lessons)/[^)]+\.md(?:#[^)]+)?\)")
    for path in sorted(missions.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        text = read(path)
        frontmatter_type = FRONTMATTER_TYPE_RE.search(text)
        if frontmatter_type and frontmatter_type.group(1) != "mission":
            continue
        for marker in required:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing mission marker {marker}")
        if not concept_or_lesson_link.search(text):
            errors.append(f"{path.relative_to(ROOT)}: mission must link to a concept or lesson")


def main() -> int:
    errors: list[str] = []
    if not WIKI.exists():
        print("bl4ck4t-wiki/ is missing", file=sys.stderr)
        return 1

    validate_index(errors)
    validate_links(errors)
    validate_drafts(errors)
    validate_missions(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("BL4CK4T wiki check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
