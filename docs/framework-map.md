# Framework map and standards crosswalk

This document is the navigation layer between the Universal Standard, the 16 operational checklists, and the optional Cloudflare security-audit skill.

**Purpose and limitation:** This is an internal navigation crosswalk. It is not a formal mapping to external controls, proof of equivalence, a certification, or a compliance claim. External-standard mappings must identify the exact edition and control set and be independently validated.

## How to use the map

1. Identify the product, users, data, architecture, deployment model, and material risks.
2. Read the relevant discipline in the [Universal Standard](../standards/universal-software-engineering-product-excellence-standard.md).
3. Load the operational checklist(s) listed below.
4. Apply applicability classifications and record reasons for conditional or N/A decisions.
5. Use the optional specialist security skill only when its explicit trigger and safety prerequisites are met.

## Universal Standard to operational checklist map

| Universal Standard section | Discipline | Operational checklist | Notes and optional specialist coverage |
|---|---|---|---|
| 5.1 | Architecture and engineering quality | [01 Architecture](../checklists/01-architecture.md) | Architecture boundaries, maintainability, type/static enforcement, and technical debt. |
| 5.2 | Security engineering | [02 Application Security](../checklists/02-application-security.md); [03 Authentication and Authorization](../checklists/03-authentication-authorization.md) | Add [12 DevOps](../checklists/12-devops-and-supply-chain.md) and [14 AI and Agents](../checklists/14-ai-and-agents.md) when applicable. Specialist modules include web/auth, client-side, cloud, protocols, resource exhaustion, and supply chain. |
| 5.3 | Data and backend engineering | [04 Data and Backend](../checklists/04-data-and-backend.md) | Specialist [data isolation and lifecycle](../vendor/cloudflare/security-audit-skill/skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md) is conditional on an explicit security investigation. |
| 5.4 | APIs and integrations | [05 APIs and Integrations](../checklists/05-apis-and-integrations.md) | Specialist coverage includes web protocols, RPC, messaging, and client-side integrations. |
| 5.5 | UI, UX, and visual design | [08 UX and Craft](../checklists/08-ux-and-craft.md) | Design inspiration is research material, not a compliance standard. |
| 5.6 | Motion and interaction design | [09 Motion](../checklists/09-motion.md) | Also consider [07 Accessibility](../checklists/07-accessibility.md) and reduced-motion behavior. |
| 5.7 | Accessibility and inclusive design | [07 Accessibility](../checklists/07-accessibility.md) | Manual testing remains necessary; the security skill does not provide a dedicated accessibility checklist. |
| 5.8 | Performance and scalability | [10 Performance](../checklists/10-performance.md) | Specialist resource-exhaustion guidance is for security-related availability risks, not a replacement for performance engineering. |
| 5.9 | Testing and quality assurance | [11 Testing](../checklists/11-testing.md) | Follow the deterministic protocol for risk-based verification and truthful test reporting. |
| 5.10 | Search and discoverability | [15 SEO and Discoverability](../checklists/15-seo-and-discoverability.md) | Applies principally to public-facing websites and discoverable content. |
| 5.11 | DevOps and release engineering | [12 DevOps and Supply Chain](../checklists/12-devops-and-supply-chain.md) | Specialist coverage includes cloud/deployment and supply-chain/release security. |
| 5.12 | Observability and reliability | [13 Observability and Reliability](../checklists/13-observability-and-reliability.md) | Specialist resource-exhaustion guidance can supplement availability threat analysis. |
| 5.13 | Privacy, legal, regulatory, and intellectual property | [06 Privacy, Legal, and Compliance](../checklists/06-privacy-legal-compliance.md); [16 Documentation, Governance, and Product](../checklists/16-docs-governance-product.md) | Vendor skill is not legal advice. Legal applicability and licensing questions need qualified review. |
| 5.14 | AI, machine learning, and autonomous agents | [14 AI and Agents](../checklists/14-ai-and-agents.md) | Specialist [AI and LLM](../vendor/cloudflare/security-audit-skill/skills/security-audit/AI-AND-LLM.md) module applies to security audits of LLM-backed systems. |
| 5.15 | Documentation and engineering governance | [16 Documentation, Governance, and Product](../checklists/16-docs-governance-product.md) | Also follow contribution, exception, evidence, and document-control guidance. |
| 5.16 | Product strategy and user trust | [16 Documentation, Governance, and Product](../checklists/16-docs-governance-product.md); [08 UX and Craft](../checklists/08-ux-and-craft.md) | Product outcomes and interaction quality are assessed together where scope overlaps. |

