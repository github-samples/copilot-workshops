---
title: "Lesson 6 - Validate functionality with Playwright MCP"
description: "Inspect or configure Playwright MCP in Copilot CLI and use it to explore the filtering feature in a browser."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

As we've already highlighted, there's more to writing code than just writing code. We need to work with data, external services, and even allow for additional automations to be available to Copilot. This is where MCP servers come into play. MCP servers allow Copilot to go beyond what's built into the CLI, providing it even more tools and services.

In this lesson, you will:

- understand what Model Context Protocol (MCP) is and how Copilot CLI uses it.
- add the Playwright MCP server if it is not already available.
- ask the agent to drive a browser and explore your filtering feature.

## Scenario

While unit and end-to-end tests are important, validating updates to the UI requires actually interacting with the UI. You want to allow Copilot to use the website you're working on as a user would to further automate how changes are made, providing more confidence the updates perform as expected.

## What is Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] provides AI agents with a way to communicate with external tools and services. By using MCP, AI agents can communicate with external tools and services in real time. This allows them to access up-to-date information and perform actions on your behalf.

These tools and resources are accessed through an MCP server, which acts as a bridge between the AI agent and the external tools and services. Each MCP server represents a different set of tools and resources that the AI agent can access.

A couple of popular existing MCP servers are:

- **[GitHub MCP Server][github-mcp]**: Provides access to APIs for managing GitHub repositories, issues, and pull requests.
- **[Playwright MCP Server][playwright-mcp-server]**: Provides browser automation capabilities using Playwright.

There are many other MCP servers available. GitHub hosts an [MCP registry][mcp-registry] to enhance discoverability and contributions to the ecosystem.

> [!CAUTION]
> Treat MCP servers as you would any other dependency in your project. Before using one, review its source code, verify the publisher, and consider the security implications.

## Add the Playwright MCP server

MCP servers configured for Copilot CLI may already be available, so check before adding a duplicate.

1. Enter:

   ```plaintext
   /mcp list
   ```

2. If a connected Playwright server is listed, continue to the next section.
3. If Playwright is missing, enter:

   ```plaintext
   /mcp add
   ```

4. Name the server `playwright`, choose a local or STDIO server, and use this command:

   ```plaintext
   npx -y @playwright/mcp@latest --headless
   ```

   If the form separates the command from its arguments, use `npx` as the command and `-y`, `@playwright/mcp@latest`, and `--headless` as the arguments.

5. Review the publisher and command, save the configuration, then use `/mcp list` to confirm the server is connected.

> [!NOTE]
> Copilot CLI does not load `.vscode/mcp.json`, which is why this lesson checks the active CLI configuration.

## Ask Copilot to explore the feature via Playwright

The issue and your planning decisions are already in context. Copilot can start the application and use the headless browser tools from the same Codespace.

1. Use the following prompt:

   ```plaintext
   Start the app and use Playwright MCP to check filtering against the issue and our plan. Tell me what works and what doesn't, without making changes. Stop the server you started when you're done.
   ```

2. Sit back and watch!
3. Read the report and compare it with the filtering issue and the decisions you made during planning.

Copilot will start the server, use Playwright to interact with the website, stop the server, and give you a report.

## Summary and next steps

Congratulations, you used the Playwright MCP server to explore your feature in a real browser from Copilot CLI! To recap, you:

- learned what Model Context Protocol (MCP) is and how Copilot CLI uses it.
- added the Playwright MCP server if it was not already available.
- asked the agent to drive a browser and explore your filtering feature.

Next, you'll [create a QA custom agent][next-lesson] that brings the skill and browser tools together in a specialist role.

## Resources

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Add MCP servers to Copilot CLI][add-mcp]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[github-mcp]: https://github.com/github/github-mcp-server
[mcp-registry]: https://github.com/mcp
[add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
