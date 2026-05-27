# BL4CK4T Wiki Log

Append-only chronological record of wiki operations.

## [2026-05-26] schema | Initialize BL4CK4T worldbuilding wiki

Created the BL4CK4T wiki structure, operating instructions, templates, canon pages, character pages, initial source ingests, lessons, style guides, and villain backlog. Existing blog/project content was ingested as soft canon to support future story generation.

Touched areas:

- `AGENTS.md`
- `bl4ck4t-wiki/`
- `src/layouts/Layout.astro`

## [2026-05-26] canon | Build first wiki-to-blog production pipeline

Expanded the BL4CK4T wiki from seed canon into a usable story-production system. Added deeper canon rules, character guidance, district mapping, naming rules, mission and villain templates, first real-world inspiration sources, first active villains, the first mission packet, the first wiki-generated draft, and lightweight wiki validation.

Touched areas:

- `AGENTS.md`
- `package.json`
- `tools/check_bl4ck4t_wiki.py`
- `bl4ck4t-wiki/`

## [2026-05-26] lint | Wiki structure and maturity review

Ran the BL4CK4T wiki checker and a manual maturity review. Link/index validation passed. Filed a lint report identifying the main next attention areas: seed-status canon pages, unresolved character backstories, thin location/faction pages, source provenance depth, and promotion criteria for the first draft.

Touched pages:

- [reports/2026-05-26-wiki-lint.md](reports/2026-05-26-wiki-lint.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-26] canon | Select hero anchors for core characters

Recorded the selected hero/persona anchors for BL4CK4T and the Script Kitties. Added the policy that anchors guide ethos and development arcs, not direct biography copying, because the Script Kitties are younger characters still forming. Updated each character page with its anchor and growth direction.

Touched pages:

- [canon/hero-anchor-policy.md](canon/hero-anchor-policy.md)
- [characters/bl4ck4t.md](characters/bl4ck4t.md)
- [characters/whiskers.md](characters/whiskers.md)
- [characters/grimalkin.md](characters/grimalkin.md)
- [characters/pixel.md](characters/pixel.md)
- [characters/byte.md](characters/byte.md)
- [characters/cipher.md](characters/cipher.md)
- [characters/jinx.md](characters/jinx.md)
- [characters/shadow.md](characters/shadow.md)
- [index.md](index.md)

## [2026-05-26] canon | Establish season architecture

Recorded the user's direction to structure BL4CK4T like a streaming series. Marked the existing three blog posts as a standalone pilot season and added planned season pages based on major cybersecurity history arcs, from phone phreaking through XZ Utils. Added the rule that planned seasons can use user-supplied creative direction, but episode drafts require separate source pages before factual details are used publicly.

Touched pages:

- [sources/creative-briefs/cyber-history-season-brief.md](sources/creative-briefs/cyber-history-season-brief.md)
- [seasons/season-architecture.md](seasons/season-architecture.md)
- [seasons/pilot-season.md](seasons/pilot-season.md)
- `bl4ck4t-wiki/seasons/season-*.md`
- [story-arcs/origin-arc.md](story-arcs/origin-arc.md)
- [templates/season.md](templates/season.md)
- [index.md](index.md)
- [AGENTS.md](../AGENTS.md)

## [2026-05-26] canon | Require historical accounts before season transformation

Added the rule that every historically inspired BL4CK4T season must first produce an accurate, source-backed historical account before any BL4CK4T-world decomposition, mission planning, or episode drafting. Added a historical-account directory, template, canon policy, and season workflow updates.

Touched pages:

- [canon/historical-grounding-policy.md](canon/historical-grounding-policy.md)
- [historical-accounts/README.md](historical-accounts/README.md)
- [templates/historical-account.md](templates/historical-account.md)
- [seasons/season-architecture.md](seasons/season-architecture.md)
- [templates/season.md](templates/season.md)
- [index.md](index.md)
- [AGENTS.md](../AGENTS.md)

## [2026-05-26] canon | Add historical journalism standard

Added a journalistic research standard for historical cybersecurity accounts. The standard requires separation of known facts, allegations, inferences, disputed claims, and unknowns; timeline discipline; attribution confidence; primary-source preference; technical mechanism clarity; attacker and defender perspectives; victim specificity; incentive analysis; and careful treatment of operational detail before any historical season is transformed into BL4CK4T fiction.

Touched pages:

