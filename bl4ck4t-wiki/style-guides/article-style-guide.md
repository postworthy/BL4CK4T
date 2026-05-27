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
- BL4CK4T speaks through short, memorable drops.
- The ending ties the technical concept to character, ethics, or life skills.

## Storytelling Principle

The stories should inspire curiosity rather than parent the reader. Keep dangerous operational details out of the narrative by omission and transformation, not by repeatedly warning the audience. When a cyber concept has risk, let character choices, consequences, mystery, and craft carry the meaning.

Do not nerf the mystique of hacking with constant safety reminders. Humanize the characters, preserve the art and intrigue of technical discovery, and make the story compelling enough that the lesson rides inside the plot.

## Recommended Article Structure

1. Frontmatter matching the existing Astro blog schema.
2. Title with story flavor.
3. Opening scene in Cybertropolis or a related location.
4. `The Drop` section with BL4CK4T's prompt.
5. `The Lesson Begins` section for first explanation.
6. `Trial and Error` section for team exploration.
7. `Closing Scene` section with reflection and final BL4CK4T message.
8. Required `Teaching Tie-In` for season episodes.

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

## Publication Rule

Draft in `bl4ck4t-wiki/drafts/` first. Promote to `content/blogs/` only after continuity review, production review, and `TROPES.md` validation. Run `pnpm tropes:check <path>` on the draft before publication review and on the final `content/blogs/` file before publishing.
