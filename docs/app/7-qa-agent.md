---
title: "Lesson 7 - Create and use a QA agent"
description: "Create a requirements-first QA profile that combines test coverage, the quality-checks skill, and direct browser evidence."
authors:
  - geektrainer
lastUpdated: 2026-09-14
---

In the previous lessons, you built a quality-checks skill and gave Copilot a browser through Playwright MCP. Now bring those capabilities together with a **QA custom agent** that reviews the filtering feature against its requirements.

In this lesson, you will:

- understand how a custom agent works with instructions, skills, and MCP tools.
- create and inspect a reusable QA profile.
- select the QA agent and review its findings against the filtering issue.
- save the profile and any justified tests for the feature PR.

## Scenario

Tailspin Toys is preparing to ship category and publisher filtering. The automated checks and browser exploration have given the team useful evidence, but passing tests alone cannot show whether every agreed requirement is covered. Before opening the PR, the team wants a focused review of what was requested, what was built, and what still needs attention.

You'll create a QA agent that starts from the issue and your approved planning decisions, checks coverage, and uses the skill and browser tools to gather evidence. Its job is to identify gaps and explain whether the feature is ready for review, not to approve its own work or merge the PR.

## What is a custom agent?

A custom agent is a reusable specialist role defined in a Markdown profile. Its instructions shape how Copilot approaches a task; selecting the profile applies that role to your conversation. For this workshop, you'll define the role in `.github/agents/qa.agent.md` and select it in the app.

The customizations you've built have different jobs. Repository instructions describe the team's standards. The quality-checks skill packages repeatable checks. Playwright MCP supplies browser tools. The QA profile tells Copilot how to use those capabilities to assess requirements and report findings. It doesn't replace them or require another agent session.

## Create the QA profile

Continue in the filtering session from Lesson 6, keeping the same worktree and branch. Confirm the session is in **Interactive** mode, the quality-checks skill is present, and Playwright MCP is available. The feature PR comes in Lesson 8; this lesson adds a profile and, only where needed, tests.

Send the following prompt to the ordinary Copilot agent. You'll inspect the resulting file before selecting QA:

```plaintext
Create a reusable QA custom agent in .github/agents/qa.agent.md. First inspect the repository instructions, package.json, test configuration, and .github/skills/quality-checks/SKILL.md. Give the profile valid YAML frontmatter with the name QA and a description explaining when to use it. Do not pin a model or add a tools list; inherit the harness's available tools and permissions. Create only the agent definition, then stop so I can inspect it before running it.

In the agent's instructions, require every QA task to start from the issue and any approved acceptance criteria supplied by the user. Treat these requirements as the source of truth, not the implementation. Ask when requirements are missing or ambiguous. Inspect the feature and existing tests, and map each criterion to suitable automated coverage and observable behavior.

Require direct browser validation through the configured Playwright MCP server and execution of lint, unit tests, end-to-end tests, and type checks through the existing quality-checks skill and its bundled scripts. Read the skill explicitly if it has not been automatically discovered. Report missing skills, MCP tools, prerequisites, or access as blocked; do not silently substitute another workflow or label skipped checks as passes. Identify the checkout and server under test, avoid reusing another worktree's server, stop only servers the agent started, and ask before any installation or stopping another process.

Allow the QA agent to add the smallest necessary tests for genuine coverage gaps, following repository instructions; no additional tests is valid when coverage is already adequate. Do not weaken assertions, disable failing tests, change acceptance criteria to match the code, or modify application code without my approval. After changes, rerun affected checks and complete final verification of the resulting revision. Require a concise report mapping criteria to evidence and pass/fail/blocked status, listing tests added or explaining why none were needed, reporting all four check results, and identifying unresolved defects. GO requires all required checks and evidence; otherwise report NO-GO with the reason. Do not change branches, commit, push, open or merge PRs, or create additional agents or skills during QA.
```

## Inspect the profile

