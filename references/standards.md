# Standards and references

Every link used in the checklists, grouped by purpose. Verify currency before relying on any version number. A checklist is not a certification: for formal compliance, evaluate the actual standard.

## Security standards

| Resource | Use it for |
|---|---|
| [OWASP Top 10:2025](https://owasp.org/Top10/) | Awareness list of the 10 most critical web app risks. Start here. |
| [OWASP ASVS 5.0](https://github.com/OWASP/ASVS) | Testable security requirements at levels L1/L2/L3. Aim for L2 in production. CSV/JSON export available. |
| [OWASP API Security Top 10](https://owasp.org/API-Security/) | Risks specific to APIs (object-level authorization, excessive data exposure, etc.). |
| [OWASP MASVS](https://mas.owasp.org/MASVS/) | Mobile app security requirements (iOS/Android). |
| [NIST SSDF (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure software development practices across the lifecycle. |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | High-level frame for organizing a security program. |

## Security guidance

| Resource | Use it for |
|---|---|
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Concrete how-to for each control: password storage, CSRF, sessions, SSRF, and more. |
| [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | How to test for each vulnerability class. Source of rigorous "Verify" steps. |
| [Threat Modeling Cheat Sheet (STRIDE)](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | Simple structure for threat modeling before building. |
| [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Hardening baselines for cloud, OS, containers, databases. |

## Identity

| Resource | Use it for |
|---|---|
| [NIST SP 800-63 (Digital Identity)](https://pages.nist.gov/800-63-4/) | Authoritative password, session and authenticator rules (length over composition rules, breached-password checks). |
| [WebAuthn and passkeys](https://passkeys.dev/) | Phishing-resistant sign-in; the industry direction for strong authentication. |

## Vulnerability prioritization

| Resource | Use it for |
|---|---|
| [CVSS](https://www.first.org/cvss/) | Technical severity score. Not a substitute for business risk. |
| [EPSS](https://www.first.org/epss/) | Probability a vulnerability will be exploited soon. |
| [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Vulnerabilities actively exploited now. Treat as urgent. |

## Supply chain

| Resource | Use it for |
|---|---|
| [SLSA](https://slsa.dev/) | Build integrity and provenance levels. |
| [OpenSSF Scorecard](https://scorecard.dev/) | Automatically grades a repo's security practices. |
| [SPDX](https://spdx.dev/) | SBOM format (also ISO standardized). |
| [CycloneDX](https://cyclonedx.org/) | SBOM format popular in security tooling. |

## Accessibility

| Resource | Use it for |
|---|---|
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | The accessibility specification. Target Level AA. |
| [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | Filterable checklist. Best starting point; filter to A and AA. |
| [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) | Plain-language explanation of each success criterion. |
| [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Correct keyboard and ARIA patterns for menus, dialogs, tabs, comboboxes. |

## UX and design

| Resource | Use it for |
|---|---|
| [Nielsen's 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) | Baseline for UX reviews. |
| [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | Platform-native behavior for Apple devices. |
| [Material Design 3](https://m3.material.io/) | Design system and guidance for Android and web. |
| [shadcn/ui](https://ui.shadcn.com/) | Copy-in React components built on accessible primitives. |
| [Radix UI](https://www.radix-ui.com/) | Accessible unstyled component primitives. |
| [Motion](https://motion.dev/) | Animation library (formerly Framer Motion). |

## Design inspiration

| Resource | Use it for |
|---|---|
| [Mobbin](https://mobbin.com/) | Real mobile and web app screens and flows. |
| [Refero](https://refero.design/) | Real product UI references. |
| [Land-book](https://land-book.com/) | Landing page gallery. |
| [Supahero](https://supahero.io/) | Hero section examples. |
| [Navbar Gallery](https://navbar.gallery/) | Navigation and header examples. |
| [Pricing Pages](https://pricingpages.design/) | SaaS pricing layouts. |
| [Social Proof Examples](https://socialproofexamples.com/) | Testimonials and trust elements. |
| [Really Good Emails](https://reallygoodemails.com/) | Transactional and marketing email design. |
| [Deck Gallery](https://deck.gallery/) | Presentation design. |
| [OG Image Gallery](https://ogimage.gallery/) | Social share card examples. |

## Performance

| Resource | Use it for |
|---|---|
| [Core Web Vitals](https://web.dev/articles/vitals) | LCP, INP, CLS targets measured at the 75th percentile. |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse) | Automated performance, accessibility and SEO audits. |

## Delivery and reliability

| Resource | Use it for |
|---|---|
| [Twelve-Factor App](https://12factor.net/) | Foundations for config, logging, statelessness, deploys. |
| [DORA metrics](https://dora.dev/) | Deploy frequency, lead time, change failure rate, time to restore. |
| [Google SRE books](https://sre.google/books/) | SLOs, error budgets, blameless postmortems. |
| [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) | Free review questions per pillar. |
| [Azure Well-Architected](https://learn.microsoft.com/azure/well-architected/) | Same idea for Azure. |
| [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) | Same idea for Google Cloud. |
| [Semantic Versioning](https://semver.org/) | Version numbers that signal breaking changes. |
| [Conventional Commits](https://www.conventionalcommits.org/) | Commit message convention that enables automated changelogs. |
| [Keep a Changelog](https://keepachangelog.com/) | Human-readable changelog format. |

## Observability

| Resource | Use it for |
|---|---|
| [OpenTelemetry](https://opentelemetry.io/) | Vendor-neutral traces, metrics and logs. |

## APIs

| Resource | Use it for |
|---|---|
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Machine-readable API contracts. |

## Privacy and legal

| Resource | Use it for |
|---|---|
| [GDPR (EU 2016/679)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | EU privacy law. Applies if you serve EU residents. |
| [CCPA/CPRA](https://oag.ca.gov/privacy/ccpa) | California privacy law. |
| [HIPAA](https://www.hhs.gov/hipaa/) | US health data law. Applies if you handle PHI for covered entities. |
| [COPPA](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) | US rules for children under 13. |
| [CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) | US commercial email rules. |
| [PCI DSS 4.0.1](https://www.pcisecuritystandards.org/) | Card data security. Hosted payment fields shrink your scope. |

## Compliance frameworks

| Resource | Use it for |
|---|---|
| [SOC 2 (AICPA Trust Services Criteria)](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) | What B2B customers ask for first. Requires an audit; do not claim without one. |
| [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Information security management system certification. |

## AI

| Resource | Use it for |
|---|---|
| [OWASP AISVS 1.0](https://github.com/OWASP/AISVS) | Testable security requirements for AI systems (released June 2026). Aim for L2. |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | Awareness list for LLM-specific risks. |
| [MITRE ATLAS](https://atlas.mitre.org/) | Catalog of adversary tactics against AI systems. |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | AI risk governance. |

## Search and discoverability

| Resource | Use it for |
|---|---|
| [Google Search Central](https://developers.google.com/search/docs) | Official crawling, indexing and structured data guidance. |
| [Schema.org](https://schema.org/) | Structured data vocabulary. |
| [Open Graph protocol](https://ogp.me/) | Social preview metadata. |

## Tools

| Resource | Use it for |
|---|---|
| [gitleaks](https://github.com/gitleaks/gitleaks) | Secret scanning for repos and CI. |
| [Semgrep](https://semgrep.dev/) | Static analysis (SAST) with community rules. |
| [OWASP ZAP](https://www.zaproxy.org/) | Dynamic scanning (DAST) and proxy. |
| [Trivy](https://trivy.dev/) | Scans dependencies, containers and IaC. |
| [axe](https://www.deque.com/axe/) | Automated accessibility testing. |
| [Playwright](https://playwright.dev/) | End-to-end browser testing. |

