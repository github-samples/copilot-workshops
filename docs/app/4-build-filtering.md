---
title: "Lesson 4 - Build filtering with Plan and Autopilot"
description: "Plan filtering from its issue, explicitly approve Autopilot, validate with the existing npm checks and a manual browser visit, and save a checkpoint."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

You have merged star ratings and the documentation standard with its code demonstration. Now build the filtering feature. This is the start of one larger PR milestone: keep this same session, worktree, and branch through Lessons 4–8.

In this lesson, you will:

- start from updated `main` and read the actual filtering issue.
- resolve requirements in **Plan** mode before explicitly approving **Autopilot**.
- review filtering and tests, then run the four existing npm checks.
- visit the feature manually in a browser and save a checkpoint.

The skill, MCP validation, QA profile, and feature PR come in later modules. Do not create them during this implementation step.

## Scenario

Tailspin Toys' catalog is growing, and visitors need to narrow the games by category and publisher. The backlog issue describes the feature, but details such as combining categories need agreement before coding. You'll use Plan mode to resolve those decisions, then authorize a bounded implementation with Autopilot.

## Session modes

The mode selector below the prompt controls the agent's autonomy:

- **Interactive** keeps you involved as the agent works and requests input.
- **Plan** prepares a plan for review before implementation.
- **Autopilot** implements and iterates autonomously within the approved scope and permissions.

Plan first, make approval explicit, then return to Interactive before creating reusable customizations.

## Start from updated main

Confirm PR 1 and PR 2 are merged on GitHub. Create a fresh worktree for filtering rather than continuing either earlier branch.

1. Select **My work** and find **Allow users to filter games by category and publisher** by title. Open it and copy its actual URL; issue numbers vary between repositories.
2. Select **New session** and choose a **new working tree**. Keep **Interactive** mode for the baseline update.

   ![The issue view in the GitHub Copilot app with an arrow pointing to the New session button](../_images/app-new-session-from-issue.png)

3. Send this setup request before planning or editing:

   ```plaintext
   Prepare this fresh filtering session without implementing anything. Identify the checkout and branch, confirm the worktree is clean, fetch origin, and fast-forward this session branch to origin/main. Confirm HEAD matches origin/main and includes the merged star-rating and coding-standards PRs.

   Stop and explain if the checkout is dirty, diverged, or missing either merge. Do not reset or discard work, switch branches, create another branch, or edit application files. Report the baseline revision.
   ```

4. Check the reported baseline. Fetching alone does not update the worktree: the current session branch must be fast-forwarded and its `HEAD` must match the fetched `origin/main` before work begins.

## Plan the filtering feature

Switch the mode selector to **Plan**. Replace the issue placeholder below with the URL you copied.

```plaintext
Plan the filtering feature from this issue: <filtering-issue-URL>. Read its full acceptance criteria and the repository instructions, then inspect the current static Astro application and its existing data-access helpers and tests. Do not implement yet.

Cover multiple-category selection, publisher filtering, combined category and publisher filtering, suitable data-access helpers, accessible controls, and unit and end-to-end coverage required by the issue. Ask me to resolve unspecified behavior, such as how multiple categories combine, clearing filters, and empty results, rather than silently invent requirements. Do not introduce a server API unless the requirements and existing architecture justify it.

Propose a bounded implementation and verification plan that follows the repository documentation convention and adds or updates the necessary unit and end-to-end tests. After confirming the commands in package.json, plan to run npm run lint, npm run test:unit, npm run test:e2e, and npm run typecheck:all using the existing project tooling. Record the issue URL and my approved clarifications in the plan so I can reuse them for QA.

Include these execution safeguards in the plan before I approve it: identify the checkout and server under test; inspect prerequisites before running checks; ask before installing software, dependencies, or browsers; do not reuse another worktree's server; stop only servers you started; and report other port conflicts rather than stopping unrelated processes. Missing prerequisites and skipped checks must be reported as blockers, not passes.

Include this implementation boundary in the plan: after I explicitly approve Autopilot, implement only the agreed filtering feature and its tests in this same worktree and branch, run the four checks, report the implementation and all check results including failures or blockers, then stop for my review and manual browser check. Do not create skills or custom agents, configure MCP, change branches, commit, push, or open a PR during implementation. The manual browser check and checkpoint commit happen later under my separate direction.

For now, stay in Plan mode and stop with the plan for my review. Do not implement, create skills or custom agents, configure MCP, change branches, commit, push, or open a PR.
```

