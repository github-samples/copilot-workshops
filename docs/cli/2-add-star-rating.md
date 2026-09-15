---
title: "Exercise 2 - Add star ratings: a quick win"
description: "Display existing game ratings, review and validate the change, and merge your first pull request."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Start with a small change you can understand and verify. Tailspin Toys already stores each game's `starRating` and shows it on the details page. You'll display that existing value on the game cards, including a clear message when a game has no rating.

In this exercise, you will:

- request a focused change in an Interactive CLI session.
- inspect the diff and verify rated and unrated cards.
- commit, open, review, and merge PR 1.

## Scenario

Visitors can see ratings on a game's details page but cannot compare them while browsing the catalog. Tailspin Toys wants the existing ratings on the game cards, with a clear unrated state. This small change lets you practice requesting, reviewing, and shipping work before tackling a larger feature.

## Start the first milestone

From your learner repository root, confirm the working tree is clean, update `main`, and create a branch. If `git status` shows unexpected changes, resolve them before switching; do not discard them.

```bash
git status
git switch main
git pull --ff-only
git switch -c add-star-rating
copilot --enable-all-github-mcp-tools
```

Trust the repository when prompted. Check that you are in **Interactive** mode and use `/model` to inspect the available models or select **Auto**. Review tool approvals as they appear.

## Request the change

Send this prompt:

```plaintext
On the game cards, show each game's star rating. The Game type already includes a starRating field — it's a number out of 5, or null when a game hasn't been rated yet. Display it on each card in src/components/GameCard.astro, and when starRating is null show "No rating yet" instead. Keep the change small and don't restructure the card layout.

Inspect and follow the repository instructions. Use the existing data model; do not add a rating API, new schema, or unrelated feature. Add or update appropriate tests for the rated and unrated cases. Do not commit, push, or open a pull request yet.
```

Copilot should inspect the existing type and component before editing. Read its tool activity as well as its final response. A confident summary is not evidence that the implementation is correct.

## Review and validate

1. Enter `/diff` and inspect every changed file in your editor or the diff view.
2. Confirm the card uses the existing `starRating`, displays a value out of 5, and shows `No rating yet` for `null`. A truthiness check alone can incorrectly treat a numeric zero as unrated.
3. Check that the change preserves the card layout and gives the rating a meaningful text label rather than relying only on a star symbol or color.
4. Ask Copilot to verify the change using the existing checks:

   ```plaintext
   Inspect package.json and the test configuration, then run lint, type checks, and the existing unit or E2E tests appropriate to this card change. Verify both numeric ratings and the null fallback; report the exact commands and results, including any missing coverage or blocked checks. Do not install anything, change branches, commit, push, or open a PR.
   ```

5. Review the command output and any test changes. Resolve failures before shipping; ask before installing missing prerequisites.

To observe the card in a browser, open a second terminal in this same checkout and run:

```bash
npm run dev
```

Open the forwarded port in your codespace's **Ports** panel. Inspect rated cards on the home page. If the current seed data has no unrated example, require an automated fixture covering `null`; do not claim you observed an unrated card. Stop your development server with <kbd>Ctrl</kbd>+<kbd>C</kbd> in its terminal before E2E checks or leaving the exercise. Playwright's automated tests must not reuse a server from another checkout.

## Create and merge PR 1

After reviewing the change and passing checks, authorize this milestone separately:

```plaintext
Review the current diff and check results. Commit only the reviewed star-rating change and its tests, push the current branch, and create a pull request into main using this repository's PR template if one exists. Include the change summary and actual verification results. Do not merge the PR or start another task.
```

Open the returned PR URL. Inspect **Files changed** and the check results, not just the agent's summary. Review the workflow definitions in your Tailspin repository when interpreting CI; CI does not replace your browser observation. Address any failures and reverify changed code.

When the PR meets the repository's review and check requirements, select **Merge pull request** and confirm the merge on GitHub. If branch protection requires another reviewer, wait for that approval. Confirm the PR is **Merged** before continuing.

Exit the Copilot session with `/exit`. In the next exercise, you'll update local `main` before creating the instructions branch; do not start it from this unmerged feature branch.

## Summary and next steps

You've completed the first cycle: a bounded prompt, reviewed code, verification evidence, and a merged PR. Next, [guide Copilot with custom instructions][next-lesson] and demonstrate a documentation convention in a second small PR.

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-custom-instructions/
