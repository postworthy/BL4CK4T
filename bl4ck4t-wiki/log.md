# BL4CK4T Wiki Log

Append-only chronological record of wiki operations.


## [2026-05-27] publish | Release Seasons 6-10: The Civic Dependency Arc

Completed the autonomous release pipeline for Seasons 6 through 10. Added source pages, historical accounts, documentary treatments, story arcs, support canon, production bibles, mission packets, draft mirrors, public season pages, public episodes, validation reports, and continuity support for the Civic Dependency Arc.

Touched areas:

- `content/blogs/season-0{6..9}-episode-*.md`
- `content/blogs/season-10-episode-*.md`
- `content/seasons/season-0{6..9}-*.md`
- `content/seasons/season-10-*.md`
- `bl4ck4t-wiki/historical-accounts/`
- `bl4ck4t-wiki/historical-documentary-treatments/`
- `bl4ck4t-wiki/story-arcs/`
- `bl4ck4t-wiki/production-bibles/`
- `bl4ck4t-wiki/missions/`
- `bl4ck4t-wiki/drafts/`
- `bl4ck4t-wiki/reports/`
- `bl4ck4t-wiki/artifacts/`
- `bl4ck4t-wiki/concepts/`
- `bl4ck4t-wiki/factions/`
- `bl4ck4t-wiki/locations/`
- `bl4ck4t-wiki/villains/`
- [index.md](index.md)

## [2026-05-27] canon | Plan Seasons 6-10 Civic Dependency Arc

Formalized the next five-season planning path after Season 5. Added the Civic Dependency Arc as a macro story document and revised the planned Season 6-10 pages around Estonia 2007, MSBlaster/Welchia, Operation Aurora, Stuxnet, and Mirai/Dyn. Preserved the source-first rule: these are planning documents only until each historical account is completed.

Touched areas:

- [story-arcs/seasons-06-10-civic-dependency-arc.md](story-arcs/seasons-06-10-civic-dependency-arc.md)
- `bl4ck4t-wiki/seasons/season-06-*.md`
- `bl4ck4t-wiki/seasons/season-07-*.md`
- `bl4ck4t-wiki/seasons/season-08-*.md`
- `bl4ck4t-wiki/seasons/season-09-*.md`
- `bl4ck4t-wiki/seasons/season-10-*.md`
- [seasons/season-architecture.md](seasons/season-architecture.md)
- [historical-accounts/README.md](historical-accounts/README.md)
- [index.md](index.md)

## [2026-05-27] publish | Release Season 5: The Love Letter Plague

Completed the Season 5 source-first production pipeline for the ILOVEYOU-inspired story arc. Added the historical account, documentary treatment, story-world import, production bible, mission packets, draft mirrors, public season page, public episodes, continuity audit, historical anchor analysis, and entity inventory. Updated canon continuity, open threads, index, and status READMEs.

Touched areas:

- `content/blogs/season-05-episode-*.md`
- `content/seasons/season-05-the-love-letter-plague.md`
- `bl4ck4t-wiki/historical-accounts/iloveyou-love-bug.md`
- `bl4ck4t-wiki/historical-documentary-treatments/iloveyou-love-bug.md`
- `bl4ck4t-wiki/story-arcs/season-05-the-love-letter-plague-arc.md`
- `bl4ck4t-wiki/production-bibles/season-05-the-love-letter-plague.md`
- `bl4ck4t-wiki/missions/season-05-episode-*.md`
- `bl4ck4t-wiki/drafts/season-05-episode-*.md`
- `bl4ck4t-wiki/reports/season-05-*.md`
- `bl4ck4t-wiki/reports/published-entity-inventory-season-05.md`
- `bl4ck4t-wiki/artifacts/`
- `bl4ck4t-wiki/concepts/`
- `bl4ck4t-wiki/factions/`
- `bl4ck4t-wiki/locations/`
- `bl4ck4t-wiki/canon/`
- `bl4ck4t-wiki/index.md`

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

## [2026-05-27] ingest | Start Season 2 historical account

