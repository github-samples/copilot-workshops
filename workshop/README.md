<!--
  GENERATED FILE — do not edit.
  Source: docs/src/content/docs/index.mdx
  Run `python scripts/render-markdown.py` to regenerate.
-->

# Agents in the software development lifecycle (SDLC)

The recent additions to the capabilities of GitHub Copilot provide powerful tools to the developer across the entire software development lifecycle (SDLC). This includes working with issues and pull requests on GitHub, interacting with external services, and of course code creation. This lab explores the functionality, providing real-world use cases and tips on how to get the most out of the tools.

> [!WARNING]
> Because GitHub Copilot, and generative AI at large, is probabilistic rather than deterministic, the exact code, files changed, etc., may vary. As a result, you may notice slight differences between screenshots and code snippets in the lab and your experience. This is to be expected, and is just the nature of working with this class of tools.
>
> If something appears broken or isn't running correctly, please ask a mentor!

## Choose your learning path

This workshop offers multiple paths depending on how you want to interact with GitHub Copilot. All paths begin with the same shared prerequisites, then each path opens with its own custom-instructions exercise before moving into tool-specific content.

### 🖥️ [VS Code Path](vscode/README.md)

Focused on GitHub Copilot features within **Visual Studio Code** and GitHub Codespaces. Covers Copilot Chat agent mode, MCP integration, and custom agents — all from your IDE.

**Best for**: Developers who prefer IDE-based workflows.

| # | Exercise |
|---|---------|
| 0 | [Prerequisites](shared/0-prereqs.md) |
| 1 | [MCP with VS Code](vscode/1-mcp.md) |
| 2 | [Custom instructions](vscode/2-custom-instructions.md) |
| 3 | [Agent mode](vscode/3-agent-mode.md) |
| 4 | [Custom agents](vscode/4-custom-agents.md) |
| 5 | [Managing agents](vscode/5-managing-agents.md) |
| 6 | [Iterating on Copilot's work](vscode/6-iterating.md) |

---

### 💻 [CLI Path](cli/README.md)

Focused on **GitHub Copilot CLI** — a powerful agentic assistant that runs in your terminal. Covers installation, MCP, code generation with plan mode, agent skills, custom agents, and slash commands.

**Best for**: Developers who live in the terminal and want AI assistance without leaving the command line.

| # | Exercise |
|---|---------|
| 0 | [Prerequisites](shared/0-prereqs.md) |
| 1 | [Install Copilot CLI](cli/1-install-copilot-cli.md) |
| 2 | [Custom instructions](cli/2-custom-instructions.md) |
| 3 | [MCP with CLI](cli/3-mcp.md) |
| 4 | [Generating code](cli/4-generating-code.md) |
| 5 | [Agent skills](cli/5-agent-skills.md) |
| 6 | [Custom agents](cli/6-custom-agents.md) |
| 7 | [Slash commands](cli/7-slash-commands.md) |
| 8 | [Review](cli/8-review.md) |

---

### ☁️ [Cloud / Cloud Agent Path](cloud/README.md)

Focused on **Copilot cloud agent** — the asynchronous peer programmer that works on GitHub issues in the background. Covers assigning issues, custom agents, monitoring with the agents dashboard, and reviewing generated work.

**Best for**: Developers who want to offload tasks and let Copilot work asynchronously.

> [!NOTE]
> Requires **Copilot Pro+, Business, or Enterprise** with cloud agent enabled.

| # | Exercise |
|---|---------|
| 0 | [Prerequisites](shared/0-prereqs.md) |
| 1 | [Custom instructions](cloud/1-custom-instructions.md) |
| 2 | [Copilot cloud agent](cloud/2-cloud-agent.md) |
| 3 | [Custom agents](cloud/3-custom-agents.md) |
| 4 | [Managing agents](cloud/4-managing-agents.md) |
| 5 | [Iterating on Copilot's work](cloud/5-iterating.md) |

---

### 🗺️ Complete Path

Want to explore everything? Work through all three paths to experience the full breadth of GitHub Copilot's agent capabilities.

**Recommended order:**

1. **Shared setup**: [Prerequisites](shared/0-prereqs.md)
2. **VS Code**: [MCP](vscode/1-mcp.md) → [Custom instructions](vscode/2-custom-instructions.md) → [Agent mode](vscode/3-agent-mode.md)
3. **CLI**: [Install CLI](cli/1-install-copilot-cli.md) → [Custom instructions](cli/2-custom-instructions.md) → [MCP](cli/3-mcp.md) → [Generating code](cli/4-generating-code.md) → [Agent skills](cli/5-agent-skills.md) → [Slash commands](cli/7-slash-commands.md)
4. **Cloud**: [Custom instructions](cloud/1-custom-instructions.md) → [Cloud agent](cloud/2-cloud-agent.md) → [Custom agents](cloud/3-custom-agents.md) → [Managing agents](cloud/4-managing-agents.md) → [Iterating](cloud/5-iterating.md)

---

## Scenario

You are a new developer for Tailspin Toys, a fictional company who provides crowdfunding for board games with a developer theme - a huge market! You are tasked with creating issues to document the desired updates to the application and implementing the ability to filter games by both category and publisher. You'll work iteratively, exploring both the site and Copilot's capabilities, to complete the tasks.

## Get started

Choose your path above and start with [Exercise 0: Prerequisites](shared/0-prereqs.md)!
