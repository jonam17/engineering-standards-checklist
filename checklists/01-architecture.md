---
id: ARC
title: Architecture and code quality
applies_when: always
---

# 01. Architecture and code quality

**In plain English:** Keep the code organized so it can be changed safely later.

**Applies when:** always.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **ARC-01** `P1` Clear separation of UI, business logic, data access; single source of truth for critical logic
  - *Verify:* Review module boundaries; no business rules in UI code
- [ ] **ARC-02** `P1` Strict typing, linter, formatter enforced in CI
  - *Verify:* CI fails on violations
- [ ] **ARC-03** `P1` Config separated per environment; no hardcoded env values
  - *Verify:* Grep; deploy to staging with only env changes
- [ ] **ARC-04** `P1` Reproducible setup: README, lockfile, one-command dev environment
  - *Verify:* Fresh machine runs in under 30 minutes
- [ ] **ARC-05** `P2` ADRs for major decisions; dead code and unused deps removed
  - *Verify:* Docs exist; knip/depcheck clean
- [ ] **ARC-06** `P2` Money stored as integer or decimal; timestamps in UTC; i18n and browser support matrix decided
  - *Verify:* Review schema; test non-US locale and oldest supported browser

## Standards and tools

- [Twelve-Factor App](https://12factor.net/): Foundations for config, logging, statelessness, deploys.
- [Semantic Versioning](https://semver.org/): Version numbers that signal breaking changes.
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/): Free review questions per pillar.
- [Azure Well-Architected](https://learn.microsoft.com/azure/well-architected/): Same idea for Azure.
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework): Same idea for Google Cloud.
