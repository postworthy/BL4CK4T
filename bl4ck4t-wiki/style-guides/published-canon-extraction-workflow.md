---
type: style-guide
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [canon, workflow, seasons]
---

# Published Canon Extraction Workflow

Run this workflow after every season release. This is a final reconciliation pass, not the first time season entities should enter the wiki. New entities should already be created during the historical documentary import workflow.

## Steps

1. Read the final public season page and every public episode.
2. Extract details that are now hard canon because readers can see them.
3. Classify each detail as character, location, faction, artifact, villain/force, concept, timeline event, or open thread.
4. Backfill the appropriate wiki pages.
5. Create artifact pages for recurring story objects.
6. Create character, faction, location, villain, concept, or artifact pages for every named recurring entity.
7. File or update a published entity inventory report under `bl4ck4t-wiki/reports/`.
8. Update [Continuity Timeline](../canon/continuity-timeline.md) and [Open Threads](../canon/open-threads.md).
9. Update [index.md](../index.md) and [log.md](../log.md).
10. Run `pnpm wiki:check`.

## Extraction Rules

- Public posts override draft intent.
- Do not invent new public events during backfill.
- Prefer concise season-specific notes over full episode summaries.
- If a detail is implied but not stated, mark it as soft canon or leave it out.
- Keep historical-account documents free of fictional canon.
- If a named public entity is intentionally not promoted to a page, document the deferral and reason in the entity inventory.
