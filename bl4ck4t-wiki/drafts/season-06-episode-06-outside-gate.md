---
type: article-draft
status: promoted
created: 2026-05-27
updated: 2026-05-27
target_slug: season-06-episode-06-outside-gate
tags: [season-6, episode-6, access, resilience]
sources:
  - ../missions/season-06-episode-06-outside-gate.md
canon_pages:
  - ../production-bibles/season-06-the-day-the-city-would-not-answer.md
  - ../concepts/civic-resilience.md
  - ../locations/status-wall.md
---

# Draft: The Outside Gate

## Publication Frontmatter

Promoted to `content/blogs/season-06-episode-06-outside-gate.md`.

## Story Draft

An outside reader cannot reach a legitimate school notice while local services recover behind a temporary limit. Grimalkin and Shadow make the restriction visible, reviewed, and humane.

## Teaching Tie-In

- Concept: resilience under constrained access.
- Story idea: narrowing a gate protects some services while creating new access problems.
- Key distinction: outside is not the same as hostile.
- Defensive habit: explain temporary limits, provide help paths, and review restrictions often.
- Season thread: availability is part of trust.

## Behind the Signal

One of the most concrete defender stories from Estonia was traffic triage. CERT and later analyses describe temporary restrictions on foreign access to some government pages, and some banks reportedly limited foreign traffic to preserve domestic access before widening it selectively. Those choices were not magic fixes. They were difficult availability tradeoffs made under pressure.

The Outside Gate keeps that complexity visible. A filter can protect local clinic and school services while also catching real people who belong. Toma's request gives the false-positive problem a face, and Shadow's explanation preserves the historical nuance: hostile traffic may arrive through outside paths, but outside does not mean hostile.

## Technical Texture Remediation

- Public copy now adds source-path and service-priority filtering, an exception queue with reason, timestamp, and review mark, plus false-positive language for real requests caught by broad limits.

## Continuity Checks

- Character consistency: Grimalkin handles procedure; Shadow protects the outside perspective.
- World consistency: Outside-gate restriction fits Queue District and Status Wall logic.
- Lesson accuracy: Resilience includes fairness and review.
- Safety review: No filtering mechanics.
- TROPES.md validation: passed after public promotion.
