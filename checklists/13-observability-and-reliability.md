---
id: OBS
title: Observability and reliability
applies_when: always once deployed
---

# 13. Observability and reliability

**In plain English:** Know when it breaks, why, and how to recover.

**Applies when:** always once deployed.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **OBS-01** `P0` Error monitoring and uptime alerts reach a human
  - *Verify:* Trigger test alert
- [ ] **OBS-02** `P1` Structured logs with trace IDs and PII redaction; retention set
  - *Verify:* Sample log review
- [ ] **OBS-03** `P1` Actionable alerts by severity; runbooks; incident process; post-incident reviews
  - *Verify:* Drill held
- [ ] **OBS-04** `P1` SLIs/SLOs for critical journeys; dependency and queue health dashboards
  - *Verify:* Dashboard live
- [ ] **OBS-05** `P2` DR drills, error budgets, capacity planning
  - *Verify:* Calendar and notes

## Standards and tools

- [OpenTelemetry](https://opentelemetry.io/): Vendor-neutral traces, metrics and logs.
- [Google SRE books](https://sre.google/books/): SLOs, error budgets, blameless postmortems.
- [DORA metrics](https://dora.dev/): Deploy frequency, lead time, change failure rate, time to restore.
