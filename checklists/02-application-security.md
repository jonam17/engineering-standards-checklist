---
id: SEC
title: Application security
applies_when: always
---

# 02. Application security

**In plain English:** Stop attackers from breaking in, stealing data, or abusing your app.

**Applies when:** always.

> Maps to OWASP Top 10:2025 (SSRF now sits inside Broken Access Control).

> OWASP Top 10:2025 identifiers and category references: Copyright The OWASP Foundation, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); not covered by this repository's Apache-2.0 license. See [THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md#owasp-materials-cc-by-sa).

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **SEC-01** `P0` No secrets in repo, client bundle, logs, or error reports
  - *Verify:* gitleaks in CI; grep built JS
- [ ] **SEC-02** `P0` All queries parameterized; ORM raw queries reviewed
  - *Verify:* Grep string-built SQL; sqlmap smoke test
- [ ] **SEC-03** `P0` Output context-encoded (XSS); user HTML sanitized
  - *Verify:* Inject script payloads in every field
- [ ] **SEC-04** `P0` HTTPS only, HSTS, TLS 1.2+ (1.3 preferred)
  - *Verify:* SSL Labs A; http redirects
- [ ] **SEC-05** `P0` Errors fail closed and never leak stacks or internals (A10:2025)
  - *Verify:* Force 500s and malformed input; generic response
- [ ] **SEC-06** `P1` CSRF defense and SameSite cookies; CORS allowlist, never wildcard with credentials
  - *Verify:* Cross-origin request rejected
- [ ] **SEC-07** `P1` CSP, nosniff, frame-ancestors, Referrer-Policy; SRI on third-party scripts
  - *Verify:* Header scan clean
- [ ] **SEC-08** `P1` SSRF, path traversal, open redirect protections
  - *Verify:* Request cloud metadata IP: blocked; ../ rejected
- [ ] **SEC-09** `P1` Uploads: size, extension, magic-byte checks; stored outside web root
  - *Verify:* Upload disguised exe: rejected
- [ ] **SEC-10** `P1` Security events logged and alerted (A09:2025)
  - *Verify:* Failed logins and permission denials appear in alerts
- [ ] **SEC-11** `P2` Threat model, SAST/DAST in CI, pen test by risk, security.txt published
  - *Verify:* Artifacts exist

## Standards and tools

- [OWASP Top 10:2025](https://owasp.org/Top10/): Awareness list of the 10 most critical web app risks. Start here.
- [OWASP ASVS 5.0](https://github.com/OWASP/ASVS): Testable security requirements at levels L1/L2/L3. Aim for L2 in production. CSV/JSON export available.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): Concrete how-to for each control: password storage, CSRF, sessions, SSRF, and more.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): How to test for each vulnerability class. Source of rigorous "Verify" steps.
- [Threat Modeling Cheat Sheet (STRIDE)](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html): Simple structure for threat modeling before building.
- [OWASP ZAP](https://www.zaproxy.org/): Dynamic scanning (DAST) and proxy.
- [Semgrep](https://semgrep.dev/): Static analysis (SAST) with community rules.
- [gitleaks](https://github.com/gitleaks/gitleaks): Secret scanning for repos and CI.
