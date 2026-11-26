# Release readiness prompt

```text
Do a release-readiness review using AGENTS.md (or CLAUDE.md if that is the provided instruction file), the applicable checklists, and the release-readiness phase in the Universal Standard. Apply docs/scoring.md; do not let averages offset P0 findings or the Security, Data, and Accessibility maturity gates.

Confirm with evidence: no open P0 items, build and tests pass, secrets scan clean, dependency scan has no unresolved high or critical issues, backups restored successfully at least once where relevant, rollback is documented and tested where applicable, monitoring and alerts reach a human, and accessibility checks pass on the main user journeys.

Any permitted open P1 finding requires documented mitigation, accountable risk-owner approval, residual risk, and a review/expiry date.

Give a clear Ready / Not ready / Conditional / Not determined verdict and list what I must verify myself (real devices, payments in test mode, legal copy, anything you cannot run). Distinguish verified, failed, not run, N/A, and known limitations.
```
