<!--
  GENERATED FILE — do not edit.
  Source: docs/src/content/docs/cli/5-agent-skills.mdx
  Run `python scripts/render-markdown.py` to regenerate.
-->

# Exercise 5 - Using agent skills

Doing app development often involves repeatable tasks like generating builds, running tests, or creating pull requests. **Agent skills** let you give Copilot — and other AI agents — guidance on how to perform those tasks. A skill is a folder of instructions, scripts, and resources that the agent can load on demand. [Agent Skills is an open standard][agent-skills-repo] used by a range of agents, so the same skill can work across Copilot Chat in agent mode, Copilot cloud agent, and Copilot CLI.

Skills live in the `.github/skills` folder of a project, or globally in `~/.copilot/skills`. Each skill is a folder containing a `SKILL.md` file with YAML frontmatter (a `name` and a `description`) followed by the markdown instructions:

```yaml
---
name: branching-commits-prs
description: All changes to the repository must be done through a pull request (PR). A branch must always be created, and commits grouped together logically. Whenever asked to create commit messages, to push code, or create a pull request (PR), use this skill so everything is done correctly.
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

1. Open `.github/skills/branches-commits-prs/SKILL.md`.
2. Note the name and description. Notice how the description highlights the scenario in which it should be used, which is whenever a request is made to create a pull request or committing code.
3. Read through the skill. Notice the rules are defined about how branches should be created, commits generated, and the contents of the pull request.

## Using the skill

As highlighted previously, skills are automatically invoked by Copilot CLI. As a result, all we need to do is ask Copilot to create a PR!

> [!TIP]
> **Start a Copilot CLI session**
>
> Before you start the exercises below, return to your codespace and open a terminal (<kbd>Ctrl</kbd>+<kbd>\`</kbd> if one isn't already open). Then start Copilot CLI with the `--allow-all-tools` flag so it can run commands without prompting for each one:
>
> ```bash
> copilot --allow-all-tools
> ```
>
> To pick up your most recent session for this project instead of starting fresh, run `copilot --allow-all-tools --continue`. If Copilot CLI is already running from an earlier exercise, send `/clear` to start a clean conversation.
>
> > [!WARNING]
> > `--allow-all-tools` skips Copilot's per-action approval prompts. Only use it in an isolated environment like a Codespace or VM, and never alias it as your default. See [Generating code with Copilot CLI][allow-all-warning] for the full explanation.

[allow-all-warning]: 4-generating-code.md#utilize-plan-mode

1. Ask Copilot to create a PR by using the following prompt:

    ```
    Can you please create a pull request for me!
    ```

2. Copilot will acknowledge the request. After a few moments, you'll notice Copilot will indicate it's utilizing the **branches-commits-prs** skill.

    ![Screenshot of the agent skill being called by Copilot CLI](../images/cli-5-agent-skill.png)

3. Copilot will then follow the instructions in the skill. It will start by running the tests, then create a branch, commits, and eventually the PR.
4. Once the PR is created, return to your repository and open the PR. Note the sections follow the guidelines set forth in the skill, matching the requirements the team put forth.

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

[previous-lesson]: 4-generating-code.md
[next-lesson]: 6-custom-agents.md
[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
