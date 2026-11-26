# Fix findings prompt

```text
Fix the findings in the audit report, P0 first. Follow protocols/deterministic-engineering-verification-protocol.md, including its correction-to-constraint feedback loop.

Rules:
- One finding at a time, smallest change that works, preserve existing behavior.
- Run the relevant tests before and after. If there are no tests for it, add one.
- Never weaken a check or test to make it pass.
- After each fix, show the item ID, what changed, and the evidence it now passes.
- Evaluate whether the root cause should be prevented through types, schemas, architecture, static analysis, tests, or CI. Add the smallest proportionate guardrail where justified.
- Stop and ask me before database changes on live data, deleting anything, changing sign-in, or taking another destructive or irreversible action.
- Report checks not run and remaining limitations honestly.
```