Answer any clarifying questions and review the plan against the issue. Look for the data-access changes, accessible controls, and tests rather than accepting a UI-only implementation. Save the actual issue URL and approved clarifications from the plan for Lessons 6 and 7; use `none` when no extra criteria were needed.

Before approving, confirm the plan itself contains the four checks, documentation convention, prerequisite and server safeguards, same-worktree/branch requirement, and the stop after implementation and verification. It must prohibit later skills, agents, MCP setup, commits, pushes, and PRs during implementation. If any boundary is missing, request a revised plan while still in **Plan** mode and inspect the revision before approving.

## Explicitly approve Autopilot

Only after the reviewed plan contains your requirements and all execution boundaries, select **Approve and implement with autopilot** in the plan approval controls, or the equivalent explicit Autopilot option shown in your version. Confirm the mode indicator shows **Autopilot**.

Approval can start execution immediately. All implementation scope, safety rules, and stop boundaries must therefore be in the reviewed plan before you approve; do not rely on adding them in a follow-up message after execution starts.

Autopilot can write code and tests and iterate on failures, but this permission is not permission to complete later workshop modules. A missing prerequisite is a blocker to resolve with approval, not a passed check.

## Review and verify the implementation

1. Open **Changes** and inspect the filtering implementation and tests.
2. Compare the result with the issue and approved clarifications, including multiple categories and publisher combinations. Check that new or modified helpers follow the documentation standard from Lesson 3.
3. Inspect actual command output for all four npm checks. These run directly now because you have not created the quality-checks skill yet.
4. Resolve failures and rerun affected checks before accepting the implementation. Playwright's E2E configuration builds and serves a preview and can reuse a local server; make sure the tested server belongs to this worktree, not an earlier lesson.

## Check the feature manually

Return the session to **Interactive** mode before manual review and keep it there for Lesson 5.

1. Open **Terminal** in this session's review panel. If needed, select **+**, then **Terminal**.
2. Confirm the terminal is in the filtering worktree and run:

   ```shell
   npm run dev
   ```

3. Open the URL printed by this server in your browser, normally `http://localhost:4321`. If the port is occupied, identify its owner instead of stopping an unrelated process or assuming the existing server contains your changes.
4. Exercise category selection, publisher selection, and their combination against the approved behavior. Check keyboard access and the agreed clearing and empty-result behavior.
5. If anything fails, request a focused correction, review the diff, rerun affected automated checks, and repeat the relevant browser checks.
6. Return to the terminal and press <kbd>Control</kbd>+<kbd>C</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) to stop the server you started. Confirm it stopped before the next module's E2E run.

This is your manual browser observation. Agent-driven browser observation through MCP comes in Lesson 6.

## Save a checkpoint

After reviewing the changes and verification, authorize a local commit:

```plaintext
Review the current diff and create a checkpoint commit for the filtering implementation and its tests. Keep this same filtering branch and worktree. Do not create skills or agents, configure MCP, push, or open a pull request.
```

## Summary and next steps

You've agreed the filtering requirements, reviewed the implementation and tests, and checked the feature manually. This checkpoint is part of PR 3, not a separate PR. Stay in **Interactive** mode in the same session for [Lesson 5 - Create and use a quality-checks skill][next-lesson].

## Resources

- [Working with agent sessions in the GitHub Copilot app][agent-sessions]
- [About cloud and local sandboxes for GitHub Copilot][sandboxes]

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
