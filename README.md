<div align="center">

```text
 _____ _   _  ____ ___ _   _ _____ _____ ____  ___ _   _  ____ 
| ____| \ | |/ ___|_ _| \ | | ____| ____|  _ \|_ _| \ | |/ ___|
|  _| |  \| | |  _ | ||  \| |  _| |  _| | |_) || ||  \| | |  _ 
| |___| |\  | |_| || || |\  | |___| |___|  _ < | || |\  | |_| |
|_____|_| \_|\____|___|_| \_|_____|_____|_| \_\___|_| \_|\____|
                                                               
     ____ _____  _    _   _ ____    _    ____  ____  ____      
    / ___|_   _|/ \  | \ | |  _ \  / \  |  _ \|  _ \/ ___|     
    \___ \ | | / _ \ |  \| | | | |/ _ \ | |_) | | | \___ \     
     ___) || |/ ___ \| |\  | |_| / ___ \|  _ <| |_| |___) |    
    |____/ |_/_/   \_\_| \_|____/_/   \_\_| \_\____/|____/     
                                                               
        ____ _   _ _____ ____ _  ___     ___ ____ _____        
       / ___| | | | ____/ ___| |/ / |   |_ _/ ___|_   _|       
      | |   | |_| |  _|| |   | ' /| |    | |\___ \ | |         
      | |___|  _  | |__| |___| . \| |___ | | ___) || |         
       \____|_| |_|_____\____|_|\_\_____|___|____/ |_|         
                                                               
              [ ENGINEERING INTEGRITY FRAMEWORK ]              
                                                               
                   SYSTEM STATUS: DOCUMENTED                   
                   VISIBILITY TARGET: PUBLIC                   
                VERIFICATION: EVIDENCE REQUIRED                
```

**AUDIT. VERIFY. HARDEN. SHIP.**

*Engineering standards for software developers, product teams, and AI-assisted builders.*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

