# Exercise 6 - Custom agents with GitHub Copilot CLI

| [← Previous lesson: Agent Skills][previous-lesson] | [Next lesson: Slash Commands →][next-lesson] |
|:--|--:|

[Custom agents][custom-agents] in GitHub Copilot allow you to create specialized AI assistants tailored to specific tasks or domains within your development workflow. By defining agents through markdown files in the `.github/agents` folder of your repository, you can provide Copilot with focused instructions, best practices, coding patterns, and domain-specific knowledge that guide it to perform particular types of work more effectively. This allows teams to codify their expertise and standards into reusable agents. You might create an accessibility agent that ensures [WCAG][wcag] compliance, a security agent that follows secure coding practices, or a testing agent that maintains consistent test patterns—enabling developers to leverage these specialized capabilities on-demand for faster, more consistent implementations.

You'll explore the following with custom agents:

- how to create a custom agent.
- using a custom agent in Copilot CLI.

## Scenario

Tailspin Toys is committed to ensuring their crowdfunding platform is accessible to all users, regardless of their visual abilities or preferences. Recent user feedback has highlighted that some users find the current dark theme difficult to read due to insufficient contrast between text and background colors. To address this accessibility concern, the design team has requested the implementation of a high-contrast mode that users can toggle on and off.

Because accessibility is critical, you want to ensure this is implemented as quickly as possible. You're going to utilize a custom agent to generate the functionality.

In this exercise, you will:

- explore custom agents.
- enable a custom agent and assign it a task using Copilot CLI.

## Custom agents

Custom agents are defined by markdown files in the **.github/agents** folder of your project, or globally in **~/.copilot/agents**. The markdown files will contain guidance for Copilot on how best to perform at task.

## Custom agents vs skills

There is some logical overlap between custom agents and skills. Both are primarily defined with markdown files, and provide an AI guidance on how to perform operations. The best way to breakdown the difference is to think of a custom agent as the worker, and skills as tools.

Custom agents have their own context window, and are built to use skills as part of their orchestration. In our example, we have an accessibility custom agent, which is designed to review and make updates to the site based on defined accessibility guidelines. As part of its work, it could then call skills such as the pull request skill we saw previously, or one to run and manage tests.

Custom agents are launched by using the `/agent` command in Copilot CLI. Skills are launched dynamically, thus can be reused across multiple agents.

## Reviewing the accessibility custom agent

A custom agent has already been created for you for accessibility. Let's review the contents to understand how it will guide Copilot.

1. Return to your codespace.
2. Open **.github/agents/accessibility.md**.
3. Note the header section with the name and description of the agent.

> [!IMPORTANT]
> This section is required for custom agents.

4. From there, scan and review the next sections which highlight:
    - Core responsibilities when generating code for an accessible website.
    - Best practices for accessibility.
    - Code examples for HTML, CSS and JavaScript.
    - A list of common pitfalls and mistakes.

> [!NOTE]
> There is no "best markdown" for a custom agent. As with anything in AI, you will want to test and explore to determine what works best for your environments and scenarios.

## Using a custom agent in Copilot CLI

You can start a custom agent in Copilot CLI by using the `/agent` command. Let's perform an accessibility pass on our website.

1. Return to your codespace.
2. If not already open, open a terminal window by utilizing <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. If not already running, start Copilot CLI by issuing the following command in the terminal window:

    ```bash
    copilot --allow-all-tools
    ```

4. Bring up the list of agents by typing `/agent` in the prompt window in Copilot CLI and selecting <kbd>Enter</kbd>.
5. Select the **Accessibility agent** from the list of available agents.
6. Use the following prompt to ask the accessibility agent to perform a review and generate fixes for one particular class of possible errors related to HTML headers:

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. We're going to build in stages, so for now focus on headers, ensuring we're following good guidelines. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

7. Copilot gets to work on the task! It will start by retrieving the issue, then performing the review, generating updates, and finally creating the PR. You should also notice when it creates the PR it utilizes the skill focused on PRs for the project.

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

---

| [← Previous lesson: Agent Skills][previous-lesson] | [Next lesson: Slash Commands →][next-lesson] |
|:--|--:|

[previous-lesson]: ./5-agent-skills.md
[next-lesson]: ./7-slash-commands.md
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
