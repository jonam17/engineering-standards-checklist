---
id: PRF
title: Performance and scalability
applies_when: always for public web apps
---

# 10. Performance and scalability

**In plain English:** Make it fast on real phones and slow connections.

**Applies when:** always for public web apps.

Priority: `P0` blocks release, `P1` fix before launch or within 30 days, `P2` backlog. See [scoring](../docs/scoring.md).

## Checklist

- [ ] **PRF-01** `P1` LCP 2.5s or less, INP 200ms or less, CLS 0.1 or less at p75 on mobile
  - *Verify:* PageSpeed and field data
- [ ] **PRF-02** `P1` Images sized, modern formats, lazy-loaded; fonts subset; third-party scripts justified
  - *Verify:* Lighthouse audits
- [ ] **PRF-03** `P1` Caching and CDN set; sensitive pages not publicly cacheable
  - *Verify:* Cache-Control review
- [ ] **PRF-04** `P1` Load test at expected peak plus margin; spend and abuse caps on costly endpoints
  - *Verify:* Test report
- [ ] **PRF-05** `P2` Bundle budget, code splitting, profiling of memory and CPU
  - *Verify:* CI budget check

## Standards and tools

- [Core Web Vitals](https://web.dev/articles/vitals): LCP, INP, CLS targets measured at the 75th percentile.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse): Automated performance, accessibility and SEO audits.
