---
type: historical-account
status: research-foundation-complete
created: 2026-05-29
updated: 2026-05-29
tags: [season-7, msblaster, welchia, nachi, patch-debt, worms]
source_pages:
  - ../sources/real-world/msblaster-welchia-worm-era.md
journalism_standard: ../style-guides/historical-journalism-standard.md
---

# MSBlaster, Welchia/Nachi, And The Early-2000s Worm Era

## Executive Summary

In the early 2000s, major worms repeatedly showed that public internet dependence had outpaced routine maintenance. Code Red and Nimda demonstrated how internet-facing services, web servers, email, shares, and leftover compromises could be chained into broad disruption. SQL Slammer showed how quickly a small worm could create global network effects when a patch existed but many systems remained exposed. MSBlaster, discovered in August 2003 after Microsoft had released MS03-026 in July, made patch delay painfully visible for Windows users and administrators. Welchia/Nachi complicated the story by trying to remove Blaster and install fixes without authorization, proving that even "helpful" self-spreading repair can still disrupt networks and violate control.

The historical lesson is not simply "patch faster." It is that maintenance is a shared security responsibility involving vendors, administrators, home users, network operators, responders, and institutions. Patch debt becomes civic risk when exposed systems are numerous, homogeneous, hard to inventory, and relied upon for ordinary work.

## Source List

| Source | Type | URL | Notes |
| --- | --- | --- | --- |
| Microsoft Security Bulletin MS03-026 | Primary vendor bulletin | https://learn.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-026 | Patch and vulnerability baseline; published July 16, 2003 and later revised. |
| Microsoft Blaster worm virus alert | Primary/near-primary vendor incident page | https://learn.microsoft.com/en-us/troubleshoot/windows-server/security-and-malware/blaster-worm-virus-alert | Establishes Microsoft investigation and recovery framing for Blaster. |
| CERT Advisory CA-2003-20 | Primary incident advisory | https://seclists.org/cert/2003/22 | Public response guidance for W32/Blaster. |
| CERT Advisory CA-2003-04 | Primary incident advisory | https://seclists.org/cert/2003/1 | SQL Slammer context for worm speed and exposed SQL Server/MSDE systems. |
| CAIDA Sapphire/Slammer analysis | Technical analysis | https://www.caida.org/archive/sapphire/ | High-value analysis of Slammer spread and network impact. |
| CERT Advisory CA-2001-19 | Primary incident advisory | https://seclists.org/cert/2001/13 | Code Red context for IIS worming and public web-service exposure. |
| CERT Advisory CA-2001-26 | Primary incident advisory | https://seclists.org/bugtraq/2001/Sep/193 | Nimda context for multi-vector spread and defender complexity. |
| F-Secure Welchi description | Security vendor analysis | https://www.f-secure.com/v-descs/welchi.shtml | Welchia/Nachi behavior and first-reported timeframe. |
| DOJ Parson sentencing release | Primary legal source | https://www.justice.gov/archive/criminal/cybercrime/press-releases/2005/parsonSent.htm | Legal aftermath for a Blaster variant, not proof of original authorship. |
| Nextgov/FCW State Department Welchia report | Contemporary reporting | https://www.nextgov.com/digital-government/2003/09/worm-hits-state-dept/224104/ | Institutional impact from Welchia, including shutdown of State Department network functions. |
| Stateline state-government report | Contemporary reporting | https://stateline.org/2003/09/04/de-bugging-computers-a-state-priority/ | State-service impact and patching scramble. |
| GAO testimony on computer viruses | Government testimony | https://www.gao.gov/pdf/product/new-items-d04816t | Broad policy and damage-estimate framing. |

## Evidence Classification

| Claim | Classification | Source(s) | Notes |
| --- | --- | --- | --- |
| Microsoft released MS03-026 on July 16, 2003 for a critical RPC/DCOM vulnerability. | known | Microsoft MS03-026 | Vendor bulletin is primary source. |
| Blaster exploited the vulnerability addressed by MS03-026. | known | Microsoft Blaster alert; CERT CA-2003-20 | Mechanism should be described only at high level in fiction. |
| Blaster was discovered/reported in August 2003. | known | Microsoft Blaster alert; CERT CA-2003-20 | Microsoft states investigation began August 11, 2003. |
| Systems patched before August 11, 2003 were not vulnerable to Blaster via the addressed flaw. | known | Microsoft Blaster alert | Important patch-debt fact. |
| Welchia/Nachi attempted to remove Blaster and install patches. | known/high confidence | F-Secure; contemporary reporting | Intent is inferred from behavior; moral interpretation remains analytical. |
| Welchia/Nachi caused real disruption despite "helpful" behavior. | known | Nextgov/FCW; Stateline; security vendor reporting | Network traffic and institutional shutdowns matter. |
| The original Blaster author is definitively known. | unknown/disputed | DOJ; public reporting | DOJ source concerns a variant author, not proof of original author. |
| Patch delay alone caused the crisis. | incomplete/inferred | All sources | Patch delay mattered, but exposure, inventory, home users, firewall defaults, monoculture, and response practices also mattered. |
| Early-2000s worms changed patch management and vendor communication practices. | inferred/high confidence | Microsoft, GAO, historical synthesis | Exact causal weight varies by source and organization. |

