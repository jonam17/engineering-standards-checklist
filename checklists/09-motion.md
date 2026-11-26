---
id: MOT
title: Motion and interaction
applies_when: app has animation
---

# 09. Motion and interaction

**In plain English:** Use animation to explain what is happening, never to slow people down.

**Applies when:** app has animation.

> Starting values to tune by testing.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **MOT-01** `P1` Motion conveys state or hierarchy; never blocks task completion; interruptible
  - *Verify:* Rapid-click test
- [ ] **MOT-02** `P2` Micro 150-250ms, standard 200-350ms, exits about 20% faster, stagger 30-50ms, press scale 0.97-0.99
  - *Verify:* Review motion tokens
- [ ] **MOT-03** `P2` Popovers anchored to trigger; safe-triangle for nested menus; hit slop on small targets
  - *Verify:* Manual test
- [ ] **MOT-04** `P2` Animate transform and opacity only; no layout shift from motion
  - *Verify:* Performance panel

## Standards and tools

- [Motion](https://motion.dev/): Animation library (formerly Framer Motion).
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): Platform-native behavior for Apple devices.
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/): Correct keyboard and ARIA patterns for menus, dialogs, tabs, comboboxes.
