---
title: "Lesson 10 - Wrap-up and next steps"
description: "Recap the Copilot CLI workflow, two pull requests, reusable customizations, and further resources."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

You used GitHub Copilot CLI across a continuous Tailspin Toys workflow. You:

- prepared a Codespace, installed Copilot CLI, explored the project, and found the seeded filtering issue.
- added star ratings, reviewed the result in a forwarded browser, and manually merged your first pull request (PR).
- started from the filtering issue, defined the approach in Plan mode, built it in Autopilot mode, and reviewed it in Interactive mode.
- guided the agent with custom instructions, then customized the existing `quality-checks` skill and used it to run the project checks.
- added the Playwright Model Context Protocol (MCP) server and used it to explore filtering in a real browser.
- created and selected a quality assurance (QA) custom agent to assess requirements, coverage, skill results, and browser evidence.
- reviewed the complete filtering change and authorized Agent Merge for the filtering PR.
- explored slash commands for context, models, sharing, and optional cloud delegation.

## What you shipped

The workshop has two PR milestones, each on its own branch from updated `main`:

1. **Star ratings:** display the existing `starRating` and an explicit unrated state on game cards.
2. **Filtering and quality workflow:** implement filtering, update the instructions and apply them to the feature, customize the `quality-checks` report, create a QA profile, and include the associated tests.

From planning filtering through opening its PR, you used the same conversation and branch. We combined that work in one PR to streamline the workshop.

## Different kinds of verification

You checked the code in several ways: automated tests, your own browser inspection, and Copilot's browser exploration through MCP. The `quality-checks` skill ran the project checks and reported them in your new format. QA brought those results together with a review of requirements and test coverage before the PR.

Tests added should close genuine gaps; a QA run that needs no new tests can be correct. Review code and evidence before authorizing merge, and refresh affected evidence after changes.

## Best practices

The context and tools you give Copilot shape its work. In this workshop, you updated instructions, customized a skill, created a QA profile, and configured an MCP server. Reuse these customizations across conversations and adjust them as your team's needs change. Instructions set standards, skills describe repeatable tasks, custom agents define specialist roles, and MCP servers connect external tools. Review the actual changes and tool results, not just the agent's summary.

Match the **mode and model** to the task. Use **Plan** to think through an approach before building, **Interactive** to stay in the loop on focused changes, and **Autopilot** for well-scoped tasks. Choose a faster model for routine edits and a more capable model for complex work.

Context still matters as much as infrastructure. Clearly describing *what* you want built, *why*, and *how* meaningfully changes the output.

## More to explore

You've covered the core workflow. A few more CLI features worth a look:

- `/review` to ask the code review agent to analyze changes.
- `/rubber-duck` to talk through a problem and get another perspective.
- `/fleet` to orchestrate independent subtasks in parallel.
- `/worktree` to isolate a separate task.
- `/delegate` to send a task to Copilot cloud agent.

## Next steps

The best way to improve with any tool is to keep using it! Use it for production code, for hobby code, for the little app you've had in mind for years but never got around to building. Share your learnings with your team, and learn from theirs. And, as always, explore the documentation.

If you want to extend Tailspin Toys from the terminal, continue with the optional [Foundry Backer Concierge series][foundry]. To compare other environments, explore the [VS Code workshop][vscode], the [GitHub Copilot app workshop][app], or the [Copilot cloud agent workshop][cloud].

## Resources

- [About GitHub Copilot CLI][about-cli]
- [Copilot CLI command reference][cli-reference]
- [Customize Copilot CLI][customize-cli]
- [Manage pull requests with Copilot CLI][manage-prs]

[previous-lesson]: ../9-cli-power-tools/
[foundry]: ../8-foundry-agent/
[vscode]: ../../vscode/
[app]: ../../app/
[cloud]: ../../cloud/
[about-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[customize-cli]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot
[manage-prs]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests
