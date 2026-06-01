---
type: audit
status: complete
created: 2026-06-01
updated: 2026-06-01
tags: [field-guide, nist, standards-alignment, public-episodes, audit]
sources:
  - ../canon/cyber-habit-standards-alignment.md
  - ../style-guides/story-draft-checklist.md
  - ../../content/blogs/season-01-episode-01-sound-beneath-signal-row.md
  - ../../content/blogs/season-02-episode-08-investigators-case.md
  - ../../content/blogs/season-03-episode-09-first-bell.md
  - ../../content/blogs/season-04-episode-06-chase-map.md
  - ../../content/blogs/season-05-episode-07-warning-that-worked.md
  - ../../content/blogs/season-06-episode-05-we-do-not-know-yet.md
  - ../../content/blogs/season-07-episode-09-patch-bell.md
---

# Field Guide Habit Alignment Audit

## Purpose

This audit checks published Season 1-7 episodes against the standards-backed BL4CK4T Field Guide habits in [Cyber Habit Standards Alignment](../canon/cyber-habit-standards-alignment.md). It does not rewrite public episodes. It identifies where the stories already teach the habits and where a future consistency pass could make the habit language clearer.

## Summary Judgment

The seasons already align strongly with the new Field Guide habits. Most episodes teach the right defender behavior through story action before naming it, which matches the canon rule for keeping public fiction approachable.

The main consistency gap was language, not substance. Teaching Tie-Ins previously used the older line label `Defensive habit:` and many episode pages described excellent behavior without explicitly naming the new Field Guide habit. That gap has now been addressed with a concise linked `Field Guide habit:` line in each public season episode and a primary Field Guide tie-in on each public season page.

## Field Guide Habits

1. Know what you protect.
2. Guard the trusted paths.
3. Watch for strange signals.
4. Keep evidence before story.
5. Report early, kindly, and clearly.
6. Recover with consent and care.
7. Improve the city after the case.

## Season-Level Alignment

| Season | Primary habit | Secondary habits | Consistency opportunity |
| --- | --- | --- | --- |
| Season 1: The Singing Network | Guard the trusted paths | Watch for strange signals; Keep evidence before story | Make the Hushline the season's clearest Field Guide artifact for trusted message and command paths. |
| Season 2: The Seventy-Five Cent Thread | Keep evidence before story | Watch for strange signals; Report early, kindly, and clearly | Standardize Threadboard language around facts, theories, ruled-out ideas, unknowns, and requested action. |
| Season 3: The Escaped Experiment | Recover with consent and care | Know what you protect; Improve the city after the case | Tie sandbox boundaries, affected rooms, restore slips, and First Bell Desk to the habit sequence. |
| Season 4: The Invisible Chase | Keep evidence before story | Report early, kindly, and clearly; Improve the city after the case | Use Chase Map language as the season's strongest Field Guide anchor. |
| Season 5: The Love Letter Plague | Report early, kindly, and clearly | Guard the trusted paths; Recover with consent and care | Tie Quarantine Tray and Message Office lanes to trusted paths and shame-free reporting. |
| Season 6: The Day The City Would Not Answer | Know what you protect | Watch for strange signals; Improve the city after the case | Connect Service Map and Status Wall more explicitly to knowing what services and people need protection. |
| Season 7: The Patch Bell War | Recover with consent and care | Guard the trusted paths; Improve the city after the case | Keep Patch Bell, Repair Lane, and Consent Ledger as direct product/University alignment anchors. |

## Episode Mapping

