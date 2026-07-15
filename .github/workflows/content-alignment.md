---
# Content-alignment check for the Copilot Workshops content.
#
# The workshop content is pure Markdown with prose duplicated inline across lessons
# (no partials / single-sourcing). When a PR edits one lesson, the other copies can
# silently drift. This workflow runs the same analysis as the `check-content-alignment`
# skill on every docs PR and posts ONE advisory comment listing other lessons that
# may need the same change. It is advisory only and never fails the build.

# Trigger - only when published lesson content changes.
on:
  pull_request:
    types: [opened, synchronize, reopened]
    paths:
      - "docs/**"

# Engine - GitHub Copilot (the default agentic engine).
engine: copilot

# Permissions - read-only. Writing the comment is handled by the safe-outputs job
# below, which runs with its own scoped permissions.
permissions:
  contents: read
  pull-requests: read

# Tools - read-only GitHub API access for PR context plus the checked-out repo files.
tools:
  github:
    toolsets: [pull_requests, repos, context]

# Network access - default allow-list is sufficient (analysis is repo-local).
network: defaults

# Outputs - post a single advisory comment on the pull request.
safe-outputs:
  add-comment:
    max: 1

---

# Content alignment check

You are reviewing a pull request that changes lesson content in **Copilot Workshops**, an Astro + Starlight docs site. The lessons live under `docs/` and are **pure Markdown**. Conceptually shared prose is **duplicated inline** across lessons rather than single-sourced, so an edit to one lesson often needs to be mirrored in others. Your job is to find those other lessons and post one advisory comment. **Do not edit any files.**

## What changed

Inspect the pull request diff, restricted to `docs/**`. For each changed lesson, identify what changed *in meaning* (not just formatting): corrected facts (versions, library names, counts, behavior, UI labels, the Tailspin Toys demo-app description), edited callouts or steps, renamed/retitled/added/removed lessons or headings, and changed links, lesson numbers, URLs, or image references. Ignore pure whitespace/wrapping changes.

## Where it might need mirroring

Search the rest of `docs/**` for passages that should stay in sync with each change. Focus on three drift categories:

1. **Formerly-shared copies.** Short callouts and steps that used to be shared partials are now copied verbatim into multiple lessons (for example, the Copilot CLI "Allow all" approval callout, and the "Approve and run workflows" step in `cloud/5-iterating.md` and `vscode/6-iterating.md`). Quote a distinctive phrase from the change and grep for it across all lessons.
2. **Parallel concepts across harnesses.** The same idea is taught once per harness in `cli/`, `vscode/`, `app/`, and `cloud/`. A conceptual change usually needs the same correction in the sibling lessons of the other harnesses.
3. **Cross-references and shared facts.** Reference-style links to a renamed/retitled lesson, lesson numbers in prose, the published URL shape, the `github.com/github-samples/tailspin-toys/...` demo-app URL, tool/library names, and shared screenshots.

Exclude the files already changed in this PR from your candidate list.

## What to post

Post exactly one pull-request comment. Structure it as:

- A one-line summary (for example, "Content-alignment check: N lessons may need a matching update").
- A short grouped list. For each candidate, give the **file** (and heading or approximate line range), **why** it's a candidate (which change it parallels + drift category), and a **suggested action** (mirror the edit, or "review - may be intentionally harness-specific").
- Lead with high-confidence verbatim duplicates; separate lower-confidence cross-harness suggestions.

If you find no likely drift, post a brief comment saying the change looks self-contained and no other lessons appear to need updating.

## Rules

- This check is **advisory only**. Never fail the workflow and never block the PR.
- **Read-only.** Do not modify any files; your only output is the single advisory comment.
- Only reason about content under `docs/**`. Do not flag instruction files, skills, or other repo docs.
- False positives are acceptable; clearly mark anything low-confidence so a human can decide.
