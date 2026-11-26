---
id: AI
title: AI and agents (if applicable)
applies_when: app uses LLMs, ML, or autonomous agents
---

# 14. AI and agents (if applicable)

**In plain English:** Keep AI features from being tricked, running wild, or being trusted too much.

**Applies when:** app uses LLMs, ML, or autonomous agents.

> OWASP AISVS 1.0 (aim L2 for production), NIST AI RMF, ISO/IEC 42001.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **AI-01** `P0` Model output never trusted as input or authorization; validate against schema before acting
  - *Verify:* Adversarial output test
- [ ] **AI-02** `P0` Prompt injection (direct and indirect) defenses; untrusted content isolated from instructions
  - *Verify:* Red-team prompts in retrieved docs
- [ ] **AI-03** `P0` Agents least-privilege; human approval for sensitive or irreversible actions; audit trail
  - *Verify:* Attempt out-of-scope tool call
- [ ] **AI-04** `P1` Retry caps, loop prevention, token and cost limits, per-user quotas
  - *Verify:* Runaway test halts
- [ ] **AI-05** `P1` Eval suite for accuracy, hallucination, grounding; prompt and model versions pinned; regression on change
  - *Verify:* Eval run in CI
- [ ] **AI-06** `P1` No sensitive data to model vendors without terms; AI use disclosed where required
  - *Verify:* Vendor and policy review
- [ ] **AI-07** `P2` Drift, cost, latency monitoring; fallback non-AI path; bias testing where relevant
  - *Verify:* Dashboard

## Standards and tools

- [OWASP AISVS 1.0](https://github.com/OWASP/AISVS): Testable security requirements for AI systems (released June 2026). Aim for L2.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): Awareness list for LLM-specific risks.
- [MITRE ATLAS](https://atlas.mitre.org/): Catalog of adversary tactics against AI systems.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): AI risk governance.
