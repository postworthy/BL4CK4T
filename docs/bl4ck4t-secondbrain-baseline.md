# BL4CK4T / Secondbrain Baseline

Created: 2026-05-26

This document captures the current state of the BL4CK4T project and surveys the `../secondbrain` project as the reference model for a future BL4CK4T-specific agentic workflow. It is intentionally descriptive. The next step is to decide which parts of the secondbrain approach should transfer, which should change, and which should be omitted.

## 1. BL4CK4T Current State

### Purpose and Positioning

BL4CK4T is currently an Astro-powered public website for "The Script Kitty Chronicles." Its content and metadata position it as a neon-cyberpunk cybersecurity education hub for teens, teachers, homeschoolers, STEM clubs, and cyber clubs.

The site blends:

- Narrative episodes about BL4CK4T and the Script Kitties.
- Beginner-friendly cybersecurity lessons.
- Classroom-oriented project/lab pointers.
- Search and social metadata around cryptography, networking, OSINT, OWASP, firmware basics, AI safety, CTFs, and ethical hacking.

The current repo is primarily a publishing site, not yet a knowledge-base automation system.

### Repository Shape

Top-level files and directories:

- `README.md` - currently only contains the project title.
- `package.json` - Astro/Tailwind project scripts and dependencies.
- `astro.config.mjs` - minimal Astro config with Tailwind Vite plugin.
- `content/` - TOML site configuration plus markdown blog/project content.
- `src/` - Astro layouts, pages, components, utilities, and global CSS.
- `public/` - static public assets including `robots.txt` and favicon.
- `images/` - image directory exists, but the inspected site content mostly references remote `https://bl4ck4t.com/...` image URLs.
- `CNAME` - custom domain configuration for `bl4ck4t.com`.
- `LICENSE.md` - license file.

Measured project size at inspection:

- 4 markdown content files under `content/`.
- 24 source files under `src/`.
- Clean git worktree at the start of this survey.

### Technology Stack

Runtime and build tooling:

- Astro `^5.10.1`.
- Tailwind CSS `^4.1.11`.
- `@tailwindcss/typography`.
- TOML parsing via `toml`.
- Package manager locked to `pnpm@10.6.0`.

Available scripts:

- `pnpm dev` -> `astro dev`.
- `pnpm build` -> `astro build`.
- `pnpm preview` -> `astro preview`.
- `pnpm astro` -> `astro`.
- `preinstall` enforces pnpm through `npx only-allow pnpm`.

There are no project-specific automation scripts, ingest scripts, lint scripts, source discovery tools, agent instructions, or knowledge-base maintenance utilities yet.

### Site Configuration

The site uses `content/configuration.toml` as its central content/config source. Astro loads this through the `configuration` content collection using a TOML parser.

Important configuration areas:

- `site.baseUrl` is `https://bl4ck4t.com`.
- `globalMeta`, `blogMeta`, `projectMeta`, and `notFoundMeta` drive SEO, Open Graph, Twitter card, and page metadata.
- `hero` controls the homepage hero title, subtitle, image, CTA text, and CTA URL.
- `personal` includes BL4CK4T social/profile links.
- `texts` controls common UI labels such as Articles, Projects, View All, and empty states.
- `menu` currently exposes `home`, `projects`, and `blog`.

The schema comment in `src/content.config.ts` notes that Astro's inference required prefixed TOML keys, but the loaded data is exposed to the app as normal keys.

### Content Model

The site defines three Astro content collections:

- `configuration` - file loader for `content/configuration.toml`.
- `blog` - markdown files from `content/blogs`.
- `project` - markdown files from `content/projects`.

Blog frontmatter supports:

- `title`
- `slug` optional, generated from title if absent
- `description`
- `longDescription`
- `cardImage`
- `tags`
- `readTime`
- `featured`
- `timestamp`

Project frontmatter supports:

- `title`
- `slug` optional, generated from title if absent
- `description`
- `longDescription`
- `cardImage`
- `tags`
- `githubUrl`
- `liveDemoUrl`
- `timestamp`
- `featured`

Current content:

- `content/blogs/script-kitties-episode-1-hidden-code.md`
  - Caesar cipher pilot episode.
  - Teaches shift ciphers, pattern spotting, trial and error, teamwork, and verification.
