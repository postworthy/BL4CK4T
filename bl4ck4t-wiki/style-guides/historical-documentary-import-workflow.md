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
2. Create a pre-translation import inventory before writing the BL4CK4T-world story arc.
3. Identify the story function of each historical person, institution, system, mechanism, clue, location, and consequence.
4. Record the safe technical texture for each movement: technical terms that should survive into public prose, defender-side actions that can be shown, and operational details that must remain private.
5. Search the wiki for an existing BL4CK4T-world entity that already fits each function.
6. Reuse existing entities only when continuity and historical clarity both support reuse.
7. Create a new wiki page during import when the story needs a new named character, faction, villain, location, institution, system, artifact, or recurring concept.
8. Record how each new entity enters the season in the season story arc and production bible.
9. Update [Continuity Timeline](../canon/continuity-timeline.md) or [Open Threads](../canon/open-threads.md) when the import changes durable canon.
10. Update [Index](../index.md) and [Log](../log.md).
11. Run `pnpm wiki:check` before treating the imported story arc as complete.

## Pre-Translation Import Inventory

Before translating a historical account or documentary treatment into BL4CK4T fiction, create an import inventory under `bl4ck4t-wiki/reports/` or inside the season production-control artifact. This inventory prevents the story from forcing historically important systems into confusing pre-existing metaphors.

The inventory must list candidate imports from the historical story:

- infrastructure and platforms;
- user-facing systems and ordinary devices;
- back-end systems and dependencies;
- logs, records, artifacts, and technical clues;
- defender roles, institutions, and workflows;
- adversary patterns and motive classes;
- legal, policy, or aftermath structures;
- human-impact settings where the technical event becomes visible.

For each candidate, decide one of four outcomes:

- `reuse`: an existing BL4CK4T entity already maps clearly to the historical function;
- `create`: the season needs a new first-class BL4CK4T entity or infrastructure layer;
- `merge`: an existing entity should be expanded because the fit is clear but incomplete;
- `omit`: the detail is historically real but not needed for the season's story or would create unsafe operational detail.

The import inventory should be complete before episode drafting starts. If drafting later reveals a missing historical system, pause and update the inventory and wiki support pages before continuing.

## Infrastructure Fidelity Rule

Historical fidelity comes before reuse of existing lore. If the real event depends on infrastructure, roles, systems, or behaviors that Cybertropolis does not yet have, introduce the needed BL4CK4T-world element clearly instead of forcing the event through an existing metaphor.

Use existing lore when the fit is direct and easy to explain. Do not stretch a prior artifact, district, or concept merely because it is already available. A new fictional element is better than a strained analogy when the new element makes the historical mechanism clearer.

Before drafting, identify:

- the real systems the historical event affected;
- the real dependencies that made the event matter;
- the real defender actions that shaped response;
- the BL4CK4T-world systems that already map cleanly to those functions;
- any missing BL4CK4T-world infrastructure that should be introduced.

If a reader would need internal wiki language or several invented bridge terms to understand the analogy, redesign the translation. The public story should make the fictional equivalent feel natural before it becomes plot-critical.

## Analogy Fit Test

For each episode-level movement, answer these questions before drafting or publishing:

- What real historical system, behavior, or consequence is this scene translating?
- What BL4CK4T-world element represents it?
- Would a reader understand that element from the episode itself?
- Are we reusing an existing concept because it truly fits, or because it is convenient?
- Would a new piece of city infrastructure make the historical idea clearer?

If the answer requires a stretched explanation, introduce clearer infrastructure and add the corresponding wiki support page during the same work.

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
