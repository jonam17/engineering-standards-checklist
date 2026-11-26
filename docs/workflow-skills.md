# Optional workflow skills

This repository bundles two sets of third-party agent skills as **optional
workflow aids**. They help an AI coding agent carry out the work that the
checklists ask for (writing tests first, debugging, reviewing, hardening,
documenting). They are not part of the core standard, they do not add or change
checklist requirements, and passing a skill's workflow is not evidence that a
checklist item is met. Each checklist item's own *Verify* step still decides that.

Both sets are copied verbatim from their upstream repositories, keep their
original MIT licenses, and are credited in
[THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md). They are not relicensed
under this repository's Apache-2.0 license, and no endorsement by their authors
is implied.

| Source | Author | License | Location in this repo |
|---|---|---|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | MIT | [`vendor/addyosmani/agent-skills/`](../vendor/addyosmani/agent-skills/) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock | MIT | [`vendor/mattpocock/skills/`](../vendor/mattpocock/skills/) |

## How to use them

1. Pick the checklist area you are working on, then find the matching skill in the
   table below.
2. Copy that skill's folder (the folder containing `SKILL.md`) into your agent's
   skills directory, for example `.claude/skills/<skill-name>/`. For Addy Osmani's
   skills, also keep the skill's own `references/` folder, which is already inside
   the skill folder.
3. Keep the upstream `LICENSE` file with any copy you distribute.
4. Load only the skills a task needs. Do not run every skill on every change.

The Cloudflare `security-audit` skill remains the specialist option for an
explicitly requested full security audit; see the
[security-audit integration guide](security-audit-integration.md).

## Skill map by checklist area