Started the Season 2 historical research foundation for The Cuckoo's Egg and the Hanover hackers. Added a real-world source page, created the historical account draft, updated the Season 2 status, and indexed the new source and account. The document remains historical-only and does not include BL4CK4T-world transformation material.

Closed the initial research gaps by adding contemporaneous indictment and conviction reporting, German court-reporting detail, publication metadata, dated investigation milestones from Stoll's CACM article, and caveated actor roles for Hess, Brzezinski, Carl, Koch, and Huebner.

Touched pages:

- [historical-accounts/cuckoos-egg-hanover-hackers.md](historical-accounts/cuckoos-egg-hanover-hackers.md)
- [sources/real-world/cuckoos-egg-hanover-hackers.md](sources/real-world/cuckoos-egg-hanover-hackers.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] ingest | Create Season 2 documentary treatment

Created the nonfiction documentary movement structure for The Cuckoo's Egg and the Hanover hackers. The treatment follows the completed historical account from the seventy-five-cent accounting mismatch through LBL infrastructure, evidence building, institutional friction, cross-border tracing, the Celle convictions, and the defender-as-detective legacy. The document remains historical-only and does not include BL4CK4T-world transformation material.

Touched pages:

- [historical-documentary-treatments/cuckoos-egg-hanover-hackers.md](historical-documentary-treatments/cuckoos-egg-hanover-hackers.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] canon | Create Season 2 story arc

Created the BL4CK4T-world story arc adaptation for The Seventy-Five Cent Thread. The arc imports the nonfiction documentary movements into Cybertropolis while preserving the historical spine: a tiny accounting mismatch, shared computing infrastructure, evidence building, institutional friction, cross-system tracing, an indirect adversary layer, and the defender-as-detective focus. The arc centers Jinx's suspicion-to-evidence growth and seeds the Morris Worm-inspired Season 3 cliffhanger.

Touched pages:

- [story-arcs/season-02-the-seventy-five-cent-thread-arc.md](story-arcs/season-02-the-seventy-five-cent-thread-arc.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] canon | Create Season 2 production bible

Created the Season 2 production bible for The Seventy-Five Cent Thread. The bible defines the release gate, source chain, season promise, story engine, core canon, character production notes, episode control grid, episode requirements, Season 3 cliffhanger, required concept/world pages, continuity rules, publication voice rules, production workflow, and draft tracker.

Touched pages:

- [production-bibles/season-02-the-seventy-five-cent-thread.md](production-bibles/season-02-the-seventy-five-cent-thread.md)
- [production-bibles/README.md](production-bibles/README.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] canon | Add Season 2 support canon

Created the required Season 2 support canon before mission drafting: logging, intrusion detection, anomaly investigation, evidence preservation, account misuse, incident reporting, shared-system accounting, Civic Learning Grid, Ledger Lab, Glass Bureau, Far Relay, and Ledgerjack. These pages stabilize the concepts, institutions, locations, and adversary layer used by The Seventy-Five Cent Thread.

Touched pages:

- [concepts/logging-and-audit-trails.md](concepts/logging-and-audit-trails.md)
- [concepts/intrusion-detection.md](concepts/intrusion-detection.md)
- [concepts/anomaly-investigation.md](concepts/anomaly-investigation.md)
- [concepts/evidence-preservation.md](concepts/evidence-preservation.md)
- [concepts/account-misuse.md](concepts/account-misuse.md)
- [concepts/incident-reporting.md](concepts/incident-reporting.md)
- [concepts/shared-system-accounting.md](concepts/shared-system-accounting.md)
- [concepts/civic-learning-grid.md](concepts/civic-learning-grid.md)
- [locations/ledger-lab.md](locations/ledger-lab.md)
- [factions/glass-bureau.md](factions/glass-bureau.md)
- [factions/far-relay.md](factions/far-relay.md)
- [villains/ledgerjack.md](villains/ledgerjack.md)
- [index.md](index.md)

## [2026-05-27] draft | Create Season 2 mission packets and episode drafts

