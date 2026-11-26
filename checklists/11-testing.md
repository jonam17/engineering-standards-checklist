---
id: TST
title: Testing and QA
applies_when: always
---

# 11. Testing and QA

**In plain English:** Prove it works, instead of trusting that it does.

**Applies when:** always.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **TST-01** `P0` Critical flows (auth, payments, data writes) covered by automated tests that gate deploys
  - *Verify:* CI blocks on failure
- [ ] **TST-02** `P1` Unit, integration, E2E, API contract, migration tests; flaky tests tracked
  - *Verify:* Test pyramid report
- [ ] **TST-03** `P1` Regression: baseline before change, test adjacent features, desktop and mobile
  - *Verify:* Checklist per release
- [ ] **TST-04** `P1` Security and accessibility checks automated (axe, SCA, SAST)
  - *Verify:* Pipeline output
- [ ] **TST-05** `P2` Visual regression, property/fuzz testing for parsers, mutation testing for critical logic
  - *Verify:* Used where justified

## Standards and tools

- [Playwright](https://playwright.dev/): End-to-end browser testing.
- [axe](https://www.deque.com/axe/): Automated accessibility testing.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): How to test for each vulnerability class. Source of rigorous "Verify" steps.
- [OWASP ZAP](https://www.zaproxy.org/): Dynamic scanning (DAST) and proxy.
