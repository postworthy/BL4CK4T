---
type: historical-documentary-treatment
status: complete
created: 2026-05-29
updated: 2026-05-29
tags: [season-7, documentary, msblaster, welchia, patching]
historical_account: ../historical-accounts/msblaster-welchia-worm-era.md
---

# MSBlaster, Welchia/Nachi, And The Patch-Debt Era Documentary Treatment

## Purpose

This treatment turns the Season 7 historical account into a nonfiction story structure that can later be transformed into BL4CK4T fiction. It preserves the real sequence: warning, delay, worm, disruption, emergency repair, unauthorized "help," and changed practice.

## Source Boundary

Use only the historical account and its source page as the nonfiction foundation. Do not introduce BL4CK4T-world names, places, villains, or artifacts into historical analysis.

## Documentary Thesis

The MSBlaster/Welchia era matters because the patch existed before the crisis, and because the attempted "helpful" repair proved that solving a technical problem without consent can create a new security problem.

## Cold Open

A computer restarts before its user can save work. Somewhere else, a public-service desk cannot finish a form. The screen does not show stolen secrets. It shows interruption. The question is simple: what happens when a known repair existed, but the repair did not reach the machines before the worm did?

## Movement Structure

### Movement 1: The Warning Before The Fever

- Historical function: Establish MS03-026 as a known critical vulnerability before Blaster's August outbreak.
- Narrative question: what does it mean for a crisis to arrive after the warning?
- Key beats: Microsoft publishes MS03-026; affected Windows versions are named; patch and mitigations exist; administrators face testing, inventory, and deployment realities.
- Evidence anchors: Microsoft MS03-026; Microsoft Blaster alert.
- Visual/audio language: bulletin pages, clocks, patch queues, machines still working under a quiet red mark.
- Uncertainty guardrails: do not imply every unpatched system was negligent; include home users, unmanaged machines, and operational constraints.

### Movement 2: A Decade Of Exposed Doors In Two Years

- Historical function: Place Blaster inside the worm-era pattern created by Code Red, Nimda, and SQL Slammer.
- Narrative question: why had defenders already learned to fear speed?
- Key beats: Code Red shows internet-facing service risk; Nimda spreads through multiple paths; SQL Slammer shows extreme speed and network impact.
- Evidence anchors: CERT Code Red advisory; CERT Nimda advisory; CERT SQL Slammer advisory; CAIDA Slammer analysis.
- Visual/audio language: public web signs changing, email and share paths crossing, a tiny packet storm becoming network weather.
- Uncertainty guardrails: keep these as context, not equal Season 7 centers.

### Movement 3: Blaster Turns Delay Into Weather

- Historical function: Show how Blaster made patch debt visible.
- Narrative question: when does a postponed fix become everyone else's emergency?
- Key beats: Blaster appears in August; patched systems are safer; exposed systems spread disruption; support and response loads grow.
- Evidence anchors: Microsoft Blaster alert; CERT CA-2003-20.
- Visual/audio language: restarts, help-desk phones, blocked ports, late-night patch rooms, public confusion.
- Uncertainty guardrails: do not overclaim data theft; focus on disruption, instability, response, and patch deployment.

### Movement 4: Ordinary Institutions Feel The Cost

- Historical function: Ground harm in real civic and institutional consequences.
- Narrative question: what does a worm cost when it interrupts ordinary public work?
- Key beats: state systems delay services; institutions disconnect or clean networks; users lose work; public-facing operations slow.
- Evidence anchors: Stateline state-government report; GAO testimony; contemporary reports.
- Visual/audio language: licensing counters, permit desks, network cables pulled, forms waiting.
- Uncertainty guardrails: caveat exact damage numbers and distinguish local reports from global estimates.

### Movement 5: The Repair Channel Problem

- Historical function: Explain why emergency repair needs trusted channels.
- Narrative question: how do people know which urgent repair notice to trust?
- Key beats: real patches exist; scanning and verification tools are discussed; administrators must verify patch state; rushed communication can confuse users.
- Evidence anchors: Microsoft MS03-026 revisions; Microsoft Blaster alert; CERT guidance.
- Visual/audio language: two nearly identical notices, one verified path, one rumor path, administrators checking before installing.
- Uncertainty guardrails: avoid giving procedural attack or scan instructions.

### Movement 6: The Helpful Worm That Still Broke The Door

- Historical function: Center Welchia/Nachi as the moral complication.
- Narrative question: can unauthorized repair be good if it patches the machine?
- Key beats: Welchia/Nachi attempts to remove Blaster and install fixes; it spreads without consent; it creates traffic and disruption; institutions still must stop and clean it.
- Evidence anchors: F-Secure Welchi description; Nextgov/FCW State Department report; Stateline.
- Visual/audio language: a silver repair tool entering through a broken door, leaving patched locks and broken trust behind.
- Uncertainty guardrails: describe behavior, not exploit steps; do not romanticize self-spreading repair.

### Movement 7: What Changed After The Bells

- Historical function: Show aftermath in practice, policy, and culture.
- Narrative question: what remains after the machines stop restarting?
- Key beats: patching becomes more urgent; firewalls, asset inventory, emergency change, vendor communication, and response coordination gain importance; legal consequences follow for a Blaster variant.
- Evidence anchors: DOJ Parson sentencing release; Microsoft bulletin revisions; GAO testimony.
- Visual/audio language: quieter patch calendars, inventories, warning bells, and repair ledgers.
- Uncertainty guardrails: do not claim one incident alone created all modern patch practice.

## Recurring Motifs

- Red mark: a known flaw waiting while the system still appears to work.
- Restart weather: visible disruption from invisible maintenance failure.
- Repair lane: the trusted path between warning and fix.
- Silver helper: the moral danger of help without consent.
- Bell: the public signal that maintenance cannot be silently deferred.

## Interview Targets Or Archival Voices

- Vendor bulletin voice: Microsoft MS03-026 and Blaster guidance.
- Incident response voice: CERT advisories.
- Network measurement voice: CAIDA Slammer analysis.
- Institutional victim voice: state-government and State Department reporting.
- Legal aftermath voice: DOJ sentencing release.
- Administrator voice: patch testing, inventory, emergency change, and user communication.

## Narration Guardrails

- Claims to state plainly: MS03-026 preceded Blaster; Blaster exploited the addressed exposure; Welchia/Nachi spread without authorization despite attempted cleanup behavior.
- Claims to qualify: damage totals, broad causal claims about long-term patching practice, and any claim about original Blaster authorship.
- Claims to avoid: exploit steps, malware internals, exact reproduction paths, and "helpful worm" framing that excuses unauthorized entry.

## Ending

End after the restarts stop. The lesson is not that the world learned to patch perfectly. The lesson is that maintenance became harder to dismiss as background work. A patch delayed long enough becomes a public problem, and a repair that enters without permission leaves a second lesson behind: trust is part of repair.

## Open Research Needs

- Exact local impact figures vary by institution and should be sourced case by case.
- Broader industry practice-change claims should remain qualified unless tied to specific sources.