## Chronology

| Date | Event | Source |
| --- | --- | --- |
| 2001-07 | Code Red exploits IIS Indexing Service vulnerability and becomes a landmark internet-facing service worm. | CERT CA-2001-19 |
| 2001-09-18 | CERT publishes Nimda advisory describing multiple propagation paths. | CERT CA-2001-26 |
| 2002-07 | Microsoft releases MS02-039 for SQL Server/MSDE vulnerabilities later relevant to Slammer context. | Microsoft/CERT context |
| 2003-01-25 | SQL Slammer/Sapphire begins spreading rapidly and causing internet-scale disruption. | CERT CA-2003-04; CAIDA |
| 2003-07-16 | Microsoft publishes MS03-026 for a critical RPC/DCOM vulnerability. | Microsoft MS03-026 |
| 2003-08-11 | Microsoft begins investigating Blaster; public reports identify a worm exploiting MS03-026 exposure. | Microsoft Blaster alert; CERT CA-2003-20 |
| 2003-08-18 | Welchia/Nachi is first reported by security vendors around this period. | F-Secure |
| 2003-08 to 2003-09 | State and federal institutions report disruption from worm outbreaks and patching efforts. | Stateline; Nextgov/FCW |
| 2003-09-10 | Microsoft updates MS03-026 to reference MS03-039 and scanning-tool supersedence. | Microsoft MS03-026 |
| 2005-01-28 | Jeffrey Lee Parson is sentenced for creating and releasing a Blaster variant. | DOJ |

## What Was Known When

In July 2003, defenders had a vendor bulletin, a patch, temporary mitigation guidance, and warning that the vulnerability was critical. They did not yet know which self-spreading code would appear or how quickly ordinary unpatched systems would turn the bulletin into a public incident.

When Blaster appeared in August, defenders quickly knew the broad relationship between the worm and MS03-026. They also knew that applying the patch ahead of infection mattered. Administrators still faced practical problems: finding vulnerable machines, reaching remote or home users, dealing with already unstable systems, choosing temporary blocks, and communicating urgent repair without creating confusion.

Welchia/Nachi arrived after Blaster and made later interpretation harder. It appeared to remove Blaster and install patches, but it still entered systems without permission and generated network traffic and operational disruption. At the time, institutions had to treat it as a worm, not as a legitimate repair channel.

## Key Actors And Institutions

- Microsoft: vendor that issued MS03-026, recovery guidance, and later bulletin revisions.
- CERT/CC: public advisory and incident-response coordination voice.
- Security vendors: analyzed and named worm behavior, including Welchia/Nachi.
- System administrators and network operators: had to patch, isolate, clean, and communicate under pressure.
- Home users and small organizations: often lacked managed patching or firewall posture.
- State and federal institutions: experienced public-service and network disruption.
- DOJ and law enforcement: handled legal aftermath for a Blaster variant.

## Technical Background

RPC and DCOM allowed Windows components to communicate across machines. MS03-026 addressed a critical flaw in that interface. The historically important point is not the exploit recipe; it is that a network-reachable default service on widely deployed systems created wormable conditions when many machines remained unpatched.

Worms differ from ordinary one-at-a-time intrusions because they copy themselves automatically. Code Red and Slammer showed how fast exposed services could be found. Nimda showed that multiple propagation paths could make containment harder. Blaster made endpoint patch debt visible to ordinary users through instability and forced recovery work. Welchia/Nachi showed that unauthorized self-spreading "repair" still creates a security and operations problem.

## Historical Narrative

By 2003, defenders had already seen internet worms move from novelty to infrastructure problem. Code Red had made web-server exposure visible. Nimda had blurred client and server boundaries with multiple spread paths. SQL Slammer had demonstrated that a small worm could create huge network effects in minutes when vulnerable services were exposed and patches had not reached enough systems.

MS03-026 arrived in July 2003 as an urgent warning. The patch existed before the most famous crisis, which is what makes the episode historically important. The story is not zero-day surprise; it is the gap between known fix and deployed fix. That gap included administrators who needed testing time, unmanaged home systems, exposed defaults, incomplete inventories, support burdens, and users who did not yet experience patching as ordinary civic hygiene.

Blaster appeared in August and exploited that gap. It did not need to be technically elegant to matter. It turned a bulletin into restarts, support calls, network blocks, emergency scans, and public fear. The worm's fame came from the way it made invisible maintenance visible to ordinary users.

