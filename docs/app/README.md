---
slug: app
title: "GitHub Copilot app"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

The **[GitHub Copilot app](https://docs.github.com/copilot/concepts/agents/github-copilot-app)** is a desktop application built on Copilot CLI that brings agent-driven development into a single, focused workspace. It adds parallel agent sessions, switchable session modes, shared canvases, and native GitHub issue and pull request management — including **Agent Merge**, which shepherds a pull request through rebases, review feedback, CI fixes, and merge.

Setup Lessons 0–1 prepare your project and App workspace. The nine core modules, Lessons 2–10, begin with a star-rating quick win and a documentation convention demonstrated in real code. Then you'll plan and build filtering, create and execute a shell-bundled quality-checks skill, observe the feature through Playwright MCP, and create a QA custom agent to assess requirements and coverage. You'll review the complete feature PR and authorize Agent Merge, then create and merge a shared triage canvas.

The workshop has four PR milestones: star ratings; instructions with their demonstration; filtering with the skill, QA profile, and tests; then the canvas. Start each milestone from updated `main`, using one branch per PR rather than one per module. Lessons 4–8 stay in the same filtering session, worktree, and branch. Reopening the canvas adds issue context without launching another feature or fifth PR. Automations are linked as a next step, not an additional exercise.

## Lessons

| Lesson | Topic | Description |
|--------|-------|-------------|
| [0. Prerequisites][ex0] | Setup | Install Node.js and create your copy of the Tailspin Toys project |
| [1. Install the Copilot app][ex1] | Setup | Install the app, connect your project, and get oriented in the workspace |
| [2. Add star ratings: a quick win][ex2] | First change | Display existing ratings and the null fallback, then merge PR 1 |
| [3. Guide Copilot with custom instructions][ex3] | Context | Add a documentation standard and a real demonstration, then merge PR 2 |
| [4. Build filtering with Plan and Autopilot][ex4] | Implementation | Approve the plan, implement and check filtering, and checkpoint |
| [5. Create and use a quality-checks skill][ex5] | Repeatable checks | Create, inspect, and execute bundled shell scripts |
| [6. Validate functionality with Playwright MCP][ex6] | Browser observation | Configure MCP through Customize and inspect filtering behavior |
| [7. Create and use a QA agent][ex7] | Requirements and coverage | Select a specialist profile and gather final verification evidence |
| [8. Create and merge the feature PR][ex8] | Review and merge | Review filtering, the skill, QA profile, and tests, then authorize Agent Merge for PR 3 |
| [9. Create a triage canvas][ex9] | Collaboration | Share a repository-backed canvas in PR 4 and add issue context |
| [10. Wrap-up and next steps][ex10] | Summary | Review the workflow, artifacts, and further resources |

## Prerequisites

Before attending this workshop, please ensure you have:

- [ ] A GitHub account with an active **Copilot Student, Pro, Pro+, Business, or Enterprise** plan
- [ ] A computer running **macOS, Linux, or Windows**
- [ ] [Git installed][install-git] on your computer

> [!TIP]
> No paid plan? Verified students can get GitHub Copilot for free through [GitHub Education][callout-student-plan-education]. The **Copilot Student** plan includes the agent, MCP, code review, and Copilot CLI features this workshop uses — so you can complete every harness with it.

> [!NOTE]
> Because the Copilot app runs on your own machine rather than in a codespace, [Lesson 0][ex0] walks you through installing Node.js and creating your copy of the project before you install the app.

> [!NOTE]
> If you are using Copilot Business or Copilot Enterprise, your administrator must enable the **Copilot CLI** policy before you can use the app.

## Get Started

**[Start with Lesson 0: Prerequisites →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students
