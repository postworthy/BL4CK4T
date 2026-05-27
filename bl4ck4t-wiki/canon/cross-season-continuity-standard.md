---
type: canon
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [canon, continuity, seasons, review]
sources:
  - continuity-timeline.md
  - canon-policy.md
  - world-bible.md
---

# Cross-Season Continuity Standard

## Purpose

This standard protects BL4CK4T from long-running continuity drift. Every new season, mission packet, article draft, public promotion, and major canon update must be checked against prior seasons before it is treated as complete.

The goal is not to freeze the world. The goal is to make every change deliberate, recorded, and compatible with what readers already know.

## Required Continuity Sources

Before drafting or revising season material, read:

- [World Bible](world-bible.md)
- [Canon Policy](canon-policy.md)
- [Continuity Timeline](continuity-timeline.md)
- Relevant character pages.
- Relevant location, faction, villain, concept, lesson, and source pages.
- Prior season pages, story arcs, production bibles, mission packets, and published articles that touch the same characters, places, artifacts, or themes.

## Continuity Classes

### Hard Continuity

Hard continuity cannot change without explicit user approval.

- Published episode events.
- Public article titles, slugs, and season ordering.
- Named Script Kitties and their core roles.
- BL4CK4T as an unseen mentor who guides through drops but does not simply solve the mission.
- Cybertropolis as the main setting.
- Major resolved season outcomes, such as the Hushline separating Echo Grid message and command paths.
- Published cliffhangers that launch later seasons.

### Soft Continuity

Soft continuity can be refined, but changes must be recorded.

- Exact visual details.
- Background locations.
- Running jokes.
- Incidental props.
- Unpublished draft events.
- Early character habits that have not yet become repeated public behavior.
- Wiki-only villain backlog ideas.

### Active Draft Continuity

Active draft continuity governs planned material that is not public yet.

- Private mission packets.
- Private article drafts.
- Production bible trackers.
- Draft-only story reports.
- Planned season arcs.

Draft continuity can still change, but changes must preserve the source chain and update affected wiki pages.

## Cross-Season Checks

Every season-level review must answer:

- Does the new season contradict any published event?
- Does it preserve the prior season's closing state?
- Does the new season honor the prior cliffhanger?
- Does each recurring character behave in line with prior growth?
- Does the season reuse locations and institutions consistently?
- Does it introduce new institutions without making older ones impossible?
- Does it resolve or intentionally carry forward open threads?
- Does it create any duplicate artifact, villain, or concept under a new name?
- Does it accidentally weaken a prior season's lesson?
- Does it leave a clear bridge into the next season?

## Character Continuity Checks

For each recurring character, track:

- What the character learned in prior seasons.
- Which flaw or growth edge remains active.
- Whether the new season repeats an old lesson without development.
- Whether a new behavior needs backstory support.
- Whether the character's hero anchor is being echoed in spirit without copying biography.

## World Continuity Checks

For each major location, institution, artifact, or system, track:

- First appearance.
- Current state.
- Who knows about it.
- Whether it is public, hidden, retired, repaired, or unresolved.
- Which season changed it.
- Which future stories may depend on it.

## Contradiction Handling

If a contradiction appears:

1. Identify the older source that established the fact.
2. Identify the new material that conflicts.
3. Classify the older fact as hard, soft, or draft continuity.
4. Prefer revising unpublished material.
5. If the contradiction improves the story, record it as an intentional continuity revision and ask the user before changing public canon.
6. Update [Continuity Timeline](continuity-timeline.md), affected canon pages, and [log.md](../log.md).

## Required Reports

Create a continuity audit report when:

- A full season is drafted.
- A season is promoted to public blog posts.
- A major recurring character backstory changes.
- A prior public event is reinterpreted.
- A new season begins after another season has already been developed.

Report location:

- `bl4ck4t-wiki/reports/`

Report title pattern:

- `season-XX-continuity-audit.md`
- `series-continuity-audit-YYYY-MM-DD.md`

## Publication Gate

No future season should be published until:

- The season has a continuity audit.
- The continuity audit checks prior seasons and the current season as a full set.
- Any contradictions are resolved or explicitly recorded.
- `pnpm wiki:check` passes.
- Public-facing markdown passes `TROPES.md` validation.
