---
title: "Lesson 8 - Create and merge the feature PR"
description: "Review filtering, instructions, the skill update, QA profile, and tests together, then create a PR and use Agent Merge."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

Your filtering implementation, instruction updates, skill update, quality assurance (QA) profile, and tests are saved on one branch. It's time to review them together and open a pull request. You merged the star-rating pull request (PR) yourself; this time you'll allow **Agent Merge** to manage the process.

> [!NOTE]
> Normally, we'd split the feature, instruction updates, skill update, and QA agent into a few separate PRs. To streamline the workshop, you've kept the full filtering and quality workflow in one conversation and branch, with all that work going into this PR.

In this lesson, you will:

- learn what Agent Merge is and how it automates the merge lifecycle.
- inspect the full feature change and verification evidence.
- create the filtering PR.
- enable Agent Merge only after review and confirm the PR is merged.

## Scenario

Throughout the filtering workflow, you've used Copilot to plan, implement, and verify a feature. Tailspin Toys now wants to automate the remaining PR work while keeping merge authorization under the developer's control.

## Introducing Agent Merge

**Agent Merge** automates the remaining work needed to land a pull request. When you enable it, Copilot works through what is blocking the PR — fixing failing continuous integration (CI) checks, responding to review comments, and rebasing when needed — then enables GitHub auto-merge when the repository allows it.

Up to this point you've selected **Merge pull request** yourself. Agent Merge can take on that responsibility. Review the work and decide it is ready before enabling Agent Merge.

## Use Agent Merge to manage the PR

With all of your code created, let's review it together, create the PR, and allow Agent Merge to manage the rest of the process.

1. Enter `/agent`, select the default agent, and confirm it is active.
2. Ask Copilot for a final review:

   ```plaintext
   Review everything on this branch against the filtering issue and our plan. Is it ready for a PR?
   ```

3. Enter `/diff`, inspect the complete change, and resolve anything that still needs attention.
4. Ask Copilot to commit the reviewed work:

   ```plaintext
   Commit the reviewed filtering and quality workflow changes with an appropriate commit message.
   ```

5. Enter `/pr create`. Review the resulting PR title and description. `/pr create` can push the existing commit as part of creating the PR.
6. Open the resulting PR and inspect its commits, changed files, linked issue, and checks.
7. Once you decide the PR is ready for Agent Merge, return to Copilot CLI and enter:

   ```plaintext
   /pr automerge
   ```

   `/pr agentmerge` is an alias for the same command.

   In this `--yolo` session, the command can act immediately.

8. Follow the progress in Copilot CLI and on the PR.
9. If Agent Merge changes code, review the new commit and affected checks.
10. Confirm the PR is merged.

> [!IMPORTANT]
> Agent Merge does not bypass required approvals, branch protection, merge queues, repository settings, or missing permissions. If it is blocked, read the reported reason and complete the reviewed merge manually when your repository permits it.

## Summary and next steps

You've automated several parts of the development process, including generating code, testing and validating code, and now the pull request process. You:

- learned what Agent Merge is and how it automates the merge lifecycle.
- inspected the full feature change and verification evidence.
- created the filtering PR.
- enabled Agent Merge only after review and confirmed the PR was merged.

Next, you'll [explore more useful Copilot CLI slash commands][next-lesson] for context, models, sharing, and optional cloud delegation.

## Resources

- [Manage pull requests with Copilot CLI][manage-prs]
- [Copilot CLI command reference][cli-reference]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-cli-power-tools/
[manage-prs]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
