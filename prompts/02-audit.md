# Audit prompt

```text
Read AGENTS.md (or CLAUDE.md if that is the provided instruction file) and the checklists that apply to this project. Use docs/framework-map.md to map applicable Universal Standard disciplines to the operational checklists. For a whole-product assessment, use the Universal Standard's ten-phase workflow. Apply the applicability, finding-priority, maturity, and release-gate models in docs/scoring.md.

Audit the codebase. For every applicable item: run its Verify step or inspect the code, then mark Pass, Fail, Not verified, or N/A with a reason. Cite the item ID and evidence (file, line, command output). Do not give credit for things that only appear to exist. Do not fix anything yet.

Output using templates/audit-report.md. List P0 findings first. End with what you could not verify.

Do not silently switch a focused security review into a full specialist audit. For an explicitly requested comprehensive security audit, read docs/security-audit-integration.md and follow the vendored Cloudflare skill only if all of its agent, Node.js, and OS-enforced sandbox prerequisites are available.
```