- [style-guides/historical-journalism-standard.md](style-guides/historical-journalism-standard.md)
- [templates/historical-account.md](templates/historical-account.md)
- [canon/historical-grounding-policy.md](canon/historical-grounding-policy.md)
- [seasons/season-architecture.md](seasons/season-architecture.md)
- [index.md](index.md)
- [AGENTS.md](../AGENTS.md)

## [2026-05-26] ingest | Draft Season 1 historical account

Created the first draft historical account for Season 1, covering phone phreaking and the blue-box era. The account follows the historical journalism standard, separates claim confidence, lists source classes, builds an initial chronology, explains in-band telephone signaling, and records unresolved source gaps. It remains `status: draft` and should not yet be used for BL4CK4T story decomposition.

Touched pages:

- [historical-accounts/phone-phreaking-blue-box-era.md](historical-accounts/phone-phreaking-blue-box-era.md)
- [historical-accounts/README.md](historical-accounts/README.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] research | Closed Season 1 historical-account gaps

Closed the initial Season 1 historical-account gaps for phone phreaking and the blue-box era. Added stronger source anchors for Engressia/Joybubbles, Wozniak/Jobs, Draper, Sid Bernay, Bell countermeasures, legal exposure, damage-estimate limits, and the recommended 1968-1976 season scope. The account is now `status: research-foundation-complete` and can support BL4CK4T transformation planning, while detailed legal article claims should still check court records before publication.

Touched pages:

- [historical-accounts/phone-phreaking-blue-box-era.md](historical-accounts/phone-phreaking-blue-box-era.md)
- [historical-accounts/README.md](historical-accounts/README.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)

## [2026-05-26] canon | Keep historical accounts historically clean

Removed project-specific transformation language from the historical account directory and historical-account template. Historical accounts now remain factual research anchors only; adaptation notes, character guidance, installments, and project-specific directives must live outside `historical-accounts/`.

Touched pages:

- [historical-accounts/phone-phreaking-blue-box-era.md](historical-accounts/phone-phreaking-blue-box-era.md)
- [historical-accounts/README.md](historical-accounts/README.md)
- [templates/historical-account.md](templates/historical-account.md)
- [canon/historical-grounding-policy.md](canon/historical-grounding-policy.md)

## [2026-05-26] narrative | Add documentary treatment step

Added a nonfiction documentary-treatment layer that follows completed historical accounts and precedes fictional adaptation. Created the phone-phreaking/blue-box treatment as a movement-based documentary structure with cold open, narrative questions, evidence anchors, visual language, uncertainty guardrails, interview targets, narration guardrails, and open research needs for a full script.

Touched pages:

- [historical-documentary-treatments/README.md](historical-documentary-treatments/README.md)
- [historical-documentary-treatments/phone-phreaking-blue-box-era.md](historical-documentary-treatments/phone-phreaking-blue-box-era.md)
- [templates/historical-documentary-treatment.md](templates/historical-documentary-treatment.md)
- [canon/historical-grounding-policy.md](canon/historical-grounding-policy.md)
- [index.md](index.md)

## [2026-05-26] story | Adapt Season 1 documentary treatment into BL4CK4T arc

Created the Season 1 story arc adaptation for The Singing Network. The arc preserves the documentary treatment's movement flow while transforming historical details into Cybertropolis, Signal Row, the Echo Grid, the Tonebox, the Hushline, and Script Kitties character growth. Updated the Season 1 page with the documentary treatment, story arc, full character roster, and nine-episode shape.

Touched pages:

- [story-arcs/season-01-the-singing-network-arc.md](story-arcs/season-01-the-singing-network-arc.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] style | Preserve mystique while withholding operational detail

Revised the Season 1 story arc and style guidance to reduce repeated safety/permission language in story-facing material. The updated approach keeps exploit-enabling detail out through omission and fictional transformation while letting mystery, craft, character choice, and consequence carry the ethics.

Touched pages:

- [story-arcs/season-01-the-singing-network-arc.md](story-arcs/season-01-the-singing-network-arc.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)
- [style-guides/article-style-guide.md](style-guides/article-style-guide.md)
- [style-guides/real-world-transformation-guide.md](style-guides/real-world-transformation-guide.md)

## [2026-05-26] style | Add TROPES.md publication gate

Added `TROPES.md` validation as a required publication-readability gate for user-facing documents. Public blog and project markdown must pass `pnpm tropes:check <path>` before publication. Added the checker script, package command, article workflow guidance, draft checklist item, and article template marker.

Touched pages:

- [../AGENTS.md](../AGENTS.md)
- [../TROPES.md](../TROPES.md)
- [../tools/check_tropes.py](../tools/check_tropes.py)
- [../package.json](../package.json)
- [style-guides/story-draft-checklist.md](style-guides/story-draft-checklist.md)
- [templates/article-draft.md](templates/article-draft.md)
- [style-guides/article-style-guide.md](style-guides/article-style-guide.md)
- [drafts/phishmonger-signal-row.md](drafts/phishmonger-signal-row.md)

## [2026-05-26] production | Create Season 1 production bible

Created the Season 1 production bible for The Singing Network. The bible locks the release strategy: develop and vet all nine episodes, including the Season 2 cliffhanger, before publishing any Season 1 episode to the public blog. It also records episode requirements, recurring props, character production notes, cliffhanger design, publication voice rules, and the production workflow.

Touched pages:

- [production-bibles/README.md](production-bibles/README.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)
- [index.md](index.md)
- [../AGENTS.md](../AGENTS.md)

## [2026-05-26] draft | Create Season 1 Episode 1

Created the mission packet and article draft for Season 1 Episode 1, "The Sound Beneath Signal Row." The episode introduces Signal Row at night, Pixel hearing the three-note tone, Shadow spotting the beacon response, BL4CK4T's `LISTEN. MAP. STOP.` drop, and the first Echo Grid model. The draft passes `pnpm wiki:check` and `pnpm tropes:check bl4ck4t-wiki/drafts/season-01-episode-01-sound-beneath-signal-row.md`.

Touched pages:

- [missions/season-01-episode-01-sound-beneath-signal-row.md](missions/season-01-episode-01-sound-beneath-signal-row.md)
- [drafts/season-01-episode-01-sound-beneath-signal-row.md](drafts/season-01-episode-01-sound-beneath-signal-row.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] draft | Create Season 1 Episode 2

Created the mission packet and article draft for Season 1 Episode 2, "The Listeners' Marks." The episode follows Pixel, Jinx, Shadow, Cipher, and Whiskers as they find older listener marks around Signal Row, distinguish old marks from fresh evidence, and discover the first `Little Blue Pawprint` sticker. The draft passes `pnpm wiki:check` and `pnpm tropes:check bl4ck4t-wiki/drafts/season-01-episode-02-listeners-marks.md`.

Touched pages:

- [missions/season-01-episode-02-listeners-marks.md](missions/season-01-episode-02-listeners-marks.md)
- [drafts/season-01-episode-02-listeners-marks.md](drafts/season-01-episode-02-listeners-marks.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] draft | Create Season 1 Episode 3

Created the mission packet and article draft for Season 1 Episode 3, "The Little Blue Pawprint." The episode brings the Echo Grid rumor into Packet Market through a handmade zine, tracks how partial knowledge mutates through stickers and charms, and ends with the Crunch Charm entering public language. The draft passes `pnpm wiki:check` and `pnpm tropes:check bl4ck4t-wiki/drafts/season-01-episode-03-little-blue-pawprint.md`.

Touched pages:

- [missions/season-01-episode-03-little-blue-pawprint.md](missions/season-01-episode-03-little-blue-pawprint.md)
- [drafts/season-01-episode-03-little-blue-pawprint.md](drafts/season-01-episode-03-little-blue-pawprint.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] draft | Create remaining Season 1 episodes

Created mission packets and article drafts for Season 1 Episodes 4 through 9: "The Crunch Charm," "The Row Rebels," "The Tonebox Demo," "The False Closure," "The Hushline," and "The City Still Sings." The finale includes the `-0.75` discrepancy and `FOLLOW SMALL THREADS.` cliffhanger into Season 2. All remaining drafts pass `pnpm wiki:check` and `pnpm tropes:check` on the draft files. No public blog files were published.

Touched pages:

- [missions/season-01-episode-04-crunch-charm.md](missions/season-01-episode-04-crunch-charm.md)
- [missions/season-01-episode-05-row-rebels.md](missions/season-01-episode-05-row-rebels.md)
- [missions/season-01-episode-06-tonebox-demo.md](missions/season-01-episode-06-tonebox-demo.md)
- [missions/season-01-episode-07-false-closure.md](missions/season-01-episode-07-false-closure.md)
- [missions/season-01-episode-08-hushline.md](missions/season-01-episode-08-hushline.md)
- [missions/season-01-episode-09-city-still-sings.md](missions/season-01-episode-09-city-still-sings.md)
- [drafts/season-01-episode-04-crunch-charm.md](drafts/season-01-episode-04-crunch-charm.md)
- [drafts/season-01-episode-05-row-rebels.md](drafts/season-01-episode-05-row-rebels.md)
- [drafts/season-01-episode-06-tonebox-demo.md](drafts/season-01-episode-06-tonebox-demo.md)
- [drafts/season-01-episode-07-false-closure.md](drafts/season-01-episode-07-false-closure.md)
- [drafts/season-01-episode-08-hushline.md](drafts/season-01-episode-08-hushline.md)
- [drafts/season-01-episode-09-city-still-sings.md](drafts/season-01-episode-09-city-still-sings.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-26] publish | Release Season 1 public article files