Created mission packets and private article drafts for all nine Season 2 episodes in The Seventy-Five Cent Thread. The draft set carries Jinx's investigation arc from the `-0.75` mismatch through the Ledger Lab, Borrowed Door, Threadboard, Glass Bureau, old trust paths, Far Relay, formal case presentation, changed reporting practice, and the Season 3 toy-process cliffhanger. The draft set passes `pnpm wiki:check` and `pnpm tropes:check` across the nine Season 2 draft files.

Touched pages:

- [missions/season-02-episode-01-seventy-five-cent-thread.md](missions/season-02-episode-01-seventy-five-cent-thread.md)
- [missions/season-02-episode-02-ledger-lab.md](missions/season-02-episode-02-ledger-lab.md)
- [missions/season-02-episode-03-borrowed-door.md](missions/season-02-episode-03-borrowed-door.md)
- [missions/season-02-episode-04-threadboard.md](missions/season-02-episode-04-threadboard.md)
- [missions/season-02-episode-05-nobody-owns-thread.md](missions/season-02-episode-05-nobody-owns-thread.md)
- [missions/season-02-episode-06-old-trust-paths.md](missions/season-02-episode-06-old-trust-paths.md)
- [missions/season-02-episode-07-far-relay.md](missions/season-02-episode-07-far-relay.md)
- [missions/season-02-episode-08-investigators-case.md](missions/season-02-episode-08-investigators-case.md)
- [missions/season-02-episode-09-records-changed.md](missions/season-02-episode-09-records-changed.md)
- [drafts/season-02-episode-01-seventy-five-cent-thread.md](drafts/season-02-episode-01-seventy-five-cent-thread.md)
- [drafts/season-02-episode-02-ledger-lab.md](drafts/season-02-episode-02-ledger-lab.md)
- [drafts/season-02-episode-03-borrowed-door.md](drafts/season-02-episode-03-borrowed-door.md)
- [drafts/season-02-episode-04-threadboard.md](drafts/season-02-episode-04-threadboard.md)
- [drafts/season-02-episode-05-nobody-owns-thread.md](drafts/season-02-episode-05-nobody-owns-thread.md)
- [drafts/season-02-episode-06-old-trust-paths.md](drafts/season-02-episode-06-old-trust-paths.md)
- [drafts/season-02-episode-07-far-relay.md](drafts/season-02-episode-07-far-relay.md)
- [drafts/season-02-episode-08-investigators-case.md](drafts/season-02-episode-08-investigators-case.md)
- [drafts/season-02-episode-09-records-changed.md](drafts/season-02-episode-09-records-changed.md)
- [production-bibles/season-02-the-seventy-five-cent-thread.md](production-bibles/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] maintenance | Review Season 2 private draft set

Completed the Season 2 private draft review pass against the historical account, documentary treatment, story arc, and production bible. The review confirms the full draft set preserves the Cuckoo's Egg-inspired historical spine while keeping public fiction transformed into BL4CK4T-world elements. The pass covers continuity, Jinx's character arc, evidence/concept handling, historical cleanliness, and the Season 3 cliffhanger. Updated the production bible tracker to show draft-level continuity and TROPES checks complete, with publication still blocked until user approval.

Touched pages:

- [reports/season-02-draft-review.md](reports/season-02-draft-review.md)
- [production-bibles/season-02-the-seventy-five-cent-thread.md](production-bibles/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] canon | Establish cross-season continuity discipline

Added a formal cross-season continuity standard and expanded the continuity timeline from pilot-only coverage into a series-level memory for the pilot, Season 1, and private Season 2 draft continuity. Updated agent workflow guidance, the story draft checklist, season architecture, and canon policy so future seasons must be checked against prior seasons before publication. Filed the first series continuity audit and found no blocking contradictions across the pilot, Season 1, and Season 2 draft set.

Touched pages:

