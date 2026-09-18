---
title: "Lesson 7 - Create and use a QA agent"
description: "Create a QA custom agent that combines issue requirements, the quality-checks skill, and Playwright MCP."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

You've used the `quality-checks` skill to run automated checks and Playwright MCP to observe the filtering experience in a browser. Now you'll bring those capabilities together in a custom agent with a clearly defined QA process.

In this lesson, you will:

- explore how a custom agent works with instructions, skills, and MCP tools.
- create and inspect a reusable quality assurance profile.
- select the QA agent and review its findings against the filtering issue.

## Scenario

Tailspin Toys wants a consistent review of requirements, code quality, automated checks, test coverage, and browser behavior before opening a pull request (PR). A custom agent can coordinate that QA process and provide a reusable report.

## What is a custom agent?

A custom agent is a specialized version of Copilot defined in a Markdown profile. The profile describes the agent's purpose, instructions, and available tools. For this workshop, you'll define a QA role in `.github/agents/qa.agent.md` and select it in Copilot CLI.

The customizations you've used have different jobs. Repository instructions describe the team's standards. The `quality-checks` skill packages repeatable checks. Playwright MCP supplies browser tools. The QA profile tells Copilot how to use those capabilities to assess requirements and report findings. It doesn't replace them or require another conversation.

## Create the QA profile

Before opening the feature PR, you'll ask Copilot to create a reusable QA profile. The profile will define both the checks QA performs and the boundaries it must follow.

1. Confirm the filtering conversation is in Interactive mode.
2. Ask the default agent to create the new custom agent:

   ```plaintext
   Create a custom agent named QA in .github/agents/qa.agent.md. It should check features against their issues and agreed requirements, follow the repository instructions, run the quality-checks skill, use Playwright MCP to verify behavior, and add tests when coverage is missing.

   Have it report each requirement as pass, fail, or blocked with supporting evidence. It must ask before changing implementation code, and it must not commit changes or open pull requests. Use the current model and available tools. Just create the profile for now so I can review it.
   ```

## Inspect the profile

Before using the new agent, review its profile to confirm Copilot captured the intended QA workflow and boundaries. This prevents an incomplete or overly broad agent from changing the feature when you only want it verified.

1. Enter `/diff` and open `.github/agents/qa.agent.md`.
2. Read the frontmatter. The `description` is required; `name` is optional, but including it gives the agent a clear display name.
3. Read the profile instructions and confirm that QA starts from requirements, follows repository instructions, runs the `quality-checks` skill, and uses Playwright MCP.
4. Confirm that QA reports supporting evidence, asks before changing implementation code, and does not commit changes or open pull requests.
5. If the generated profile misses any of these responsibilities or boundaries, ask the default agent to revise it before continuing.

## Run QA against the issue

Copilot CLI loads project agents when a conversation starts. Resume the same filtering conversation after creating the profile, then select QA so it can use the issue and planning decisions already in context.

1. Exit Copilot CLI with `/exit`.
2. From the `game-filters-cli` branch, resume the conversation:

   ```bash
   copilot --resume "CLI filtering workflow" --yolo
   ```

3. Enter `/agent`, select **QA**, and confirm it is the active agent.
4. Ask QA to review the feature:

   ```plaintext
   Review the filtering feature against the issue and the decisions in our plan. Is it ready for a PR?
   ```

5. Confirm QA uses the correct issue and planning decisions. Provide the issue URL or missing context if it asks.
6. Read through the report it provides once it's done doing its work!

## Summary and next steps

You've added a reusable specialist role to the workflow and reviewed its work. In this lesson, you:

- explored how a custom agent works with instructions, skills, and MCP tools.
- created and inspected a reusable quality assurance profile.
- selected the QA agent and reviewed its findings against the filtering issue.

You now have the implementation, skill update, QA profile, tests, and verification report ready for review. Next, you'll [bring them together in a feature PR and use Agent Merge][next-lesson].

## Resources

- [Create custom agents for Copilot CLI][create-agents]
- [Custom agent configuration][agent-config]

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[create-agents]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli
[agent-config]: https://docs.github.com/copilot/reference/custom-agents-configuration
