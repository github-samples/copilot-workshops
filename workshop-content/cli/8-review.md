# Exercise 8 - Review and Next Steps

| [← Previous lesson: Slash Commands][previous-lesson] | |
|:--|--:|

Over the last several exercises, you explored some of the most common uses cases for GitHub Copilot CLI, including:

- interacting with GitHub and other MCP servers.
- using instructions files to guide code generation.
- implementing skills to add tools to the Copilot CLI toolbox.
- calling custom agents for advanced and more complex tasks.
- using slash commands to manage your session, and optionally bridging back to coding agent via `/delegate`.

Let's talk about some slash commands, best practices, and next steps.

## Slash commands

Copilot CLI has a series of slash commands available to interact with it, including ones which allow you to configure it or see what's going on behind the scenes. You've already used `/clear` to start a new chat which clears the current context, and `/mcp` to register MCP servers. Some additional ones you might find helpful are:

| Command            | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir`         | Add a directory to the trusted list for Copilot               |
| `/clear`, `/new`   | Clear the conversation history and start fresh                |
| `/compact`         | Summarize conversation history to reduce context window usage |
| `/context`         | Show context window token usage and visualization             |
| `/diff`            | Review the changes made in the current directory              |
| `/model`           | Select AI model to use (Claude Sonnet, GPT-5, etc.)           |
| `/plan <prompt>`   | Create an implementation plan before coding                   |
| `/review <prompt>` | Run code review agent to analyze changes                      |
| `/delegate`        | Delegate task to Copilot coding agent for async processing    |
| `/session`         | Show session info and workspace summary                       |
| `/share`           | Share session to markdown file or GitHub gist                 |
| `/skills`          | Manage skills for enhanced capabilities                       |
| `/usage`           | Display session usage metrics and statistics                  |

> [!TIP]
> Use `/help` to see the full list of available commands and keyboard shortcuts.

## Best practices

When using any AI tool, investing in the underlying infrastructure will drive better code and a better experience. These include having robust instructions files, custom agents, and agent skills. You explored each of these in the workshop. A great resource for templates is [awesome-copilot][awesome-copilot]. You can also ask Copilot to explore your project and create these for you as a starting point!

Always remember that context is key, both in life and when working with AI tools. A good infrastructure certainly goes a long way in helping generate the highest quality code, but prompts also have a large impact. Clearly describing what you want built, why you want it built, and how you want it built will help Copilot. Basically, if there's a piece of information that Copilot would benefit from having, ensure you pass that along!

## Next steps

The best way to improve your skills with any tool is to keep using the tool! Use it for production code, for hobby code, for the little app you've had in your mind for years but never got around to building. Share your learnings with your team, and learn from your team. And, as always, explore the documentation.

If you'd like to explore more of the GitHub Copilot ecosystem, check out the [VS Code path](../vscode/README.md) or the [Cloud/Coding Agent path](../cloud/README.md).

## Resources

- [About Copilot CLI][about-copilot-cli]
- [Using Copilot CLI][using-copilot-cli]
- [Awesome Copilot Repository][awesome-copilot]
- [Custom Instructions Guide][repo-instructions]
- [Agent Skills Documentation][agent-skills]
- [Custom Agents Documentation][custom-agents]
- [MCP Specification][mcp-spec]

---

| [← Previous lesson: Slash Commands][previous-lesson] | |
|:--|--:|

[previous-lesson]: ./7-slash-commands.md
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
