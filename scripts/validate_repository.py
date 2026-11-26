#!/usr/bin/env python3
"""Validate repository structure, checklist IDs, internal Markdown links, and vendor integrity."""
from __future__ import annotations
import argparse
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CHECKLISTS = 16
EXPECTED_ITEMS = 101
ITEM_RE = re.compile(r"^\s*-\s*\[[ xX]\]\s+\*\*([A-Z][A-Z0-9]{1,5}-\d{2,3})\*\*", re.M)
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
REQUIRED_FILES = [
    "SECURITY.md",
    "README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "CHANGELOG.md", ".gitignore",
    "LICENSE", "NOTICE", "LICENSE-STATUS.md", "THIRD-PARTY-NOTICES.md",
    "standards/universal-software-engineering-product-excellence-standard.md",
    "protocols/deterministic-engineering-verification-protocol.md",
    "docs/framework-map.md", "docs/scoring.md", "docs/security-audit-integration.md",
    "templates/audit-report.md", "templates/assessment-scope.md",
    "templates/applicability-matrix.md", "templates/audit-scorecard.md",
    "templates/risk-register.md", "templates/exception-register.md", "templates/evidence-register.md",
    "scripts/validate_repository.py", ".github/workflows/repository-validation.yml",
    "vendor/cloudflare/security-audit-skill/LICENSE",
    "vendor/cloudflare/security-audit-skill/README.md",
    "vendor/cloudflare/security-audit-skill/skills/security-audit/SKILL.md",
    "vendor/cloudflare/security-audit-skill.sha256",
    "vendor/addyosmani/agent-skills/LICENSE",
    "vendor/addyosmani/agent-skills.sha256",
    "vendor/mattpocock/skills/LICENSE",
    "vendor/mattpocock/skills.sha256",
    "docs/workflow-skills.md",
]

# Vendored upstream snapshots: (directory, checksum manifest, expected file count).
VENDORS = [
    ("vendor/cloudflare/security-audit-skill", "vendor/cloudflare/security-audit-skill.sha256", 22),
    ("vendor/addyosmani/agent-skills", "vendor/addyosmani/agent-skills.sha256", None),
    ("vendor/mattpocock/skills", "vendor/mattpocock/skills.sha256", None),
]

# Links inside upstream files that are deliberately illustrative (they point at an
# example project layout, not at files in this repository). Upstream text is kept
# verbatim, so these are allow-listed instead of edited.
UPSTREAM_EXAMPLE_LINKS = {
    ("vendor/mattpocock/skills/skills/domain-modeling/GLOSSARY-FORMAT.md", "./src/ordering/GLOSSARY.md"),
    ("vendor/mattpocock/skills/skills/domain-modeling/GLOSSARY-FORMAT.md", "./src/billing/GLOSSARY.md"),
    ("vendor/mattpocock/skills/skills/domain-modeling/GLOSSARY-FORMAT.md", "./src/fulfillment/GLOSSARY.md"),
}

def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)

def check_files(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        if not (ROOT / item).is_file(): fail(f"missing required file: {item}", errors)
    checklists = sorted((ROOT / "checklists").glob("*.md"))
    if len(checklists) != EXPECTED_CHECKLISTS:
        fail(f"expected {EXPECTED_CHECKLISTS} checklist files; found {len(checklists)}", errors)
    all_ids: list[str] = []
    for path in checklists:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"missing YAML front matter: {path.relative_to(ROOT)}", errors)
        front = text.split("---", 2)[1] if text.startswith("---\n") and text.count("---") >= 2 else ""
        for key in ("id:", "title:", "applies_when:"):
            if key not in front:
                fail(f"front matter missing {key[:-1]}: {path.relative_to(ROOT)}", errors)
        ids = ITEM_RE.findall(text)
        all_ids.extend(ids)
        # Every checklist item must have a verification line before the next item.
        starts = [m.start() for m in ITEM_RE.finditer(text)]
        for i, start in enumerate(starts):
            end = starts[i + 1] if i + 1 < len(starts) else len(text)
            block = text[start:end]
            if "*Verify:*" not in block:
                fail(f"checklist item has no Verify line: {path.relative_to(ROOT)} near {text[start:start+80]!r}", errors)
    if len(all_ids) != EXPECTED_ITEMS:
        fail(f"expected {EXPECTED_ITEMS} checklist items; found {len(all_ids)}", errors)
    duplicates = sorted({item for item in all_ids if all_ids.count(item) > 1})
    if duplicates:
        fail("duplicate checklist IDs: " + ", ".join(duplicates), errors)
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").is_file() else ""
    status_text = (ROOT / "LICENSE-STATUS.md").read_text(encoding="utf-8") if (ROOT / "LICENSE-STATUS.md").is_file() else ""
    notices_text = (ROOT / "THIRD-PARTY-NOTICES.md").read_text(encoding="utf-8") if (ROOT / "THIRD-PARTY-NOTICES.md").is_file() else ""
    if "Apache License" not in license_text or "Version 2.0" not in license_text:
        fail("root LICENSE is not the Apache License, Version 2.0", errors)
    if "Selected — Apache License 2.0" not in status_text:
        fail("LICENSE-STATUS.md does not record Apache-2.0 as selected", errors)
    if "separately licensed under MIT" not in notices_text and "original MIT License" not in notices_text:
        fail("third-party notices do not clearly preserve Cloudflare's separate MIT license", errors)
    for owner in ("Addy Osmani", "Matt Pocock"):
        if owner not in notices_text:
            fail(f"third-party notices do not credit {owner}", errors)
    stale_license_phrases = ("license has not yet been selected", "license remains unselected", "status: not yet selected")
    for candidate in (ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "CHANGELOG.md", ROOT / "docs/security-audit-integration.md"):
        candidate_text = candidate.read_text(encoding="utf-8").lower()
        for phrase in stale_license_phrases:
            if phrase in candidate_text:
                fail(f"stale licensing status remains in {candidate.relative_to(ROOT)}: {phrase}", errors)
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if "$IDX" in agents:
        fail("unexpanded $IDX placeholder remains in AGENTS.md", errors)
    if (ROOT / "CLAUDE.md").is_file() and (ROOT / "CLAUDE.md").read_bytes() != (ROOT / "AGENTS.md").read_bytes():
        fail("CLAUDE.md must be an exact mirror of AGENTS.md", errors)

