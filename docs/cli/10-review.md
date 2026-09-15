---
title: "Exercise 10 - Wrap-up and next steps"
description: "Review the shared development workflow, reusable artifacts, and three CLI pull-request milestones."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

You've used Copilot CLI to move from a small change to a planned feature with reusable verification. Setup in Exercises 0–1 prepared your environment; the nine core modules in Exercises 2–10 taught a complete development workflow.

## Review the three PR milestones

| Milestone | Merged outcome | Review habit |
| --- | --- | --- |
| PR 1: star ratings | Existing `starRating` displayed on game cards, including `No rating yet` for `null` | Keep the change bounded and verify both cases |
| PR 2: custom instructions | A focused documentation convention and a small real-code demonstration | Check that instructions improve actual code, not just chat examples |
| PR 3: filtering and verification | Filtering, the quality-checks skill, QA profile, and associated tests | Review all checkpoints, current QA evidence, and CI before merging |

The first two PRs merged before the next milestone began from updated `main`. Exercises 4–8 shared one branch and checkout. Checkpoint commits preserved progress without creating a PR for every module. The controls exercise did not launch another feature or PR.

## Review the shared artifacts

These are the same core outcomes as the [Copilot app workshop][app-workshop], reached through a terminal interface:

- **Repository instructions** explain project context and standards; path-scoped instructions add detail for relevant files.
- **The filtering implementation and tests** satisfy the issue and the clarifications you approved during planning.
- **The quality-checks skill** packages reusable instructions and actual shell scripts that run the project's four checks.
- **Playwright MCP configuration** supplies browser tools for direct observation. In this CLI flow it lives in user configuration rather than the feature PR.
- **The QA custom agent** defines a reusable role that starts from requirements, checks coverage, uses the skill and browser tools, and reports truthful results.
- **PR and verification evidence** connects the reviewed changes to test results, browser observations, limitations, and CI.

A skill is more than a list of commands, and a profile is more than a filename. You inspected generated assets, confirmed actual execution, and selected the custom agent before relying on its report.

## Keep the validation purposes distinct

Planning clarified the requirements before implementation. Autopilot carried out that bounded plan; returning to Interactive restored deliberate review points before customization authoring.

The implementation used existing npm checks before any skill existed. The skill exercise proved its bundled scripts and argument forwarding worked. MCP demonstrated direct browser interaction rather than repeating a full suite. QA combined criteria, coverage, browser evidence, and all four skill-driven checks. The PR reused current QA results while CI checked the submitted revision.

Failures and blockers are useful outcomes. Missing browser tools, skipped tests, stale servers, or an unresolved requirement mean **NO-GO**, not permission to lower the standard. Test additions are justified by real gaps; adding no tests is correct when existing coverage is adequate.

## Carry these habits forward

- Give Copilot the issue, the reason for the change, and clear boundaries.
- Review plans before approving autonomous work.
- Inspect generated instructions, skills, and profiles before running them.
- Know which checkout, branch, server, and revision a result describes.
- Use the smallest justified correction and refresh evidence after changes.
- Keep installations, destructive actions, sharing, and PR merges explicit.

## Continue learning

The [Copilot app workshop][app-workshop] reaches the shared outcomes through its graphical interface and adds a canvas milestone. The [VS Code workshop][vscode-workshop] and [Cloud agent workshop][cloud-workshop] explore other ways to work with agents.

Use [Awesome Copilot][awesome-copilot] to find instruction, skill, and custom-agent examples. The [skill examples in Exercise 5][skill-examples] include contribution workflows, requirements documents, diagrams, and browser testing. Review prerequisites and behavior before adopting community content.

For everyday reference, consult the [CLI command reference][cli-reference], [agent skills documentation][agent-skills], and [custom-agent documentation][custom-agents]. Keep experimenting on bounded tasks and share only reviewed material through approved channels.

[previous-lesson]: ../9-slash-commands/
[app-workshop]: ../../app/
[vscode-workshop]: ../../vscode/
[cloud-workshop]: ../../cloud/
[skill-examples]: ../5-agent-skills/#more-skill-examples
[awesome-copilot]: https://github.com/github/awesome-copilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/concepts/agents/copilot-cli/about-custom-agents
