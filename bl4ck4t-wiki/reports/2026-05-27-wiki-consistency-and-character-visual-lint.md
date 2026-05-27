---
type: report
status: complete
created: 2026-05-27
updated: 2026-05-27
tags: [wiki-lint, consistency, characters, visual-language]
sources:
  - ../canon/continuity-timeline.md
  - ../style-guides/published-canon-extraction-workflow.md
  - ../../content/blogs/season-06-episode-01-spinning-board.md
  - ../../content/blogs/season-06-episode-09-city-answers.md
---

# Wiki Consistency And Character Visual Lint

## Scope

This pass checked the wiki after Season 6 publication for structural inconsistencies, stale status language, missing release artifacts, and character-profile gaps that would make future art direction harder.

## Automated Check

- `pnpm wiki:check`: pass before cleanup.

## Findings And Fixes

| Finding | Action |
| --- | --- |
| Season 6 wiki season page used `released`, while published seasons use `published`. | Updated Season 6 status to `published`. |
| Production Bibles README still said Season 6 mission packets were pending. | Updated Season 6 production bible status to released. |
| Season 6 lacked a published entity inventory report required by the published-canon extraction workflow. | Added [Published Entity Inventory: Season 6](published-entity-inventory-season-06.md). |
| Main character pages had uneven published-season coverage after Seasons 4-6. | Added Season 4-6 notes where relevant. |
| Character pages had motifs but not enough render-ready visual direction. | Added Visual Description For Art sections grounded in blog and wiki details. |

## Character Visual Source Notes

- Pixel has hard public visual detail: smallest Script Kitty, bright orange hoodie, chalk, stickers, and visible excitement.
- Cipher has hard public visual detail: purple hoodie, notebooks, grids, and key diagrams.
- Byte has hard public visual detail: blue hooded gadgeteer, tablet, old terminal, demos, and cable/device work.
- Shadow has hard public visual detail: hood, shadows, reflections, edge-of-room observation, and physical-detail inspection.
- Whiskers, Grimalkin, Jinx, BL4CK4T, Ms. Vale, Mira, Rook, and Mr. Olan have stronger motif/tool canon than fixed body-color or clothing-color canon. Their new art notes mark implied presentation and avoid overclaiming fixed visual facts.

## Residual Recommendations

- Future public stories should include a few repeatable physical cues for Whiskers, Grimalkin, Jinx, and Shadow so visual canon becomes less inferred.
- When a new recurring character appears, add an art-direction section during the same wiki-entry creation pass.
- Do not treat character art direction as immutable canon unless the public blog has made the detail visible.
