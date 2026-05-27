---
type: style-guide
status: active
created: 2026-05-26
updated: 2026-05-26
tags: [drafts, review, safety, continuity]
sources: []
---

# Story Draft Checklist

## Summary

Use this checklist before reporting a draft complete and again before promoting a draft into `content/blogs/`.

## Continuity Check

- The story matches the [World Bible](../canon/world-bible.md).
- Character behavior matches the relevant character pages.
- The mission has a clear place in the [Continuity Timeline](../canon/continuity-timeline.md).
- New canon details are recorded in the wiki.

## Lesson Check

- The lesson is beginner-friendly.
- The core concept is accurate.
- The story explains why the concept matters.
- The `Teaching Tie-In` is usable by a teacher or mentor.

## Safety Check

- The public story avoids operational abuse steps.
- Any real-world inspiration is transformed into fictional story mechanics.
- Defensive actions are emphasized.
- Consent, safe labs, reporting, or repair are part of the frame when relevant.

## Publication Check

- Draft has complete Astro-compatible frontmatter in its `Publication Frontmatter` block.
- Public article title, slug, description, tags, read time, and timestamp are chosen before publication.
- `TROPES.md` validation has been run against the draft or public markdown file.
- Any TROPES.md findings have been revised or explicitly accepted by the user.
- `pnpm wiki:check` passes.
- `pnpm tropes:check content/blogs/<post-file>.md` passes before publishing a public blog post.
- `pnpm build` passes after any public content change.
