# Guide for non-programmers building with AI

You do not need to read every line of code. You do need to make the AI prove its work.

## Setup (5 minutes)

1. Put this repo's `AGENTS.md` in your project's root folder. For Claude Code, also save a copy named `CLAUDE.md`. Cursor, Codex, and most agent tools read `AGENTS.md` or accept it as rules.
2. Keep the `checklists/` folder alongside it so the AI can read the details.
3. Start with `prompts/01-kickoff.md`.

## The loop

1. **Kickoff:** AI classifies your project and proposes a simple plan. You approve.
2. **Build in small pieces.** Ask for one feature at a time.
3. **Audit** with `prompts/02-audit.md` after each major milestone and always before launch.
4. **Fix** with `prompts/03-fix-findings.md`, P0 first.
5. **Release check** with `prompts/04-release-readiness.md`.

## What the AI cannot do for you

- Test on a real phone, with real screen readers, or with real payments.
- Decide what the law requires of your business. Ask a lawyer, especially for health data, children's data, payments, and subscriptions.
- Know that a claim is true just because it said so. Require evidence: command output, screenshots, test results.

## Red flags in AI answers

- "This should work" or "I've fixed it" with no test run.
- Secrets or API keys pasted into code or chat.
- Turning off a security feature "to make it work."
- Deleting or rewriting tests to get them to pass.
- Inventing a library, setting, or law that you cannot find online.
- Huge rewrites when you asked for a small change.

## Glossary

| Term | Meaning |
|---|---|
| Authentication | Proving who you are (signing in) |
| Authorization | What you are allowed to do or see |
| IDOR | Changing an ID in a URL to see someone else's data |
| XSS | Attackers injecting scripts into your pages |
| CSRF | Tricking a signed-in user's browser into taking an action |
| SQL injection | Attackers sneaking database commands through input fields |
| Rate limiting | Capping how fast one user or bot can make requests |
| Secret | A password or API key the app needs; never put in code |
| RLS | Row-level security: the database itself restricts who sees which rows |
| Idempotency | Doing something twice has the same result as once (no double charges) |
| SBOM | Ingredient list of every library your software uses |
| CI/CD | Automatic checks and deployment when code changes |
| RTO/RPO | How fast you must recover, and how much data loss is acceptable |
| WCAG | The accessibility standard; target level AA |
| Core Web Vitals | Google's speed and stability measures for web pages |
| PHI/PII | Health information / personal information; triggers legal duties |
| P0/P1/P2 | This repo's severity levels; P0 blocks release |
