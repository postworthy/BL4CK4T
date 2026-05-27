---
type: style-guide
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [season, production, checklist, validation]
---

# Season Artifact Checklist

Use this checklist for every historically inspired season so the source-first process remains repeatable across the full series.

## Required Private Artifacts

- Season page in `bl4ck4t-wiki/seasons/`.
- Real-world source page in `bl4ck4t-wiki/sources/real-world/`.
- Historical account in `bl4ck4t-wiki/historical-accounts/`.
- Historical documentary treatment in `bl4ck4t-wiki/historical-documentary-treatments/`.
- BL4CK4T-world story arc in `bl4ck4t-wiki/story-arcs/`.
- Historical documentary import pass using `bl4ck4t-wiki/style-guides/historical-documentary-import-workflow.md`.
- Support canon pages for new characters, concepts, locations, factions, villains, institutions, systems, and recurring artifacts introduced during story import.
- Production bible in `bl4ck4t-wiki/production-bibles/`.
- Mission packets for the declared episode count.
- Private drafts for the declared episode count.
- Draft review report in `bl4ck4t-wiki/reports/`.
- Cross-season continuity audit or explicit update to an existing audit.
- Release historical-anchor analysis after public copy is frozen.
- Season release quality gate report entries using `bl4ck4t-wiki/style-guides/season-release-quality-gate.md`.

## Required Public Artifacts

- Public season landing page in `content/seasons/`.
- Public blog posts in `content/blogs/` for every episode.
- Season and episode metadata on every public post.
- Simultaneous timestamps when the user requests a single-drop release.

## Required Validation

- Draft-level `pnpm tropes:check` for every private draft before promotion.
- Public `pnpm tropes:check` for every public post and season page before release.
- Full `pnpm tropes:check` before any season-wide publication commit.
- `pnpm wiki:check` before reporting private artifacts complete and before publication.
- `pnpm build` after public files are staged.
- Manual continuity pass against the pilot, all prior seasons, the current production bible, and `bl4ck4t-wiki/canon/continuity-timeline.md`.
- Manual historical-anchor pass against the historical account and documentary treatment.
- Manual entity pass confirming every non-incidental named character, faction, villain, location, institution, system, artifact, and recurring concept introduced during the season has a wiki page or an explicit deferral note.
- Manual prose-quality and episode-differentiation pass using `bl4ck4t-wiki/style-guides/season-release-quality-gate.md`.

## Status Conventions

- Season page: `planned`, `researching`, `drafting`, or `published`.
- Historical account: `draft` or `research-foundation-complete`.
- Documentary treatment: `draft` or `complete`.
- Story arc: `draft`, `complete`, or `released`.
- Production bible: `draft`, `complete`, or `released`.
- Draft review report: `complete` once the full draft set has been checked.
- Release historical-anchor analysis: `complete` only after final public copy exists.

## Index And Log Requirements

- Add every new artifact to `bl4ck4t-wiki/index.md`.
- Add a dated entry to `bl4ck4t-wiki/log.md` for every ingest, canon update, draft batch, review, publication, or maintenance pass.
- When a season publishes, update stale private statuses during the same maintenance window so future comparison does not mistake old planning language for current state.
