---
id: AUT
title: Authentication and authorization
applies_when: app has user accounts
---

# 03. Authentication and authorization

**In plain English:** Make sure only the right people can sign in and see only their own stuff.

**Applies when:** app has user accounts.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **AUT-01** `P0` Server-side authorization on every object and action; deny by default (IDOR)
  - *Verify:* User A requests user B resources: 403/404
- [ ] **AUT-02** `P0` Passwords hashed with Argon2id or bcrypt; breached-password check; no composition rules theater
  - *Verify:* Code review; DB inspection
- [ ] **AUT-03** `P1` Login, reset, signup rate-limited; no account enumeration via messages or timing
  - *Verify:* Same response for known and unknown email
- [ ] **AUT-04** `P1` Sessions rotate on login/privilege change, expire, revocable; cookies HttpOnly Secure SameSite
  - *Verify:* DevTools; logout invalidates server-side
- [ ] **AUT-05** `P1` MFA offered; required for admins and sensitive actions
  - *Verify:* Admin login demands second factor
- [ ] **AUT-06** `P1` Least privilege roles; admin routes separate and audited
  - *Verify:* Role matrix test
- [ ] **AUT-07** `P2` OAuth/OIDC with PKCE and state validation
  - *Verify:* Library defaults reviewed

## Standards and tools

- [NIST SP 800-63 (Digital Identity)](https://pages.nist.gov/800-63-4/): Authoritative password, session and authenticator rules (length over composition rules, breached-password checks).
- [WebAuthn and passkeys](https://passkeys.dev/): Phishing-resistant sign-in; the industry direction for strong authentication.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): Concrete how-to for each control: password storage, CSRF, sessions, SSRF, and more.
- [OWASP ASVS 5.0](https://github.com/OWASP/ASVS): Testable security requirements at levels L1/L2/L3. Aim for L2 in production. CSV/JSON export available.
