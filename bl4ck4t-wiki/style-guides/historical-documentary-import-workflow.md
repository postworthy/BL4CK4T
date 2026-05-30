---
type: style-guide
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [season, canon, workflow, continuity]
---

# Historical Documentary Import Workflow

Use this workflow when transforming a completed historical documentary treatment into a BL4CK4T-world season arc.

## Purpose

The import stage is where real historical structure becomes fictional canon. This is the right time to establish lore for every new person, group, place, adversary, system, artifact, institution, or recurring concept the season needs. Do not wait until after publication to backfill entities that are already steering the story.

## Required Context Pass

Before writing the BL4CK4T-world story arc, read:

1. [Index](../index.md).
2. [Continuity Timeline](../canon/continuity-timeline.md).
3. [Open Threads](../canon/open-threads.md).
4. Relevant season pages, prior story arcs, production bibles, missions, and drafts.
5. Relevant character, villain, faction, location, artifact, concept, lesson, and style-guide pages.
6. The historical account and documentary treatment for the season being imported.

## Import Steps

1. Map the documentary movements to fictional season movements.
2. Identify the story function of each historical person, institution, system, mechanism, clue, location, and consequence.
3. Record the safe technical texture for each movement: technical terms that should survive into public prose, defender-side actions that can be shown, and operational details that must remain private.
4. Search the wiki for an existing BL4CK4T-world entity that already fits each function.
5. Reuse existing entities when continuity supports reuse.
6. Create a new wiki page during import when the story needs a new named character, faction, villain, location, institution, system, artifact, or recurring concept.
7. Record how each new entity enters the season in the season story arc and production bible.
8. Update [Continuity Timeline](../canon/continuity-timeline.md) or [Open Threads](../canon/open-threads.md) when the import changes durable canon.
9. Update [Index](../index.md) and [Log](../log.md).
10. Run `pnpm wiki:check` before treating the imported story arc as complete.

## Technical Texture Requirement

Use [Technical Texture Standard](technical-texture-standard.md) during import. The BL4CK4T-world adaptation must preserve enough safe system language and cause/effect that the public story still feels rooted in cybersecurity history.

For each episode-level movement, capture:

- historical mechanism in one sentence;
- fictional transformation;
- safe technical terms to include in the story;
- defender-side action to show on page;
- details to omit because they would become operationally harmful.

## Entity Rules

- A named entity that appears in a season arc, production bible, mission packet, draft, or public article should have a wiki page unless it is explicitly incidental.
- Incidental named entities may stay unpaged only when they are one-scene texture and are not expected to recur.
- If an entity is intentionally not paged, note the reason in the story arc, production bible, or a report.
- New pages should use the structure already established in their directory.
- Historical-account documents must remain free of BL4CK4T-world entities and fictional canon.

## Completion Gate

The import is not complete until the story arc can be read alongside the wiki without creating unresolved names, undefined locations, missing adversary records, or unsupported continuity jumps.

The import is also incomplete if the fictional arc replaces every technical mechanism with metaphor. The story arc must preserve a visible bridge between the historical anchor and the public fiction.
