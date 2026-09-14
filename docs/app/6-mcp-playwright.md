---
title: "Lesson 6 - Validate functionality with Playwright MCP"
description: "Configure Playwright MCP through Customize and observe filtering in a browser in the existing feature worktree."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

In the previous lesson you packaged and ran the project's checks through your quality-checks skill. Now give the agent access to a browser so it can observe the filtering UI directly. Stay in the same filtering session, worktree, and branch. This lesson adds browser evidence, not another feature, full test-suite run, or PR.

In this lesson, you will:

- understand what Model Context Protocol (MCP) is and how the GitHub Copilot app uses it.
- add the Playwright MCP server through **Customize**.
- ask the agent to drive a browser and explore your filtering feature.

## Scenario

While unit and end-to-end tests are important, validating updates to the UI requires actually interacting with the UI. You want to allow Copilot to use the website you're working on as a user would to further automate how changes are made, providing more confidence the updates perform as expected.

## What is Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] provides AI agents with a way to communicate with external tools and services. By using MCP, AI agents can communicate with external tools and services in real-time. This allows them to access up-to-date information (using resources) and perform actions on your behalf (using tools).

These tools and resources are accessed through an MCP server, which acts as a bridge between the AI agent and the external tools and services. The MCP server is responsible for managing the communication between the AI agent and the external tools (such as existing APIs or local tools like NPM packages). Each MCP server represents a different set of tools and resources that the AI agent can access.

A couple of popular existing MCP servers are:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: This server provides access to a set of APIs for managing your GitHub repositories. It allows the AI agent to perform actions such as creating new repositories, updating existing ones, and managing issues and pull requests.
- **[Playwright MCP Server][playwright-mcp-server]**: This server provides browser automation capabilities using Playwright. It allows the AI agent to perform actions such as navigating to web pages, filling out forms, and clicking buttons.

There are many other MCP servers available that provide access to different tools and resources. GitHub hosts an [MCP registry](https://github.com/mcp) to enhance discoverability and contributions to the ecosystem.

> [!CAUTION]
> Treat MCP servers as you would any other dependency in your project. Before using an MCP server, carefully review its source code, verify the publisher, and consider the security implications. Only use MCP servers that you trust and be cautious about granting access to sensitive resources or operations.

## Add the Playwright MCP server

The current [App customization documentation][customize-app] uses **Customize** in the sidebar for MCP discovery and management. MCP servers configured for your repositories or Copilot CLI can already be available in the App; inspect installed servers before adding a duplicate.

1. Select **Customize** in the sidebar.
2. Select **MCP**, then check **Installed** for an existing Playwright server.
3. If needed, find **Playwright** among the available servers, or use the custom-server flow documented by the publisher.
4. Review the publisher, configuration, and any installation prompts before approving them. Follow the prompts to add the server; organization policy or missing prerequisites can block setup.
5. Return to the existing filtering session, keeping **Interactive** mode. Confirm Playwright MCP browser tools are available before asking for validation. Do not create a new feature worktree as a setup workaround.

If setup fails, resolve the configuration or permission issue rather than accepting a claim that the agent browsed without tools. Browser visibility depends on the server configuration; actual tool activity and observations are the evidence.

## Ask Copilot to explore the feature via Playwright

Use the actual issue URL and approved clarifications saved in Lesson 4. Stop any manual dev server from earlier lessons before the agent starts its own. It must identify the checkout and server it is testing.

1. Use the following prompt to ask Copilot to validate the new functionality:

   ```plaintext
   Use the configured Playwright MCP server to observe the filtering feature against this issue: <filtering-issue-URL>. These are my approved planning clarifications: <paste the agreed clarifications, or write none>. Stay in this filtering worktree and branch.

   Identify the checkout, start its dev server, and use actual browser tools to exercise the required multiple-category selection, publisher filtering, combined filtering, accessible controls, and any agreed clearing or empty-result behavior. Report observations against the criteria, including failures or blocked checks. Do not claim behavior you did not observe.

   This step is browser observation, not another full automated test run. Do not change application code, tests, skills, or agent profiles, commit, push, or create a PR. Report missing MCP tools or prerequisites as blocked and ask before installing anything. Do not reuse another checkout's server or stop unrelated processes. Stop only the server you started when finished.
   ```

Inspect the Playwright MCP tool calls, the URL under test, and the reported browser observations. A narrative based only on source code or earlier E2E results does not demonstrate MCP.

2. Read the summary against the issue and approved clarifications. If there is a defect, authorize a focused fix separately, review the changed diff, and repeat relevant automated checks and browser observations. Evidence from before the fix is not proof of the resulting revision.
3. Confirm the agent stopped its own server. Keep this filtering session open and remain in **Interactive** mode before creating the QA profile in Lesson 7.

This stage establishes direct observation, not a replacement for automated coverage. A failure or blocked observation remains visible for QA.

## Summary and next steps

Congratulations, you used the Playwright MCP server to explore your feature in a real browser from the GitHub Copilot app! To recap, you:

- learned what Model Context Protocol (MCP) is and how the app makes MCP tools available.
- configured the Playwright MCP server through **Customize**.
- asked the agent to drive a browser and explore your filtering feature.

Next, bring the requirements, browser observations, coverage, and skill together with a specialist profile. Continue in this same session to [Lesson 7 - Create and use a QA agent][next-lesson]. Do not create the feature PR yet.

## Resources

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Configuring MCP servers in the GitHub Copilot app][customize-app]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
