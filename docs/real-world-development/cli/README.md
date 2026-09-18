---
slug: real-world-development/cli
title: "GitHub Copilot CLI"
description: "Build, verify, and deliver two Tailspin Toys changes while learning Copilot CLI modes, customizations, MCP tools, and pull request automation."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

**[GitHub Copilot CLI][about-copilot-cli]** puts GitHub Copilot in your terminal as an agentic coding assistant. It explores codebases, generates code, runs commands, and connects to external tools — all from the command line, so you can stay in the flow without switching to a graphical editor.

The workshop follows one continuous Tailspin Toys workflow:

1. Prepare the project in GitHub Codespaces, install Copilot CLI, and get oriented.
2. Make a focused star-rating change, review it in the browser, and manually merge your first pull request (PR).
3. Start from the filtering issue, define the approach in Plan mode, build it in Autopilot mode, then review it in Interactive mode.
4. Update the repository instructions and apply them to the filtering work.
5. Customize the existing `quality-checks` skill and use it to run the project checks.
6. Add the Playwright Model Context Protocol (MCP) server and use it to explore filtering in a browser.
7. Create a quality assurance (QA) custom agent and use it to review requirements, coverage, and verification evidence.
8. Review the complete filtering change and use Agent Merge for the filtering PR.
9. Explore useful slash commands for context, models, sharing, and optional cloud delegation.

To keep the workshop focused, you'll create two PRs: star ratings, then filtering with the instruction updates, skill update, QA profile, and tests. The filtering and quality workflow shares one conversation and branch so you can build on your work as you explore each tool.

## Lessons

| Lesson | Topic | Description |
| ------ | ----- | ----------- |
| [0. Prerequisites][ex0] | Setup | Create your repository and Codespace |
| [1. Installing Copilot CLI][ex1] | Installation | Install and authenticate Copilot CLI, then get oriented |
| [2. Add star ratings: a quick win][ex2] | First change | Display existing ratings and the null fallback, then merge your first PR |
| [3. Agent modes: Plan and Autopilot][ex3] | Agent modes | Plan the feature from its issue, build with Autopilot, then review in Interactive mode |
| [4. Guide Copilot with custom instructions][ex4] | Context | Explore and update instructions, then apply them to filtering |
| [5. Customize and use a quality-checks skill][ex5] | Repeatable checks | Explore the existing skill, change its report format, and run it |
| [6. Validate functionality with Playwright MCP][ex6] | Browser observation | Configure MCP in the CLI and inspect filtering behavior |
| [7. Create and use a QA agent][ex7] | Requirements and coverage | Create and select a specialist profile, then gather final verification evidence |
| [8. Create and merge the feature PR][ex8] | Review and merge | Review the complete change, create the PR, and use Agent Merge |
| [9. Slash commands in GitHub Copilot CLI][ex9] | CLI features | Explore context, models, sharing, and optional delegation to cloud agent |
| [10. Wrap-up and next steps][ex10] | Summary | Review the workflow, reusable customizations, and further resources |
| [Optional: Incorporate Foundry][foundry] | Hosted agents | Prepare a model, deploy a catalog-grounded agent, and connect it to the website |

## Prerequisites

Before attending this workshop, please ensure you have:

- [ ] A GitHub account with an active **Copilot Student, Pro, Pro+, Business, or Enterprise** plan
- [ ] Permission to create a repository and Codespace
- [ ] Basic familiarity with terminal or command-line operations

> [!TIP]
> No paid plan? Verified students can get GitHub Copilot for free through [GitHub Education][student-plan]. The **Copilot Student** plan includes the agent, MCP, code review, and Copilot CLI features this workshop uses.

> [!NOTE]
> If you are using Copilot Business or Copilot Enterprise, ensure your administrator has enabled Copilot CLI for use.

## Get started

**[Start with the prerequisites →][ex0]**

[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[student-plan]: https://github.com/education/students
[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-agent-modes/
[ex4]: 4-custom-instructions/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-cli-power-tools/
[ex10]: 10-review/
[foundry]: 8-foundry-agent/
