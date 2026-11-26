---
id: PRV
title: Privacy, legal, compliance
applies_when: always (scope varies by users, data, jurisdiction)
---

# 06. Privacy, legal, compliance

**In plain English:** Follow the laws and be honest about privacy and security. Get counsel review.

**Applies when:** always (scope varies by users, data, jurisdiction).

> Applicability depends on users, data, and jurisdiction; get counsel review.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **PRV-01** `P0` If PHI/PII is touched: HIPAA/GDPR/CCPA scoping done, BAAs/DPAs signed, no PHI in logs or analytics
  - *Verify:* Data-flow map approved
- [ ] **PRV-02** `P0` Accurate privacy policy and terms; no false compliance or security claims (SOC 2, HIPAA)
  - *Verify:* Copy reviewed against reality
- [ ] **PRV-03** `P0` Card data via hosted fields or processor (limits PCI scope); never store PAN or CVV
  - *Verify:* Network and DB inspection
- [ ] **PRV-04** `P1` One-click online cancellation; clear pricing and renewal terms (ROSCA and state auto-renewal laws; verify current FTC rule status, the 2024 click-to-cancel rule was vacated in 2025)
  - *Verify:* Cancel a test subscription unaided
- [ ] **PRV-05** `P1` Email: unsubscribe, postal address, SPF, DKIM, DMARC aligned
  - *Verify:* Mail-tester and DMARC report
- [ ] **PRV-06** `P1` Cookie consent with real Reject; no non-essential trackers before consent
  - *Verify:* Network tab pre-consent
- [ ] **PRV-07** `P1` Data export and deletion; breach response plan with notification deadlines
  - *Verify:* Tabletop done
- [ ] **PRV-08** `P1` Licenses audited (no AGPL surprises); fonts, images, AI-generated assets cleared
  - *Verify:* license-checker report
- [ ] **PRV-09** `P2` COPPA/age gating if minors; subprocessor list; privacy impact assessment
  - *Verify:* Documents exist

## Standards and tools

- [GDPR (EU 2016/679)](https://eur-lex.europa.eu/eli/reg/2016/679/oj): EU privacy law. Applies if you serve EU residents.
- [CCPA/CPRA](https://oag.ca.gov/privacy/ccpa): California privacy law.
- [HIPAA](https://www.hhs.gov/hipaa/): US health data law. Applies if you handle PHI for covered entities.
- [PCI DSS 4.0.1](https://www.pcisecuritystandards.org/): Card data security. Hosted payment fields shrink your scope.
- [COPPA](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy): US rules for children under 13.
- [CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business): US commercial email rules.
- [SOC 2 (AICPA Trust Services Criteria)](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2): What B2B customers ask for first. Requires an audit; do not claim without one.
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001): Information security management system certification.
- Also search for: EU Accessibility Act, EN 301 549 (accessibility); EU AI Act and Cyber Resilience Act (dates are still shifting, verify current timelines).
