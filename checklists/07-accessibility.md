---
id: A11
title: Accessibility (WCAG 2.2 AA)
applies_when: always
---

# 07. Accessibility (WCAG 2.2 AA)

**In plain English:** Make the app usable by people with disabilities. Also a legal requirement in many places.

**Applies when:** always.

> Also legal exposure: ADA, Section 508, EU Accessibility Act, EN 301 549.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **A11-01** `P0` Every flow keyboard operable; visible focus; no traps; logical order
  - *Verify:* Tab through without mouse
- [ ] **A11-02** `P0` Contrast 4.5:1 text, 3:1 UI; no color-only meaning
  - *Verify:* axe and manual checks
- [ ] **A11-03** `P1` Semantic HTML, labels, alt text, headings, landmarks; ARIA only when needed
  - *Verify:* axe: zero critical
- [ ] **A11-04** `P1` Forms: errors identified and announced; accessible authentication (no cognitive tests)
  - *Verify:* Screen reader walkthrough
- [ ] **A11-05** `P1` Respects prefers-reduced-motion; no flashing; works at 200% zoom and 320px width
  - *Verify:* OS setting and zoom test
- [ ] **A11-06** `P1` Targets at least 24px (aim 44px); alternatives to drag and complex gestures
  - *Verify:* Measure in DevTools
- [ ] **A11-07** `P2` VoiceOver/NVDA full-journey test; accessibility statement
  - *Verify:* Test log

## Standards and tools

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): The accessibility specification. Target Level AA.
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/): Filterable checklist. Best starting point; filter to A and AA.
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/): Plain-language explanation of each success criterion.
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/): Correct keyboard and ARIA patterns for menus, dialogs, tabs, comboboxes.
- [axe](https://www.deque.com/axe/): Automated accessibility testing.
