# Exercise 3 - MCP Servers with GitHub Copilot CLI

| [← Previous lesson: Installing Copilot CLI][previous-lesson] | [Next lesson: Generating Code →][next-lesson] |
|:--|--:|

There's more to writing code than just writing code. Issues need to be filed, external services need to be called, and information needs to be gathered. Typically this involves interacting with external tools, which can break a developer's flow. Through the power of Model Context Protocol (MCP), you can access all of this functionality right from Copilot CLI!

## Scenario

You are a part-time developer for Tailspin Toys - a crowdfunding platform for board games with a developer theme. You've been assigned various tasks to introduce new functionality to the website. Being a good team member, you want to file issues to track your work. To help future you, you've decided to enlist the help of Copilot. You will set up your backlog of work for the rest of the lab, using GitHub Copilot CLI and the GitHub Model Context Protocol (MCP) server to create the issues for you.

In this exercise, you will:

- understand what Model Context Protocol (MCP) is and how it works with Copilot CLI.
- set up the GitHub MCP server in your repository.
- use GitHub Copilot CLI to create issues in your repository.

By the end of this exercise, you will have created a backlog of GitHub issues for use throughout the remainder of the lab.

## What is Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] provides AI agents with a way to communicate with external tools and services. By using MCP, AI agents can communicate with external tools and services in real-time. This allows them to access up-to-date information (using resources) and perform actions on your behalf (using tools).

These tools and resources are accessed through an MCP server, which acts as a bridge between the AI agent and the external tools and services. The MCP server is responsible for managing the communication between the AI agent and the external tools (such as existing APIs or local tools like NPM packages). Each MCP server represents a different set of tools and resources that the AI agent can access.

A couple of popular existing MCP servers are:

- **[GitHub MCP Server][github-mcp-server]**: This server provides access to a set of APIs for managing your GitHub repositories. It allows the AI agent to perform actions such as creating new repositories, updating existing ones, and managing issues and pull requests.
- **[Playwright MCP Server][playwright-mcp-server]**: This server provides browser automation capabilities using Playwright. It allows the AI agent to perform actions such as navigating to web pages, filling out forms, and clicking buttons.

There are many other MCP servers available that provide access to different tools and resources. GitHub hosts an [MCP registry][mcp-registry] to enhance discoverability and contributions to the ecosystem.

> [!IMPORTANT]
> With regard to security, treat MCP servers as you would any other dependency in your project. Before using an MCP server, carefully review its source code, verify the publisher, and consider the security implications. Only use MCP servers that you trust and be cautious about granting access to sensitive resources or operations.

## Setting up the GitHub MCP server in Copilot CLI

Copilot CLI supports MCP servers via a configuration file at **~/.copilot/mcp.json**. Additionally, in your project the **.vscode/mcp.json** file can configure MCP servers for VS Code-based workflows, and Copilot CLI also reads from this file.

1. Return to your codespace.
2. Open a terminal window by pressing <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Start Copilot CLI:

   ```bash
   copilot
   ```

4. Register the GitHub MCP server in Copilot CLI using the `/mcp` command:

   ```
   /mcp add github https://api.githubcopilot.com/mcp/
   ```

5. Copilot CLI will prompt you to authenticate with GitHub. Follow the on-screen instructions to authorize.
6. Once authentication is complete, confirm the server is registered:

   ```
   /mcp list
   ```

You should see the GitHub MCP server listed and marked as active.

## Creating a backlog of tasks

Now that you have set up the GitHub MCP server, you can use Copilot CLI to create a backlog of tasks for use in the rest of the lab.

1. In the Copilot CLI prompt, type or paste the following prompt to create the issues you'll be working on in the lab:

   ```markdown
   In my GitHub repo, create GitHub issues for our Tailspin Toys backlog. Each issue should include:
   - A clear title
   - A brief description of the task and why it is important to the project
   - A checkbox list of acceptance criteria

   From our recent planning meeting, the upcoming backlog includes the following tasks:

   1. Allow users to filter games by category and publisher
   2. Update our repository coding standards (including rules about Python formatting and docstrings) in a custom instructions file
   3. Stretch Goal: Implement pagination on the game list page
   ```

2. Press <kbd>Enter</kbd> to send the prompt to Copilot.
3. Copilot will ask you to confirm any write operations before proceeding. Review the issue details and confirm each one.

> [!IMPORTANT]
> Remember, AI can make mistakes, so make sure to review the issues before confirming.

4. In a separate browser tab, navigate to your GitHub repository and select the **Issues** tab.
5. You should see a list of issues that have been created by Copilot. Each issue should include a clear title and a checkbox list of acceptance criteria.

## Summary and next steps

Congratulations, you have created issues on GitHub using Copilot CLI and MCP!

To recap, in this exercise you:

- understood what Model Context Protocol (MCP) is and how it works with Copilot CLI.
- set up the GitHub MCP server in your repository.
- used GitHub Copilot CLI to create issues in your repository.

You can now continue to the next exercise, where you will [add project features with GitHub Copilot CLI][next-lesson].

### Optional exploration exercise – Set up the Microsoft Playwright MCP server

If you are feeling adventurous, you can try installing and configuring another MCP server, such as the [Microsoft Playwright MCP server][playwright-mcp-server]. This will allow you to use Copilot CLI to perform browser automation tasks, such as navigating to web pages, filling out forms, and clicking buttons.

## Resources

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [GitHub MCP Server][github-mcp-server]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [GitHub MCP Registry][mcp-registry]

---

| [← Previous lesson: Installing Copilot CLI][previous-lesson] | [Next lesson: Generating Code →][next-lesson] |
|:--|--:|

[previous-lesson]: ./2-install-copilot-cli.md
[next-lesson]: ./4-generating-code.md
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[mcp-registry]: https://github.com/mcp