- [canon/cross-season-continuity-standard.md](canon/cross-season-continuity-standard.md)
- [canon/continuity-timeline.md](canon/continuity-timeline.md)
- [canon/canon-policy.md](canon/canon-policy.md)
- [style-guides/story-draft-checklist.md](style-guides/story-draft-checklist.md)
- [seasons/season-architecture.md](seasons/season-architecture.md)
- [reports/series-continuity-audit-2026-05-27.md](reports/series-continuity-audit-2026-05-27.md)
- [index.md](index.md)
- [../AGENTS.md](../AGENTS.md)

## [2026-05-27] publish | Release Season 2 public article files

Promoted all nine Season 2 drafts into public blog markdown files under `content/blogs/` and added the public Season 2 landing page under `content/seasons/`. All Season 2 public timestamps are aligned to `2026-05-27T00:00:00+00:00` so the season publishes simultaneously. Ran TROPES.md validation on the final public Season 2 markdown files, cleaned older public Pilot/Project copy so the full public TROPES gate passes, ran the wiki check, ran the site build, and filed the final historical anchor analysis comparing the released season against the Cuckoo's Egg historical account and documentary treatment.

Touched pages:

- [../content/seasons/season-02-the-seventy-five-cent-thread.md](../content/seasons/season-02-the-seventy-five-cent-thread.md)
- [../content/blogs/season-02-episode-01-seventy-five-cent-thread.md](../content/blogs/season-02-episode-01-seventy-five-cent-thread.md)
- [../content/blogs/season-02-episode-02-ledger-lab.md](../content/blogs/season-02-episode-02-ledger-lab.md)
- [../content/blogs/season-02-episode-03-borrowed-door.md](../content/blogs/season-02-episode-03-borrowed-door.md)
- [../content/blogs/season-02-episode-04-threadboard.md](../content/blogs/season-02-episode-04-threadboard.md)
- [../content/blogs/season-02-episode-05-nobody-owns-thread.md](../content/blogs/season-02-episode-05-nobody-owns-thread.md)
- [../content/blogs/season-02-episode-06-old-trust-paths.md](../content/blogs/season-02-episode-06-old-trust-paths.md)
- [../content/blogs/season-02-episode-07-far-relay.md](../content/blogs/season-02-episode-07-far-relay.md)
- [../content/blogs/season-02-episode-08-investigators-case.md](../content/blogs/season-02-episode-08-investigators-case.md)
- [../content/blogs/season-02-episode-09-records-changed.md](../content/blogs/season-02-episode-09-records-changed.md)
- [../content/blogs/script-kitties-episode-1-hidden-code.md](../content/blogs/script-kitties-episode-1-hidden-code.md)
- [../content/blogs/crypto_key_chapter.md](../content/blogs/crypto_key_chapter.md)
- [../content/blogs/compound_interest_lesson.md](../content/blogs/compound_interest_lesson.md)
- [../content/projects/classoverride.md](../content/projects/classoverride.md)
- [reports/season-02-release-historical-anchor-analysis.md](reports/season-02-release-historical-anchor-analysis.md)
- [production-bibles/season-02-the-seventy-five-cent-thread.md](production-bibles/season-02-the-seventy-five-cent-thread.md)
- [canon/continuity-timeline.md](canon/continuity-timeline.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)

## [2026-05-27] maintenance | Normalize season artifact parity

Cleaned up the private season-production records after comparing Season 1 and Season 2 artifacts. Backfilled the Season 1 real-world source page and draft review report, added a reusable season artifact checklist, linked the Season 1 source page from the historical account, and normalized stale season/production-bible statuses now that both seasons have been released.

Touched pages:

- [sources/real-world/phone-phreaking-blue-box-era.md](sources/real-world/phone-phreaking-blue-box-era.md)
- [reports/season-01-draft-review.md](reports/season-01-draft-review.md)
- [style-guides/season-artifact-checklist.md](style-guides/season-artifact-checklist.md)
- [historical-accounts/phone-phreaking-blue-box-era.md](historical-accounts/phone-phreaking-blue-box-era.md)
- [seasons/season-01-the-singing-network.md](seasons/season-01-the-singing-network.md)
- [seasons/season-02-the-seventy-five-cent-thread.md](seasons/season-02-the-seventy-five-cent-thread.md)
- [production-bibles/season-02-the-seventy-five-cent-thread.md](production-bibles/season-02-the-seventy-five-cent-thread.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] publish | Release Season 3 public article files

