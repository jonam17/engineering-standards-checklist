---
id: DAT
title: Data and backend
applies_when: app stores data
---

# 04. Data and backend

**In plain English:** Keep data correct, private, backed up, and recoverable.

**Applies when:** app stores data.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **DAT-01** `P0` Backups automated and encrypted; restore tested with RTO/RPO written down
  - *Verify:* Timed restore to scratch environment
- [ ] **DAT-02** `P0` Row-level security or equivalent tenant isolation on every table
  - *Verify:* Cross-tenant query returns nothing
- [ ] **DAT-03** `P0` Idempotency keys on payments and non-repeatable writes
  - *Verify:* Double-click: one charge, one row
- [ ] **DAT-04** `P1` DB constraints (FK, unique, not null) plus server validation; transactions for multi-step writes
  - *Verify:* Violate each constraint deliberately
- [ ] **DAT-05** `P1` Migrations versioned, reviewed, reversible or expand/contract
  - *Verify:* Migrate and roll back in staging
- [ ] **DAT-06** `P1` Timeouts, retries with backoff and jitter, queues with dead-letter handling
  - *Verify:* Kill a dependency; system degrades gracefully
- [ ] **DAT-07** `P1` Pagination and query limits; indexes on hot paths
  - *Verify:* EXPLAIN on top queries
- [ ] **DAT-08** `P1` Retention, deletion, and export procedures; encryption at rest; PII out of logs
  - *Verify:* Run deletion on test user
- [ ] **DAT-09** `P2` Concurrency and partial-failure reconciliation jobs
  - *Verify:* Race test passes

## Standards and tools

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): Concrete how-to for each control: password storage, CSRF, sessions, SSRF, and more.
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/): Free review questions per pillar.
- [Google SRE books](https://sre.google/books/): SLOs, error budgets, blameless postmortems.
