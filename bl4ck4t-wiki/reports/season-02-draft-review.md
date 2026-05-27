---
type: report
status: complete
created: 2026-05-27
updated: 2026-05-27
tags: [season-2, review, continuity, historical-anchor, drafts]
sources:
  - ../historical-accounts/cuckoos-egg-hanover-hackers.md
  - ../historical-documentary-treatments/cuckoos-egg-hanover-hackers.md
  - ../story-arcs/season-02-the-seventy-five-cent-thread-arc.md
  - ../production-bibles/season-02-the-seventy-five-cent-thread.md
---

# Season 2 Draft Review: The Seventy-Five Cent Thread

## Review Scope

This report reviews the complete private Season 2 draft set before promotion to public blog files. It checks the nine mission packets and nine article drafts against the historical account, documentary treatment, story arc, and production bible.

Reviewed draft files:

- [Episode 1: The Seventy-Five Cent Thread](../drafts/season-02-episode-01-seventy-five-cent-thread.md)
- [Episode 2: The Ledger Lab](../drafts/season-02-episode-02-ledger-lab.md)
- [Episode 3: The Borrowed Door](../drafts/season-02-episode-03-borrowed-door.md)
- [Episode 4: The Threadboard](../drafts/season-02-episode-04-threadboard.md)
- [Episode 5: Nobody Owns The Thread](../drafts/season-02-episode-05-nobody-owns-thread.md)
- [Episode 6: Old Trust Paths](../drafts/season-02-episode-06-old-trust-paths.md)
- [Episode 7: The Far Relay](../drafts/season-02-episode-07-far-relay.md)
- [Episode 8: The Investigator's Case](../drafts/season-02-episode-08-investigators-case.md)
- [Episode 9: What The Records Changed](../drafts/season-02-episode-09-records-changed.md)

## Historical Anchor Mapping

| Historical / documentary movement | Season 2 transformation | Draft coverage | Review result |
| --- | --- | --- | --- |
| Small accounting discrepancy | `-0.75` Hushline and Ledger Lab resource mismatch | Episodes 1-2 | Strong. The clue stays small and does not become proof too early. |
| Research computing environment | Ledger Lab and Civic Learning Grid | Episodes 1-2, 6 | Strong. Shared resources, queues, old terminals, and trust paths make the system tangible. |
| Intruder becomes visible through records | Borrowed Door behavior, warm terminal, timing, print slips | Episode 3 | Strong. The episode keeps the view defender-side and avoids method detail. |
| Evidence under pressure | Threadboard, preservation, caretaker-approved summaries | Episode 4 | Strong. Byte's tool records and orders instead of attacking or trapping. |
| No one owns the problem | Glass Bureau jurisdiction and shared case stub | Episode 5 | Strong. Institutional friction is credible rather than foolish. |
| Trail leaves the lab | Library terminal, museum false pattern, old research relay | Episode 6 | Strong. The trail expands gradually and includes a false pattern removed from the case. |
| Hanover/KGB wider layer | Far Relay and Ledgerjack broker mark | Episode 7 | Good. The wider layer appears through records and remains indirect. |
| Defender as detective | Jinx's case presentation | Episode 8 | Strong. The episode explicitly separates knowns, changes, ruled-out theories, unknowns, and supported conclusions. |
| What changed | Reporting practice, shared evidence channel, Season 3 toy-process clue | Episode 9 | Strong. The finale ends with changed practice rather than total victory. |

## Continuity Pass

Season continuity passes.

- The `-0.75` clue opens the season and remains a thread rather than a solved answer.
- Project Orchard gives the season a stable affected-project label without blaming the project owners.
- The Threadboard grows across the season and becomes the visible evidence-control object.
- The Glass Bureau becomes more useful as the evidence improves.
- The old trust paths expand the map without turning the season into an all-powerful adversary plot.
- The Far Relay and Ledgerjack remain fictional and indirect.
- The finale resolves the Ledger Lab case enough for closure while leaving a broader city risk for future seasons.

## Jinx Character Arc Pass

Jinx's arc passes.

The draft set starts with Jinx noticing a tiny mismatch before she can prove why it matters. Early episodes show her learning normal behavior, preserving alternatives, and resisting premature accusation. The middle episodes pressure her through institutional delay and false patterns. The later episodes pay off the Nancy Drew anchor: she removes dramatic but weak cards, presents uncertainty clearly, and makes the mystery useful to responders.

Season endpoint achieved: Jinx can present what was known first, what changed, what was ruled out, what remains unknown, and what the evidence supports.

## Evidence And Concept Pass

Evidence and concept handling passes.

- Logging and accounting are treated as witnesses that need context.
- Anomaly investigation is shown through repeated comparison, not instinct alone.
- Account misuse is transformed into the Borrowed Door metaphor and stays non-operational.
- Evidence preservation uses public summaries, caretaker notes, and record order.
- Incident reporting improves through knowns, unknowns, ownership, and requested action.
- The Far Relay is treated as a wider broker layer, but the drafts do not explain marketplace mechanics or real-world abuse paths.

The drafts keep the mystique of investigation without repeated warning-label prose.

## Season 3 Cliffhanger Pass

The Season 3 cliffhanger passes.

The toy process appears only after the Season 2 case closes, which prevents the finale from undercutting Jinx's resolution. The simulator is contained and fictional, the copying behavior is described at story level, and the final BL4CK4T drop points toward the Morris Worm-inspired season without naming the historical anchor publicly.

## Historical Cleanliness

The public-facing draft layer does not import real historical names, real institutions, or real prosecution details. Historical facts remain in the historical account and documentary treatment. The fictional season uses transformed equivalents: Ledger Lab, Civic Learning Grid, Glass Bureau, Far Relay, Ledgerjack, and the Borrowed Door.

## Revisions Made During Review

- Added body-level concept links to all nine Season 2 mission packets so `pnpm wiki:check` recognizes their lesson anchors.
- Cleaned Season 2 draft prose flagged by `TROPES.md` validation, mainly short standalone paragraph clusters and false-range phrasing.
- Updated the production bible tracker to record mission, draft, continuity, and draft-level TROPES status.

## Remaining Publication Gate

The season is ready for user review as a private draft set. It is not ready for public publication until the user approves the draft direction and requests promotion to `content/blogs/`.

Required publication work after approval:

- Promote all nine drafts to public blog markdown.
- Add public season metadata and simultaneous timestamps.
- Run `pnpm tropes:check` against the final public markdown.
- Run `pnpm wiki:check`.
- Run `pnpm build`.
- Create the final historical-anchor release comparison after publication copy is frozen.