Completed the Season 3 pipeline for The Escaped Experiment. Created the Morris Worm historical account and documentary treatment, transformed the nonfiction spine into a BL4CK4T story arc, added support canon, created the production bible, mission packets, private draft mirrors, draft review, continuity audit, release historical-anchor analysis, public season page, and nine public blog posts. Season 3 publishes as a simultaneous drop and preserves the Season 2 toy-process cliffhanger while closing with a Season 4 chase-story clue.

Touched areas:

- `bl4ck4t-wiki/historical-accounts/morris-worm.md`
- `bl4ck4t-wiki/historical-documentary-treatments/morris-worm.md`
- `bl4ck4t-wiki/story-arcs/season-03-the-escaped-experiment-arc.md`
- `bl4ck4t-wiki/production-bibles/season-03-the-escaped-experiment.md`
- `bl4ck4t-wiki/concepts/`
- `bl4ck4t-wiki/missions/season-03-episode-*.md`
- `bl4ck4t-wiki/drafts/season-03-episode-*.md`
- `bl4ck4t-wiki/reports/season-03-*.md`
- `content/seasons/season-03-the-escaped-experiment.md`
- `content/blogs/season-03-episode-*.md`
- [canon/continuity-timeline.md](canon/continuity-timeline.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] canon | Backfill published season canon into wiki

Ran a post-season canon extraction pass across the published Pilot, Season 1, Season 2, and Season 3 material. Added artifact pages for recurring public story objects, created the open-thread tracker and published-canon extraction workflow, and updated character, faction, location, villain, index, and log pages so future seasons can depend on what readers have actually seen.

Touched areas:

- `bl4ck4t-wiki/artifacts/`
- [canon/open-threads.md](canon/open-threads.md)
- [style-guides/published-canon-extraction-workflow.md](style-guides/published-canon-extraction-workflow.md)
- `bl4ck4t-wiki/characters/`
- `bl4ck4t-wiki/factions/`
- `bl4ck4t-wiki/locations/`
- `bl4ck4t-wiki/villains/`
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] maintenance | Enforce wiki structural consistency

Ran a same-directory structure lint pass across core wiki page types. Normalized character, concept, faction, location, and villain pages so pages of the same role carry consistent sections. Expanded `pnpm wiki:check` to enforce same-type section requirements for artifacts, characters, concepts, factions, locations, and villains, preventing future drift like missing published-season canon or inconsistent character fields.

Touched areas:

- [../tools/check_bl4ck4t_wiki.py](../tools/check_bl4ck4t_wiki.py)
- `bl4ck4t-wiki/characters/`
- `bl4ck4t-wiki/concepts/`
- `bl4ck4t-wiki/factions/`
- `bl4ck4t-wiki/locations/`
- `bl4ck4t-wiki/villains/`
- [log.md](log.md)

## [2026-05-27] canon | Backfill missing public story entities

Audited public blog posts from the pilot season through Season 3 for named BL4CK4T-world entities without wiki representation. Added missing character, faction, location, and artifact pages for recurring public canon including Ms. Vale, Mira, Rook, Mr. Olan, Row Rebels, Project Orchard, civic desks, Signal Row, Packet Market, Keylight Gate, Copy Map, and Restore Slips. Filed an entity inventory report and updated the published-canon extraction workflow so future releases require entity inventory backfill.

Touched areas:

- `bl4ck4t-wiki/characters/`
- `bl4ck4t-wiki/factions/`
- `bl4ck4t-wiki/locations/`
- `bl4ck4t-wiki/artifacts/`
- [reports/published-entity-inventory-2026-05-27.md](reports/published-entity-inventory-2026-05-27.md)
- [style-guides/published-canon-extraction-workflow.md](style-guides/published-canon-extraction-workflow.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] maintenance | Require entity creation during season import