- `content/blogs/crypto_key_chapter.md`
  - Public/private cryptography and Diffie-Hellman story chapter.
  - Teaches asymmetric encryption, key exchange, signatures, and HTTPS relevance.
- `content/blogs/compound_interest_lesson.md`
  - Compound-interest story chapter.
  - Expands beyond cybersecurity into math and financial literacy.
- `content/projects/classoverride.md`
  - Project page for the ClassOverride teaching repo.
  - Describes notebook-first labs for cryptography, compound interest, adversarial prompting, Wargames-style exercises, Nmap, and OWASP Juice Shop.

All current content is user-facing publication content. There is not yet a separation between raw source material, durable wiki pages, editorial drafts, lesson plans, maps, or agent logs.

### Application Routes

Primary routes:

- `/` - homepage with hero, featured projects, and featured articles.
- `/blog` - chronological blog index.
- `/blog/[id]` - static blog detail pages keyed by slug.
- `/projects` - chronological project index.
- `/projects/[id]` - static project detail pages keyed by slug.
- `/404` - not-found page.

Routing is simple and content-driven. There is no private admin surface, feed reader, raw ingest area, internal wiki route, or agent-facing dashboard.

### Layouts and Components

Important layout files:

- `src/layouts/Layout.astro`
  - Shared document shell.
  - Loads global CSS.
  - Adds Google Analytics tag `G-CMBBG0K2PD`.
  - Loads IBM Plex Mono from Bunny Fonts.
  - Handles dark/light theme initialization before render.
  - Renders `Header`, page `slot`, and `Footer`.
- `src/layouts/BlogLayout.astro`
  - Adds article metadata tags.
  - Renders title, date, read time, prose body, and BL4CK4T sign-off.
- `src/layouts/ProjectLayout.astro`
  - Adds project metadata tags.
  - Renders title, tags, GitHub/Demo links, and prose body.

Component layer:

- `Header.astro`, `Footer.astro`, and `ThemeToggle.astro` provide site chrome.
- `Hero.astro`, `FeaturedArticles.astro`, and `FeaturedProjects.astro` compose the homepage.
- `ArticleSnippet.astro` and `ProjectSnippet.astro` render list entries.
- `Prose.astro` handles article/project body styling.
- `common/Anchor.astro` and `common/Section.astro` provide small shared primitives.

### Visual System

The CSS is a retro/hacker-styled Tailwind setup:

- Monospace base font: IBM Plex Mono.
- Display font: Press Start 2P.
- Serif font: Literata.
- Light/dark theme variables based on neutral colors and emerald accents.
- Custom `zag-*` utility classes for background, text, muted text, borders, transitions, dotted hover grid, and theme inversion.

The site inherits "Zaggonaut" theme language in comments and schema defaults, but the visible configuration and content have been rebranded around BL4CK4T.

### Current Operational Gaps

Relative to the desired secondbrain-style workflow, BL4CK4T currently lacks:

- Agent operating instructions such as `AGENTS.md`.
- A `raw/` area for immutable inputs.
- A `wiki/` or internal knowledge layer.
- Templates for internal source, concept, entity, query, map, daily, or lesson pages.
- A process log like `log.md`.
- A content index like `index.md`.
- Source ingestion tools.
- Cross-linking, correlation, or vector tooling.
- Feed discovery or article discovery.
- Daily brief generation.
- Explicit distinction between user-facing publication content and internal research/knowledge content.
- Commit discipline around workflow operations.
- A companion app or capture inbox.
- Validation scripts beyond the normal Astro build.

This makes BL4CK4T a good candidate for a tailored version of the secondbrain operating model, but the model should not be copied blindly because this repo is a public curriculum/story site rather than a private general-purpose knowledge base.

## 2. Secondbrain Project Survey

### Purpose

`../secondbrain` is an established personal knowledge base maintained by an LLM agent. It is designed to compound over time: raw inputs are preserved, durable wiki pages are synthesized, pages are connected, and recurring discovery processes find new material that matches the user's interests.

The central operating pattern:

1. Immutable source material goes into `raw/`.
2. The LLM ingests one or more sources.
3. The LLM writes or updates structured markdown pages in `wiki/`.
4. The LLM lints the wiki, draws connections, discovers feeds when URLs are involved, updates indexes/logs, and records work.
5. The LLM commits each completed ingest or maintenance pass with a descriptive git commit.

The repository is meant to be browsed in Obsidian and versioned with git. Humans curate sources and ask questions; the LLM maintains summaries, cross-references, filing, and upkeep.

### Repository Scale and Layout

Measured project size at inspection:

- 1874 markdown files under `wiki/`.
- 584 files under `raw/`.
- 22 tool files under `tools/`.

Top-level files and directories:

- `README.md` - overview and common workflows.
- `AGENTS.md` - detailed operating contract for LLM agents.
- `index.md` - content-oriented catalog read first for answering/planning.
- `log.md` - append-only chronological operations log.
- `templates/` - page skeletons.
- `raw/` - immutable source material and input snapshots.
- `wiki/` - LLM-owned durable markdown knowledge base.
- `tools/` - helper scripts for ingest, discovery, correlation, vectors, linting, and cron.
- `apps/` - companion applications and services.
- `.var/` - runtime caches/logs/locks used by tools; not treated as committed knowledge.

The inspected secondbrain worktree had uncommitted user/project changes in `.gitignore`, `README.md`, `.obsidian/`, `apps/secondbrain-ios/`, `raw/inbox/`, `raw/interactions/`, and `wiki/.obsidian/`. Those were only observed, not modified.

### Directory Roles

Raw source areas:

- `raw/articles/` - queued or clipped articles.
- `raw/assets/` - downloaded images and attachments.
- `raw/books/` - book sources.
- `raw/github-awesome-repos/` - repository data discovered from awesome/list repos.
- `raw/github-readmes/` - fetched GitHub README snapshots.
- `raw/github-stars/` - GitHub starred repository exports in markdown, JSON, and TSV.
- `raw/hackernews/` - immutable HN API snapshots.
- `raw/inbox/` - companion/mobile user-supplied captures.
- `raw/interactions/` - companion reader preference events.
- `raw/notes/` - user notes and link collections.
- `raw/papers/` - papers.
- `raw/transcripts/` - transcripts.

Wiki areas:

- `wiki/sources/` - one page per ingested source.
- `wiki/sources/articles/` - article source pages.
- `wiki/sources/github-awesome-repos/` - repos discovered from catalog/awesome repos.
- `wiki/sources/github-stars/` - GitHub starred repository source pages.
- `wiki/sources/links/` - imported URL/link collection pages.
- `wiki/entities/` - people, organizations, products, projects, places, and institutions.
- `wiki/concepts/` - reusable ideas, themes, methods, patterns, and questions.
- `wiki/syntheses/` - higher-level summaries and evolving interpretations.
- `wiki/queries/` - durable answers, reports, and analyses.
- `wiki/queries/correlation-reports/` - lexical/cross-source correlation reports.
- `wiki/queries/feed-discovery/` - feed discovery reports.
- `wiki/queries/feed-hunts/` - RSS/Atom candidate queues and reports.
- `wiki/queries/hackernews-hunts/` - Hacker News candidate queues and reports.
- `wiki/queries/lint-reports/` - lint and maintenance reports.
- `wiki/queries/vector-reports/` - vector similarity reports.
- `wiki/maps/` - navigation pages, topic hubs, registries, and reading trails.
- `wiki/daily/` - daily information briefs.
- `wiki/daily/assets/` - local daily brief images.

### Core Agent Rules

The operating contract in `AGENTS.md` is the heart of the project. Key rules:

- Raw sources are immutable unless the user explicitly asks otherwise.
- `wiki/` is LLM-owned; the agent may create, revise, split, merge, and cross-link pages there.
- Durable claims should preserve provenance through source pages, raw paths, or wiki pages that carry provenance.
- Internal links prefer Obsidian-style wikilinks.
- Pages should be concise syntheses, not chat transcripts.
- `index.md` and `log.md` are updated after every ingest, filed query, or maintenance pass.
- Every raw-source ingest must be followed by lint, correlation, URL/feed discovery when relevant, and a descriptive git commit.
- Citations must not be fabricated; inferred claims must be labeled as inferences.
- Conflicts are preserved in `Contradictions / Tensions` rather than erased.
- ASCII filenames are preferred where practical, with descriptive title case page names.