[START HERE](#start-here) · [FRAMEWORK](#how-the-framework-fits-together) · [CHECKLISTS](#the-checklist-library) · [SECURITY AUDIT](#specialist-security-audit) · [CONTRIBUTING](CONTRIBUTING.md) · [SECURITY POLICY](SECURITY.md)

</div>

---

```text
$ python3 scripts/validate_repository.py
REPOSITORY VALIDATION: PASSED
- Checklist files: 16
- Unique checklist items: 101
- Local Markdown links checked: 525
- Vendor files integrity-checked (Cloudflare, Addy Osmani, Matt Pocock): 100
- AGENTS.md / CLAUDE.md mirror is synchronized
```

## Start here

This repository is a modular engineering framework. You do not need to read every file. Start with the path that matches your task.

| I want to... | Start here | Then use |
|---|---|---|
| Understand the framework | [Universal Software Engineering & Product Excellence Standard](standards/universal-software-engineering-product-excellence-standard.md) | [Framework map](docs/framework-map.md) |
| Build or change software safely | [Deterministic Engineering & Verification Protocol](protocols/deterministic-engineering-verification-protocol.md) | [AGENTS.md](AGENTS.md) and applicable checklists |
| Build with AI | [Vibe-coding guide](docs/vibe-coding-guide.md) | [AGENTS.md](AGENTS.md) and [kickoff prompt](prompts/01-kickoff.md) |
| Review an existing codebase | [Framework map](docs/framework-map.md) | [Audit prompt](prompts/02-audit.md) and [audit report](templates/audit-report.md) |
| Assess a complete product | [Universal Standard — audit workflow](standards/universal-software-engineering-product-excellence-standard.md#10-audit-and-improvement-workflow) | [Assessment templates](#assessment-and-reporting-templates) |
| Investigate security vulnerabilities | [Security-audit integration guide](docs/security-audit-integration.md) | [Upstream Cloudflare skill](vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md) |
| Prepare a release | [Release-readiness prompt](prompts/04-release-readiness.md) | [Scoring and gates](docs/scoring.md) |
| Find standards and tools | [Standards reference](references/standards.md) | [Universal Standard — references](standards/universal-software-engineering-product-excellence-standard.md#7-standards-and-reference-frameworks) |

### Repository setup

```bash
git clone https://github.com/jonam17/engineering-standards-checklist.git
cd engineering-standards-checklist
```

To install the instructions into a project you are building, copy the file(s) into that project's root (replace the source path with the location of this repository):

```bash
cp /path/to/engineering-standards-checklist/AGENTS.md /path/to/your-project/AGENTS.md
cp /path/to/engineering-standards-checklist/CLAUDE.md /path/to/your-project/CLAUDE.md
```

Keep the instruction file(s) available to your coding agent. The repository's `AGENTS.md` and `CLAUDE.md` are exact mirrors.

### Quick start by audience

**AI-assisted builder:** Read [AGENTS.md](AGENTS.md), then [docs/vibe-coding-guide.md](docs/vibe-coding-guide.md). Use the [kickoff prompt](prompts/01-kickoff.md) before implementation.

**Developer:** Read the [Deterministic Engineering & Verification Protocol](protocols/deterministic-engineering-verification-protocol.md), select relevant checklists using [docs/framework-map.md](docs/framework-map.md), and verify each applicable requirement.

**Engineering lead, product manager, or auditor:** Start with the [Universal Standard](standards/universal-software-engineering-product-excellence-standard.md), define scope and applicability, then use the assessment templates and risk model.

**AI coding agent:** Read [AGENTS.md](AGENTS.md) first. Load only the framework documents and checklists relevant to the task. Do not automatically run the specialist full security-audit workflow.

## How the framework fits together

The repository has four layers. Each has a distinct purpose; none replaces the others.

```text
                 ENGINEERING FRAMEWORK
                           |
          +----------------+----------------+
          |                                 |
   UNIVERSAL STANDARD              DETERMINISTIC PROTOCOL
   WHAT GOOD LOOKS LIKE             HOW TO BUILD & VERIFY
          |                                 |
          +----------------+----------------+
                           |
                    FRAMEWORK MAP
                           |
                  16 ENGINEERING AREAS
                     101 ITEMS
                           |
          +----------------+----------------+
          |                |                |
       PROMPTS          TEMPLATES       REFERENCES
          |                |                |
          +----------------+----------------+
                           |
                  EVIDENCE & REPORTING
                           |
              OPTIONAL SPECIALIST SECURITY
```

| Layer | Canonical source | Purpose |
|---|---|---|
| **Universal standard** | [`standards/`](standards/) | Defines quality objectives, scope, applicability, evidence, risk, maturity, and governance across software and digital products. |
| **Engineering protocol** | [`protocols/`](protocols/) | Defines verification-first development and the preference for enforceable controls over prose-only rules. |
| **Operational checklists** | [`checklists/`](checklists/) | Converts selected requirements into stable IDs, priorities, and concrete verification steps. |
| **Workflow skills** | [`vendor/addyosmani/`](vendor/addyosmani/), [`vendor/mattpocock/`](vendor/mattpocock/) | Optional third-party agent skills for carrying out checklist work (TDD, debugging, review, hardening, documentation). They add no requirements. |
| **Specialist security** | [`vendor/cloudflare/`](vendor/cloudflare/) | Provides an optional, source-first vulnerability investigation workflow for explicitly requested comprehensive security audits. |

The [framework map](docs/framework-map.md) links the Universal Standard's 16 disciplines to the operational checklists and specialist security modules. This is a navigation crosswalk, not a claim of formal equivalence or certification.

## The checklist library

The core library contains **16 checklists and 101 uniquely identified requirements**. Original checklist IDs and item contents are retained.

| # | Engineering area | File | ID prefix | Items |
|---:|---|---|---|---:|
| 01 | Architecture and code quality | [01-architecture.md](checklists/01-architecture.md) | `ARC` | 6 |
| 02 | Application security | [02-application-security.md](checklists/02-application-security.md) | `SEC` | 11 |
| 03 | Authentication and authorization | [03-authentication-authorization.md](checklists/03-authentication-authorization.md) | `AUT` | 7 |
| 04 | Data and backend | [04-data-and-backend.md](checklists/04-data-and-backend.md) | `DAT` | 9 |
| 05 | APIs and integrations | [05-apis-and-integrations.md](checklists/05-apis-and-integrations.md) | `API` | 6 |
| 06 | Privacy, legal, and compliance | [06-privacy-legal-compliance.md](checklists/06-privacy-legal-compliance.md) | `PRV` | 9 |
| 07 | Accessibility | [07-accessibility.md](checklists/07-accessibility.md) | `A11` | 7 |
| 08 | UX and craft | [08-ux-and-craft.md](checklists/08-ux-and-craft.md) | `UX` | 7 |
| 09 | Motion and animation | [09-motion.md](checklists/09-motion.md) | `MOT` | 4 |
| 10 | Performance | [10-performance.md](checklists/10-performance.md) | `PRF` | 5 |
| 11 | Testing and QA | [11-testing.md](checklists/11-testing.md) | `TST` | 5 |
| 12 | DevOps and supply chain | [12-devops-and-supply-chain.md](checklists/12-devops-and-supply-chain.md) | `OPS` | 5 |
| 13 | Observability and reliability | [13-observability-and-reliability.md](checklists/13-observability-and-reliability.md) | `OBS` | 5 |
| 14 | AI and agents | [14-ai-and-agents.md](checklists/14-ai-and-agents.md) | `AI` | 7 |
| 15 | SEO and discoverability | [15-seo-and-discoverability.md](checklists/15-seo-and-discoverability.md) | `SEO` | 3 |
| 16 | Documentation, governance, and product | [16-docs-governance-product.md](checklists/16-docs-governance-product.md) | `DOC` | 5 |

Use [AGENTS.md](AGENTS.md) for project-type selection, or [docs/framework-map.md](docs/framework-map.md) for discipline-by-discipline mapping.

## Specialist security audit

The Cloudflare `security-audit` skill is an optional specialist extension, not a mandatory step in ordinary development or every checklist review.

- Use **guidance mode** for focused security questions and narrow reviews.
- Use **full audit mode** only when a comprehensive codebase security audit, penetration-test review, or audit artifacts are explicitly requested.
- Full mode requires a capable delegated-agent environment, Node.js for the supplied validators, and an OS-enforced sandbox with the controls specified by the upstream skill.
- If those controls are unavailable, do not execute target-controlled code; report the exact limitation and keep unresolved claims in `needs_validation`.

Read the [integration guide](docs/security-audit-integration.md), then the original upstream [README](vendor/cloudflare/security-audit-skill/README.md) and [SKILL.md](vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md). The upstream files and MIT license are preserved under `vendor/cloudflare/`.

## Optional workflow skills

Two sets of community agent skills are bundled as optional helpers for doing the work the checklists describe: test-first development, debugging, code review, hardening, accessibility, performance, documentation, and more.

- [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills): all 26 skills, in [`vendor/addyosmani/agent-skills/`](vendor/addyosmani/agent-skills/).
- [Matt Pocock's skills](https://github.com/mattpocock/skills): five standalone engineering skills (`tdd`, `diagnosing-bugs`, `codebase-design`, `domain-modeling`, `improve-codebase-architecture`), in [`vendor/mattpocock/skills/`](vendor/mattpocock/skills/).

They are copied unchanged, keep their MIT licenses, and do not change any checklist requirement. The [workflow skills guide](docs/workflow-skills.md) maps each skill to a checklist area and explains how to install one in your agent.

## Assessment and reporting templates

| Template | Use |
|---|---|
| [Assessment scope](templates/assessment-scope.md) | Define product, architecture, data, boundaries, assumptions, and exclusions. |
| [Applicability matrix](templates/applicability-matrix.md) | Record Mandatory, Recommended, Conditional, or N/A decisions with rationale. |
| [Audit scorecard](templates/audit-scorecard.md) | Record maturity scores, open findings, owners, and evidence confidence. |
| [Audit report](templates/audit-report.md) | Summarize results, findings, verification, and release readiness. |
| [Risk register](templates/risk-register.md) | Track prioritized findings, remediation, owners, and residual risk. |
| [Exception register](templates/exception-register.md) | Record approved deviations, safeguards, approvers, and review dates. |
| [Evidence register](templates/evidence-register.md) | Index evidence artifacts and how they support each control. |

Use [docs/scoring.md](docs/scoring.md) to distinguish applicability, checklist priority, finding priority, security severity, and maturity. These are separate concepts and must not be converted mechanically into one another.

## Prompts and supporting documentation

- **Prompts:** [kickoff](prompts/01-kickoff.md) · [audit](prompts/02-audit.md) · [fix findings](prompts/03-fix-findings.md) · [release readiness](prompts/04-release-readiness.md)
- **Guides:** [vibe-coding guide](docs/vibe-coding-guide.md) · [framework map](docs/framework-map.md) · [security-audit integration](docs/security-audit-integration.md)
- **References:** [standards, frameworks, and tools](references/standards.md) · [full Universal Standard](standards/universal-software-engineering-product-excellence-standard.md)
- **Agent instructions:** [AGENTS.md](AGENTS.md) · [Claude Code entry point](CLAUDE.md)

## Verification and governance

The repository includes:

- A weekly and manually triggered Markdown link-check workflow (first-party files; the vendored snapshot is excluded).
- A repository validator for checklist counts, stable IDs, required files, local Markdown links, and vendored source integrity (Cloudflare, Addy Osmani, Matt Pocock).
- Automated tests for the vendored Cloudflare findings and coverage-ledger validators.

The deterministic protocol's central principle is to encode repeatable engineering rules in types, architecture, static analysis, tests, and CI wherever that is proportionate and practical. Documentation communicates intent; it is not a substitute for enforceable controls.

## Important limits

- This framework is guidance and an assessment aid, **not a certification, legal opinion, or guarantee of security or correctness**.
- Applicability depends on product context, data, users, architecture, market, and contractual obligations. Record the rationale for N/A decisions.
- Passing automated tests or completing a checklist is not proof that every defect or vulnerability has been found.
- External standards change. Confirm the authoritative edition and scope before using a reference for formal compliance, certification, or legal decisions.
- External links are checked by the repository workflow; a local validation pass does not mean every external website was live-tested.
- First-party repository materials are licensed under Apache-2.0, subject to the scope and third-party exceptions in [LICENSE-STATUS.md](LICENSE-STATUS.md). The Cloudflare, Addy Osmani, and Matt Pocock vendor snapshots remain separately licensed under MIT; see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

## Licensing

- **First-party project materials:** [Apache License 2.0](LICENSE) (`Apache-2.0`), subject to the scope and exclusions in [LICENSE-STATUS.md](LICENSE-STATUS.md).
- **Vendored Cloudflare security-audit skill:** remains under its original [MIT License](vendor/cloudflare/security-audit-skill/LICENSE); it is not relicensed by the root license.
- **Vendored workflow skills:** Addy Osmani's [agent-skills](vendor/addyosmani/agent-skills/LICENSE) and Matt Pocock's [skills](vendor/mattpocock/skills/LICENSE) remain under their original MIT Licenses, with credit in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
- **OWASP-derived material:** remains under OWASP's [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license, with attribution in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). This project is not affiliated with or endorsed by OWASP.
- **Other external standards, specifications, trademarks, and linked resources:** remain subject to their respective owners' terms. See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

The project license applies only to first-party material that the relevant contributors are authorized to license. Public availability does not itself grant rights in third-party material.

## Reporting a vulnerability

Please do not open a public issue for a security problem. See [SECURITY.md](SECURITY.md) for how to report it privately.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should preserve stable checklist IDs, provide verifiable evidence, keep the crosswalk current, and maintain clear separation between original project materials and third-party vendor content.

---

<div align="center">

```text
               [ SYSTEM MESSAGE ]              
                                               
      TRUST IS NOT A VERIFICATION METHOD.      
          CONFIDENCE IS NOT EVIDENCE.          
A PASSING TEST IS EVIDENCE WITHIN ITS COVERAGE.
                                               
                VERIFY THE WORK.               
             DOCUMENT THE EVIDENCE.            
                OWN THE RESULT.                
                                               
              [ END TRANSMISSION ]             
```

**ENGINEERING-STANDARDS-CHECKLIST**  
*Built for developers. Designed for AI-assisted engineering. Grounded in verification.*

</div>