| Checklist area | Addy Osmani (`agent-skills`) | Matt Pocock (`skills`) |
|---|---|---|
| [01 Architecture](../checklists/01-architecture.md) | [api-and-interface-design](../vendor/addyosmani/agent-skills/skills/api-and-interface-design/SKILL.md), [code-simplification](../vendor/addyosmani/agent-skills/skills/code-simplification/SKILL.md), [deprecation-and-migration](../vendor/addyosmani/agent-skills/skills/deprecation-and-migration/SKILL.md) | [codebase-design](../vendor/mattpocock/skills/skills/codebase-design/SKILL.md), [improve-codebase-architecture](../vendor/mattpocock/skills/skills/improve-codebase-architecture/SKILL.md), [domain-modeling](../vendor/mattpocock/skills/skills/domain-modeling/SKILL.md) |
| [02 Application security](../checklists/02-application-security.md) | [security-and-hardening](../vendor/addyosmani/agent-skills/skills/security-and-hardening/SKILL.md) | — |
| [05 APIs and integrations](../checklists/05-apis-and-integrations.md) | [api-and-interface-design](../vendor/addyosmani/agent-skills/skills/api-and-interface-design/SKILL.md) | — |
| [07 Accessibility](../checklists/07-accessibility.md) | [accessibility-engineering](../vendor/addyosmani/agent-skills/skills/accessibility-engineering/SKILL.md), [frontend-ui-engineering](../vendor/addyosmani/agent-skills/skills/frontend-ui-engineering/SKILL.md) | — |
| [08 UX and craft](../checklists/08-ux-and-craft.md) | [frontend-ui-engineering](../vendor/addyosmani/agent-skills/skills/frontend-ui-engineering/SKILL.md), [browser-testing-with-devtools](../vendor/addyosmani/agent-skills/skills/browser-testing-with-devtools/SKILL.md) | — |
| [10 Performance](../checklists/10-performance.md) | [performance-optimization](../vendor/addyosmani/agent-skills/skills/performance-optimization/SKILL.md) | — |
| [11 Testing](../checklists/11-testing.md) | [test-driven-development](../vendor/addyosmani/agent-skills/skills/test-driven-development/SKILL.md), [browser-testing-with-devtools](../vendor/addyosmani/agent-skills/skills/browser-testing-with-devtools/SKILL.md) | [tdd](../vendor/mattpocock/skills/skills/tdd/SKILL.md) |
| [12 DevOps and supply chain](../checklists/12-devops-and-supply-chain.md) | [ci-cd-and-automation](../vendor/addyosmani/agent-skills/skills/ci-cd-and-automation/SKILL.md), [git-workflow-and-versioning](../vendor/addyosmani/agent-skills/skills/git-workflow-and-versioning/SKILL.md), [shipping-and-launch](../vendor/addyosmani/agent-skills/skills/shipping-and-launch/SKILL.md) | — |
| [13 Observability and reliability](../checklists/13-observability-and-reliability.md) | [observability-and-instrumentation](../vendor/addyosmani/agent-skills/skills/observability-and-instrumentation/SKILL.md), [debugging-and-error-recovery](../vendor/addyosmani/agent-skills/skills/debugging-and-error-recovery/SKILL.md) | [diagnosing-bugs](../vendor/mattpocock/skills/skills/diagnosing-bugs/SKILL.md) |
| [14 AI and agents](../checklists/14-ai-and-agents.md) | [context-engineering](../vendor/addyosmani/agent-skills/skills/context-engineering/SKILL.md), [source-driven-development](../vendor/addyosmani/agent-skills/skills/source-driven-development/SKILL.md), [doubt-driven-development](../vendor/addyosmani/agent-skills/skills/doubt-driven-development/SKILL.md) | — |
| [16 Docs, governance, and product](../checklists/16-docs-governance-product.md) | [documentation-and-adrs](../vendor/addyosmani/agent-skills/skills/documentation-and-adrs/SKILL.md), [spec-driven-development](../vendor/addyosmani/agent-skills/skills/spec-driven-development/SKILL.md), [planning-and-task-breakdown](../vendor/addyosmani/agent-skills/skills/planning-and-task-breakdown/SKILL.md) | [domain-modeling](../vendor/mattpocock/skills/skills/domain-modeling/SKILL.md) |
| Any change (process) | [incremental-implementation](../vendor/addyosmani/agent-skills/skills/incremental-implementation/SKILL.md), [code-review-and-quality](../vendor/addyosmani/agent-skills/skills/code-review-and-quality/SKILL.md), [constraint-driven-development](../vendor/addyosmani/agent-skills/skills/constraint-driven-development/SKILL.md), [interview-me](../vendor/addyosmani/agent-skills/skills/interview-me/SKILL.md), [idea-refine](../vendor/addyosmani/agent-skills/skills/idea-refine/SKILL.md), [using-agent-skills](../vendor/addyosmani/agent-skills/skills/using-agent-skills/SKILL.md) | — |

Areas 03, 04, 06, 09 and 15 have no dedicated skill; use the checklists directly.

## What was included and why

- **Addy Osmani — all 26 skills plus the shared `references/` folder.** The skills
  refer to each other and to the shared references by name, so they are kept
  together. Upstream plugin tooling (`hooks/`, `commands/`, `agents/`, `evals/`,
  `scripts/`, `plugin.json`) and the upstream README were not included because
  they are specific to installing that project as a plugin and are not needed to
  read or copy the skills.
- **Matt Pocock — 5 of his engineering skills:** `tdd`, `diagnosing-bugs`,
  `codebase-design`, `domain-modeling`, and `improve-codebase-architecture`.
  These work on their own. His other engineering skills depend on his
  `setup-matt-pocock-skills` configuration and an issue-tracker setup, so they
  are better installed from his repository directly.

Upstream revisions and integrity manifests are recorded in
[THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md). Three illustrative links in
Matt Pocock's `domain-modeling/GLOSSARY-FORMAT.md` point to an example project
layout; the repository validator allow-lists them rather than editing upstream
text.

## Updating a snapshot

1. Copy the new upstream files over the vendored folder without editing them.
2. Regenerate the checksum manifest, for example
   `find vendor/addyosmani/agent-skills -type f | LC_ALL=C sort | xargs sha256sum > vendor/addyosmani/agent-skills.sha256`.
3. Record the new upstream commit in `THIRD-PARTY-NOTICES.md`, review the diff and
   the upstream license, and check for newly added third-party material.
4. Run `python3 scripts/validate_repository.py`.