### Page Conventions

Common frontmatter:

```yaml
---
type: concept
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: []
---
```

Common statuses:

- `seed` - newly created and incomplete.
- `active` - useful and maintained.
- `needs-review` - requires human review.
- `superseded` - kept for history but no longer current.

Common sections:

- `Summary`
- `Key Points`
- `Evidence`
- `Related`
- `Contradictions / Tensions`
- `Open Questions`
- `Maintenance Notes`

Templates exist for:

- `templates/source.md`
- `templates/concept.md`
- `templates/entity.md`
- `templates/query.md`
- `templates/daily-digest.md`

### Index and Log

`index.md` is the first file agents are expected to read when answering questions or planning ingests. It is organized by content category and includes one-line descriptions for pages.

Current index sections include:

- Maps
- Syntheses
- Concepts
- Entities
- Queries
- Lint and maintenance reports
- Daily digests
- Sources
- Hacker News editorial pages
- Auto-promoted article pages

`log.md` is append-only and uses parseable headings:

```markdown
## [YYYY-MM-DD] operation | Title
```

Operation names include:

- `ingest`
- `query`
- `lint`
- `maintenance`
- `schema`

Log entries summarize what happened and link to touched pages.

### Main Workflows

#### Ingest Workflow

For a source in `raw/`, the agent:

1. Identifies the raw source path.
2. Reads the source enough to extract durable knowledge.
3. Checks `index.md` for related pages.
4. Creates a source page under `wiki/sources/`.
5. Updates or creates relevant entity, concept, map, and synthesis pages.
6. Adds bidirectional links.
7. Notes contradictions, uncertainty, and open questions.
8. Runs a wiki lint pass.
9. Runs a correlation pass.
10. Runs feed discovery if URLs are involved.
11. Updates `index.md`.
12. Appends a log entry.
13. Reviews the git diff.
14. Commits with a descriptive message.
15. Reports changes, connections, feeds, unresolved issues, and commit hash.

#### Query Workflow

For questions against the wiki, the agent:

1. Reads `index.md` first.
2. Searches or inspects relevant wiki pages.
3. Consults raw sources only when provenance/detail is needed.
4. Answers with citations to wiki pages and raw sources when useful.
5. Files durable answers under `wiki/queries/` or `wiki/syntheses/` when requested or warranted.
6. Updates `index.md` and `log.md` if a durable page is filed.

#### Lint Workflow

Linting checks:

- Broken links.
- Orphan pages.
- Stale claims.
- Contradictions.
- Duplicate pages.
- Missing index entries.
- Pages without provenance.
- Repeated concepts/entities that deserve pages.

When changes are made or a durable report is filed, `log.md` is updated.

#### Correlation Workflow

Correlation is what turns source summaries into compounding knowledge:

- Search `index.md` and the existing wiki for related pages.
- Compare new material against concepts, entities, maps, syntheses, and queries.
- Add useful links.
- Strengthen existing pages with source-backed points.
- Mark weak/speculative connections explicitly.
- Prefer updating existing syntheses over creating parallel overlapping pages.

#### Feed Discovery Workflow

After URL ingests, the agent:

- Checks HTML alternate links and common feed paths.
- Applies service-specific feed patterns for Substack, Medium, GitHub, Blogspot, arXiv, and similar sources.
- Validates RSS, Atom, RDF, or JSON Feed candidates.
- Updates `wiki/maps/RSS and Atom Feed Discovery.md`.
- Updates `wiki/maps/rss_feed_candidates.tsv`.
- Updates `wiki/maps/feed_registry_seed.tsv`.
- Marks new feeds as `candidate` unless approved for polling.

#### New Content Discovery Workflow

For broad discovery, the agent runs a full discovery-to-digest loop:

1. Check raw drop locations.
2. Fetch GitHub stars for `postworthy`.
3. Run RSS/Atom/JSON feed article hunting.
4. Run Hacker News hunting.
5. Score candidate queues with lexical and vector correlation.
6. Apply promotion policy.
7. Save promoted candidates into `raw/articles/`.
8. Run normal ingest.
9. Discover feeds from new URLs.
10. Run correlation and hub updates.
11. Identify hub gaps.
12. Run lint.
13. Maintain the daily brief.
14. Update index/log, review diff, commit.
15. Report what was checked, filed, skipped, surfaced, discovered, changed, and committed.

