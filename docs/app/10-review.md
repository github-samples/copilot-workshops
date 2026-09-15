---
title: "Lesson 10 - Wrap-up and next steps"
description: "Recap the nine core App modules, four PR milestones, and reusable quality workflow, then explore further resources."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Over the last several lessons, you took a feature from idea to merge with the GitHub Copilot app, including:

- connecting a repository and orienting to the app's workspace and your seeded backlog.
- starting sessions from a direct task and from issues, and using Plan and Autopilot modes to control how the agent works.
- guiding the agent with custom instructions, then asking it to create a reusable skill with shell scripts that you inspected and ran for lint, unit tests, end-to-end tests, and type checks.
- testing your work with the Playwright MCP server in a real browser.
- creating and selecting a QA custom agent to assess requirements, coverage, skill-script results, and browser evidence.
- collaborating with the agent on a shared canvas.
- explicitly merging the early PRs yourself, then authorizing **Agent Merge** within the feature and canvas PR workflows.

Setup Lessons 0–1 led into nine core modules, Lessons 2–10. Take a moment to review the artifacts and where to go next; this wrap-up does not launch another hands-on task.

## What you shipped

The workshop has four PR milestones, each on its own branch from updated `main`:

1. **Star ratings:** display the existing `starRating` and an explicit unrated state on game cards.
2. **Instructions and demonstration:** add the documentation convention and verify its effect on a small real code change.
3. **Filtering and quality workflow:** implement the issue, create the shell-bundled `quality-checks` skill and QA profile, and include the associated tests.
4. **Repository-backed triage canvas:** share a board that adds issue context without automatically implementing another feature.

Lessons 4–8 used the same filtering session, worktree, and branch. Checkpoint commits preserved progress within PR 3; skills, MCP configuration, and QA did not need separate feature branches. Each later milestone began only after the earlier PR merged and the fresh session branch was updated from `origin/main`.

## Different kinds of verification

The early features used existing npm checks. Filtering added your manual browser inspection. The skill made the four checks repeatable through bundled scripts, MCP added direct agent browser observations, and QA combined requirements and coverage with final verification. The PR reused QA evidence only while it applied to the submitted revision.

Tests added should close genuine gaps; a QA run that needs no new tests can be correct. Missing tools, skipped checks, and failures are visible blockers, not passes. Review code and evidence before authorizing merge, and refresh affected evidence after changes.

## Best practices

When using any AI tool, the infrastructure around it drives the quality of what you get out. You created instructions, a skill, and a QA profile in this workshop — review them and reuse them across sessions. Custom agents define specialist roles and instructions, with available tools governed by configuration and harness permissions; skills package reusable task instructions, executable scripts, and supporting resources loaded on demand. A custom agent can execute scripts too, including those bundled with a skill. Confirm actual script execution and custom-agent selection rather than relying on a convincing description.

Match the **mode and model** to the task. Use **Plan** to think through an approach before building, **Interactive** to stay in the loop on focused changes, and **Autopilot** only for well-scoped, isolated tasks. Choose a faster model for routine edits and a more capable model with higher reasoning effort for complex work.

Context still matters as much as infrastructure. Clearly describing *what* you want built, *why*, and *how* meaningfully changes the output. Quick chats are a great place to scope an idea before you commit it to a full session.

## More to explore

You've covered the core workflow. A few more features worth a look:

- **Quick chats** for fast, throwaway questions that don't need a full session.
- [**Automations**][using-automations] for recurring or on-demand tasks such as summarizing recent work. Review the schedule, permissions, and scope before adopting one; creating an automation is a next step, not part of this workshop.
- **Rubber duck** to talk through a problem and get high-signal feedback before you build.
- [**Custom agents**][custom-agents] to package a role, its tools, and its instructions for repeatable, specialized work.
- [`/chronicle`][chronicle] to generate a narrative of what happened in a session.
- [Bring your own key (BYOK)][byok] to use models from your own provider, including local models via Ollama, Foundry Local, or LM Studio.
- [Cloud sandboxes][sandboxes] to run sessions in a GitHub-hosted isolated environment.
- [Deep links][deep-links] to open the app straight into a repository, session, or prompt.

## Next steps

The best way to improve with any tool is to keep using it! Use it for production code, for hobby code, for the little app you've had in mind for years but never got around to building. Share your learnings with your team, and learn from theirs. And, as always, explore the documentation.

If you'd like to explore more of the GitHub Copilot ecosystem, check out the [VS Code harness][vscode-harness], the [Copilot CLI harness][cli-harness], or the [Cloud agent harness][cloud-harness].

## Resources

- [About the GitHub Copilot app][about-copilot-app]
- [Getting started with the GitHub Copilot app][getting-started]
- [Customize the GitHub Copilot app][customize]
- [Using automations][using-automations]
- [Working with canvas extensions][canvas-docs]
- [About cloud and local sandboxes][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links
