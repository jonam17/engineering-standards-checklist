# Optional security-audit integration

## Purpose and relationship to the framework

The 16 core checklists and 101 items are the baseline engineering review system. The Universal Standard defines whole-product quality expectations, and the Deterministic Protocol defines verification-first implementation practice. The Cloudflare `security-audit` skill is an optional specialist vulnerability-investigation workflow; it does not replace any of those components.

The original upstream snapshot is retained under [`vendor/cloudflare/security-audit-skill/`](../vendor/cloudflare/security-audit-skill/). Read its [upstream README](../vendor/cloudflare/security-audit-skill/README.md) and [SKILL.md](../vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md) for authoritative usage instructions. The source subtree must remain unmodified; keep local integration notes outside it.

## Operating modes

- **Guidance mode:** for a security question, focused code review, vulnerability triage, or a specific finding. Load only relevant sections. Do not automatically launch all phases or create audit artifacts.
- **Full audit mode:** only when the user explicitly requests a comprehensive codebase security audit, penetration-test review, end-to-end review, or full audit artifacts. Follow the complete upstream six-phase workflow and terminal-state requirements.

If the requested scope is ambiguous between focused guidance and a full audit, ask one focused question before creating artifacts or launching the full process, as required by the upstream skill.

## Prerequisites and safety gates

A complete specialist run requires all capabilities specified by the upstream `SKILL.md`, including:

1. An agent environment supporting the required parent/delegated-agent roles and write isolation.
2. Node.js for the included zero-dependency findings and coverage-ledger validators.
3. An OS-enforced sandbox for target-controlled builds, tests, browsers, emulators, fuzzers, processes, and fixtures. The upstream skill specifies no external network, a sanitized allowlisted environment, resource limits, and write isolation.
4. Dummy principals, synthetic data, and local fixtures. Do not probe production endpoints, shared infrastructure, real accounts, or other users' data.

A normal working directory or a prose promise not to access files is not an OS-enforced sandbox. If the required isolation cannot be demonstrated, do not execute target-controlled code. Continue with source inspection only where appropriate, record the exact missing capability as `needs_validation`, and report the run as incomplete.

## How this fits the core checklists

Use the relevant core checklists for ordinary engineering reviews, especially:

- `02-application-security.md`
- `03-authentication-authorization.md`
- `04-data-and-backend.md`
- `05-apis-and-integrations.md`
- `12-devops-and-supply-chain.md`
- `14-ai-and-agents.md` when AI/LLM/agent behavior is in scope

Use [docs/framework-map.md](framework-map.md) to choose specialist domain companions. The specialist skill has no dedicated accessibility, UX, legal/privacy, product, or comprehensive mobile compliance checklist; use the core framework and relevant external standards for those concerns.

## Keep reporting models separate

The Cloudflare skill uses `confirmed`, `needs_validation`, and `rejected` candidate states. Only confirmed vulnerabilities receive `critical`, `high`, `medium`, `low`, or `informational` severity. A `needs_validation` record has no severity.

Do not mechanically convert these to checklist P0/P1/P2 priorities, Universal Standard P0/P1/P2/P3 finding priorities, or 0–5 maturity scores. See [docs/scoring.md](scoring.md).

## Running the supplied validator tests

From the repository root, with a compatible Node.js version:

```bash
node --test \
  vendor/cloudflare/security-audit-skill/skills/security-audit/validate-findings.test.cjs \
  vendor/cloudflare/security-audit-skill/skills/security-audit/validate-coverage-ledger.test.cjs
```

The repository CI workflow runs these tests when the vendored skill or its workflow changes. The repository does not claim that a successful validator test constitutes a security audit of a target application.

## Optional skill installation

If an agent only discovers skills in its conventional project skill directory, create a working copy from the vendored source. Do not move or edit the vendored original. For example:

```bash
mkdir -p .claude/skills
cp -R vendor/cloudflare/security-audit-skill/skills/security-audit .claude/skills/
```

For Codex-style project skills:

```bash
mkdir -p .agents/skills
cp -R vendor/cloudflare/security-audit-skill/skills/security-audit .agents/skills/
```

Refresh any working copy only from a reviewed vendor update. Preserve upstream notices in all copies.

## Provenance, copyright, and updates

- The vendored source is distributed under the MIT license. Retain its full [`LICENSE`](../vendor/cloudflare/security-audit-skill/LICENSE) and copyright notice with all copies or substantial portions.
- The vendored snapshot is byte-identical to upstream commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` (2026-09-14). Check upstream for newer revisions before relying on it as current.
- The [SHA-256 manifest](../vendor/cloudflare/security-audit-skill.sha256) records file integrity for the vendored snapshot. Recompute and review the manifest only when intentionally updating the vendor copy.
- Before updating, compare against the official [Cloudflare repository](https://github.com/cloudflare/security-audit-skill), review the complete diff and licensing, preserve notices, and rerun validator tests.
- No endorsement by Cloudflare, Inc. is implied.
- The root project's first-party materials are separately licensed under Apache-2.0; this does not change the vendor skill's MIT license. See [LICENSE-STATUS.md](../LICENSE-STATUS.md) and [THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md).
