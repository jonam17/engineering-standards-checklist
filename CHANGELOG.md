# Changelog

This file records material repository changes. It does not replace the original source documents or upstream Cloudflare change history.

## Unreleased — framework consolidation

- Added the maintainer-supplied Universal Software Engineering & Product Excellence Standard and Deterministic Engineering & Verification Protocol as separate canonical references, copied verbatim.
- Added a framework crosswalk connecting the 16 Universal Standard disciplines to the 16 operational checklists and optional Cloudflare security modules.
- Reconciled applicability, checklist requirement priority, audit finding priority, specialist vulnerability states/severity, maturity scoring, and release gates in `docs/scoring.md`.
- Added assessment, applicability, scorecard, risk, exception, and evidence templates.
- Reworked the README as the primary navigation hub and replaced the incomplete `$IDX` in `AGENTS.md` with the 16-checklist index.
- Preserved the 22-file Cloudflare security-audit snapshot in its own vendor directory, with its original MIT license and an external checksum manifest.
- Added repository and vendor-validator CI checks.
- Selected Apache-2.0 for first-party project materials; retained Cloudflare's original MIT license and documented the separate licensing boundary.
- Corrected the README banner text and replaced the illustrative `initialize.sh` block with real validator output.
- Added `SECURITY.md` with a private vulnerability-reporting process.
- Link check now runs weekly and on demand only, excludes the vendored snapshot, treats 403/429 from bot-blocking sites as reachable, and declares read-only permissions.
- Recorded the upstream Cloudflare commit (`c1c8a8c`) matching the vendored snapshot.
- Added OWASP CC BY-SA attribution, scope, and trademark notice (`THIRD-PARTY-NOTICES.md`, `NOTICE`, `LICENSE-STATUS.md`, README, checklists 02 and 12).
- Added the maintainer's GitHub username to the `NOTICE` copyright line.
- Added optional workflow skills: Addy Osmani's `agent-skills` (all 26 skills and shared references, MIT, upstream `e997ac5`) and five standalone engineering skills from Matt Pocock's `skills` (MIT, upstream `6f7f783`), copied unchanged with licenses, checksum manifests, and credit in `THIRD-PARTY-NOTICES.md` and `NOTICE`.
- Added `docs/workflow-skills.md` mapping each workflow skill to a checklist area.
- The repository validator now checks all three vendored snapshots, requires their licenses and credits, and generates heading anchors the way GitHub does (`API & Testing` becomes `api--testing`).
- README banner now spells out "ENGINEERING STANDARDS CHECKLIST".
- Link check: excluded ftc.gov and peoplecert.org (they reject GitHub-hosted runners but load in browsers), added retries, and authenticated GitHub requests with `GITHUB_TOKEN` to avoid rate-limit errors.
- Replaced the moved "OWASP AI Security and Privacy Guide" link with the OWASP AI Exchange (`https://owaspai.org/`) in the Universal Standard; only link targets and that project's name were changed.
