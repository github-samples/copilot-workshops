---
title: "Lesson 9 - Create a triage canvas"
description: "Create and review a repository-backed triage canvas, merge PR 4, and reopen it to add issue context without starting another feature."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

So far you've directed agents through chat. But a lot of work doesn't live in a conversation — it lives on a board, in a document, or on a checklist. **Canvases** give you and the agent a shared surface for exactly that kind of work, right inside the app. In this lesson you'll create a simple canvas to plan and track the backlog you've been working through.

In this lesson, you will:

- understand what a canvas is and when to use one.
- create a shared Kanban board canvas to triage your backlog.
- save the canvas to your repository and merge it for the team.
- reopen the canvas and add issue context without implementing another feature.

## Scenario

Looking at a list of issues can be daunting. Tailspin Toys' developers want a tool to triage issues and add their details to a session's context. Adding context is not authorization to implement an issue; this exercise ends with a reusable board, not a fifth PR.

## What is a canvas?

A [canvas][canvas-docs] is a shared, interactive surface for a work artifact — a plan, a triage board, a release checklist, a dashboard, or a document. While chat is great for describing intent and reasoning through ambiguity, most work happens on a *surface*. Canvases let you collaborate with the agent directly on that surface.

Canvases are **bidirectional**: the agent can update the canvas while it works, and you can edit the same surface yourself. When you create a canvas, the agent builds it based on your prompt and workflow, and you can ask it to add, remove, or revise capabilities as you go. Once created, a canvas opens in the app's right side panel.

Some common examples include:

- **Markdown canvases** for planning your day and prioritizing issues and pull requests.
- **Agentic kanban boards** where people and agents add cards and move work across columns.
- **Issue triage boards** that summarize top issues and recurring themes for a repository.

## Why use a canvas?

Reach for a canvas when a task needs structure, iteration, and verification, and a chat alone isn't enough. A canvas lets you:

- ground the agent's work in an actual artifact that fits your workflow.
- steer or correct work directly on the shared surface, then let the agent continue from your changes.
- inspect progress as visible changes to an artifact, not just chat responses.

## Create a canvas to track your work

Confirm PR 3 has merged. The star rating, documentation standard, filtering feature, quality skill, and QA profile must all be on `main` before starting the canvas. Use a fresh session and one branch for this final PR milestone.

1. Return to (or open) the GitHub Copilot app.
2. Select the **Home screen**.
3. Ensure `tailspin-toys` is selected for the repo.
4. Choose a **new working tree** and **Interactive** mode. Send this baseline request before creating any files:

   ```plaintext
   Prepare this fresh canvas session without implementing anything. Confirm this is a clean new worktree, fetch origin, and fast-forward the current session branch to origin/main. Report the checkout, branch, and matching HEAD and origin/main revisions. Verify the filtering PR is merged and the filtering feature, quality-checks skill, and QA profile are present.

   Stop if the checkout is dirty, diverged, or missing the prior merge. Do not reset, discard work, switch branches, or create another branch. Stop after reporting the baseline.
   ```

5. Check the baseline report, then request the repository-backed canvas:

   ```plaintext
   Create a basic repository-backed Kanban triage canvas for this repository using the App's supported canvas-extension workflow. Save its definition under .github/extensions/ so the team can reuse it. Inspect existing extensions and preserve them; do not overwrite the supplied database explorer.

   Read the current open issues. Highlight the three most likely to need attention, with the remainder below. Include each highlighted issue's title, content summary, URL, and a justification for its priority. Treat the ranking as a suggestion, not an instruction to change issues.

   Give every card an Add to current context action that attaches the issue details to this session only. It must not start implementation, create sessions or branches, change issue state, or create PRs. Keep the canvas bounded and keyboard-accessible.

   Show me the generated files and open the canvas for inspection. Do not change application code, commit, push, or create a PR. Ask before installing anything or adding dependencies.
   ```

Copilot creates the canvas files and opens the shared surface. Review the generated extension before trusting its actions; it is executable repository content, not just a picture.

