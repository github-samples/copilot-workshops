---
name: check-content-alignment
description: Find workshop content that may need matching changes after a lesson edit. Use for content drift reviews before committing or updating a PR. Discover duplicated passages, parallel concepts, translations, and cross-references from the diff and current content tree. Report actionable candidates without editing files.
---

# Check content alignment

Lessons repeat concepts, prompts, and instructions across harnesses and translations. Given a content change, find other passages that may now be inconsistent. This skill is advisory and read-only: recommend changes, but do not edit files or publish comments unless separately requested.

## 1. Establish the review scope

Use the comparison requested by the user. For in-progress work, inspect both unstaged and staged changes:

```bash
git diff -- docs
git diff --staged -- docs
git ls-files --others --exclude-standard -- docs
```

Read relevant untracked files as well; they do not appear in a normal diff. For a PR or branch review, identify its actual base ref and compare from the merge base to the head. Do not assume every PR targets `main`. Fetch the relevant refs when needed.

If there are no lesson changes under `docs/`, report that this content review does not apply. Repository guidance and tooling belong to the [build and verification consistency pass][build-verification].

## 2. Identify changes in meaning

Extract changed facts, requirements, prompts, steps, UI labels, titles, navigation, links, and image references. Ignore formatting-only changes.

Use the current content tree and locale configuration in `website/astro.config.mjs` to discover related harnesses and translations. Do not maintain a list of lesson numbers, filenames, locale counts, or historical shared passages in this skill.

## 3. Find and inspect related passages

Search across `docs/` using distinctive old and new phrases, technical identifiers, link targets, and related concepts from the diff. Inspect surrounding text before reporting a match.

- **Repeated content:** copied prompts, instructions, setup steps, and facts that should still agree.
- **Parallel concepts:** the same topic taught through another harness. Preserve intentional differences in UI, permissions, setup, and workflow.
- **Translations:** corresponding localized lessons. Match by content paths and meaning; an English text search alone will miss translated prose.
- **References:** links, titles, lesson numbers, and shared image references affected by a rename or content change.

Check already-modified related files too; being included in the diff does not prove the matching change is complete. Exclude passages whose alignment is already resolved, not every file that was touched.

## 4. Report actionable candidates

Group findings by the source change. For each candidate, give the file and line range or heading, explain the inconsistency, and suggest the matching edit or a review of an intentional difference.

Lead with confirmed mismatches. Clearly separate uncertain candidates from required corrections, and do not recommend identical wording where behavior legitimately differs. If no likely drift remains, say so briefly and identify the scope reviewed.

Stop at recommendations. Apply edits only as a separately authorized content-editing task, then verify them using the normal authoring process.

[build-verification]: ../build-and-verify-docs/SKILL.md