### Promotion Policy and Preference Classes

The project distinguishes source evidence classes:

- First-class evidence:
  - User-supplied raw drops.
  - Original second-brain link collection.
  - GitHub stars.
  - README-derived GitHub-star pages.
  - Daily-brief items explicitly liked through the companion reader.
- Second-class evidence:
  - RSS/Atom discovery stream.
  - Hacker News discovery stream.
  - Already auto-ingested discovery-stream items.

Current vector promotion policy:

- First-class strongest evidence can auto-ingest around `0.750` vector threshold, assuming no duplicate/noise issue.
- Second-class-only evidence uses a stricter gate around `0.880` plus at least `3` above-threshold connections unless the user approves otherwise.
- Near-misses around `0.750` with at least `1` strong connection can appear in a daily watchlist, not as source pages.

This policy is important because it prevents automated discovery streams from recursively amplifying themselves too aggressively.

### Daily Information Brief

Daily briefs live in `wiki/daily/YYYY-MM-DD.md` and use `templates/daily-digest.md`.

The daily brief is reader-facing and should sound like an information brief, not an internal process log. It avoids words like ingest, candidate, promotion, lint, or workflow in reader-facing sections.

Required sections:

- `Executive Summary`
- `Featured Articles`
- `Also Important`
- `Near Miss Watchlist`
- `Complete Reading List`
- `Knowledge Base Updates`
- `Connections To Follow`
- `Source Monitoring Notes`
- `Collection Notes`

Important rules:

- Update one daily page throughout the day.
- Aim for at least 25 reader-visible items by 16:00 local time when enough material exists.
- Primary item links point to original external URLs, not source-page links.
- Featured items require local images under `wiki/daily/assets/YYYY-MM-DD/`.
- If no source image is usable, generated images may be created and captioned as generated.
- Back-matter can link to source pages, reports, maps, and workflow artifacts.

### GitHub Stars Workflow

GitHub stars are treated as durable interest signals:

- `tools/fetch_github_stars.py USERNAME` exports public starred repositories.
- Outputs go under `raw/github-stars/` as markdown, JSON, and TSV.
- `starred_at` timestamps are preserved when available.
- Repositories are not automatically source pages unless asked.
- `tools/ingest_github_stars.py` can create one source page per repository and update the GitHub Stars map, index, and log.
- Promoted repos can lead to deeper project/entity pages and follow-up sources such as releases, tags, README, docs, issues, and Atom feeds.

The current secondbrain has used this workflow heavily, including GitHub README ingestion and expansion through awesome/list-style repositories.

### RSS/Atom and Hacker News Hunting

Feed hunting:

- `tools/hunt_feed_articles.py` reads the feed registry and writes candidates under `wiki/queries/feed-hunts/`.
- `tools/wiki_correlations.py` compares candidates to existing source pages and writes promotion reports.
- Candidates above the threshold can be promoted into `raw/articles/`.
- Obvious duplicates, comment feeds, release-note churn, vendor fluff, and transient news are filtered.

Hacker News hunting:

- `tools/hunt_hackernews.py` stores raw API snapshots under `raw/hackernews/`.
- Queue reports go under `wiki/queries/hackernews-hunts/`.
- Vector and lexical correlation inform promotion.
- HN is also treated as an editorial discovery surface, so durable technical posts may be promoted even below strict vector gate.
- Job posts, transient drama, generic chatter, thin links, duplicates, and off-topic high-score items are filtered.

### Vector Embedding Workflow

Vector tooling adds semantic similarity:

- `tools/embed_wiki.py` embeds wiki markdown pages with Gemini Embedding 2.
- Embeddings live locally under `.var/embeddings/` and are not committed.
- Default model is `gemini-embedding-2` at 768 dimensions.
- `tools/vector_correlations.py` creates reports and scores candidates.
- Candidate page fetches are cached under `.var/candidate-fetches/`.
- Candidate embeddings are cached in SQLite.
- Vector scores are evidence, not authority.
- Template-heavy pages can inflate similarity and require review.

The project explicitly notes provider quota handling and local cache behavior.

### Duplicate Consolidation

Duplicate/parallel pages are not deleted. Instead:

- The non-canonical page becomes a redirect-style page.
- It uses `type: redirect` and `status: superseded`.
- It preserves former path, source path, URL, vector score, reason, and date.
- The canonical page receives a `Consolidated Pages` section.
- Similar but distinct companion projects, SDKs, samples, series posts, and implementation families remain separate and are cross-linked.

### Tooling Inventory

Current tools:

- `tools/apply_vector_connection_pass.py` - applies conservative vector-discovered links.
- `tools/check_wiki_links.py` - checks Obsidian wikilinks under `wiki/`.
- `tools/consolidate_vector_duplicates.py` - creates redirect-style duplicate consolidations.
- `tools/discover_feeds.py` - discovers RSS/Atom feeds associated with URL source pages.
- `tools/discover_source_feeds.py` - discovers feeds for source pages without feed coverage.
- `tools/embed_wiki.py` - embeds wiki markdown pages with Gemini Embedding 2 and local cache.
- `tools/enrich_daily_digest_images.py` - downloads header images for featured daily items.
- `tools/fetch_github_stars.py` - exports GitHub starred repositories.
- `tools/github_stars_second_pass.py` - runs post-ingest maintenance for GitHub stars.
- `tools/hunt_feed_articles.py` - finds feed articles for review.
- `tools/hunt_hackernews.py` - finds Hacker News items for review.
- `tools/ingest_article_queue.py` - ingests queued article URLs from `raw/articles/`.
- `tools/ingest_awesome_repo_links.py` - ingests repos linked from starred awesome/list repos.
- `tools/ingest_github_readmes.py` - fetches and summarizes README files for starred repos.
- `tools/ingest_github_stars.py` - ingests GitHub stars export into wiki pages.
- `tools/ingest_link_collection.py` - ingests a delimited link collection into source pages.
- `tools/resolve_source_open_questions.py` - replaces generic hub questions with concrete correlations.
- `tools/vector_correlations.py` - generates vector similarity reports from the embedding cache.
- `tools/wiki_correlations.py` - measures article-to-wiki lexical correlations.
- `tools/enable_codex_bwrap_sandbox.sh` - configures Ubuntu/bubblewrap support for Codex sandboxing.
- `tools/run_codex_ingest_cron.sh` - scheduled ingest wrapper.

### Scheduled Ingest

`tools/run_codex_ingest_cron.sh` runs the full workflow non-interactively.

Behavior:

- Uses `SECOND_BRAIN_REPO_DIR` or defaults to `/home/landon/code/secondbrain`.
- Loads `.env` if present.
- Takes a lock under `.var/locks/`.
- Writes logs under `.var/logs/codex-ingest/`.
- Asks Codex to run the full `AGENTS.md` workflow through validation and commit.

The README includes a crontab example running every four hours.

### Companion App Layer

The companion app layer lives under `apps/` and is separate from the wiki content.

`apps/secondbrain-companion/`:

- Python service serving the daily brief as a mobile reader.
- Reads from `wiki/daily/`.
- Serves images from `wiki/daily/assets/`.
- Writes mobile share captures to `raw/inbox/mobile-shares/YYYY-MM-DD.jsonl`.
- Writes reader interactions to `raw/interactions/YYYY-MM-DD.jsonl`.
- Does not create or edit wiki pages.
- Intended for private LAN or Tailscale use without an API token.

Endpoints:

- `GET /health`
- `GET /api/briefs`
- `GET /api/briefs/today`
- `GET /api/briefs/YYYY-MM-DD`
- `POST /api/captures`
- `POST /api/interactions`

`apps/secondbrain-ios/`:

- SwiftUI shell around a `WKWebView` for the local companion reader.
- Share Extension posts captured URLs, selected text, notes, and tags to `/api/captures`.
- Captures are written as first-class raw inputs.

Reader feedback:

- `like` events are explicit first-class positive interest evidence.
- `dislike` events are negative preference samples and do not rewrite history.
- `open` and `impression` are weaker behavioral signals.

