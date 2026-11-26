# AGENTS.md — Engineering framework entry point

This file is mirrored verbatim as `CLAUDE.md` for Claude Code. Keep both files identical; repository validation enforces the mirror.

Read this file first. It routes AI coding agents to the appropriate framework documents; it is not a substitute for reading the relevant source material.

## Canonical sources and loading order

1. **Always follow repository and user instructions.** Resolve material conflicts explicitly; never silently weaken a security, data-integrity, or release requirement.
2. **For material code changes, use the [Deterministic Engineering & Verification Protocol](protocols/deterministic-engineering-verification-protocol.md).** It defines inspection, planning, baseline, implementation, verification, and correction-to-constraint feedback.
3. **Use [docs/framework-map.md](docs/framework-map.md) to select applicable checklists.** Load only relevant files; do not read every checklist by default.
4. **Use the [Universal Software Engineering & Product Excellence Standard](standards/universal-software-engineering-product-excellence-standard.md)** for whole-product assessments, scope and applicability decisions, evidence expectations, risk prioritization, maturity scoring, governance, or when the task materially changes system architecture or product behavior.
5. **Use [docs/scoring.md](docs/scoring.md) and the applicable [templates](templates/) when recording audit results.** Keep applicability, checklist priority, finding priority, security severity, and maturity separate.
6. **Use the optional Cloudflare security-audit skill only under its stated trigger conditions.** Do not run a full specialist audit for routine implementation or a narrow security question.

## Non-negotiable operating rules

1. **Preserve existing behavior and public contracts.** Do not remove features, change APIs, data formats, or critical workflows without explicit approval.
2. **Inspect before changing.** Understand architecture, relevant files, dependencies, conventions, and current behavior before editing.
3. **Prefer deterministic guardrails.** When proportionate, enforce recurring requirements with types, schemas, architecture boundaries, static analysis, tests, and CI—not prose alone.
4. **Verify before claiming completion.** Report exactly which checks ran and their outcomes. Never claim unexecuted checks passed.
5. **Protect security and data.** Never commit secrets, weaken authentication or validation, bypass authorization, expose sensitive data, or weaken tests to obtain a passing result.
6. **Treat accessibility as functionality.** Include relevant keyboard, semantic, assistive-technology, responsive, and reduced-motion checks.
7. **Avoid unjustified complexity.** Do not add dependencies, services, abstractions, custom tooling, or unrelated refactors without a concrete benefit.
8. **Do not invent facts.** Verify versions, API behavior, legal requirements, standard editions, or URLs using authoritative sources, or state that they remain unverified.
9. **Do not claim certification or compliance because a checklist passes.** State scope, edition, evidence, and limitations for any assessment claim.
10. **Ask before destructive, irreversible, costly, or legally consequential actions.** This includes production data changes, deletion, live payment operations, security testing of systems without authorization, and material legal copy.

## Standard development workflow

1. **Classify and scope:** identify project type, task risk, affected users, data, routes, modules, APIs, integrations, and public contracts.
2. **Select controls:** use the project-type guide and framework map to load relevant checklists. Record conditional and N/A decisions with reasons when performing an assessment.
3. **Plan:** identify the change, applicable checklist IDs, likely regressions, dependencies, and verification strategy.
4. **Baseline:** inspect repository state and run relevant existing checks before modifying code when feasible.
5. **Implement incrementally:** preserve established architecture and conventions; add or update tests with the change.
6. **Verify:** run checks proportionate to scope and risk. Inspect runtime behavior when the change affects runtime functionality or user experience.
7. **Correct the guardrail:** for meaningful recurring defects or agent mistakes, consider whether types, architecture, linting, tests, or CI can prevent recurrence.
8. **Report:** use the [audit report](templates/audit-report.md) for assessments. Distinguish Verified, Failed, Not run, Not applicable, and Known limitations.

## Project-type checklist selection

Start with the relevant row, then add conditional checklists based on actual features and deployment context.

| Project type | Core checklists to load |
|---|---|
| Marketing or landing site | 01, 02, 06, 07, 08, 09, 10, 15, 16; add 12 and 13 once deployed |
| Web app or SaaS with accounts | 01–13 and 16; add 15 for public pages |
| E-commerce | Web app/SaaS set; assess payment scope. `PRV-03` is P0 when cardholder-data processing is in scope. |
| API or backend service | 01–06, 11–13, 16 |
| Mobile app | Relevant web-app controls plus OWASP MASVS; see `references/standards.md`; note that no dedicated mobile checklist is currently included |
| Internal tool | 01–05, 07, 11–13; add 06 and 16 according to data and governance context |
| Uses AI, LLMs, ML, or agents | Add 14 to the applicable project set |

This table is a starting point, not a substitute for applicability assessment. The framework map explains the relationship between the Universal Standard and the 16 operational checklists.

## Checklist index

| # | Checklist | File | ID prefix | Items |
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

Total: **16 checklists, 101 unique checklist items**. Stable IDs must not be renumbered; deprecate rather than reuse an ID.

## Optional specialist security-audit skill

The core checklists are the default for general engineering reviews. Use the vendor skill as follows:

- **Guidance mode:** focused security questions, narrow code reviews, vulnerability triage, or investigation of an individual finding. Load only the relevant portions; do not automatically create full audit artifacts.
- **Full audit mode:** only for an explicit comprehensive codebase security audit, penetration-test review, end-to-end security review, or requested full audit artifacts. Follow the upstream six-phase workflow exactly.
- Read [the integration guide](docs/security-audit-integration.md), then the original [upstream README](vendor/cloudflare/security-audit-skill/README.md) and [SKILL.md](vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md).
- Preserve the vendor subtree unchanged, including its MIT license. Keep repository-specific guidance outside it.
- Apply the root Apache-2.0 license only to first-party materials whose contributors have the rights to license them; never imply it overrides vendor or other third-party terms. Preserve each third-party license and attribution notice.
- Full mode requires the capabilities and OS-enforced sandbox defined by the upstream skill. If they are unavailable, do not execute target-controlled code and do not claim a complete audit.
- Never probe production endpoints, shared infrastructure, real accounts, or other users' data.

## Optional workflow skills

- Third-party skills from Addy Osmani and Matt Pocock are bundled under `vendor/addyosmani/` and `vendor/mattpocock/`. See [the workflow skills guide](docs/workflow-skills.md) for which skill matches which checklist area.
- Load a workflow skill only when it fits the task. They are aids, not requirements: completing a skill's workflow never replaces a checklist item's *Verify* step.
- Do not edit files under `vendor/`. Keep each snapshot's MIT `LICENSE` with any copy.

## When to stop and ask a human

Stop and obtain explicit human direction before:

- Deleting data, files, resources, or user content where recovery is uncertain.
- Modifying production databases, migrations, or live infrastructure.
- Making live payment, purchase, billing, or subscription changes.
- Changing authentication, account recovery, access-control policy, or security boundaries in a way that could lock users out or expand access.
- Handling health, children's, financial, or similarly sensitive data beyond approved scope.
- Performing security tests against systems without explicit authorization and the required isolation controls.
- Making legal, regulatory, certification, or contractual representations.
- Proceeding with unresolved P0 risk or materially weakening a required control.

## Completion report

For each task, state:

- What changed and which checklist IDs or standard sections were relevant.
- Checks actually run, with pass/fail outcomes.
- Checks not run and why.
- Known limitations, assumptions, and residual risks.
- Any guardrails added or recommended to prevent recurrence.

Never invent evidence, test results, approvals, or deployment status.
