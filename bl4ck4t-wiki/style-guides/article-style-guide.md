---
type: style-guide
status: active
created: 2026-05-26
updated: 2026-05-27
tags: [style, articles, blog]
sources:
  - ../sources/blog-script-kitties-episode-1-hidden-code.md
  - ../sources/blog-keys-to-the-city.md
  - ../sources/blog-interest-of-time.md
---

# Article Style Guide

## Summary

BL4CK4T blog posts should read like short cyberpunk classroom adventures. The story comes first, but every article must carry a clear educational lesson.

## Current Voice

- Neon, playful, curious, and mission-driven.
- Beginner-friendly explanations.
- Team dialogue that makes concepts easier to understand.
- Safe technical vocabulary woven into the story, not saved only for the Teaching Tie-In.
- BL4CK4T speaks through short, memorable drops.
- The ending ties the technical concept to character, ethics, or life skills.

## Storytelling Principle

The stories should inspire curiosity rather than parent the reader. Keep dangerous operational details out of the narrative by omission and transformation, not by repeatedly warning the audience. When a cyber concept has risk, let character choices, consequences, mystery, and craft carry the meaning.

Do not nerf the mystique of hacking with constant safety reminders. Humanize the characters, preserve the art and intrigue of technical discovery, and make the story compelling enough that the lesson rides inside the plot.

## Technical Texture

Follow [Technical Texture Standard](technical-texture-standard.md) for season drafts and historically inspired articles. Fictional artifacts should make the cyber idea vivid, not replace it. Public prose should include safe terms such as logs, terminals, endpoints, services, messages, attachments, signatures, patches, updates, vulnerabilities, traffic, requests, rollback, quarantine, or incident response when they fit the story.

Write for curious teens, teachers, and adult readers who may be new to cybersecurity. Do not assume prior tool knowledge, but do not strip out ordinary technical language. A reader should be able to name the cybersecurity concept from the story before reaching the Teaching Tie-In.

## Recommended Article Structure

1. Frontmatter matching the existing Astro blog schema.
2. Title with story flavor.
3. Opening scene in Cybertropolis or a related location.
4. Bespoke narrative `###` sections that match the episode's actual scene turns.
5. A BL4CK4T prompt/drop moment, titled in language specific to that episode rather than the generic `The Drop`.
6. A first-explanation section, titled around the episode's concrete artifact, location, or pressure point rather than the generic `The Lesson Begins`.
7. A team exploration or complication section, titled around what changes in that episode rather than the generic `Trial and Error`.
8. When the episode needs a final story section, use a bespoke reflective title rather than the generic `Closing Scene`.
9. Required `Teaching Tie-In` for season episodes.
10. Optional but recommended `Behind the Signal` narrative companion for historically anchored season episodes.

Do not use formulaic in-story section titles such as `The Drop`, `The Lesson Begins`, `Trial and Error`, or `Closing Scene` in final public season episodes unless a season production bible explicitly approves the exception. The story rhythm can remain familiar, but the visible headings should feel like chapter cards from that specific episode.

## Teaching Tie-In Format

Every public season episode must end with this exact five-bullet structure:

```markdown
## Teaching Tie-In

- Concept: ...
- Story idea: ...
- Key distinction: ...
- Defensive habit: ...
- Season thread: ...
```

Use `pnpm wiki:check` to enforce this structure for `content/blogs/season-*-episode-*.md`.

## Behind The Signal Format

Historically anchored public season episodes may include a `Behind the Signal` section immediately after the Teaching Tie-In. This section explains the story behind the story in clear narrative prose. It should not use numbered lists or worksheet-style bullets.

Write this section like a short documentary companion note: two to four compact paragraphs that name the real historical anchor, explain the safe high-level mechanism or human context, and describe how the episode transformed that history into BL4CK4T-world story material. Keep operationally harmful details out by omission. The purpose is to reward curiosity, not interrupt the fiction or replace the historical account.

## Publication Rule

Draft in `bl4ck4t-wiki/drafts/` first. Promote to `content/blogs/` only after continuity review, production review, and `TROPES.md` validation. Run `pnpm tropes:check <path>` on the draft before publication review and on the final `content/blogs/` file before publishing.
