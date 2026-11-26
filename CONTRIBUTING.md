# Contributing

Contributions should improve the framework without weakening traceability, evidence quality, safety, or licensing clarity.

## Where to make changes

- `standards/` contains the Universal Standard and defines broad product and engineering expectations.
- `protocols/` contains the deterministic development and verification methodology.
- `checklists/` contains operational requirements with stable IDs and individual verification steps.
- `docs/framework-map.md` connects the Universal Standard to checklists and specialist material.
- `docs/` contains navigation, scoring, and implementation guidance.
- `prompts/` provides copy-paste instructions for AI coding agents.
- `templates/` provides reusable assessment and governance artifacts.
- `references/` contains external standards, frameworks, tools, and design resources.
- `vendor/` contains third-party material. Do not edit vendored source in place.

## Checklist requirements

Every new checklist item must have:

1. A stable ID (`PREFIX-NN`).
2. A requirement priority (`P0`, `P1`, or `P2`) consistent with the existing checklist convention.
3. One specific, testable requirement.
4. A *Verify* line describing how a person or tool can check it.
5. A relevant source/standard citation where the requirement derives from an external source.

Do not renumber or reuse IDs. Deprecate an item rather than deleting or recycling its identifier. Update the README and `AGENTS.md` counts, keep `CLAUDE.md` byte-identical to `AGENTS.md`, and update `docs/framework-map.md` and relevant prompts/templates whenever checklist structure changes.

## Framework and scoring consistency

- Keep the four applicability classifications (Mandatory, Recommended, Conditional, N/A) consistent with the Universal Standard.
- Keep checklist requirement priority, audit finding priority, vulnerability severity, and maturity score distinct; see `docs/scoring.md`.
- Use evidence-based language. Distinguish requirements from recommendations and house-style preferences.
- Do not claim external-standard equivalence or compliance without a verified mapping to the named edition and control set.
- Update navigation links when a canonical document moves or is renamed.

## Source and licensing requirements

- Cite the standard, source, or original project when incorporating externally derived material.
- By submitting a contribution for inclusion, contributors confirm they have the rights needed to submit it and agree that the contribution is offered under Apache-2.0, unless a separate written agreement applies. Identify third-party material and its license before inclusion.
- Review license and attribution requirements before adding code, content, datasets, fonts, icons, images, design assets, or documentation from third parties.
- Preserve all copyright and license notices.
- Material adapted from OWASP is CC BY-SA, not Apache-2.0. Reword into original text where practical; otherwise credit OWASP, indicate changes, and record it in the OWASP section of `THIRD-PARTY-NOTICES.md`.
- Do not modify files under `vendor/addyosmani/` or `vendor/mattpocock/`. To update a snapshot, follow [docs/workflow-skills.md](docs/workflow-skills.md#updating-a-snapshot): copy upstream unchanged, regenerate the checksum manifest, record the new commit in `THIRD-PARTY-NOTICES.md`, and rerun the validator.
- Do not modify files under `vendor/cloudflare/security-audit-skill/`. Propose an upstream update as a reviewed replacement, retain the MIT notice, update the checksum manifest, document the source revision if known, and rerun tests.
- Do not copy substantial proprietary standards text. Link to authoritative sources and write original summaries or requirements.
- First-party materials are licensed under Apache-2.0, subject to `LICENSE-STATUS.md`; third-party components retain their own licenses as documented in `THIRD-PARTY-NOTICES.md`.

## Verification before pull request

Run the repository validator:

```bash
python3 scripts/validate_repository.py
```

Run the Cloudflare vendor validator tests when the vendor files, integration, or associated workflow changes:

```bash
node --test \
  vendor/cloudflare/security-audit-skill/skills/security-audit/validate-findings.test.cjs \
  vendor/cloudflare/security-audit-skill/skills/security-audit/validate-coverage-ledger.test.cjs
```

Also run a Markdown link check before opening a pull request. Local repository validation checks internal paths; the GitHub Actions workflow checks Markdown links, including external references.

## Writing and review expectations

- Keep one canonical home for each concept; link to it rather than duplicating rules across documents.
- Preserve source terminology when quoting or incorporating source documents.
- Make scope, assumptions, limitations, and review date clear.
- Mark opinions and design heuristics as house style, not formal compliance controls.
- Include a short change note for material updates and identify any migration needed by downstream users.
