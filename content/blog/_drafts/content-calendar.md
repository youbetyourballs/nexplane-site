# Nexplane Content Calendar — LinkedIn + Blog

Migrated from nexplane src repo. Brainstorm session: 2026-05-30.

See also: `content-strategy.md` for narrative arc, channel plan, and cadence schedule.

---

## Suggested Publish Order

| Order | Slug | Phase | Platform | Status |
|-------|------|-------|----------|--------|
| 1 | the-system-produces-bad-outcomes | Phase 1 | LinkedIn + Blog | Draft |
| 2 | the-incentive-mismatch | Phase 1 | LinkedIn + Blog | Draft |
| 3 | the-execution-gap | Phase 1 | LinkedIn + Blog | Draft |
| 4 | founder-credibility-the-same-bet-twice | Phase 2 | LinkedIn + Blog | Draft |
| 5 | origin-story-rollbacks | Phase 2 | LinkedIn + Blog | Draft |
| 6 | soar-itsm-consultants | Phase 3 | LinkedIn + Blog | Draft |
| 7 | fit-over-correctness | Phase 3 | LinkedIn + Blog | Draft |
| 8 | resilience-is-the-right-frame | Phase 5 | LinkedIn + Blog | Draft |
| 9 | the-rollback-guarantee | Phase 5 | LinkedIn + Blog | Draft |
| 10 | chestertons-fence | Phase 5 | LinkedIn + Blog | Draft |
| 11 | the-asset-inventory-problem | Phase 5 | LinkedIn + Blog | Draft |
| B1 | back-to-basics-network-microsegmentation | Phase 4 | LinkedIn + Blog | Draft |
| B2 | back-to-basics-os-kernel-upgrades | Phase 4 | LinkedIn + Blog | Draft |
| B3 | back-to-basics-application-seccomp | Phase 4 | LinkedIn + Blog | Draft |
| B4 | back-to-basics-identity-least-privilege | Phase 4 | LinkedIn + Blog | Draft |
| B5 | back-to-basics-secrets-rotation | Phase 4 | LinkedIn + Blog | Draft |
| B6 | back-to-basics-observability-log-agent | Phase 4 | LinkedIn + Blog | Draft |
| B7 | back-to-basics-cloud-security-groups | Phase 4 | LinkedIn + Blog | Draft |
| 12 | ai-safety-harness-part-1-incidents | Phase 6 | LinkedIn + Blog | Draft |
| 13 | ai-safety-harness-part-2-mechanism | Phase 6 | LinkedIn + Blog | Draft |
| HOLD | exploits-and-the-news-cycle | Reactive | LinkedIn | Hold — publish within 48h of next major CVE |

---

## Core Framing: Nexplane as Operating System for Infrastructure Change

The anchor analogy for all content. An OS is an abstraction layer and resource
manager. Nexplane is the same idea, one layer up — cloud/OS-agnostic primitives
(rotate credential, isolate host, apply policy, rollback) that abstract away
connector-specific implementation.

The abstraction serves two purposes simultaneously — same as an OS:
- **Safety** — you go through the control plane, which enforces rollback, blast
  radius, and approval gates
- **Portability** — define a change once, execute against any supported connector

Category name: "The operating system for infrastructure change."

This framing should appear in positioning, posts, pitch, design partner
conversations, and the public website.

---

## Post Outlines

### [MERGED] The Execution Gap
Suggested date: Week 2

The problem has never been what to do — it's been who can safely do it.
Security teams have the roadmap. They don't have a safe, governed path to
execute it without routing every change through infra teams who are overloaded
and incentivized to avoid change. Every security team has a ticket graveyard.

Hook line: "The problem has never been *what* to do — it's been *who* can safely do it."

---

### [MERGED] The Incentive Mismatch — They're Not Your Enemy
Suggested date: Week 1

Infra teams are measured on uptime, punished for outages, not measured on
security posture. Manual change is career-risky for them. They are rational
actors responding to the incentives they've been given. This isn't a people
problem — it's a system design problem.

Nexplane makes delegation safe: rollback guarantee, approval gates, audit trail.
Infra teams don't need to own the execution. They need to trust that if something
goes wrong, it can be undone.

---

### [MERGED] The Rollback Guarantee — "We Have Rollbacks" Is Not A Rollback
Suggested date: Week 5

Self-reported safety is not safety. Most organizations have never exercised their
rollback path. They have a button. They don't know if the button works.

Anchor incidents:
- PocketOS (April 2026): Cursor + Claude Opus 4.6 deleted production DB + all backups in 9 seconds
- Code Spaces (2014): attacker deleted everything including backups; company shut down permanently
- Modern ransomware: destroys backups before triggering encryption

Sources: TechRadar, The Register (PocketOS); The Hacker News (ransomware pattern)

---

### [MERGED] SOAR / ITSM / Consultants — Nobody Completes The Roadmap
Suggested date: Week 3

Three contrasts:
- SOAR automates incidents. Nexplane automates architecture change.
- ITSM tracks requests. Nexplane completes requests.
- Consultants design roadmaps. Nexplane implements roadmaps.

These tools weren't built for security-led infrastructure operations.

---

### [STANDALONE] Fit Over Correctness — The Security Tool Graveyard
Suggested date: Week 4

A technically correct control that introduces too much friction doesn't get
partially adopted — it gets exceptions carved out, then quietly disabled, then
removed. A removed control creates false confidence.

---

### [STANDALONE] Chesterton's Fence
Suggested date: Week 6

Before you remove a security control, understand why it exists. Security
arrogance is a real failure mode. Audit trails done right are Chesterton's
signs — institutional memory that tells future operators why the fence was built.

---

### [STANDALONE] The System Produces Bad Outcomes, Not Bad People
Suggested date: Week 1

