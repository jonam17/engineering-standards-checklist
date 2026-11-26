# Assessment model: applicability, priorities, severity, and maturity

This document reconciles the assessment models used by the Universal Standard, the original operational checklists, and the optional Cloudflare security-audit skill. These models answer different questions and must remain distinct.

## 1. Applicability classification

Classify each Universal Standard discipline or control before scoring it.

| Classification | Meaning | Required treatment |
|---|---|---|
| **Mandatory** | Needed for a material risk, contractual obligation, legal duty, or baseline quality expectation. | Implement and verify. Exceptions require documented approval and compensating controls where possible. |
| **Recommended** | A recognized practice that materially improves quality, maintainability, usability, or operational maturity. | Implement where practical; otherwise document the rationale and review it periodically. |
| **Conditional** | Applies only when a stated technology, feature, data type, deployment model, or regulatory context is present. | Evaluate the trigger and apply the control when the condition is met. |
| **N/A** | No meaningful relationship to the current product scope or risks. | Record the reason and reassess when the product changes. |

Do not use N/A merely because a control is difficult to verify or not yet implemented. Use **Not verified** when evidence is unavailable.

## 2. Checklist requirement priority (P0–P2)

The priorities embedded in the 16 original checklists are **requirement/remediation priorities**. Preserve their existing values and stable item IDs unless the project maintainer approves a separately reviewed change.

| Priority | Existing checklist meaning |
|---|---|
| **P0** | Blocks release. A critical requirement that must be satisfied or the affected capability must remain disabled. |
| **P1** | Fix before launch or within the defined remediation window (the original convention uses 30 days). |
| **P2** | Backlog or planned improvement, subject to context and risk. |

These values are a project convention, not priorities defined by OWASP, NIST, WCAG, ISO, or another external standard.

## 3. Audit finding priority (P0–P3)

The Universal Standard uses a four-level finding-priority model for material audit findings. This is separate from the static priority attached to a checklist requirement.

| Priority | Finding meaning | Typical response |
|---|---|---|
| **P0 — Critical** | Active exploitation, catastrophic exposure, severe safety risk, irreversible data corruption, or a critical failure making the product unsafe or unusable. | Contain immediately; disable affected capability if necessary; escalate and verify remediation before normal operation resumes. |
| **P1 — High** | Serious security, privacy, integrity, accessibility, reliability, or business risk with material impact. | Expedite remediation; apply temporary mitigations and define an accountable resolution path. |
| **P2 — Moderate** | Meaningful weakness or quality gap with limited exposure, workable mitigation, or lower likelihood of severe impact. | Schedule in a planned improvement cycle and track to completion. |
| **P3 — Low** | Minor defect, polish opportunity, maintainability improvement, or low-impact deviation. | Backlog and address according to value and capacity. |

Assess impact, likelihood, exploitability, exposure, reach, persistence, detectability, recoverability, and compensating controls. Record the rationale. Do not mechanically convert a checklist item's P0/P1/P2 into a finding priority.

## 4. Specialist vulnerability severity and candidate state

The optional Cloudflare security-audit skill uses a distinct vulnerability model:

- Candidate states: `confirmed`, `needs_validation`, and `rejected`.
- Only `confirmed` vulnerabilities receive a severity rating.
- `needs_validation` means a specific, source-grounded hypothesis is blocked by an unresolved fact; it has no severity.
- `rejected` records a candidate that independent validation disproved.
- Confirmed vulnerability severity uses `critical`, `high`, `medium`, `low`, or `informational` according to the upstream skill's evidence and impact anchors.

Do not map these severity values automatically to the Universal Standard's P0–P3 priorities. Follow the original [upstream skill](../vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md) and preserve its schema and validators.

For ordinary checklist assessments, use the result states in the [audit report template](../templates/audit-report.md): `Pass`, `Fail`, `Not verified`, or `N/A` with a reason.

## 5. Maturity score (0–5)

Use the Universal Standard's maturity definitions across discipline-level scorecards.

| Score | Level | Description |
|---:|---|---|
| **0** | Absent | No meaningful implementation or evidence exists. |
| **1** | Ad hoc | Practices are informal, inconsistent, reactive, or dependent on individuals. |
| **2** | Partial | Some controls exist, but coverage, ownership, repeatability, or verification is incomplete. |
| **3** | Defined | Controls are documented, assigned, implemented consistently, and verified in normal workflows. |
| **4** | Measured | Performance and effectiveness are measured; exceptions and trends are reviewed. |
| **5** | Optimized | Controls are continually improved using evidence, automation, feedback, and changing risk. |

Score only applicable disciplines and controls. Base scores on evidence, not intent or confidence. Mark genuinely non-applicable areas N/A with a written reason. Where evidence is missing, do not assume effectiveness.

A high average does not prove that a product is secure, compliant, accessible, or ready for release. Report P0/P1 findings separately; do not let high scores offset critical risk.

## 6. Evidence and result states

For each checklist item, report one of the following:

- **Pass:** the acceptance criterion was checked and supported by evidence.
- **Fail:** the acceptance criterion was checked and not met.
- **Not verified:** the check could not be completed or evidence was insufficient; explain why.
- **N/A:** the requirement does not apply to the assessed scope; record the rationale.

For implementation work, the Deterministic Protocol additionally distinguishes checks that were **Verified**, **Failed**, **Not run**, **Not applicable**, and **Known limitations**. Do not mark an activity complete because it was only planned.

Evidence may include source/configuration, architecture and data-flow diagrams, tests and CI output, scan results, performance measurements, deployment/recovery records, policies, or direct observation. Evidence must support the specific acceptance criterion.

## 7. Release-readiness gates

Apply the strict gates from the original scoring model alongside the Universal Standard's risk-acceptance guidance:

1. **Any open P0 finding means Not release-ready.** Contain or resolve the risk, or keep the affected capability disabled.
2. **Security, Data, or Accessibility maturity below 3 means Not release-ready** under the original checklist framework's gate. A written exception must not silently override this gate; any proposed change to this rule requires an explicit governance decision.
3. An open **P1** finding may remain only with documented mitigation, accountable risk-owner approval, scope, residual risk, and review/expiry date. Acceptance of a P1 does not override either gate above.
4. A release decision must also review build/test status, secrets and dependency findings, backups and recovery where relevant, rollback, monitoring, approvals, and applicable legal/privacy/accessibility obligations.
5. Mark unrun checks and limitations explicitly. Do not state “ready” when material verification remains incomplete without an approved, documented basis.

## 8. Standard audit sequence

For a whole-product assessment, follow the Universal Standard's ten phases:

1. Discovery and scope.
2. Baseline and evidence collection.
3. Standards mapping and applicability.
4. Technical and product audit.
5. Risk assessment.
6. Remediation roadmap.
7. Controlled implementation.
8. Verification and regression.
9. Release readiness.
10. Continuous improvement.

For normal implementation work, follow the shorter [Deterministic Engineering & Verification Protocol](../protocols/deterministic-engineering-verification-protocol.md). For an explicit comprehensive security audit, follow the Cloudflare skill's separate six-phase specialist process.

## 9. Related resources

- [Universal Software Engineering & Product Excellence Standard](../standards/universal-software-engineering-product-excellence-standard.md)
- [Deterministic Engineering & Verification Protocol](../protocols/deterministic-engineering-verification-protocol.md)
- [Framework crosswalk](framework-map.md)
- [Audit report template](../templates/audit-report.md)
- [Scorecard template](../templates/audit-scorecard.md)
- [Security-audit integration guide](security-audit-integration.md)