> [!NOTE]
> If the first version needs work, request focused improvements within the triage scope. Do not turn this exercise into implementing one of the backlog issues.

## Inspect and exercise the canvas

1. Open **Changes** and confirm the canvas definition is repository-backed under `.github/extensions/`, not saved only for your user or session. Check that existing extensions and application files are unchanged.
2. Compare the board with the actual open issues and assess the ranking explanations.
3. Check that cards and controls are readable and usable with a keyboard.
4. Select **Add to current context** for an issue and confirm only its details enter the conversation. No implementation or issue-state change should start.
5. Review any corrections and ask Copilot to run the applicable existing validation for the files changed. Record results and blockers, rather than assuming an interactive surface is correct because it opened.

## Save the canvas and merge it to the repository

The canvas is already a repository asset. Commit and submit only the reviewed canvas work as PR 4:

1. In the same session, send:

   ```plaintext
   Review the repository-backed triage canvas diff and its validation evidence. Commit the approved canvas files on this session branch, push it, and create one PR targeting main using the repository's PR template. Describe the canvas behavior and how we verified that adding an issue only adds context. Do not merge yet or implement a backlog issue.
   ```

2. Review the full PR diff and checks in **My work**. Confirm it contains the canvas, not unrelated application work.
3. In the same canvas session, open the PR action dropdown and select **Agent merge**. Review its allowed actions and keep **Merge pull request** off until you approve the final result.
4. Set the scope before starting Agent Merge:

   ```plaintext
   Manage this existing canvas PR with Agent Merge. Address only in-scope review and CI blockers; ask before unrelated changes or installations. If the canvas changes, repeat its affected validation and update the evidence. Do not merge until I explicitly enable Merge pull request after review. Do not implement backlog issues or create another PR.
   ```

5. Select **Agent merge** and review any follow-up changes. Inspect the learner repository's actual CI checks and resolve failures; CI is not a replacement for exercising the canvas.

6. When the final diff and current evidence are approved and required checks and reviews pass, explicitly allow Agent Merge to merge by selecting its dropdown, then **Merge pull request**.

   ![The Agent merge dropdown showing the agent's allowed actions — Address reviews, Fix CI failures, Resolve conflicts — with an arrow pointing to Merge pull request](../_images/app-agent-merge-merge.png)

7. Confirm GitHub shows PR 4 as **Merged** before continuing.

You've now created a new shared canvas for your team!

## Reopen the canvas without starting another feature

Reopen the repository-backed canvas in the same canvas session after its PR is merged. This is an inspection step, not another branch or PR milestone.

1. Return to the canvas session, keep **Interactive** mode, and close the canvas panel if it is still open.
2. Send:

   ```plaintext
   Reopen the repository's triage canvas in this same session. I will add an issue to context to inspect its details only. Do not edit files, implement the issue, change its state, create another session or branch, commit, push, or open a PR.
   ```

3. Confirm the saved canvas opens again without regenerating its definition.
4. Select **Add to current context** on one of the issues that's of most interest to you.
5. Confirm the selected issue's details appear in context without starting implementation. Stop there: the workshop has four PR milestones, not five.

You've now used a canvas you created to streamline the development process.

## Summary and next steps

You created a shared surface where you and the agent can collaborate! You:

- learned what canvases are and when to use them.
- created a shared Kanban triage board canvas with the agent.
- saved and merged the canvas to your repository with Agent Merge.
- reopened the merged canvas and added issue context without launching another feature.

With your backlog tracked, take a step back to review everything you've built and where to go next. Continue to [Lesson 10 - Wrap-up and next steps][next-lesson].

## Resources

- [Working with canvas extensions in the GitHub Copilot app][canvas-docs]
- [Canvases on Awesome Copilot][awesome-copilot-canvases]
- [About the GitHub Copilot app][about-copilot-app]

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[awesome-copilot-canvases]: https://awesome-copilot.github.com/extensions/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