| Episode range | Strongest habit alignment | Notes for future revision |
| --- | --- | --- |
| Season 1 Episodes 1-3 | Watch for strange signals; Keep evidence before story | The opening episodes already emphasize observation, old marks, and rumor sorting. Add Field Guide habit labels without making the prose feel procedural. |
| Season 1 Episodes 4-8 | Guard the trusted paths | Crunch Charm, Tonebox, false closure, and Hushline all point toward trusted path separation. Use "trusted paths" language in Teaching Tie-Ins. |
| Season 1 Episode 9 | Improve the city after the case | The listening exhibit and `-0.75` bridge already show improvement plus new detection. |
| Season 2 Episodes 1-4 | Watch for strange signals; Keep evidence before story | Strong alignment through small mismatch, normal logs, borrowed door, and Threadboard. |
| Season 2 Episodes 5-8 | Report early, kindly, and clearly; Keep evidence before story | Glass Bureau and Investigator's Case are ideal for reporting and requested-action language. |
| Season 2 Episode 9 | Improve the city after the case | The new report form and evidence channel are already Field Guide-ready. |
| Season 3 Episodes 1-3 | Watch for strange signals; Guard the trusted paths | Unexpected marker, sandbox boundaries, and old trust paths map cleanly to Detect and Protect. |
| Season 3 Episodes 4-6 | Know what you protect; Report early, kindly, and clearly | Affected rooms, people-first scope, Copy Map, and Bell Desk make impact and coordination visible. |
| Season 3 Episodes 7-9 | Recover with consent and care; Improve the city after the case | Builder's Note, Restore Slips, and First Bell Desk are strong Recover and Improve anchors. |
| Season 4 Episodes 1-3 | Keep evidence before story | Monster Word, Notice Wall, and Shadow's Trace already separate labels, claims, and traces. |
| Season 4 Episodes 4-7 | Guard the trusted paths; Keep evidence before story | Borrowed Voice adds verification context; Chase Map and Wrong Poster protect against accusation. |
| Season 4 Episodes 8-9 | Recover with consent and care; Improve the city after the case | Accountability, corrected public record, and identity-claim process already support the habit language. |
| Season 5 Episodes 1-4 | Guard the trusted paths; Watch for strange signals | Pink Envelope, familiar sender, Quarantine Tray, and Hidden Ending all teach message-path caution. |
| Season 5 Episodes 5-7 | Report early, kindly, and clearly | Address Book Bloom, Quarantine Tray, and Warning That Worked are the strongest current reporting-culture examples. |
| Season 5 Episodes 8-9 | Recover with consent and care; Improve the city after the case | The season closes with reporting, quarantine, verification, and contact-warning habits ready for product reuse. |
| Season 6 Episodes 1-4 | Know what you protect | Clinic board, blank receipts, Queue District, and Service Map all build the protection scope. |
| Season 6 Episodes 5-8 | Report early, kindly, and clearly; Guard the trusted paths | Status Wall, Outside Gate, Flood Prince, and Priority Lanes show honest updates, claims discipline, and reviewed limits. |
| Season 6 Episode 9 | Improve the city after the case | Keeps Status Wall, Service Map reviews, priority lanes, and fallback desk drills. |
| Season 7 Episodes 1-4 | Know what you protect; Guard the trusted paths | Runtime list, owner gaps, exposed systems, and desk terminals show inventory and trusted repair paths. |
| Season 7 Episodes 5-8 | Recover with consent and care | Repair Lane, Helpful Ghost, bounded evidence, and Consent Ledger are the strongest standards-aligned recovery material. |
| Season 7 Episode 9 | Improve the city after the case | Patch Bell turns one crisis into durable maintenance governance. |

## Implemented Consistency Pass

Public episodes now use a small, repeatable Teaching Tie-In addition:

```markdown
- Field Guide habit: Keep evidence before story. Public link: `/field-guide`.
```

Do not replace the story-specific `Defensive habit:` line unless the replacement reads naturally. The best pattern is:

- `Concept:` names the technical or security concept.
- `Story idea:` names the fictional transformation.
- `Key distinction:` preserves the lesson edge.
- `Field Guide habit:` names one of the seven habits.
- `Defensive habit:` gives the concrete action the Script Kitties practiced.
- `Season thread:` preserves continuity.

## Remaining Priority Improvements

1. Keep the habit wording exact across public pages, social posts, product briefs, and University modules.
2. Preserve public voice: do not mention NIST, CISA, or CIS inside the story body unless the page is explicitly educator/enterprise-facing.
3. Create derivative product notes that map each case deck, classroom resource, and University module to the habit and standards root.
4. Use analytics to determine whether season and episode Field Guide links drive meaningful guide traffic.

## High-Value Product Hooks

- Hushline: Guard the trusted paths.
- Threadboard: Keep evidence before story.
- First Bell Desk: Report early, kindly, and clearly.
- Chase Map: Keep evidence before story.
- Quarantine Tray: Guard the trusted paths.
- Status Wall: Report early, kindly, and clearly.
- Service Map: Know what you protect.
- Repair Lane: Guard the trusted paths.
- Consent Ledger: Recover with consent and care.
- Patch Bell: Improve the city after the case.

## Residual Risk

Low. The published episodes already contain the behavior the habits require. The risk is brand-language drift: older phrases such as `defensive habit`, `availability is part of trust`, and `maintenance is part of trust` remain useful, but future marketing and product work should consistently route them back to the seven Field Guide habits.
