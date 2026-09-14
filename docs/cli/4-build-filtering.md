---
title: "Exercise 4 - Build filtering with Plan and Autopilot"
description: "Agree filtering requirements, approve an implementation plan, validate the code, and checkpoint on the feature branch."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Now build the larger feature: let users filter games by category and publisher. You'll plan before coding, explicitly authorize **Autopilot**, review and test the implementation, and save a checkpoint. This exercise does not create the skill, QA agent, or feature PR.

## Start the filtering milestone

Confirm PRs 1 and 2 are merged. In your learner repository terminal:

```bash
git status
git switch main
git pull --ff-only
git switch -c add-game-filtering
copilot --enable-all-github-mcp-tools
```

Continue only with a clean working tree and a successful update from `main`. Exercises 4–8 use this same branch and checkout. Later checkpoint commits will add the skill and QA profile; do not create a branch per exercise.

## Retrieve the actual issue

Find **Allow users to filter games by category and publisher** in your repository's **Issues** tab and copy its URL. Do not assume the template's filename or an issue number identifies the issue in your copy.

The current issue requires:

- selecting one or more categories.
- filtering by publisher and combining that with categories.
- data-access helpers in `src/lib/` that support both filters.
- accessible controls with keyboard navigation, appropriate ARIA, visible focus states, and `data-testid` attributes.
- Vitest unit coverage for helpers and Playwright E2E coverage for filtering behavior.

Read the live issue as the source of truth. Keep its URL and any clarifications you approve available for the QA prompt in Exercise 7.

## Plan before coding

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> to select **Plan** mode, or begin with `/plan`. Replace the issue placeholder and send:

```plaintext
Plan the filtering feature described in this issue: <filtering-issue-URL>. Read the issue, repository instructions, existing data-access helpers, UI, and tests before proposing changes. Treat the current checkout as the baseline; do not assume a publisher helper has already been created.

Cover multiple-category selection, publisher filtering, their combination, data-access support, accessible controls, and unit/E2E coverage. Ask me to clarify unspecified behavior such as how multiple categories combine, clearing filters, and empty results; record the decisions with the approved plan. Preserve the static Astro architecture rather than introducing an unnecessary server API.

Plan implementation on the current branch, including the required unit and E2E tests, and verification with npm run lint, npm run test:unit, npm run test:e2e, and npm run typecheck:all. Inspect prerequisites and server ownership first; report blockers rather than install software or stop unrelated processes.

Include these execution boundaries in the plan: after I approve it, implement only the filtering feature and required tests, run the checks, then stop so I can review. Do not create the quality-checks skill, a QA agent, or other later workshop artifacts. Do not change branches, commit, push, or open or merge a PR.

Do not edit application code or begin implementation until I approve the plan.
```

Answer the follow-up questions. Do not add hidden acceptance criteria later: save the agreed answers with the issue URL so the implementation, browser checks, and QA can all use the same requirements.

Review the plan for data-layer and UI changes, tests, accessible controls, and the documentation convention you merged. Confirm it explicitly includes all four checks, the stop-for-review boundary, and the prohibitions on later workshop artifacts, branch changes, commits, pushes, and PR operations. Ask for revisions before approval if any limit or criterion is missing or it proposes work outside the issue.

## Explicitly approve Autopilot

Only after the plan includes the reviewed scope and execution boundaries, use the plan approval option to **Accept plan and build on autopilot**. If your version presents different wording, explicitly select the option that switches to **Autopilot**, then check the mode indicator. Approval starts execution of the bounded plan; do not rely on a later prompt to add limits after work has begun.

> [!CAUTION]
> Autopilot controls continued work, not just tool permissions. Review the permissions dialog before choosing. Full permissions allow tool, path, and URL access; limited permissions may block actions that require approval. A codespace is not permission to expose secrets or change unrelated resources. Resolve blocked access deliberately rather than treating skipped checks as passing.

Monitor the work and command results. Autopilot may pause at a continuation limit or report a blocker before completing the plan. Review that state before authorizing it to continue, preserving the same scope.

## Return to Interactive and review

When implementation stops, use <kbd>Shift</kbd>+<kbd>Tab</kbd> to return to **Interactive** mode before sending any further prompts. Autopilot can remain active after a task; do not assume it switched back.

Enter `/diff` and inspect all changed files. Compare the implementation with the issue and your approved clarifications:

- Can users select multiple categories, filter by publisher, and combine them as agreed?
- Do the data-access helpers actually support the filters rather than only changing the UI?
- Do controls have meaningful labels, keyboard support, visible focus, and stable test identifiers?
- Do tests assert behavior, including the agreed clearing and empty-result cases, without weakening existing assertions?
- Does the code follow the documentation convention and preserve the static app's architecture?

Review evidence for all four npm checks. You have not created `quality-checks` yet, so these checks run directly. Playwright's E2E configuration builds and serves a preview; stop only a development server you started before running the suite so it cannot reuse stale content. A port conflict or missing browser is a blocker to resolve, not a reason to kill another process or claim a pass.

Request focused corrections if needed, rerun affected checks, and ensure the final implementation has complete verification. Direct browser observation comes in Exercise 6; it has a different purpose from this automated verification.

## Save the implementation checkpoint

Once the diff and results are satisfactory, authorize a local checkpoint:

```plaintext
Review the current diff and verification results. Create a checkpoint commit containing only the reviewed filtering implementation and its tests. Keep the current filtering branch and checkout. Do not push, open a PR, or create the skill or QA agent yet.
```

Record the tested revision and keep the issue URL and approved clarifications. Stay **Interactive** and continue in this same checkout to [Exercise 5 - Create and use a quality-checks skill][next-lesson].

## Resources

- [Autopilot mode and permissions][autopilot] explains autonomous continuation and switching back to Interactive.
- [Copilot CLI command reference][cli-reference] lists current mode controls and commands.

[previous-lesson]: ../3-custom-instructions/
[next-lesson]: ../5-agent-skills/
[autopilot]: https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