Updated the season production workflow so new named story entities are created or updated in the wiki during the historical-documentary import stage, instead of waiting for post-release backfill. Added a dedicated import workflow covering required wiki context, entity reuse, new entity page creation, continuity updates, and completion gates. Tightened the season artifact checklist and published-canon extraction workflow to make post-release extraction a reconciliation pass rather than the primary lore creation process.

Touched areas:

- [../AGENTS.md](../AGENTS.md)
- [style-guides/historical-documentary-import-workflow.md](style-guides/historical-documentary-import-workflow.md)
- [style-guides/season-artifact-checklist.md](style-guides/season-artifact-checklist.md)
- [style-guides/published-canon-extraction-workflow.md](style-guides/published-canon-extraction-workflow.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] publish | Release Season 4: The Invisible Chase

Completed the Season 4 pipeline for The Invisible Chase. Created the Mitnick/Shimomura hacker-manhunt historical account and documentary treatment, imported the nonfiction spine into BL4CK4T story canon, added support pages for the Vanishing Caller, City Chronicle, Mirrorline Arcade, Notice Wall, Chase Map, Public Mythology, Trace Evidence, and Proportionality, created the production bible, mission packets, private draft mirrors, draft review, continuity audit, release historical-anchor analysis, public season page, and nine public blog posts. Season 4 publishes as a simultaneous drop and closes the Season 3 anonymous-caller thread while opening the Season 5 pink-envelope clue.

Touched areas:

- [sources/real-world/mitnick-shimomura-hacker-manhunt.md](sources/real-world/mitnick-shimomura-hacker-manhunt.md)
- [historical-accounts/mitnick-shimomura-hacker-manhunt.md](historical-accounts/mitnick-shimomura-hacker-manhunt.md)
- [historical-documentary-treatments/mitnick-shimomura-hacker-manhunt.md](historical-documentary-treatments/mitnick-shimomura-hacker-manhunt.md)
- [story-arcs/season-04-the-invisible-chase-arc.md](story-arcs/season-04-the-invisible-chase-arc.md)
- [production-bibles/season-04-the-invisible-chase.md](production-bibles/season-04-the-invisible-chase.md)
- `bl4ck4t-wiki/missions/season-04-*`
- `bl4ck4t-wiki/drafts/season-04-*`
- `content/blogs/season-04-*`
- [../content/seasons/season-04-the-invisible-chase.md](../content/seasons/season-04-the-invisible-chase.md)
- [canon/continuity-timeline.md](canon/continuity-timeline.md)
- [canon/open-threads.md](canon/open-threads.md)
- [index.md](index.md)
- [log.md](log.md)

## [2026-05-27] maintenance | Standardize teaching tie-ins

Normalized public season episode teaching tie-ins to a consistent five-bullet structure: Concept, Story idea, Key distinction, Defensive habit, and Season thread. Updated the article style guide and article draft template, then extended `pnpm wiki:check` so future `content/blogs/season-*-episode-*.md` files must use the same structure before publication.

Touched areas:

- `content/blogs/season-03-*`
- `content/blogs/season-04-*`
- [style-guides/article-style-guide.md](style-guides/article-style-guide.md)
- [templates/article-draft.md](templates/article-draft.md)
- [../tools/check_bl4ck4t_wiki.py](../tools/check_bl4ck4t_wiki.py)
- [log.md](log.md)

## [2026-05-27] maintenance | Create future season candidate backlog

Created a private candidate backlog for major future-season options while keeping Season 5 selected as the ILOVEYOU-inspired Love Letter Plague. Added structured briefs for WannaCry, Log4Shell, Colonial Pipeline / DarkSide, and MOVEit / CL0P, plus a reusable candidate template and backlog README. These pages are selection aids only; any selected candidate still requires the full source-first historical account, documentary treatment, import, production, drafting, validation, and publication process.

Touched areas:

- `bl4ck4t-wiki/season-candidates/`
- [index.md](index.md)
- [log.md](log.md)
