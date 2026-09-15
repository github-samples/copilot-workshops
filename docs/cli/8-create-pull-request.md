---
title: "Exercise 8 - Create and merge the feature PR"
description: "Review the full filtering milestone, reuse current QA evidence, and merge the third pull request after CI and review."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Now bring the filtering milestone together in PR 3. Stay on the branch and checkout used in Exercises 4–7. It contains the filtering implementation, quality-checks skill and scripts, QA profile, and associated tests.

In this exercise, you will:

- review the complete milestone diff and current QA evidence.
- request one feature PR and inspect its checks and review feedback.
- explicitly merge the reviewed PR and update local `main`.

## Scenario

The filtering work is spread across several checkpoints, but reviewers need to assess one complete feature. Tailspin Toys wants a PR that connects the requirements, implementation, reusable checks, and QA findings. You'll prepare that handoff and resolve blockers before merging.

This is a normal scoped PR request using the repository's conventions. It does not require a contribution skill.

> [!NOTE]
> A production team might separate a feature from reusable quality infrastructure. This workshop combines them deliberately to show the complete workflow in one feature PR. The earlier star-rating and instructions PRs should already be merged into `main`, not appear again as unrelated work.

## Check readiness and evidence

1. Review the QA verdict and its requirement-to-evidence mapping. A **NO-GO**, missing browser evidence, or skipped required check is a blocker to resolve before merging.
2. Confirm all four checks actually ran through the quality-checks skill: lint, unit tests, E2E, and type checks.
3. Review the tested revision and any changes since those checks. Reuse the current QA evidence only while the tested code, tests, and verification scripts remain unchanged. A checkpoint commit alone does not invalidate identical file contents, but code changes do.
4. If the implementation or tested inputs changed, run the relevant skill checks and browser observations again and update the evidence. Do not rerun the entire suite solely because you are opening a PR when current QA results still apply.
5. Inspect the full branch diff, not just the latest checkpoint or uncommitted changes.

From another terminal in the same checkout:

```bash
git status
git fetch origin
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
git --no-pager diff origin/main...HEAD
```

The three-dot diff shows this branch's changes since its common ancestor with `origin/main`, including earlier checkpoints. Verify it includes only the intended filtering milestone. Inspect new files too; unexpected untracked or uncommitted files must be reviewed before staging.

## Request PR 3

Exercise 7 returned you to a normal **Interactive** session before the checkpoint. Continue in that established session if the QA profile is no longer active and the filtering checkout and branch are unchanged. Keep the issue URL, approved planning clarifications, and current QA report, including the tested revision and check results, available.

The QA profile prohibits commit and PR actions during QA. If it is still active, return to a normal session before requesting the PR:

1. Wait until QA is idle, then enter `/exit` at its CLI prompt. If the CLI remains open because another session is active, finish or preserve that work before returning to the normal prompt and pressing <kbd>Ctrl</kbd>+<kbd>D</kbd> to shut down this CLI instance.
2. At the shell prompt, stay in the same filtering checkout and branch. Confirm their identity, then start a fresh normal session without `--agent qa` or a resume flag:

   ```bash
   pwd
   git branch --show-current
   git status
   copilot
   ```

3. Confirm you are in **Interactive** mode and the QA profile is no longer active. Do not create another worktree, change branches, or resume the QA session.

Replace all placeholders below with the real issue URL, approved clarifications, and current QA evidence. Supply them explicitly even if you stayed in the normal session from Exercise 7; a fresh conversation must not rely on the QA session's memory.

```plaintext
Prepare the filtering feature PR for this issue: <filtering-issue-URL>. These are the additional acceptance criteria I approved during planning: <paste the agreed clarifications, or write none>. This is the current QA evidence: <paste the QA report, including the tested revision, browser observations, coverage assessment, all four check results, and any limitations>.

Confirm the checkout and current filtering branch. Inspect the full diff against main, all milestone checkpoint commits, git status, the repository PR template, and the supplied QA evidence. Include only the reviewed filtering implementation, quality-checks skill and bundled scripts, QA agent definition, and associated tests.

Reuse the QA results while they still describe the final file contents. If code, tests, or verification scripts changed afterward, report that and run the relevant checks through the skill and affected browser validation before presenting them as current. Do not label failed, blocked, or skipped checks as passes.

Commit any remaining reviewed milestone changes if needed, push this current branch, and create one PR into main following the repository conventions. Include the issue and approved criteria, implementation summary, tests added or why none were needed, browser observations, all four check results, and remaining limitations. Do not merge, create another branch, invoke a contribution skill, or start another feature.
```

## Review the PR and CI

Open the returned URL and inspect **Files changed** across the entire PR. Check that the skill's scripts and QA profile are included, and that no credentials, local MCP configuration, unrelated files, generated reports, or dependency installs slipped into the diff.

Use the PR's **Checks** tab, or run these commands in the terminal on the feature branch:

```bash
gh pr view
gh pr diff
gh pr checks --watch
```

Inspect your repository's `.github/workflows/` rather than assume a green badge covers every kind of verification. The current Tailspin **Run tests** workflow runs lint, type checks, Vitest unit tests, and Playwright E2E tests against the built static site. It does not substitute for the direct MCP browser observations in your QA report. The workshop site's Astro build and link checks validate a different repository.

If a check fails, inspect its logs and address the cause. A focused fix must be reviewed and reverified on the updated revision before pushing. If `main` changes and resolving a conflict changes the feature, refresh the affected evidence too. Wait for any required human review; an agent's own approval does not override branch protection.

## Merge and update local main

When the PR meets all review and check requirements, explicitly choose **Merge pull request** on GitHub and confirm the merge. Verify PR 3 is **Merged**.

Exit the CLI session with `/exit`. With a clean working tree, update the local checkout:

```bash
git status
git switch main
git pull --ff-only
```

## Summary and next steps

No new branch is needed for the next exercise. You have now merged exactly three workshop PRs: star ratings; instructions and a demonstration; filtering with the quality skill, QA profile, and tests.

Continue to [Exercise 9 - Explore slash commands and CLI options][next-lesson] for a bounded tour of CLI controls, not another implementation task.

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-slash-commands/
