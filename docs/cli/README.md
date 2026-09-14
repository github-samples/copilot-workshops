---
slug: cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** puts GitHub Copilot in your terminal as an agentic coding assistant. It explores codebases, generates code, runs commands, and connects to external tools — all from the command line, so you can stay in the flow without switching to a graphical editor.

After setup in Exercises 0–1, you'll complete nine core modules in Exercises 2–10. Start with a star-rating quick win, establish documentation instructions, and build filtering with **Plan** and **Autopilot** modes. Then create a reusable quality-checks skill, validate behavior with Playwright MCP, create a QA agent, and ship the feature. Finish by exploring CLI controls and reviewing what you've built.

## Exercises

| Exercise | Topic | Description |
|----------|-------|-------------|
| [0. Prerequisites][ex0] | Setup | Create your repository and codespace |
| [1. Installing Copilot CLI][ex1] | Installation | Install and authenticate Copilot CLI |
| [2. Add star ratings: a quick win][ex2] | First change | Display existing ratings, validate, and merge PR 1 |
| [3. Guide Copilot with custom instructions][ex3] | Context | Add a documentation convention, demonstrate it, and merge PR 2 |
| [4. Build filtering with Plan and Autopilot][ex4] | Implementation | Review a plan, approve Autopilot, test, and checkpoint |
| [5. Create and use a quality-checks skill][ex5] | Skills | Generate, inspect, and run shell-bundled checks |
| [6. Validate functionality with Playwright MCP][ex6] | Browser tools | Observe filtering behavior in a real browser |
| [7. Create and use a QA agent][ex7] | Agents | Audit requirements and coverage, then collect final evidence |
| [8. Create and merge the feature PR][ex8] | Delivery | Review filtering and reusable customizations together in PR 3 |
| [9. Explore slash commands and CLI options][ex9] | CLI controls | Inspect context, models, sessions, and sharing destinations |
| [10. Wrap-up and next steps][ex10] | Summary | Review common artifacts and the three PR milestones |

## Branches and pull requests

You'll merge three pull requests: star ratings; instructions and a small demonstration; then filtering with the quality-checks skill, QA profile, and associated tests. Merge each of the first two PRs before starting the next milestone from updated `main`.

Exercises 4–8 share one feature branch and checkout. Save checkpoint commits along the way; skill creation, MCP setup, and QA selection do not start new feature branches. Exercise 9 explores controls without launching another feature or PR.

## Prerequisites

Before attending this workshop, please ensure you have:

- [ ] A GitHub account with an active **Copilot Student, Pro, Pro+, Business, or Enterprise** plan
- [ ] Basic familiarity with terminal/command line operations
- [ ] Git installed and configured

> [!TIP]
> No paid plan? Verified students can get GitHub Copilot for free through [GitHub Education][callout-student-plan-education]. The **Copilot Student** plan includes the agent, MCP, code review, and Copilot CLI features this workshop uses — so you can complete every harness with it.

> [!NOTE]
> If you are using Copilot Business or Copilot Enterprise, ensure your admin has enabled Copilot CLI for use.

## Get Started

**[Start with Exercise 0: Prerequisites →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
[callout-student-plan-education]: https://github.com/education/students