Then Welchia/Nachi complicated the moral lesson. It behaved like a worm, but it also tried to remove Blaster and install Microsoft patches. That made it tempting to call it helpful. Institutions still had to clean it, stop it, and recover from its traffic and unauthorized entry. A repair that forces its way into systems is not an approved repair; it removes control from owners and responders.

## Attacker Story And Defender Story

- Attacker or alleged attacker narrative: the original Blaster author is not established here. A later DOJ case establishes accountability for a variant author. Welchia/Nachi's author or authors are not treated as known.
- Defender narrative: defenders had to convert bulletins into action under pressure: patch, isolate, scan, communicate, verify, and recover.
- Small clues that mattered: dates matter. The patch preceded Blaster, which makes patch debt central.
- Misunderstandings or ignored warnings: "the system still works" was not the same as "the risk is acceptable."

## Consequences And Significance

- Legal consequences: Jeffrey Lee Parson was sentenced for a Blaster variant, showing criminal accountability for worm release.
- Technical consequences: organizations learned that exposed services and unmanaged patch lag can create fast, broad incidents.
- Cultural consequences: ordinary Windows users saw patching, firewalls, and worms become mainstream concerns.
- Security-practice consequences: patch management, vulnerability scanning, firewall defaults, update communication, and incident coordination became more visibly urgent.

## Attribution And Confidence

- Attribution claims: the original Blaster author is not confidently identified in this account.
- Evidence supporting attribution: DOJ establishes Parson's responsibility for a variant, not for all Blaster activity.
- Alternative explanations: multiple variants and copycat activity complicate single-author narratives.
- Confidence level: high for vendor/advisory timeline; medium for broader practice-change claims; low for claims that reduce the full event to one person.

## Damage Or Impact Estimates

Damage estimates for early-2000s worms vary widely and often combine downtime, labor, network disruption, recovery, and productivity loss. This account uses impact qualitatively unless a specific estimate is tied to a specific source and method. Government testimony and contemporary reporting support that the impact was significant, but exact global dollar totals should be caveated.

## Infrastructure Being Attacked

The infrastructure was not only "Windows computers." It was the whole maintenance chain around them: vendor bulletins, patch testing, unmanaged endpoints, exposed network services, institutional help desks, firewalls, remote users, public services, and update trust. The attacked surface became historically meaningful because so many ordinary workflows depended on systems being patched and reachable.

## Disputed Or Uncertain Points

- Original authorship of Blaster remains outside this account's confident claims.
- Welchia/Nachi's intent can be inferred from behavior, but intent does not settle ethics.
- Damage totals should be treated carefully.
- The degree to which any one worm caused a specific later policy change varies by institution.

## Source-Backed Claim Table

| Claim | Confidence | Source(s) | Notes |
| --- | --- | --- | --- |
| MS03-026 was published July 16, 2003 and rated critical. | high | Microsoft MS03-026 | Primary vendor bulletin. |
| Blaster exploited exposure addressed by MS03-026. | high | Microsoft Blaster alert; CERT CA-2003-20 | Mechanism is high-level only here. |
| Blaster's timing made patch deployment speed historically central. | high | Microsoft MS03-026; Microsoft Blaster alert | Patch preceded worm discovery. |
| Welchia/Nachi attempted cleanup and patching. | high | F-Secure; contemporary reports | Still unauthorized. |
| Welchia/Nachi disrupted institutions. | high | Nextgov/FCW; Stateline | Useful victim/impact evidence. |
| Code Red, Nimda, and Slammer form relevant worm-era context. | high | CERT advisories; CAIDA | Context, not equal focus. |
| The original Blaster author is proven. | low | DOJ only proves variant case | Avoid overclaiming. |

## What Changed

The early-2000s worm era made patching feel less like private housekeeping and more like public resilience. It pushed organizations toward better asset inventory, faster emergency change, clearer vendor communication, improved firewall posture, managed updates, scanning, and incident-response coordination. It also established a lasting ethical lesson: defenders need trusted, consent-based repair channels. A tool that helps by breaking in is still breaking in.

## Journalist Checklist

- Primary sources for central claims identified.
- Known, alleged, inferred, disputed, and unknown claims separated.
- Timeline preserves what was known at each stage.
- Technical mechanism explained without magical language.
- Attribution claims include evidence and confidence.
- Systemic causes included; no monocausal explanation.
- Attacker and defender stories both represented.
- Damage estimates sourced and caveated.
- Victims treated with specificity and agency.
- Infrastructure explained.
- Dissenting interpretations included.
- Operationally harmful detail avoided.

## Open Questions

- Which internal organizational patch decisions most shaped individual outages remains source-dependent.
- Welchia/Nachi authorship and full intent are not confidently established here.
- Exact aggregate damage remains methodologically uncertain.
