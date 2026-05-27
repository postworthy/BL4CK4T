---
type: style-guide
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [season, release, quality, prose, validation]
sources:
  - ../reports/season-06-10-release-retraction.md
---

# Season Release Quality Gate

## Purpose

This gate exists to prevent season batches from reading like lightly varied templates. It applies before any public release of a full season or multi-season arc.

Passing `pnpm tropes:check`, `pnpm wiki:check`, and `pnpm build` is necessary, but not sufficient. A season also needs a manual prose-quality review that confirms each episode earns its place as a story.

## Historical Depth Gate

Before the prose-quality gate can run, the season must pass a historical depth gate:

- The historical account must be substantial enough to support story movement, character pressure, and historical nuance.
- The documentary treatment must be movement-rich enough that episode drafts do not rely on repeated generic openings.
- The story-world import must trace each major fictional episode beat back to a documentary movement or clearly marked creative bridge.
- Thin macro planning pages are not valid substitutes for historical accounts or documentary treatments.

For Seasons 6-10, use `../reports/season-06-10-historical-depth-remediation-plan.md` as the active remediation standard.

## Hard Stop Conditions

Do not publish if any of these are true:

- Multiple episode openings use the same sentence shape, setup rhythm, or only-swapped nouns.
- Consecutive episodes begin with the same location-plus-team staging unless the repetition is an intentional story device called out in the production bible.
- The same paragraph function repeats across episodes with minimal variation, especially in openings, BL4CK4T drop arrivals, discoveries, closing reflections, or Teaching Tie-Ins.
- Characters appear as role labels only and do not make episode-specific choices.
- The episode could be summarized by replacing a proper noun in another episode's plot summary.
- The Teaching Tie-In is technically correct but detached from the episode's actual emotional or narrative turn.
- A season reaches public `content/` before every episode has had a close-reading pass.

## Required Manual Review

For every episode, record these checks in the season draft review report:

- Opening scene: what makes this episode start differently from the prior two episodes?
- Character pressure: which character wants, fears, notices, misunderstands, or changes something specific in this episode?
- Story consequence: what changes because this episode happened?
- Historical anchor: what part of the source history is being transformed here?
- Civic or emotional scale: whose ordinary life is affected, and how is that made concrete?
- Prose uniqueness: which repeated lines, sentence patterns, or structural shortcuts were removed?
- Teaching Tie-In fit: how does the lesson arise from the story rather than being appended to it?

## Batch Comparison Pass

Before publication, compare the full season as a set:

- Read the first 250 words of every episode in order and revise any duplicated opening posture.
- Read all BL4CK4T drop moments together and revise any that use the same dramatic mechanics without reason.
- Read all endings together and revise any that resolve with the same cadence.
- Read all Teaching Tie-Ins together and confirm they use the standard structure while still reflecting the specific episode.
- Search for repeated phrases longer than six words across the season and revise unless the phrase is a deliberate refrain.

Useful shell checks:

```bash
rg -n "The trouble looked small at first|stood with the team|No one cheered|teaching tie-in" bl4ck4t-wiki/drafts content/blogs
```

These checks do not replace reading the prose. They are tripwires.

## Release Discipline

Seasons 6-10 must be rebuilt one season at a time. A complete season means:

- Historical account complete.
- Documentary treatment complete.
- Story-world import complete.
- Support wiki pages complete.
- Production bible complete.
- Mission packets complete.
- Drafts complete.
- Draft review report includes this quality gate.
- Continuity audit complete.
- Historical-anchor analysis complete after final public copy exists.
- TROPES validation passes.
- Wiki check passes.
- Build passes.

Do not publish multiple rebuilt seasons in one commit unless each season has independently passed this gate.