## Specialist security domain index

The Cloudflare skill is a separate optional subsystem. The table below helps select domain companions after the upstream `SKILL.md` trigger conditions have been met.

| Specialist domain file | Typical trigger | Related core checklist |
|---|---|---|
| [AI-AND-LLM.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/AI-AND-LLM.md) | LLMs, retrieval, model tools, agent permissions, prompt injection | 14, plus 02/03/04 as relevant |
| [WEB-PROTOCOL-AND-AUTH.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/WEB-PROTOCOL-AND-AUTH.md) | HTTP framing, cache behavior, auth protocols | 02, 03, 05 |
| [CLIENT-SIDE.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/CLIENT-SIDE.md) | DOM, browser messaging, UI redress, prototype pollution | 02, 05, 08 |
| [CLOUD-AND-DEPLOYMENT.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/CLOUD-AND-DEPLOYMENT.md) | Cloud IAM, containers, serverless, ingress, runtime configuration | 12, 13 |
| [DATA-ISOLATION-AND-LIFECYCLE.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md) | Multi-tenancy, caches, exports, backups, migrations, deletion, restore | 03, 04, 06 |
| [SUPPLY-CHAIN-AND-RELEASE.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md) | Dependencies, CI, release, signing, updates, extensions | 12 |
| [RESOURCE-EXHAUSTION-AND-AVAILABILITY.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md) | Shared resources, quotas, queues, worker spend, availability boundaries | 10, 13 |
| [PROTOCOLS-RPC-AND-MESSAGING.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md) | RPC, serialization, queues, brokers, webhooks, streaming | 05, 12, 13 |
| [DESKTOP-MOBILE-AND-LOCAL-IPC.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md) | Native apps, deep links, WebViews, exported components, local IPC | 02, 03, 05; also OWASP MASVS for mobile |
| [MEMORY-SAFETY-AND-BINARY.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/MEMORY-SAFETY-AND-BINARY.md) | Native memory-unsafe languages, binary formats, kernel or low-level components | 02, 11, 12 |

**Coverage limitation:** The specialist skill is not a universal application audit. It does not replace dedicated mobile, accessibility, privacy/legal, UX, performance, product, or operational checklists. Use the relevant core documents for those areas.

## Specialist workflow and support files

The domain companions are used alongside these upstream workflow documents. Load the upstream `SKILL.md` first and follow its phase order; do not cherry-pick around its safety gates during full audit mode.

| Upstream file | Role |
|---|---|
| [SKILL.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md) | Trigger conditions, operating modes, safety rules, and six-phase overview. |
| [RECONNAISSANCE.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/RECONNAISSANCE.md) | Phase 1 discovery and coverage-ledger initialization. |
| [HUNTING.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/HUNTING.md) | Phase 2 coverage-led vulnerability hunting and review. |
| [ATTACK-CLASSES.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/ATTACK-CLASSES.md) | Core and supplemental attack-class prompts. |
| [VALIDATION-AND-REPORTING.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/VALIDATION-AND-REPORTING.md) | Phases 3–6: candidate validation, structured output, independent review, and reports. |
| [report-schema.json](../vendor/cloudflare/security-audit-skill/skills/security-audit/report-schema.json) | Machine-readable findings schema. |
| `validate-findings.cjs` and `validate-coverage-ledger.cjs` | Zero-dependency validators for specialist audit artifacts. |
| Corresponding `*.test.cjs` files | Upstream validator regression tests. |

## Optional workflow skills

Third-party workflow skills from Addy Osmani and Matt Pocock are mapped to checklist areas in [workflow-skills.md](workflow-skills.md). They support doing the work; they are not part of this crosswalk's requirements.

## Crosswalk maintenance

When adding or renaming a checklist:

- Preserve existing stable IDs; deprecate rather than reuse identifiers.
- Update this crosswalk and the README/AGENTS navigation tables.
- Confirm each Universal Standard discipline has at least one appropriate destination or explicitly document the gap.
- Do not claim an external standards-control mapping unless it has been verified against the cited edition.