def heading_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return value.replace(" ", "-")

def check_internal_links(errors: list[str]) -> tuple[int, list[str]]:
    checked = 0
    markdown_files = list(ROOT.rglob("*.md"))
    heading_index: dict[Path, set[str]] = {}
    for md_path in markdown_files:
        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        heading_index[md_path.resolve()] = {heading_slug(h) for h in HEADING_RE.findall(md_text)}
    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in MD_LINK_RE.findall(text):
            destination = raw.strip().split()[0].strip("<>\"'")
            if not destination or destination.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            if (path.relative_to(ROOT).as_posix(), destination) in UPSTREAM_EXAMPLE_LINKS:
                continue
            target, sep, fragment = destination.partition("#")
            checked += 1
            resolved = (path.parent / target).resolve() if target else path.resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"internal link escapes repository: {path.relative_to(ROOT)} -> {raw}", errors)
                continue
            if not resolved.exists():
                fail(f"broken local Markdown link: {path.relative_to(ROOT)} -> {raw}", errors)
                continue
            if sep and fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
                if heading_slug(fragment) not in heading_index.get(resolved, set()):
                    fail(f"broken local Markdown anchor: {path.relative_to(ROOT)} -> {raw}", errors)
    return checked, []

def check_vendor_integrity(errors: list[str]) -> int:
    total = 0
    for vendor_dir, manifest_rel, expected_count in VENDORS:
        total += check_one_vendor(vendor_dir, manifest_rel, expected_count, errors)
    return total

def check_one_vendor(vendor_dir: str, manifest_rel: str, expected_count: int | None, errors: list[str]) -> int:
    manifest = ROOT / manifest_rel
    vendor_root = ROOT / vendor_dir
    if not manifest.is_file():
        fail(f"missing SHA-256 manifest: {manifest_rel}", errors)
        return 0
    entries: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            expected, rel = line.split("  ", 1)
        except ValueError:
            fail(f"malformed checksum entry in {manifest_rel}: {line}", errors)
            continue
        rel_path = Path(rel)
        if rel_path.is_absolute() or ".." in rel_path.parts or not rel.startswith(vendor_dir + "/"):
            fail(f"checksum path is outside {vendor_dir}: {rel}", errors)
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            fail(f"malformed SHA-256 digest for: {rel}", errors)
            continue
        if rel in entries:
            fail(f"duplicate checksum entry: {rel}", errors)
            continue
        entries[rel] = expected
    actual_files = {
        p.relative_to(ROOT).as_posix()
        for p in vendor_root.rglob("*") if p.is_file()
    } if vendor_root.exists() else set()
    manifest_files = set(entries)
    for rel in sorted(actual_files - manifest_files):
        fail(f"vendored file is missing from checksum manifest: {rel}", errors)
    for rel in sorted(manifest_files - actual_files):
        fail(f"checksum manifest references a missing vendor file: {rel}", errors)
    for rel, expected in entries.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            fail(f"vendor file checksum mismatch: {rel}", errors)
    if expected_count is not None and (len(entries) != expected_count or len(actual_files) != expected_count):
        fail(f"expected exactly {expected_count} files in {vendor_dir}; manifest has {len(entries)}, tree has {len(actual_files)}", errors)
    if not (vendor_root / "LICENSE").is_file():
        fail(f"vendored snapshot is missing its LICENSE: {vendor_dir}", errors)
    return len(entries)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors: list[str] = []
    check_files(errors)
    links, _ = check_internal_links(errors)
    vendor_files = check_vendor_integrity(errors)
    if errors:
        print("REPOSITORY VALIDATION: FAILED")
        for error in errors: print(f"- {error}")
        return 1
    print("REPOSITORY VALIDATION: PASSED")
    print(f"- Required files present: {len(REQUIRED_FILES)}")
    print(f"- Checklist files: {EXPECTED_CHECKLISTS}")
    print(f"- Unique checklist items: {EXPECTED_ITEMS}")
    print(f"- Local Markdown links checked: {links}")
    print(f"- Vendor files integrity-checked (Cloudflare, Addy Osmani, Matt Pocock): {vendor_files}")
    print("- AGENTS.md / CLAUDE.md mirror is synchronized")
    print("- No unexpanded $IDX placeholder")
    print("- Root Apache-2.0 license and third-party license boundary documented")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
