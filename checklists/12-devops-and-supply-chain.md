---
id: OPS
title: DevOps and supply chain
applies_when: always once deployed
---

# 12. DevOps and supply chain

**In plain English:** Ship safely, repeatably, and be able to undo a bad release.

**Applies when:** always once deployed.

> SLSA, NIST SSDF.

> OWASP Top 10:2025 identifiers and category references: Copyright The OWASP Foundation, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); not covered by this repository's Apache-2.0 license. See [THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md#owasp-materials-cc-by-sa).

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **OPS-01** `P0` CI/CD with protected branches and reviews; deploy credentials scoped and secret
  - *Verify:* Settings audit
- [ ] **OPS-02** `P1` Dependency, secret, container, and IaC scanning; lockfiles committed; versions pinned
  - *Verify:* No high/critical open
- [ ] **OPS-03** `P1` Preview environments; staged rollouts or feature flags; health checks; tested rollback
  - *Verify:* Roll back in under 15 minutes
- [ ] **OPS-04** `P1` Infrastructure as code; least-privilege cloud IAM; no public buckets or default creds (A02:2025)
  - *Verify:* Config scan
- [ ] **OPS-05** `P2` SBOM generated; build provenance (SLSA); drift detection
  - *Verify:* Artifacts stored

## Standards and tools

- [SLSA](https://slsa.dev/): Build integrity and provenance levels.
- [NIST SSDF (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final): Secure software development practices across the lifecycle.
- [OpenSSF Scorecard](https://scorecard.dev/): Automatically grades a repo's security practices.
- [SPDX](https://spdx.dev/): SBOM format (also ISO standardized).
- [CycloneDX](https://cyclonedx.org/): SBOM format popular in security tooling.
- [Trivy](https://trivy.dev/): Scans dependencies, containers and IaC.
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks): Hardening baselines for cloud, OS, containers, databases.
- [CVSS](https://www.first.org/cvss/): Technical severity score. Not a substitute for business risk.
- [EPSS](https://www.first.org/epss/): Probability a vulnerability will be exploited soon.
- [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): Vulnerabilities actively exploited now. Treat as urgent.
- [DORA metrics](https://dora.dev/): Deploy frequency, lead time, change failure rate, time to restore.
- [Semgrep](https://semgrep.dev/): Static analysis (SAST) with community rules.
- [gitleaks](https://github.com/gitleaks/gitleaks): Secret scanning for repos and CI.