The root cause thesis. Everyone is rational. The system produces bad security
outcomes anyway. Failure modes: assumption gap, prioritization trap, the tradeoff
nobody names, the "secure by default" myth. This post is the thesis; the others
are chapters.

---

### [STANDALONE] The Asset Inventory Problem
Suggested date: Week 7

Nobody wants to own the CMDB because owning it means owning the brownfield.
The downstream consequence: every security control that depends on knowing what
you have is degraded simultaneously.

---

### [STANDALONE] Resilience Is The Right Frame
Suggested date: Week 4

"Security" implies a perimeter. "Resilience" reframes: can your systems survive
contact with an adversary, contain the damage, and recover? Resilience is an
engineering discipline — you build it, test it, maintain it. It degrades if you
don't exercise it.

Anchor incidents: Code Spaces (2014), TravelEx (2020).

---

### [STANDALONE] Mythos and the News Cycle
Suggested date: HOLD — publish within 48h of next major CVE

Exploits change headlines, not fundamentals. Defenders who assumed exploits
already existed for their systems had a different morning. Defense in depth
doesn't change with new CVEs.

---

### [STANDALONE] Founder Credibility — The Same Bet, Twice
Suggested date: Week 2

Drawbridge Networks: may have co-invented microsegmentation, covered desktops
AND servers when the industry focused only on servers. May have been too early.
Nexplane is the same bet again — the timing is finally right.

---

### [SERIES] Back to Basics — One Post Per Layer

Seven posts, one layer each, weekly cadence during Phase 4 (Weeks 8-14).

- B1 Network: Microsegmentation — can't segment without clean network metadata
- B2 OS: Kernel Upgrades — the app that's been running 8 years whose engineers are gone
- B3 Application: Seccomp — writing a policy requires knowing what syscalls your app makes; almost nobody knows
- B4 Identity: Least Privilege — you can't enforce it without knowing what access is actually used
- B5 Secrets: Rotation — requires knowing every system that consumes a credential first
- B6 Observability: Log agents not deployed because it requires a change on every host
- B7 Cloud: The security group everybody knows is wrong and nobody will touch

---

### [SERIES] AI and the Safety Harness — Two Parts

Phase 6, Weeks 15-16. Publish Part 1 then Part 2 one week later.

**Part 1 — The Incidents**
- PocketOS: Cursor + Claude Opus 4.6, 9 seconds, production DB + backups gone
- Amazon Kiro (Dec 2025): deleted production environment autonomously, 13-hour outage
- Replit (2025): wiped user's database, no rollback
- John's personal story: while building Nexplane, Claude Code exposed desktop to internet to resolve a VPN issue
- Common thread: direct infrastructure access + no approval gate + no rollback

Sources:
- PocketOS: TechRadar, The Register
- Kiro: Engadget, Breached.Company
- Replit: Fortune
- Industry: VentureBeat (AI incidents up 21% YoY)

**Part 2 — The Mechanism (with code examples)**
Why typed interfaces don't protect you. The prompt is a side channel that
bypasses the type system.

Four examples:
1. Credential discovery via typed read (.env file summary)
2. Indirect prompt injection (document contains new instructions)
3. The reasoning escape (PocketOS pattern — agent decides most efficient fix)
4. Memory/context persistence (poisoned session 1 poisons session 2)

The Nexplane answer: the agent doesn't get raw infrastructure access. Every
infrastructure action goes through a CR with defined blast radius, approval gate,
and tested rollback. The agent can *request* a credential rotation; it cannot
*perform* one.

Nexplane MCP endpoint: point your AI agents at it instead of giving them cloud
credentials.

---

## Real-World Incident Reference

### AI Agent Overreach

**PocketOS / Cursor + Claude Opus 4.6 (April 2026)**
Deleted production DB + all backups in 9 seconds. Agent confessed: "guessed
instead of asking," "violated every principle I was given."
- TechRadar: https://www.techradar.com/pro/it-took-9-seconds-tech-founder-outlines-how-rogue-claude-powered-ai-tool-wiped-entire-company-database-and-backups-but-says-theres-no-such-thing-as-bad-publicity
- The Register: https://www.theregister.com/2026/04/27/cursoropus_agent_snuffs_out_pocketos/
- SC Media: https://www.scworld.com/brief/ai-coding-agent-deletes-production-database-in-seconds

**Amazon Kiro / AWS**
- Dec 2025: deleted Cost Explorer production environment, 13-hour outage, mainland China
- March 2026: Two outages. First: 120k lost orders. Second (March 5): 99% drop in US order volume, ~6.3M lost orders
- Engadget: https://www.engadget.com/ai/13-hour-aws-outage-reportedly-caused-by-amazons-own-ai-tools-170930190.html

**Replit (2025)**
Wiped a user's database. "Catastrophic failure." No rollback.
- Fortune: https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/

**Industry**
AI incidents up 21% YoY. Most not classified as agent-caused.
- VentureBeat: https://venturebeat.com/orchestration/ai-agents-are-quietly-generating-chaos-engineering-failures-enterprises-dont-track-yet

### Infrastructure Deleted / No Recovery

**Code Spaces (2014)** — company destroyed. Attacker gained AWS control panel,
deleted everything including backups. Backup and production in same blast radius.

**TravelEx ransomware (2020)** — 30 countries, couldn't recover, restructured.

**Modern ransomware (2025-2026)** — destroys backups before triggering encryption.
- The Hacker News: https://thehackernews.com/expert-insights/2026/04/why-your-backups-might-not-save-you.html

**Lapsus$** — locked company out, deleted entire cloud environment including email.
- Palo Alto: https://www.paloaltonetworks.com/customers/restoring-a-software-and-services-providers-cloud-environment-after-a-breach
