# Third-party notices

## Cloudflare security-audit-skill

- **Project:** `security-audit-skill`
- **Copyright:** Copyright (c) 2025-2026 Cloudflare, Inc.
- **License:** MIT License
- **Upstream repository:** https://github.com/cloudflare/security-audit-skill
- **Bundled location:** `vendor/cloudflare/security-audit-skill/`
- **Source:** the `security-audit-skill.zip` archive supplied for this integration
- **Upstream revision:** [`c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`](https://github.com/cloudflare/security-audit-skill/commit/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) (2026-09-14, "Clarify guidance and full audit modes"); all 22 vendored files are byte-identical to that commit
- **Integrity manifest:** [`vendor/cloudflare/security-audit-skill.sha256`](vendor/cloudflare/security-audit-skill.sha256)

The 22 upstream project files are retained in their original directory structure and without edits. The original upstream `README.md`, full `LICENSE`, skill instructions, domain companions, JSON schema, validators, and validator tests are included. macOS `__MACOSX` metadata sidecars from the supplied ZIP were not included; no project source file was intentionally omitted.

The upstream MIT license permits use, copying, modification, merging, publication, distribution, sublicensing, and sale, provided its copyright and permission notice are included with copies or substantial portions. The complete notice is available at [`vendor/cloudflare/security-audit-skill/LICENSE`](vendor/cloudflare/security-audit-skill/LICENSE).

Repository-specific integration guidance is authored separately in [`docs/security-audit-integration.md`](docs/security-audit-integration.md). It does not replace, modify, or relicense the upstream skill. No endorsement by Cloudflare, Inc. is implied.

## Addy Osmani agent-skills

- **Project:** `agent-skills`
- **Copyright:** Copyright (c) 2025 Addy Osmani
- **License:** MIT License (full text at [`vendor/addyosmani/agent-skills/LICENSE`](vendor/addyosmani/agent-skills/LICENSE))
- **Upstream repository:** https://github.com/addyosmani/agent-skills
- **Upstream revision:** [`e997ac5b9a74eab332d5e9793bb38a38c8cfdd74`](https://github.com/addyosmani/agent-skills/commit/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74) (2026-11-23)
- **Bundled location:** `vendor/addyosmani/agent-skills/`
- **What is included:** the upstream `LICENSE`, all 26 folders under `skills/`, and the shared `references/` folder (59 files), byte-identical to that revision.
- **What is not included:** upstream plugin tooling (`hooks/`, `commands/`, `agents/`, `evals/`, `scripts/`, `plugin.json`) and the upstream README, top-level `AGENTS.md`, `CLAUDE.md` and `CONTRIBUTING.md`.
- **Integrity manifest:** [`vendor/addyosmani/agent-skills.sha256`](vendor/addyosmani/agent-skills.sha256)
- **Material inside this snapshot that has its own source:**
  - `skills/code-simplification/SKILL.md` states that it is inspired by and adapted from the Claude Code Simplifier plugin in [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) (Copyright Anthropic, PBC; Apache License 2.0, checked at revision `6985b2d88dc0`). The Apache-2.0 license text is included in this repository's root [`LICENSE`](LICENSE). The adaptation and its change note are Addy Osmani's and are reproduced unchanged.
  - `references/security-checklist.md` and its copies under `skills/*/references/shared/` contain quick-reference tables that use OWASP Top 10:2025 and OWASP Top 10 for LLM Applications category identifiers and names. Those portions are covered by the OWASP section below.

## Matt Pocock skills

- **Project:** `skills`
- **Copyright:** Copyright (c) 2026 Matt Pocock
- **License:** MIT License (full text at [`vendor/mattpocock/skills/LICENSE`](vendor/mattpocock/skills/LICENSE))
- **Upstream repository:** https://github.com/mattpocock/skills
- **Upstream revision:** [`6f7f7831a625f040a8e06a0e7954826b87ce775a`](https://github.com/mattpocock/skills/commit/6f7f7831a625f040a8e06a0e7954826b87ce775a) (2026-11-25)
- **Bundled location:** `vendor/mattpocock/skills/`
- **What is included:** the upstream `LICENSE` and five skill folders copied from upstream `skills/engineering/` into `skills/`: `tdd`, `diagnosing-bugs`, `codebase-design`, `domain-modeling`, and `improve-codebase-architecture` (19 files), byte-identical to that revision. Only the parent folder path changed (`skills/engineering/<name>` upstream, `skills/<name>` here).
- **What is not included:** all other upstream skills, documentation and tooling.
- **Integrity manifest:** [`vendor/mattpocock/skills.sha256`](vendor/mattpocock/skills.sha256)

## Terms common to the MIT-licensed snapshots

The MIT License permits use, copying, modification, merging, publication, distribution, sublicensing, and sale, provided the copyright notice and permission notice are included in all copies or substantial portions. Each snapshot keeps its full `LICENSE` file beside it; keep it with any copy you redistribute.

Repository-specific guidance for the workflow skills is written separately in [`docs/workflow-skills.md`](docs/workflow-skills.md) and is not part of the upstream projects. No endorsement by Addy Osmani, Matt Pocock, Cloudflare, Inc., or Anthropic, PBC is implied.

## OWASP materials (CC BY-SA)

- **Creator and copyright:** Copyright (c) 2003-2025 The OWASP(R) Foundation, Inc. and OWASP project contributors.
- **License:** Creative Commons Attribution-ShareAlike (CC BY-SA). OWASP states version 4.0 for the Top 10 and ASVS ([license text](https://creativecommons.org/licenses/by-sa/4.0/)); some OWASP projects use other CC BY-SA versions, so confirm the version at each project's own page.
- **Sources:** [OWASP Top 10:2025](https://owasp.org/Top10/), [ASVS](https://github.com/OWASP/ASVS), [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/), [Cheat Sheet Series](https://cheatsheetseries.owasp.org/), [API Security Top 10](https://owasp.org/API-Security/), [MASVS](https://mas.owasp.org/MASVS/), [AISVS](https://github.com/OWASP/AISVS), and [Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).
- **How this repository uses them:** mostly as external references (names and links). In addition, OWASP Top 10:2025 category identifiers and category names appear in `checklists/02-application-security.md` (the "Maps to" note, `SEC-05`, `SEC-10`) and `checklists/12-devops-and-supply-chain.md` (`OPS-04`). The vendored Addy Osmani snapshot also contains OWASP Top 10:2025 and OWASP Top 10 for LLM Applications quick-reference tables (`vendor/addyosmani/agent-skills/references/security-checklist.md` and its copies), and its security skill names OWASP categories. Those tables are Addy Osmani's condensed wording, distributed unchanged here.
- **Changes:** no OWASP text is reproduced verbatim as far as the maintainer is aware. Where OWASP concepts were used, they were condensed and reworded into short checklist requirements and verification steps, and combined with other material. OWASP did not review or approve these changes.
- **Scope of the license:** any OWASP-derived text in this repository, including the items listed above and any other portion later identified as adapted from OWASP, is licensed under CC BY-SA, **not** Apache-2.0. CC BY-SA requires adaptations to carry the same license, so the root Apache-2.0 license does not apply to those portions. Anyone reusing them must give OWASP credit, link to the license, indicate that changes were made, and share their own adaptations under CC BY-SA.
- **Trademark and endorsement:** OWASP(R) is a registered trademark of the OWASP Foundation, Inc. It is used here only to identify OWASP materials. This project is not affiliated with, sponsored by, or endorsed by OWASP.
- **Reporting a problem:** if you believe text here was adapted from OWASP without adequate credit, please open an issue or use [SECURITY.md](SECURITY.md) and it will be fixed or reworded promptly.

## Maintainer-supplied framework documents

The documents in `standards/` and `protocols/` were supplied by the repository maintainer for inclusion in this framework and are copied without content edits from the supplied files. Their placement in this repository does not imply that they are Cloudflare materials or covered by Cloudflare's MIT license.

## Root project license and third-party boundary

First-party materials authored for this repository by contributors with the
necessary rights are offered under the Apache License, Version 2.0
(`Apache-2.0`). See the root [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and
[`LICENSE-STATUS.md`](LICENSE-STATUS.md) for the license text, attribution, and
scope.

The root Apache-2.0 license does not replace or override licenses for third-party
components. In particular, the Cloudflare security-audit snapshot remains under
its original MIT License, retained at
[`vendor/cloudflare/security-audit-skill/LICENSE`](vendor/cloudflare/security-audit-skill/LICENSE).

External standards, specifications, names, trademarks, design galleries, and
linked resources remain subject to their respective owners' terms. The project
license does not grant rights in those materials beyond rights the relevant
contributors are authorized to grant.
