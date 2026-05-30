---
type: concept
status: active
created: 2026-05-30
updated: 2026-05-30
tags: [season-3, morris-worm, resource-pressure, incident-response]
sources:
  - ../historical-accounts/morris-worm.md
  - ../story-arcs/season-03-the-escaped-experiment-arc.md
---

# Resource Counters

## Summary

Resource counters are Cybertropolis instruments that track how much shared system capacity a process is using: copy count, room slots, queue time, printer work, fan activity, and class-tool availability.

They make resource pressure visible without teaching real worm mechanics.

## BL4CK4T Teaching Frame

Resource counters teach that a security incident can harm people by consuming capacity. Files may survive while systems slow down, queues stall, and ordinary work stops moving.

## Story Hooks

- Cipher watches copy count, pace, and counter pressure during the Copycat Sprite test.
- Byte owns the counter lane during containment.
- Restore slips cannot close until counters return to a known good state.

## Public Boundary

Use resource counters for defender-side observation only. Do not explain real resource-exhaustion techniques or replication methods.

## Canon Notes

- Season 3 is the first season where resource counters become central.
- Resource counters should stay connected to people: students waiting, caretakers diverted, tools unavailable, or rooms held out of service.
