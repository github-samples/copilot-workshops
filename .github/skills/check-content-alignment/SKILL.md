---
name: check-content-alignment
description: Find workshop lessons that should change alongside an edit. Scans a diff (staged, unstaged, or a branch range) of the Copilot Workshops docs, extracts what changed, then searches the rest of docs/** for duplicated or parallel passages that now risk drifting out of sync — prose that used to be a shared partial and is now copied across pages, the same concept taught across the VS Code / CLI / App / Cloud harnesses, and cross-references to the changed page. Use after editing lesson content under docs/, before committing or opening a PR, or whenever asked to "check content alignment", "find related content to update", "what else should change", or "check for drift". Reports candidate files with line ranges and rationale; it does NOT edit content.
---

# Check content alignment

This workshop is **pure Markdown** with no partials. Prose that is conceptually shared is **duplicated inline** across lessons instead of single-sourced. That makes editing simpler but removes the partials system's guarantee that one edit updates every copy. This skill is the replacement guardrail: given a change, it finds the *other* places that should probably change too, so duplicated copies don't drift apart.

It is **advisory and read-only** — it surfaces candidates and rationale for a human (or agent) to act on. It never edits lesson content.

Run every command from the **repo root** unless a step says otherwise.

## When to use

- After editing one or more lessons under `docs/**`, before committing or opening a PR.
- When asked to "check content alignment", "find related content to update", "what else should I change", or "check for drift".
- As the local counterpart to the **content-alignment agentic workflow** (`.github/workflows/content-alignment.md`), which runs this same analysis automatically on pull requests and comments its findings. Run the skill locally to catch drift *before* you push.

## The drift surface (what to look for)

There are three recurring kinds of duplication in this repo. Most alignment gaps fall into one of them:

1. **Formerly-shared callouts and steps.** Several short callouts and exercise steps used to live in `_shared/` and were imported into many lessons. They are now copied verbatim into each consumer. When you change one copy, the others usually need the same change. Examples of high-fan-out prose to watch:
   - The "start Copilot CLI / **Allow all**" approval callout (was used across several CLI/app pages).
   - The "**Approve and run workflows**" step (appears in `cloud/5-iterating.md` and `vscode/6-iterating.md`).
   - Shared prerequisites, MCP-setup, and recap blurbs.
2. **Parallel concepts across harnesses.** The same idea is taught up to four times, once per harness: `cli/`, `vscode/`, `app/`, and `cloud/`. A conceptual change (how MCP works, what a custom instruction is, how an agent proposes changes, the description of the Tailspin Toys demo app) often needs the same correction in the sibling lessons of the other harnesses.
3. **Cross-references and shared facts.** Reference-style links to a renamed/retitled lesson, lesson numbers in prose, the published URL shape (`/cli/3-generating-code/`), the demo-app repo URL (`github.com/github-samples/tailspin-toys/...`), tool/library names, and screenshots referenced from multiple pages.

## Procedure

### 1. Get the diff

Pick the comparison that matches what you're reviewing:

```bash
# Unstaged + staged working-tree changes (default: reviewing your own in-progress edits)
git diff -- docs
git diff --staged -- docs

# A whole branch vs. the base it will merge into (reviewing a PR-sized change)
git fetch origin
git diff origin/main...HEAD -- docs
```

Limit to `docs` — content drift is the only thing this skill reasons about.

### 2. Extract the semantic changes

For each changed lesson, summarize *what actually changed in meaning*, not just which lines moved:

- Reworded or corrected **facts** (versions, library names, counts, behavior, UI labels, the demo-app description).
- Edited **callouts / steps** that look like formerly-shared prose (see drift surface #1).
- New, renamed, or removed **headings, lesson titles, or files** (these invalidate cross-references).
- Changed **links**, lesson numbers, URLs, or image references.

Ignore pure formatting (wrapping, whitespace) and changes that are genuinely page-specific.

### 3. Find the parallel copies

For each semantic change, search the rest of the content for passages that should match. Use the changed wording (and its near-synonyms) as the query, and always search the sibling harnesses.

```bash
# Find other pages that carry the same callout/step/sentence (quote a distinctive phrase)
grep -rn "Approve and run workflows" docs --include='*.md'

# Find the parallel lesson in the other harnesses (same concept, different harness)
grep -rln "custom instruction" docs/cli docs/vscode docs/app docs/cloud --include='*.md'

# Find cross-references to a page you renamed/retitled
grep -rn "2-custom-instructions" docs --include='*.md'
```

Exclude the file(s) you already changed from the candidate list.

### 4. Report candidates

Produce a concise, actionable report. For each candidate, give:

- **File** and approximate **line range** (or heading) of the passage that may need updating.
- **Why** it's a candidate: which change it parallels, and which drift category (shared-copy, cross-harness, or cross-reference).
- **Suggested action**: the specific edit to mirror, or "review — may be intentionally different."

Group by the source change. Lead with the highest-confidence matches (verbatim shared-copy duplicates) and separate the lower-confidence cross-harness "you may also want to mirror this" items. Be explicit when a parallel passage is *intentionally* harness-specific and should NOT be changed.

### 5. Hand off

This skill stops at recommendations. If the user wants the aligned edits made, treat that as a follow-up content-editing task and apply the changes with the normal authoring conventions, then re-run **build-and-verify-docs**.

## Boundaries

- **Read-only.** Never edit lesson content as part of this skill.
- **docs content only.** Don't flag instruction files, skills, or other repo docs — only `docs/**`.
- **Advisory, not a gate.** False positives are expected; the human decides. Prefer surfacing a borderline candidate (clearly marked low-confidence) over missing a real drift.
