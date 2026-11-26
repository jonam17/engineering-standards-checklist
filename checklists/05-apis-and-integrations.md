---
id: API
title: APIs and integrations
applies_when: app exposes or calls APIs
---

# 05. APIs and integrations

**In plain English:** Make connections between systems predictable and safe when something fails.

**Applies when:** app exposes or calls APIs.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **API-01** `P0` Webhook signatures verified; replay window and event dedupe
  - *Verify:* Unsigned and replayed payloads rejected
- [ ] **API-02** `P1` Documented contract (OpenAPI/GraphQL schema); input and output validation; consistent errors
  - *Verify:* Contract tests green
- [ ] **API-03** `P1` Rate limits, body size limits, GraphQL depth/cost limits
  - *Verify:* Burst test returns 429
- [ ] **API-04** `P1` Third-party responses treated as untrusted; timeouts; graceful degradation
  - *Verify:* Block provider: app stays usable
- [ ] **API-05** `P1` Scoped, rotatable credentials per integration
  - *Verify:* Rotation drill documented
- [ ] **API-06** `P2` Versioning and deprecation policy; quota monitoring; vendor exit plan
  - *Verify:* Policy documented

## Standards and tools

- [OWASP API Security Top 10](https://owasp.org/API-Security/): Risks specific to APIs (object-level authorization, excessive data exposure, etc.).
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html): Machine-readable API contracts.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): Concrete how-to for each control: password storage, CSRF, sessions, SSRF, and more.
