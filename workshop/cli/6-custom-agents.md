<!--
  GENERATED FILE — do not edit.
  Source: docs/src/content/docs/cli/6-custom-agents.mdx
  Run `python scripts/render-markdown.py` to regenerate.
-->

# Exercise 6 - Custom agents with GitHub Copilot CLI

## What are custom agents?

[Custom agents][custom-agents-concept] in GitHub Copilot allow you to create specialized AI assistants tailored to specific tasks or domains within your development workflow. By defining agents through markdown files in the `.github/agents` folder of your repository, you can provide Copilot with focused instructions, best practices, coding patterns, and domain-specific knowledge that guide it to perform particular types of work more effectively. Teams can codify their expertise into reusable agents — an accessibility agent that enforces [WCAG][wcag] compliance, a security agent that follows secure coding practices, or a testing agent that maintains consistent test patterns.

Custom agents are defined by markdown files in the `.github/agents` folder of your project, or globally in `~/.copilot/agents`. Each file has YAML frontmatter with at least a `name` and `description`, followed by a markdown prompt that defines the agent's behavior, expertise, and instructions.

### Custom agents compared with agent skills

There's some logical overlap between custom agents and [agent skills][agent-skills-concept]. Both are primarily defined with markdown files and tell an AI how to perform operations. The cleanest way to separate them: a **custom agent** is the worker, and **skills** are tools.

Custom agents have their own context window and are built to orchestrate skills (and even other agents) as part of doing their work. In this lab, the accessibility custom agent reviews and updates the site against accessibility guidelines; as part of that work it could call skills like the PR skill you saw earlier, or one that runs and manages tests.

> [!NOTE]
> There's no single "right" way to author a custom agent. As with anything in AI, test and iterate to find what works for your environments and scenarios.

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/

## Scenario

Many web applications fall short of being accessible to all users, and the website you're working in is no exception. You'll use a custom agent to identify and resolve accessibility shortcomings.

Tailspin Toys is committed to ensuring their crowdfunding platform is accessible to all users, regardless of their visual abilities or preferences. Recent user feedback has highlighted that some users find the current dark theme difficult to read due to insufficient contrast between text and background colors. To address this accessibility concern, the design team has requested the implementation of a high-contrast mode that users can toggle on and off.

Because accessibility is critical, you want to ensure this is implemented as quickly as possible. You're going to utilize a custom agent to generate the functionality.

In this exercise, you will:

- explore custom agents.
- enable a custom agent and assign it a task using Copilot CLI.

## Reviewing the accessibility custom agent

A custom agent has already been created for you for accessibility. Let's review the contents to understand how it will guide Copilot.

1. Open `.github/agents/accessibility.md`.
2. Note the header section with the name and description of the agent.

> [!WARNING]
> This section is required for custom agents.

3. From there, scan and review the next sections which highlight:
    - Core responsibilities when generating code for an accessible website.
    - Best practices for accessibility.
    - Code examples for HTML, CSS and JavaScript.
    - A list of common pitfalls and mistakes.

## Using a custom agent in Copilot CLI

You can start a custom agent in Copilot CLI by using the `/agent` command. Let's perform an accessibility pass on our website.

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

1. Bring up the list of agents by typing `/agent` in the prompt window in Copilot CLI and selecting <kbd>Enter</kbd>.
2. Select the **Accessibility agent** from the list of available agents.
3. Use the following prompt to ask the accessibility agent to perform a review and generate fixes for one particular class of possible errors related to HTML headers:

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. We're going to build in stages, so for now focus on headers, ensuring we're following good guidelines. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. Copilot gets to work on the task! It will start by retrieving the issue, then performing the review, generating updates, and finally creating the PR. You should also notice when it creates the PR it utilizes the skill focused on PRs for the project.

> [!NOTE]
> This process will likely take a few minutes. It's a good time to reflect on everything you've learned, enjoy a beverage, or sneak ahead to the next module which talks about some additional commands available to you in Copilot CLI.

## Summary and next steps

This lesson explored [custom agents][custom-agents] in GitHub Copilot, specialized AI assistants tailored to specific tasks and domains. With custom agents you can codify your team's expertise and standards into reusable agents that guide Copilot to perform particular types of work more effectively.

You explored these concepts:

- how to create a custom agent.
- using a custom agent in Copilot CLI.

Next up, let's explore [some slash commands][next-lesson] to learn some additional tricks with Copilot CLI.

## Resources

- [Custom agents][custom-agents]
- [Creating custom agents for a repository][creating-custom-agents]
- [Custom agents on awesome-copilot][awesome-copilot-agents]
- [Preparing to use custom agents in your organization][org-custom-agents]
- [Preparing to use custom agents in your enterprise][enterprise-custom-agents]

[previous-lesson]: 5-agent-skills.md
[next-lesson]: 7-slash-commands.md
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
