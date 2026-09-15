---
title: "Lesson 8 - Create and merge the feature PR"
description: "Review filtering, the skill, QA profile, and tests together, create PR 3, and explicitly authorize Agent Merge."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Your filtering implementation, quality-checks skill, QA profile, and associated tests are checkpointed on one branch. Review them together and use the current QA evidence to prepare PR 3. You have already explicitly merged the star-rating and instructions PRs. This time you'll use **Agent Merge** within the PR workflow, not as a separate feature or branch.

In this lesson, you will:

- learn what Agent Merge is and how it automates the merge lifecycle.
- inspect the full feature PR and verification evidence.
- authorize Agent Merge only after review, and confirm the PR is merged.

## Scenario

Over the last few modules you've explored various levels of automation, from creating code to allowing Copilot to validate a UI directly. To further speed development, Tailspin Toys would like to see if there's a way pull requests that have been vetted and validated can automatically be merged.

## Introducing Agent Merge

**Agent Merge** allows automation of the last mile of landing a pull request via Copilot app. When you enable it, the app's session reads your pull request, addresses what's blocking it — fixing failing CI checks, responding to review comments, rebasing when needed — and merges it as soon as GitHub allows. It runs in the background, survives app restarts, and turns itself off once your pull request is merged.

Up to this point you've selected **Merge pull request** yourself. Agent Merge can take on that responsibility, but its ability to edit code and merge still needs your explicit authorization. Review its allowed actions and the work before granting merge permission.

## Review the complete milestone

Stay in the filtering session from Lessons 4–7. Check the full branch diff against `main`, not just the latest checkpoint: it should contain filtering, `.github/skills/quality-checks/SKILL.md`, the bundled scripts, `.github/agents/qa.agent.md`, and the associated tests.

Use the agent picker to return from **QA** to the general Copilot agent before requesting commits or PR actions, and keep **Interactive** mode. The QA profile's job was verification, not shipping. Changing the selected agent must not change the filtering session, checkout, or branch.

This workshop deliberately combines feature work and reusable quality infrastructure in one PR. A production team might split those concerns; here, checkpoint commits preserve reviewable steps without stacked branches or extra PRs.

Review Lesson 7's QA report. Reuse its evidence only if it covers the final revision being submitted, with all four checks and the relevant browser observations completed. If code changes, conflicts, or CI fixes alter what was tested, rerun affected checks and browser observations and update the evidence. A failed or blocked **NO-GO** report is not merge approval.

Once the diff and evidence are ready, send:

```plaintext
Review the full filtering branch diff against main, including the filtering feature, quality-checks skill and scripts, QA agent definition, and associated tests. Summarize the issue criteria, approved clarifications, and current QA evidence. Reuse verification only if it still applies to the final revision; report stale, missing, or failing evidence before proceeding.

If the reviewed changes and verification are ready, commit any remaining approved milestone changes, push this branch, and create one feature PR targeting main using the repository's PR template and the actual filtering issue URL. Keep the checkpoint history on this branch. Do not use a contribution skill, create another branch or PR, or merge yet.
```

Open the PR in **My work** and inspect **Files changed**, its description, reviews, and check results. Inspect Tailspin Toys' own workflow files and required checks; do not assume every local check or browser observation runs in CI. The workshop publisher's Astro build and link checker belong to another repository and do not validate this feature.

## Use Agent Merge to manage the PR

After reviewing the existing PR, configure Agent Merge in this same session. Do not create a second PR.

1. Return to the filtering session and confirm it is linked to PR 3.
2. Open the PR action dropdown in the upper right-hand corner. Before a PR exists, it is next to **Create PR**; the label can change once a PR is linked.
3. Select **Agent merge** to enable agent merge.
4. Review the available permissions, including **Address reviews**, **Fix CI failures**, **Resolve conflicts**, and **Merge pull request**. Leave merge permission off while findings or verification are unresolved.
5. Before starting it, send the following scope and authorization, then select **Agent merge**:

   ```plaintext
   Manage this existing filtering PR with Agent Merge. Address review or CI blockers only within this PR's scope. Do not weaken tests or requirements, and ask before unrelated changes or installations. Any change to the tested revision requires updated relevant checks and browser evidence; do not treat older QA results as proof of changed code.

   Do not merge until I explicitly enable Merge pull request after reviewing the final diff and evidence. Do not create another PR or begin the canvas task.
   ```

6. Review any follow-up changes and updated results. When the final diff is approved, required CI and reviews pass, and QA evidence applies to that revision, explicitly authorize merging by selecting the dropdown next to **Agent merge**, then **Merge pull request**.

   ![The Agent merge dropdown showing the agent's allowed actions — Address reviews, Fix CI failures, Resolve conflicts — with an arrow pointing to Merge pull request](../_images/app-agent-merge-merge.png)

7. Confirm GitHub shows PR 3 as **Merged**, not merely mergeable or queued. Agent Merge does not bypass repository protections or missing permissions; resolve those blockers before continuing.

Only after that merge should you start the canvas milestone. Lesson 9 creates a fresh worktree and fast-forwards its session branch to the latest `origin/main` so the canvas begins with the complete merged feature.

## Summary and next steps

You've automated several parts of the development process, including generating code, testing and validating code, and now the pull request process. You:

- learned what Agent Merge is and how it automates the merge lifecycle.
- reviewed the complete filtering, skill, QA-profile, and test diff as PR 3.
- reused current QA evidence, inspected CI, and explicitly authorized Agent Merge.

Next, you'll explore **canvases** — a richer way to plan and visualize work with the agent. Continue to [Lesson 9 - Create a triage canvas][next-lesson].

## Resources

- [Managing issues and pull requests with the GitHub Copilot app][managing-issues-prs]
- [About the GitHub Copilot app][about-copilot-app]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-canvases/
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
