---
title: "Exercise 6 - Validate functionality with Playwright MCP"
description: "Connect a browser through MCP and compare observed filtering behavior with the issue and approved plan."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Your filtering implementation and quality-checks skill already have automated verification. Now give Copilot a browser and ask it to observe the feature directly. This exercise demonstrates **Model Context Protocol (MCP)** interaction, not another full test-suite run.

Stay in **Interactive** mode on the same filtering checkout and branch. MCP configuration does not start a new feature milestone.

## What MCP adds

[MCP][mcp-overview] connects an agent to external tools and context through servers. The built-in GitHub MCP server lets Copilot work with issues and PRs. The [Playwright MCP server][playwright-mcp] gives it browser tools for opening pages, inspecting accessible elements, navigating, and interacting with controls.

The browser's accessibility snapshot helps the agent identify controls, but it does not prove complete accessibility compliance. Compare actual actions and observations with the issue's requirements rather than accept a generic “looks good.”

> [!CAUTION]
> Treat an MCP server like a project dependency: review the publisher, source, permissions, and any package download before enabling it. Organization policies may restrict which servers can run. Do not put credentials in committed configuration or approve unknown tools merely to finish the exercise.

## Configure Playwright MCP

1. In your existing CLI session, enter `/mcp` to inspect configured servers. Reuse a working Playwright configuration rather than add a duplicate.
2. If needed, enter `/mcp add` and use <kbd>Tab</kbd> to move through the form.
3. Set **Server Name** to `playwright`, **Server Type** to **STDIO** (or **Local**), and **Command** to `npx @playwright/mcp@latest --headless`.
4. Set **Tools** to `*` for this reviewed browser server. This makes its tools available; it does not replace the CLI's permission controls.
5. After reviewing the package and its startup command, press <kbd>Ctrl</kbd>+<kbd>S</kbd> to save. Registration starts the server and may download the package; approve that setup deliberately and respond to any package prompt.
6. Enter `/mcp show playwright` and confirm that the server is connected and its browser tools are available.

The headless browser does not need a desktop window, which suits Codespaces. The interactive add flow saves the configuration in `~/.copilot/mcp-config.json` and makes the server available without restarting the CLI. It is user configuration, not a file to include in the feature PR. The [MCP setup guide][mcp-setup] documents the fields and configuration sources.

> [!NOTE]
> Project E2E dependencies and the MCP browser are related but may require different setup. If a browser or system dependency is missing, inspect the actual error and resolve the specific prerequisite with approval. Do not automatically install browsers or assume a connected server proves it can launch one.

## Start the correct app

Open a separate terminal in this same filtering checkout. Confirm the directory and branch, then start the app:

```bash
pwd
git branch --show-current
npm run dev
```

Read the actual local URL from the server output. In the codespace, the MCP server and app run in the same environment, so use that local URL, usually `http://localhost:4321`, rather than assume a forwarded browser URL is required.

If the port is occupied or Astro chooses another port, identify the server owner before proceeding. Do not reuse an unknown server or terminate it. Use the URL of the process you just started and keep that terminal open while testing.

## Observe filtering behavior

Replace the placeholders with the real issue URL, approved clarifications from Exercise 4, and the app URL:

```plaintext
Use the configured Playwright MCP server to validate the filtering feature against this issue: <filtering-issue-URL>. These are the clarifications approved during planning: <paste the agreed clarifications, or write none>. The app for this checkout is running at <local-app-URL>. Confirm the checkout, branch, and server under test before relying on its results.

Open the games page, note the unfiltered state, select one and then multiple categories, apply a publisher filter, and combine category and publisher selections. Exercise clearing and empty-result behavior according to the approved criteria. Check control labels, keyboard operation, and visible focus. Compare the displayed results with the selected filters and source data; do not infer success just because a control changed.

Use actual browser tool actions and report what you observed for each criterion, with failures or missing evidence clearly marked. Do not run another full test suite solely for this browser exercise, change application code, create tests or customizations, change branches, commit, push, or open a PR. Ask before installing anything or stopping another process.
```

Inspect the browser tool calls and the report. Did Copilot really select multiple categories and combine them with a publisher? Do the returned games match the agreed behavior? Does the report distinguish observable browser behavior from data-layer and automated-test coverage?

If something fails, record the observed behavior. Authorize any focused application fix separately, then repeat the affected browser checks and automated checks. Do not alter the acceptance criteria to match the implementation or count old evidence as verification of changed code.

## Stop the owned server and continue

Stop the development server with <kbd>Ctrl</kbd>+<kbd>C</kbd> in the terminal where you started it. Keep the Playwright MCP configuration available. Exercise 7 will coordinate fresh browser observations and automated E2E checks, which must not reuse a stale development server or another checkout's app.

Stay **Interactive** before creating the QA profile. You've observed browser behavior without creating another PR or branch; next, [create and use a QA agent][next-lesson] to combine requirements, coverage, the skill, and final evidence.

## Resources

- [Adding MCP servers to Copilot CLI][mcp-setup] documents setup and management.
- [Microsoft Playwright MCP][playwright-mcp] documents browser configuration and tools.
- [GitHub MCP registry][mcp-registry] lists other servers to evaluate.

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-overview]: https://docs.github.com/copilot/concepts/context/mcp
[mcp-setup]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
[playwright-mcp]: https://github.com/microsoft/playwright-mcp
[mcp-registry]: https://github.com/mcp
