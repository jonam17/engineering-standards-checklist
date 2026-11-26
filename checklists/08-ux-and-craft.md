---
id: UX
title: UI/UX and craft
applies_when: app has a user interface
---

# 08. UI/UX and craft

**In plain English:** Make it clear, consistent, and polished. These are good habits, not legal standards.

**Applies when:** app has a user interface.

> Heuristics, not standards. Keep separate from compliance.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **UX-01** `P1` Loading, empty, error states on every view; skeletons where useful
  - *Verify:* Throttle network; force failures
- [ ] **UX-02** `P1` Destructive actions confirmed or undoable; optimistic updates roll back
  - *Verify:* Fail request mid-action
- [ ] **UX-03** `P1` Responsive with no horizontal overflow; real-device checks
  - *Verify:* iOS Safari and Android Chrome
- [ ] **UX-04** `P2` Design tokens for type, spacing, color, radius; light and dark parity
  - *Verify:* No off-scale CSS values
- [ ] **UX-05** `P2` tabular-nums for changing numbers; text-wrap: balance; optical alignment
  - *Verify:* Visual review
- [ ] **UX-06** `P2` No filler decoration (pill badges, gradient borders, blobs, random italics)
  - *Verify:* Design review
- [ ] **UX-07** `P2` Patterns researched from real products (Mobbin, Refero, galleries) and adapted, not copied
  - *Verify:* Decision notes

## Standards and tools

- [Nielsen's 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): Baseline for UX reviews.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): Platform-native behavior for Apple devices.
- [Material Design 3](https://m3.material.io/): Design system and guidance for Android and web.
- [shadcn/ui](https://ui.shadcn.com/): Copy-in React components built on accessible primitives.
- [Radix UI](https://www.radix-ui.com/): Accessible unstyled component primitives.
- [Mobbin](https://mobbin.com/): Real mobile and web app screens and flows.
- [Refero](https://refero.design/): Real product UI references.
- [Land-book](https://land-book.com/): Landing page gallery.
- [Supahero](https://supahero.io/): Hero section examples.
- [Navbar Gallery](https://navbar.gallery/): Navigation and header examples.
- [Pricing Pages](https://pricingpages.design/): SaaS pricing layouts.
- [Social Proof Examples](https://socialproofexamples.com/): Testimonials and trust elements.
- [Really Good Emails](https://reallygoodemails.com/): Transactional and marketing email design.
- [Deck Gallery](https://deck.gallery/): Presentation design.
- [OG Image Gallery](https://ogimage.gallery/): Social share card examples.
