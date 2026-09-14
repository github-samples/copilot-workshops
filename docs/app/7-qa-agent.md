---
title: "Lesson 7 - Create and use a QA agent"
description: "Create a requirements-first QA profile that combines test coverage, the quality-checks skill, and direct browser evidence."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

You've run repeatable checks and explored filtering through Playwright MCP. Now create a **QA custom agent** to bring the requirements, coverage, and browser evidence together. Keep the filtering session, checkout, and branch; the feature PR comes in Lesson 8.

## Create the QA profile

Stay in **Interactive** mode. A profile defines a specialist's role and instructions; a skill packages reusable task instructions, scripts, and resources. The QA agent will use your skill and configured MCP tools rather than replace them.

Send this prompt, then inspect the definition before running it:

```plaintext
Create a reusable QA custom agent in .github/agents/qa.agent.md. First inspect the repository instructions, package.json, test configuration, and .github/skills/quality-checks/SKILL.md. Give the profile valid YAML frontmatter with the name QA and a description explaining when to use it. Do not pin a model or add a tools list; inherit the harness's available tools and permissions. Create only the agent definition, then stop so I can inspect it before running it.

In the agent's instructions, require every QA task to start from the issue and any approved acceptance criteria supplied by the user. Treat these requirements as the source of truth, not the implementation. Ask when requirements are missing or ambiguous. Inspect the feature and existing tests, and map each criterion to suitable automated coverage and observable behavior.

Require direct browser validation through the configured Playwright MCP server and execution of lint, unit tests, end-to-end tests, and type checks through the existing quality-checks skill and its bundled scripts. Read the skill explicitly if it has not been automatically discovered. Report missing skills, MCP tools, prerequisites, or access as blocked; do not silently substitute another workflow or label skipped checks as passes. Identify the checkout and server under test, avoid reusing another worktree's server, stop only servers the agent started, and ask before any installation or stopping another process.

Allow the QA agent to add the smallest necessary tests for genuine coverage gaps, following repository instructions; no additional tests is valid when coverage is already adequate. Do not weaken assertions, disable failing tests, change acceptance criteria to match the code, or modify application code without my approval. After changes, rerun affected checks and complete final verification of the resulting revision. Require a concise report mapping criteria to evidence and pass/fail/blocked status, listing tests added or explaining why none were needed, reporting all four check results, and identifying unresolved defects. GO requires all required checks and evidence; otherwise report NO-GO with the reason. Do not change branches, commit, push, open or merge PRs, or create additional agents or skills during QA.
```

## Inspect the profile

Open `.github/agents/qa.agent.md` in **Changes** or the file review panel. `description` is required; this lesson also supplies the readable `name` of `QA`. Confirm there is no pinned `model` or invented tool list. Omitting `tools` inherits available tools; it does not bypass harness permissions. Production profiles can restrict tools deliberately.

Confirm the instructions start with requirements, require actual MCP browser activity and skill scripts, allow only justified test additions, and report blockers truthfully. Neither a specialist profile nor a skill requires a separate context window or orchestration of other agents.

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

Check the report against the issue: each criterion needs appropriate automated coverage and observable behavior. Inspect actual Playwright MCP tool activity, the checkout/server identity, and all four skill-script results. Browser checks and automated E2E must not reuse a stale server or another checkout.

Review any added tests: they should close genuine gaps without weakening assertions. No new tests is correct when coverage is adequate. A blocked or failed **NO-GO** verdict is a valid outcome, not permission to skip evidence.

If QA identifies an application defect, approve a focused fix separately and rerun affected checks and browser observations on the resulting revision. Missing prerequisites or tools need an explicit resolution. Do not treat older evidence as proof of changed code.

## Save a checkpoint

When QA has finished, keep its report, the issue URL, approved clarifications, and tested revision available. In the same session, use the documented agent picker to return to the ordinary Copilot agent and confirm **QA** is no longer selected. Keep the same checkout and branch; do not start another feature session or reload the worktree. If you cannot find the ordinary-agent choice, pause and ask your facilitator rather than issuing commit instructions to QA.

When you have reviewed the profile, any test changes, and the resulting evidence, send the checkpoint request to the ordinary agent with that QA context:

```plaintext
Review the current diff and create a checkpoint commit for the QA agent definition and any approved test changes. Stay on the existing filtering branch. Do not push or open a pull request.
```

Continue to [Lesson 8 - Create and merge the feature PR][next-lesson] with the filtering feature, skill, QA profile, tests, and current verification evidence.

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
