# Project kickoff prompt

Paste at the start of a new project, with this repository's `AGENTS.md` (or its `CLAUDE.md` mirror) available in the project root.

```text
Read AGENTS.md first (or CLAUDE.md if that is the instruction file provided in this project). Use docs/framework-map.md to select the applicable checklists. For material implementation, follow protocols/deterministic-engineering-verification-protocol.md. Consult the Universal Standard when defining product scope, architecture, applicability, or whole-product quality objectives.

I am building: [describe the app in plain language].
Users: [who]. Data it handles: [accounts, payments, health info, children, none].
Where it will run: [host/platform]. Stack preference: [or "you choose, keep it simple"].

Before writing code:
1. Tell me which project type this is and which checklists apply.
2. List any P0 checklist requirements that affect the design (auth, data isolation, payments, backups).
3. Propose the simplest architecture that satisfies them and explain tradeoffs in plain language.
4. List the questions you need answered. Do not assume.
Wait for my approval before building.
```