1. Open **Changes** and select `.github/agents/qa.agent.md`. You can also find it through the file review panel.
2. Read the frontmatter. `description` is required, and `name: QA` makes the profile recognizable in the picker. Leave `model` and `tools` unspecified for this exercise so the selected model and available tools are used; normal permissions still apply.
3. Read the instructions as a review checklist: do they start from requirements, use the skill and browser tools, add tests only for real gaps, and distinguish failures from blocked checks?
4. Ask Copilot to correct any gaps before selecting the profile. Confirm it created the definition without starting QA or changing the application.

> [!NOTE]
> A specialist profile guides behavior; it does not guarantee a correct result. You'll still inspect the agent's tool activity, test changes, and report.

## Run QA against the issue

The run prompt is for the selected **QA** custom agent, not the default agent reading a profile. Keep the same filtering checkout and branch.

1. In the current session, open the agent picker in the prompt box, or enter `/agent`, as described in the [app customization documentation][customize-app].
2. Select **QA** and verify that the app visibly identifies **QA** as the active agent before sending the run prompt.
3. If **QA** is not listed or you cannot confirm it is active, pause and ask your facilitator while retaining this worktree and branch. Do not create a new feature session, invent a reload sequence, or substitute a request for the default agent to read `qa.agent.md`.

The documented picker is available during a session, but discovery of a newly created repository profile can depend on your app version. Do not treat writing the file as proof of activation.

Replace both placeholders with the actual filtering issue URL and the clarifications approved in Lesson 4, or `none` when the issue is complete. Do not rely on the previous agent's memory.

```plaintext
Verify the filtering feature against this issue: <filtering-issue-URL>. These are the additional acceptance criteria I approved during planning: <paste the agreed clarifications, or write none>.

Validate behavior with the Playwright MCP server, inspect test coverage, add tests only for missing coverage, and run validation through the quality-checks skill. Report evidence, check results, and blockers. Do not change application code without my approval, create a commit, or open a pull request.
```

## Review the evidence

Read the report alongside the filtering issue and your approved clarifications:

1. Check that each criterion is connected to appropriate tests and observable behavior. For example, combining categories and a publisher needs evidence about the returned games, not just whether the controls respond.
2. Inspect actual Playwright MCP tool activity and confirm the tested server belongs to this checkout. Browser checks and automated E2E must not reuse a stale server or another checkout.
3. Review results for lint, unit tests, E2E tests, and type checks. All four must run through the quality-checks skill's scripts; a summary of planned commands is not execution.
4. Open **Changes** to inspect any added tests and compare them with the gaps in the report.

Review any added tests: they should close genuine gaps without weakening assertions. No new tests is correct when coverage is adequate. A blocked or failed **NO-GO** verdict is a valid outcome, not permission to skip evidence.

If QA identifies an application defect, approve a focused fix separately and rerun affected checks and browser observations on the resulting revision. Missing prerequisites or tools need an explicit resolution. Do not treat older evidence as proof of changed code.

## Save a checkpoint

QA's role is verification, so return to the ordinary agent before requesting a commit:

1. Keep the QA report, issue URL, approved clarifications, and tested revision available for the PR lesson.
2. In the same session, use the agent picker to return to the ordinary Copilot agent and confirm **QA** is no longer selected.
3. Keep the same worktree and branch. If you cannot find the ordinary-agent choice, ask your facilitator rather than starting another feature session or issuing commit instructions to QA.

When you have reviewed the profile, any test changes, and the resulting evidence, send the checkpoint request to the ordinary agent with that QA context:

```plaintext
Review the current diff and create a checkpoint commit for the QA agent definition and any approved test changes. Stay on the existing filtering branch. Do not push or open a pull request.
```

## Summary and next steps

You've added a reusable specialist role to the workflow and reviewed its work. In this lesson, you:

- created and inspected a QA profile that starts from requirements.
- selected it to assess coverage and gather evidence through the skill and Playwright MCP.
- reviewed the findings and saved the profile with any justified test changes on the filtering branch.

You now have the pieces for a feature review: the implementation, skill, QA profile, tests, and verification report. Carry any unresolved findings forward; a failed or blocked result is not merge approval. Continue to [Lesson 8 - Create and merge the feature PR][next-lesson] to review the complete milestone and use Agent Merge.

## Resources

- [Customizing the GitHub Copilot app, including selecting custom agents][customize-app]

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
