---
type: style-guide
status: active
created: 2026-05-29
updated: 2026-05-30
tags: [style, technical-texture, historical-fidelity, seasons]
---

# Technical Texture Standard

## Purpose

BL4CK4T stories transform real cybersecurity history into Cybertropolis fiction, but the transformation must not erase the cyber idea. Public stories should feel like cyber stories, not only civic fables with a cybersecurity lesson attached at the end.

Use this standard for all season imports, production bibles, mission packets, drafts, and release reviews.

## Core Rule

Fictional artifacts should illuminate the technical concept, not replace it.

An episode can use a BL4CK4T-world object such as the Echo Grid, Threadboard, Copy Map, Quarantine Tray, Service Map, or Patch Bell, but the reader should still understand the underlying cybersecurity concept before the Teaching Tie-In.

Historical fidelity comes before reuse of existing lore. If the historical anchor depends on a kind of system that Cybertropolis does not yet have, introduce a clear fictional equivalent and document it in the wiki. Do not force a real event through an existing artifact or district when the analogy becomes strained.

## Required Technical Texture

Every public season episode should include:

- at least one safe cybersecurity term in the story body, not only in metadata or the Teaching Tie-In;
- one plain-language causal explanation of what the technical issue does;
- one defender-side action, observation, or decision that maps to real security work;
- enough concrete system language that the fictional artifact remains connected to computers, networks, software, logs, messages, identity, availability, code, updates, or incident response.

Good safe terms include:

- signal, command, routing, protocol, network, service, endpoint, server, terminal, kiosk, log, audit trail, timestamp, access, account, permission, authentication, authorization;
- message, attachment, sender, recipient, address book, file extension, script, macro, quarantine, report, warning, recovery;
- worm, self-copying behavior, propagation, sandbox, containment, rollback, backup, restore, patch, update, vulnerability, exposed service;
- availability, traffic, request, response, queue, rate limit, degradation, outage, status page, fallback path;
- source code, build, dependency, package, signature, checksum, release channel, maintainer, supply chain.

Avoid operational detail:

- exploit chains;
- malware construction;
- evasion;
- credential theft steps;
- real target details;
- payload internals;
- scanning instructions;
- reproduction steps.

## Historical Anchor Fidelity

When a season is based on a historical event, the public story should preserve the historical shape at a recognizable level:

- what kind of system was involved;
- what kind of failure or abuse occurred;
- what defenders could observe;
- what was known versus unknown at the time;
- what changed afterward.

The historical names and exploit details can stay private. The public story still needs enough technical resemblance that a reader can later learn the real history and recognize why the BL4CK4T version was built that way.

## Audience Calibration

Write for curious teens, teachers, and adult readers who may be new to security but are not toddlers. Do not assume prior tool knowledge, but do not avoid normal cybersecurity words. Introduce terms through context, dialogue, and action.

Prefer:

- "The public terminal kept a log of which project label used storage credits."
- "The old service was still exposed, even though a repair notice already existed."
- "The message looked friendly, but its attachment behaved like a script."

Avoid replacing technical ideas only with soft metaphor:

- "The board felt wrong."
- "The door was too eager."
- "The city remembered something in pieces."

Those lines can work as style, but they need technical context nearby.

## Import Checklist

During historical documentary import, record:

- historical mechanism in one sentence;
- BL4CK4T-world transformation;
- pre-translation import inventory outcome: `reuse`, `create`, `merge`, or `omit`;
- whether an existing world element truly fits or whether new infrastructure is needed;
- safe technical terms that must survive into public prose;
- technical details that must remain private;
- defender-side actions that can be shown on page.

## Draft Checklist

Before an episode is considered ready:

- The cyber concept is legible before the Teaching Tie-In.
- The fictional artifact is connected to a real class of system or security work.
- At least one character uses a real technical term naturally.
- The episode shows cause and effect, not only mood and metaphor.
- The prose avoids both extremes: no operational how-to, and no over-softened allegory.
