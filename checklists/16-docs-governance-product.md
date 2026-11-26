---
id: DOC
title: Documentation, governance, product
applies_when: always
---

# 16. Documentation, governance, product

**In plain English:** Write down decisions so the project survives people changing.

**Applies when:** always.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **DOC-01** `P1` Architecture diagram, setup, deploy, env vars, runbooks, recovery steps current
  - *Verify:* New hire dry run
- [ ] **DOC-02** `P1` Code review rules, PR templates, changelog, owners for critical modules
  - *Verify:* Repo settings
- [ ] **DOC-03** `P1` No critical knowledge only in one person, undocumented prompt, or chat thread
  - *Verify:* Bus-factor check
- [ ] **DOC-04** `P2` Defined users and acceptance criteria; feedback loop; privacy-conscious analytics
  - *Verify:* Docs exist
- [ ] **DOC-05** `P2` Cost and vendor monitoring; support process; no deceptive patterns
  - *Verify:* Monthly review

## Standards and tools

- [Semantic Versioning](https://semver.org/): Version numbers that signal breaking changes.
- [Conventional Commits](https://www.conventionalcommits.org/): Commit message convention that enables automated changelogs.
- [Keep a Changelog](https://keepachangelog.com/): Human-readable changelog format.
- [DORA metrics](https://dora.dev/): Deploy frequency, lead time, change failure rate, time to restore.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework): High-level frame for organizing a security program.
- [SOC 2 (AICPA Trust Services Criteria)](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2): What B2B customers ask for first. Requires an audit; do not claim without one.
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001): Information security management system certification.
