#!/usr/bin/env python3
"""Check user-facing markdown for common AI writing tropes.

The source of truth for the rule is TROPES.md. This script implements a
practical phrase/pattern scan so publication has a concrete validation step.
It is intentionally conservative: findings should trigger human revision, not
automatic rewrites.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = [
    ROOT / "content" / "blogs",
    ROOT / "content" / "projects",
]

PHRASE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("quietly/deeply/fundamentally/remarkably/arguably as significance adverbs", re.compile(r"\b(quietly|deeply|fundamentally|remarkably|arguably)\b", re.I)),
    ("delve/certainly/utilize/leverage/robust/streamline/harness", re.compile(r"\b(delve|delving|certainly|utilize|utilizes|utilized|utilizing|leverage|leverages|leveraged|leveraging|robust|streamline|streamlines|streamlined|harness|harnesses|harnessed|harnessing)\b", re.I)),
    ("tapestry/landscape/paradigm/synergy/ecosystem/framework", re.compile(r"\b(tapestry|landscape|paradigm|synergy|ecosystem|framework)\b", re.I)),
    ("serves as / stands as / marks / represents dodge", re.compile(r"\b(serves as|stands as|marks a|marks an|represents a|represents an)\b", re.I)),
    ("it's worth noting / notably / importantly / interestingly", re.compile(r"\b(it'?s worth noting|it bears mentioning|importantly|interestingly|notably)\b", re.I)),
    ("here's the thing/kicker/deal style transition", re.compile(r"\b(here'?s the kicker|here'?s the thing|here'?s where it gets interesting|here'?s what most people miss|here'?s the starting point|here'?s the deal)\b", re.I)),
    ("think of it as / it's like analogy opener", re.compile(r"\b(think of it as|think of it like|it'?s like)\b", re.I)),
    ("imagine a world where", re.compile(r"\bimagine a world where\b", re.I)),
    ("let's break/unpack/explore/dive", re.compile(r"\blet'?s (break this down|unpack|explore|dive in|dive into)\b", re.I)),
    ("truth/reality/history is simple/clear/unambiguous", re.compile(r"\b(the truth is simple|the reality is simpler|history is unambiguous|history is clear|the real story is)\b", re.I)),
    ("vague expert attribution", re.compile(r"\b(experts argue|observers have cited|observers cite|industry reports suggest|several publications have cited)\b", re.I)),
    ("false suspense rhetorical answer", re.compile(r"\b(the result|the worst part|the scary part|the question)\?\s+[A-Z]", re.I)),
    ("negative parallelism", re.compile(r"\b(it'?s not|isn'?t|aren'?t|not because)\b[^.\n]{0,120}\b(it'?s|but because|but|they are|it is)\b", re.I)),
    ("not x. not y. just z pattern", re.compile(r"\bnot\b[^.\n]{1,80}\.\s+\bnot\b[^.\n]{1,80}\.\s+\b(just|only|a|an|the)\b", re.I)),
    ("false range from x to y", re.compile(r"\bfrom\s+[^.\n]{2,80}\s+to\s+[^.\n]{2,120}", re.I)),
    ("invented analytical trap/paradox/etc labels", re.compile(r"\b[a-z][a-z-]+\s+(paradox|trap|creep|divide|vacuum|inversion)\b", re.I)),
]


def iter_targets(args: list[str]) -> list[Path]:
    if args:
        targets = [(ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg) for arg in args]
    else:
        targets = DEFAULT_TARGETS

    files: list[Path] = []
    for target in targets:
        if target.is_dir():
            files.extend(sorted(target.rglob("*.md")))
        elif target.is_file() and target.suffix.lower() in {".md", ".mdx"}:
            files.append(target)
    return files


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    findings: list[str] = []

    em_dash_count = text.count("—")
    if em_dash_count > 3:
        findings.append(f"{rel}: excessive em dash count ({em_dash_count}); TROPES.md recommends restraint")

    short_para_count = 0
    for para in re.split(r"\n\s*\n", text):
        stripped = para.strip()
        if not stripped or stripped.startswith("---") or stripped.startswith("#") or stripped.startswith("- "):
            continue
        if len(stripped.split()) <= 4 and stripped.endswith((".", "!", "?")):
            short_para_count += 1
    if short_para_count > 3:
        findings.append(f"{rel}: {short_para_count} very short standalone paragraphs; check for manufactured emphasis")

    for label, pattern in PHRASE_PATTERNS:
        for match in pattern.finditer(text):
            lineno = line_number(text, match.start())
            snippet = " ".join(match.group(0).split())
            findings.append(f"{rel}:{lineno}: {label}: {snippet!r}")

    return findings


def main() -> int:
    tropes = ROOT / "TROPES.md"
    if not tropes.exists():
        print("TROPES.md is missing", file=sys.stderr)
        return 1

    files = iter_targets(sys.argv[1:])
    findings: list[str] = []
    for path in files:
        findings.extend(check_file(path))

    if findings:
        print("TROPES.md validation found readability issues:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1

    scanned = len(files)
    print(f"TROPES.md validation passed ({scanned} file{'s' if scanned != 1 else ''} scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
