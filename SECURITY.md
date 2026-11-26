# Security policy

## Scope

This repository contains documentation, checklists, templates, a repository
validator script, and GitHub Actions workflows. Security reports are welcome for:

- `scripts/` and `.github/workflows/` (for example, unsafe file handling or
  workflow permissions that could be abused).
- Guidance in this framework that is incorrect in a way that would lead readers
  to build something insecure.

The vendored Cloudflare `security-audit-skill` under
`vendor/cloudflare/security-audit-skill/` is maintained upstream. Report issues
in that code to Cloudflare through
[the upstream repository](https://github.com/cloudflare/security-audit-skill);
we will update the vendored snapshot when a fix is released.

## Reporting a vulnerability

Please **do not open a public issue** for a security problem.

Report it privately through GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability):
open the repository's **Security** tab and choose **Report a vulnerability**.

Include what you found, the affected file or workflow, and steps to reproduce if
applicable.

## What to expect

This is a volunteer-maintained project. We aim to acknowledge reports within
7 days and to keep you informed while a fix is prepared. We will credit
reporters in the fix notes unless you ask us not to.

## Supported versions

Only the latest version on the default branch is supported.
