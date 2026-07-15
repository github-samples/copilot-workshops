---
title: "Exercise 5 - Using agent skills"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Doing app development often involves repeatable tasks like generating builds, running tests, or creating pull requests. **Agent skills** let you give Copilot — and other AI agents — guidance on how to perform those tasks. A skill is a folder of instructions, scripts, and resources that the agent can load on demand. [Agent Skills is an open standard][agent-skills-repo] used by a range of agents, so the same skill can work across Copilot Chat in agent mode, Copilot cloud agent, Copilot CLI, and the GitHub Copilot app.

Skills live in the `.github/skills` folder of a project, or globally in `~/.copilot/skills`. Each skill is a folder containing a `SKILL.md` file with YAML frontmatter (a `name` and a `description`) followed by the markdown instructions:

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

Skills can also include subfolders with scripts, assets, and reference material. The full structure is covered in the [agent skills specification][agent-skills-spec].

> [!TIP]
> Skills are loaded dynamically. The agent decides which skill applies based on the `description` field — a clear, scenario-specific description is the difference between a skill that gets used and one that gets ignored.

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
Let's explore how a skill can ensure pull requests follow the specifications set forth by our team.

## Scenario

The team has a set of requirements for pull requests (PR):

- clear commit messages, with files grouped logically.
- all tests must pass before a PR is created.
- each PR must contain the following sections:
    - a description of why the changes were made.
    - an overview of the files changed.
    - snippets of important code blocks.
    - details of the changes made grouped together.

As the team is using Copilot to generate code and PRs, it wants to ensure the AI tools follow these requirements.

In this exercise you will:

- explore an existing skill for creating pull requests.
- learn how skills are utilized by the AI agent.
- create a PR which matches the guidelines with the help of the skill.

## Executing skills

Skills are loaded dynamically when the agent determines they're necessary. The decision of what skills to use is driven by the description in the `SKILL.md` file. As such, it's important to have clear descriptions which define the use case for the skill.

## Exploring the PR skill

Because Tailspin Toys has a set of requirements for creating PRs, they created a skill to help AI tools be able to generate PRs which follow these guidelines. Let's explore the skill to understand what it'll do.

1. Open `.github/skills/make-contribution/SKILL.md`.
2. Note the name and description. Notice how the description highlights the scenario in which it should be used, which is whenever a request is made to create a pull request or committing code.
3. Read through the skill. Notice the rules are defined about how branches should be created, commits generated, and the contents of the pull request.

## Using the skill

As highlighted previously, skills are automatically invoked by Copilot CLI. As a result, all we need to do is ask Copilot to create a PR!

> [!TIP]
> **Start a Copilot CLI session**
>
> Before you start the exercises below, return to your codespace and open a terminal (<kbd>Ctrl</kbd>+<kbd>\`</kbd> if one isn't already open). Then start Copilot CLI with `--yolo` and `--enable-all-github-mcp-tools`:
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> To pick up your most recent session for this project instead of starting fresh, run `copilot --yolo --enable-all-github-mcp-tools --continue`. If Copilot CLI is already running from an earlier exercise, send `/clear` to start a clean conversation.
>
> `--enable-all-github-mcp-tools` enables the read/write GitHub MCP tools for the current session, so Copilot can read your backlog and open pull requests during the workshop flow.

> [!CAUTION]
> `--yolo` enables full automatic permissions (`--allow-all-tools`, `--allow-all-paths`, and `--allow-all-urls`). Use it only in an isolated environment like a Codespace or VM, and never alias it as your default for day-to-day development. See [Allowing and denying tool use][allow-all-warning] for details.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
1. Ask Copilot to create a PR by using the following prompt:

    ```
    Can you please create a pull request for me!
    ```

2. Copilot will acknowledge the request. After a few moments, you'll notice Copilot will indicate it's utilizing the **make-contribution** skill.

    ![Screenshot of the agent skill being called by Copilot CLI](../_images/cli-5-agent-skill.png)

3. Copilot will then follow the instructions in the skill. It will start by running the tests, then create a branch, commits, and eventually the PR.
4. Once the PR is created, return to your repository and open the PR. Note the sections follow the guidelines set forth in the skill, matching the requirements the team put forth.
5. Before moving to the next exercise, reset your local workspace to a fresh branch from `main` so your accessibility work stays separate from this filtering PR:

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## Summary and next steps

With the help of an agent skill, you created a new PR which matches documented requirements! You:

- explored an existing skill for creating pull requests.
- learned how skills are utilized by the AI agent.
- created a PR which matches the guidelines with the help of the skill.

Skills are perfect for tasks, but for more robust operations we want to take advantage of [custom agents][next-lesson], which we'll explore next!

## Resources

- [About Agent Skills][about-agent-skills]
- [Agent Skills Specification][agent-skills-spec]
- [Agent Skills Repository][agent-skills-repo]
- [Agent Skills on awesome-copilot][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
