# BL4CK4T Agent Operating Instructions

This repo is the public BL4CK4T site plus a private-in-practice worldbuilding wiki that supports future blog articles. Treat `content/` as the publishable Astro site and `bl4ck4t-wiki/` as the durable canon, lore, research, and drafting layer.

## Core Rules

- Public articles are the final output. New public posts should match the current blog style: narrative-first Script Kitties stories with a clear learning payload.
- The wiki is the source of continuity. Before drafting or editing a story, read `bl4ck4t-wiki/index.md` and relevant canon, character, location, lesson, and source pages.
- Existing blog content is soft canon. Preserve established details unless the user approves a continuity revision.
- Keep real-world cybersecurity inspiration separated from public-facing fiction. Real sources may inform lessons, villain archetypes, tools, TTPs, and incidents, but public stories should transform them into BL4CK4T-world equivalents.
- Youth-safety and ethics matter. Avoid operationally harmful instructions, real target details, or step-by-step abuse paths in public stories. Frame skills around consent, defense, curiosity, and responsible disclosure.
- Draft first. Create article drafts under `bl4ck4t-wiki/drafts/` unless the user explicitly asks to publish directly into `content/blogs/`.
- Run `TROPES.md` validation before any user-facing document is published to the site. User-facing means anything in `content/blogs/`, `content/projects/`, or otherwise visible from the main site.
- Update `bl4ck4t-wiki/index.md` and `bl4ck4t-wiki/log.md` after every ingest, canon update, source filing, draft, or maintenance pass.
- Do not publish the whole wiki as site navigation unless the user explicitly asks. The site may include subtle source-level easter eggs pointing curious readers toward the idea of a hidden canon layer.

## Directory Roles

- `content/blogs/` - public blog articles.
- `content/projects/` - public project pages.
- `bl4ck4t-wiki/sources/` - source pages for existing blog/project content and future real-world inspiration.
- `bl4ck4t-wiki/historical-accounts/` - sourced historical narratives that must be completed before historically inspired season development.
- `bl4ck4t-wiki/canon/` - stable world rules, timeline, continuity, and style constraints.
- `bl4ck4t-wiki/characters/` - BL4CK4T and Script Kitties character pages.
- `bl4ck4t-wiki/factions/` - teams, crews, institutions, and recurring groups.
- `bl4ck4t-wiki/villains/` - fictional adversaries and adversary backlog.
- `bl4ck4t-wiki/locations/` - Cybertropolis and recurring places.
- `bl4ck4t-wiki/concepts/` - cybersecurity, math, ethics, and storytelling concepts.
- `bl4ck4t-wiki/lessons/` - reusable lesson plans and teaching payloads.
- `bl4ck4t-wiki/missions/` - story mission premises and drop structures.
- `bl4ck4t-wiki/story-arcs/` - multi-episode continuity.
- `bl4ck4t-wiki/production-bibles/` - season production control documents used before mission packets and drafts.
- `bl4ck4t-wiki/seasons/` - season-level arcs modeled like a streaming series.
- `bl4ck4t-wiki/style-guides/` - voice, structure, naming, and safety guides.
- `bl4ck4t-wiki/drafts/` - unpublished article drafts.
- `bl4ck4t-wiki/templates/` - page templates.

## Standard Article Workflow

1. Read `bl4ck4t-wiki/index.md`.
2. Read relevant character, location, lesson, villain, source, and style-guide pages.
3. If using real-world material, file or update a source page first.
4. Update canon, lesson, concept, villain, and location pages if the material changes the world.
5. Create a mission packet in `bl4ck4t-wiki/missions/` using the mission template.
6. Draft the story in `bl4ck4t-wiki/drafts/` using the article template.
7. Check continuity, lesson clarity, age appropriateness, and ethical framing with `bl4ck4t-wiki/style-guides/story-draft-checklist.md`.
8. Run `pnpm tropes:check bl4ck4t-wiki/drafts/<draft-file>.md` before reporting a draft ready for publication review.
9. Run `pnpm wiki:check` before publishing or reporting a draft complete.
10. When the user approves publication, create or update a markdown file under `content/blogs/`.
11. Run `pnpm tropes:check content/blogs/<post-file>.md` before considering the public article publishable.
12. Run `pnpm build` before considering the public site change done.
13. Update `bl4ck4t-wiki/index.md` and `bl4ck4t-wiki/log.md`.

## Season Workflow

1. Treat the existing three blog articles as the pilot season unless the user later asks to weave them into a larger arc.
2. Plan future content as seasons under `bl4ck4t-wiki/seasons/`.
3. Before transforming a real historical campaign into BL4CK4T story material, create a sourced historical account under `bl4ck4t-wiki/historical-accounts/`.
4. The historical account must follow `bl4ck4t-wiki/style-guides/historical-journalism-standard.md`.
5. Only after that historical account is complete may the season decompose the event into fictional villains, districts, artifacts, missions, and episode drafts.
6. Keep each season focused on one major historical lesson and one emotional growth arc for the Script Kitties.
7. Create a production bible before creating episode mission packets for a historically inspired season.
8. For Season 1 specifically, do not publish any episode until all episodes and the Season 2 cliffhanger are drafted, vetted, and approved.
9. Do not publish a season arc or production bible as public content by itself; they guide article generation.

## TROPES.md Validation

Use `TROPES.md` as a publication readability gate for all user-facing writing. Before publishing anything visible from the main site, run:

```bash
pnpm tropes:check <path-to-public-facing-markdown>
```

For full published-content validation, run:

```bash
pnpm tropes:check
```

If the checker flags a file, revise the prose before publication. Do not treat the check as a substitute for judgment: also read `TROPES.md` directly when drafting or editing final public copy.

## Log Format

Use this format in `bl4ck4t-wiki/log.md`:

```markdown
## [YYYY-MM-DD] operation | Title
```

Operations include:

- `schema`
- `ingest`
- `canon`
- `draft`
- `publish`
- `maintenance`
