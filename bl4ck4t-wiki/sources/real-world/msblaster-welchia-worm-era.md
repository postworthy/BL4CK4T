---
type: source
status: active
created: 2026-05-29
updated: 2026-05-29
tags: [season-7, msblaster, welchia, nachi, code-red, nimda, sql-slammer, patching]
---

# MSBlaster, Welchia/Nachi, And Early-2000s Worm Era Sources

## Purpose

This source page supports Season 7 historical research. It gathers primary, near-primary, and high-value secondary material for the early-2000s worm era, with MSBlaster and Welchia/Nachi as the season center and Code Red, Nimda, and SQL Slammer as contextual background.

## Source Inventory

| Source | Type | URL | Why It Matters |
| --- | --- | --- | --- |
| Microsoft Security Bulletin MS03-026 | Primary vendor bulletin | https://learn.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-026 | Establishes the July 16, 2003 RPC/DCOM vulnerability disclosure, affected Windows versions, severity, patch guidance, mitigations, and later revision history. |
| Microsoft Blaster worm virus alert | Primary/near-primary vendor incident page | https://learn.microsoft.com/en-us/troubleshoot/windows-server/security-and-malware/blaster-worm-virus-alert | Describes Microsoft investigation beginning August 11, 2003, Blaster's relationship to MS03-026, and customer recovery/prevention guidance. |
| CERT Advisory CA-2003-20: W32/Blaster worm | Primary incident advisory | https://seclists.org/cert/2003/22 | Establishes public incident response framing, affected systems, impact, and response recommendations for Blaster. |
| CERT Advisory CA-2003-04: MS-SQL Server Worm | Primary incident advisory | https://seclists.org/cert/2003/1 | Establishes SQL Slammer as earlier 2003 context for fast worm propagation and patch-lag consequence. |
| CAIDA Analysis of the Sapphire/Slammer Worm | Technical analysis | https://www.caida.org/archive/sapphire/ | Provides high-value analysis of Slammer/Sapphire speed, scale, and internet impact without needing exploit reproduction. |
| CERT Advisory CA-2001-19: Code Red | Primary incident advisory | https://seclists.org/cert/2001/13 | Establishes Code Red as context for internet-facing service worms before Blaster. |
| CERT Advisory CA-2001-26: Nimda Worm | Primary incident advisory | https://seclists.org/bugtraq/2001/Sep/193 | Establishes Nimda's multi-vector spread and the defender complexity of client/server worm response. |
| F-Secure Welchi description | Security vendor analysis | https://www.f-secure.com/v-descs/welchi.shtml | Establishes Welchia/Nachi behavior, first reporting timeframe, and cleanup/patching intent at a high level. |
| DOJ Parson sentencing release | Primary legal source | https://www.justice.gov/archive/criminal/cybercrime/press-releases/2005/parsonSent.htm | Establishes legal aftermath for a Blaster variant and avoids overstating the identity of the original Blaster author. |
| Nextgov/FCW State Department Welchia report | Contemporary reporting | https://www.nextgov.com/digital-government/2003/09/worm-hits-state-dept/224104/ | Shows institutional impact from Welchia, including network shutdown consequences. |
| Stateline state-government worm impact report | Contemporary reporting | https://stateline.org/2003/09/04/de-bugging-computers-a-state-priority/ | Shows ordinary civic-service impact in states, including licensing, permits, and public-service delays. |
| GAO testimony on computer viruses | Government testimony | https://www.gao.gov/pdf/product/new-items-d04816t | Useful for broad impact framing, damage-estimate caveats, and federal concern about worm outbreaks. |

## Season Scope Decision

Season 7 should not become a survey of every early-2000s worm. Code Red, Nimda, and SQL Slammer provide context for why defenders were already seeing exposed services, patch lag, and network-scale speed as public problems. MSBlaster provides the main patch-debt crisis. Welchia/Nachi provides the ethical center: unauthorized repair may appear helpful and still violate consent, disrupt systems, and create new harm.

## Source Handling Notes

- Historical-account documents may name real events, sources, affected products, and institutions.
- Public BL4CK4T stories must transform the real events into fictional civic systems.
- Public prose must not reproduce exploit steps, payload internals, scanning instructions, credential lists, or operationally useful malware detail.