### Knowledge Hubs and Current Topic Shape

The current secondbrain index contains many hub maps. Examples include:

- AI Model Training and Reasoning.
- AI Agents and Coding Tools.
- AI Safety, Jailbreaks, and Model Misuse.
- Vulnerability Research and Exploit Chains.
- Systems Programming and Infrastructure.
- Computer Vision and Generative Media.
- Networks, Privacy, and the Open Web.
- Career, Engineering Culture, and Personal Knowledge.
- Security Research Tooling and Labs.
- Agent Security and Sandboxing.
- Browser Automation and Web Agents.
- Local AI Inference and Model Serving.
- Developer Platform Supply Chain Incidents.
- World Models and Simulated Environments.

The hubs have evolved from imported link collections, GitHub stars, repository READMEs, RSS/Atom feeds, Hacker News, vector reports, and daily curation.

### Notable Historical Evolution

The log shows a rapid progression:

- Initialize wiki project and operating rules.
- Ingest a large second-brain link collection.
- Create topic hubs.
- Discover RSS/Atom feeds.
- Add feed article hunting and correlation gates.
- Add GitHub stars as interest signals.
- Ingest starred repos and READMEs.
- Expand through awesome/list repos.
- Add Hacker News discovery.
- Add Gemini embedding and vector promotion.
- Add duplicate consolidation.
- Add daily brief workflow.
- Add companion reader and mobile capture/feedback loops.

The important pattern is that automation was not just added as scripts. Each new capability became part of the operating contract, index, log, maps, reports, and commit workflow.

## 3. Transfer-Relevant Observations for BL4CK4T

These are observations to support the next conversation, not final recommendations.

### What Directly Transfers

- Immutable raw source storage.
- Agent instructions that define ownership boundaries.
- Structured internal wiki pages.
- Templates for source, concept, entity, query, map, and synthesis pages.
- Index-first retrieval.
- Append-only operation log.
- Ingest -> lint -> correlation -> index/log -> commit discipline.
- Feed discovery for curriculum-relevant sites.
- GitHub repository interest tracking for ClassOverride and related teaching/security repos.
- A daily or periodic brief concept.
- Companion capture inbox for mobile/web finds.
- Preference signals from likes/dislikes.

### What Likely Needs BL4CK4T-Specific Adaptation

- The public Astro site should remain separate from internal raw/wiki material.
- BL4CK4T needs curriculum/story production workflows, not only general knowledge ingestion.
- The project likely needs lesson/curriculum-specific page types in addition to generic source/concept/entity pages.
- Promotion thresholds should reflect educational usefulness, age appropriateness, classroom safety, and ethical hacking boundaries.
- Daily briefs may need to become editorial/curriculum briefs, drop planning briefs, or teacher-resource briefs.
- The content pipeline should probably include source-to-lesson, source-to-story, and source-to-lab transformations.
- Safety review should be stronger than in a personal second brain because BL4CK4T is aimed at younger learners and cybersecurity topics.
- Public publication steps need validation against Astro content schemas and site build, not only wiki link checks.

### Questions For The Next Step

- Should BL4CK4T have a private internal wiki inside this repo, or should it keep internal workflow artifacts outside the public site repo?
- What raw inputs matter most: articles, GitHub repos, ClassOverride notebooks, student questions, teaching notes, standards, threat reports, tool docs, or story ideas?
- What should a durable BL4CK4T knowledge page represent: a source, lesson, character, story arc, lab, skill, concept, teacher guide, CTF challenge, or project?
- Should the workflow generate public blog drafts automatically, or only prepare internal research packets for human approval?
- What level of autonomy should agents have to edit `content/blogs` and `content/projects`?
- Should there be a daily brief, weekly curriculum digest, or per-drop planning brief?
- What safety gates are required before cybersecurity content becomes public-facing youth curriculum?
- Should ClassOverride be treated as a related external source, a subproject knowledge source, or the central lab corpus?
- How should images/assets be handled: generated locally, stored under `public/`, tracked in a raw asset library, or referenced remotely?
- What counts as "done" for a BL4CK4T agentic workflow operation: internal notes updated, public page drafted, build passing, commit created, or deployment-ready?