Promoted all nine Season 1 drafts into public blog markdown files under `content/blogs/`, then aligned every Season 1 public timestamp to `2026-05-27T00:00:00+00:00` so the season publishes simultaneously. Ran TROPES.md validation on the final public markdown files, ran the wiki check, ran the site build, and added a final historical anchor analysis comparing the released season against the phone-phreaking historical account and documentary treatment.

Touched pages:

- [../content/blogs/season-01-episode-01-sound-beneath-signal-row.md](../content/blogs/season-01-episode-01-sound-beneath-signal-row.md)
- [../content/blogs/season-01-episode-02-listeners-marks.md](../content/blogs/season-01-episode-02-listeners-marks.md)
- [../content/blogs/season-01-episode-03-little-blue-pawprint.md](../content/blogs/season-01-episode-03-little-blue-pawprint.md)
- [../content/blogs/season-01-episode-04-crunch-charm.md](../content/blogs/season-01-episode-04-crunch-charm.md)
- [../content/blogs/season-01-episode-05-row-rebels.md](../content/blogs/season-01-episode-05-row-rebels.md)
- [../content/blogs/season-01-episode-06-tonebox-demo.md](../content/blogs/season-01-episode-06-tonebox-demo.md)
- [../content/blogs/season-01-episode-07-false-closure.md](../content/blogs/season-01-episode-07-false-closure.md)
- [../content/blogs/season-01-episode-08-hushline.md](../content/blogs/season-01-episode-08-hushline.md)
- [../content/blogs/season-01-episode-09-city-still-sings.md](../content/blogs/season-01-episode-09-city-still-sings.md)
- [reports/season-01-release-historical-anchor-analysis.md](reports/season-01-release-historical-anchor-analysis.md)
- [production-bibles/season-01-the-singing-network.md](production-bibles/season-01-the-singing-network.md)
- [index.md](index.md)

## [2026-05-27] publish | Make seasons first-class site navigation

Added public season landing content, `/seasons/` routes, homepage season promotion, grouped blog archive sections, and previous/next episode navigation on article pages. Added season and episode metadata to the pilot articles and Season 1 public posts so visitors can browse stories by season while `/blog/` remains the complete article archive.

Touched pages:

- [../content/seasons/pilot-season.md](../content/seasons/pilot-season.md)
- [../content/seasons/season-01-the-singing-network.md](../content/seasons/season-01-the-singing-network.md)
- [../content/blogs/script-kitties-episode-1-hidden-code.md](../content/blogs/script-kitties-episode-1-hidden-code.md)
- [../content/blogs/crypto_key_chapter.md](../content/blogs/crypto_key_chapter.md)
- [../content/blogs/compound_interest_lesson.md](../content/blogs/compound_interest_lesson.md)
- [../content/blogs/season-01-episode-01-sound-beneath-signal-row.md](../content/blogs/season-01-episode-01-sound-beneath-signal-row.md)
- [../content/blogs/season-01-episode-02-listeners-marks.md](../content/blogs/season-01-episode-02-listeners-marks.md)
- [../content/blogs/season-01-episode-03-little-blue-pawprint.md](../content/blogs/season-01-episode-03-little-blue-pawprint.md)
- [../content/blogs/season-01-episode-04-crunch-charm.md](../content/blogs/season-01-episode-04-crunch-charm.md)
- [../content/blogs/season-01-episode-05-row-rebels.md](../content/blogs/season-01-episode-05-row-rebels.md)
- [../content/blogs/season-01-episode-06-tonebox-demo.md](../content/blogs/season-01-episode-06-tonebox-demo.md)
- [../content/blogs/season-01-episode-07-false-closure.md](../content/blogs/season-01-episode-07-false-closure.md)
- [../content/blogs/season-01-episode-08-hushline.md](../content/blogs/season-01-episode-08-hushline.md)
- [../content/blogs/season-01-episode-09-city-still-sings.md](../content/blogs/season-01-episode-09-city-still-sings.md)
