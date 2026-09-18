---
title: "Lesson 1 - Installing GitHub Copilot CLI"
description: "Install and authenticate Copilot CLI in your Codespace, get oriented, and find the seeded filtering issue."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

[GitHub Copilot CLI][about-copilot-cli] is a powerful agentic coding assistant that runs in your terminal, enabling you to explore codebases, generate code, run commands, and interact with external tools — all from the command line. It allows you to offload tasks, request changes, and stay in the zone. The first step, as you might imagine, is to install the tool! Fortunately, this can be done using tools you're already familiar with.

In this lesson, you will:

- install GitHub Copilot CLI using npm.
- authenticate with your GitHub account.
- trust the workshop repository and try a quick conversation.
- find the filtering issue through the built-in GitHub MCP server.

## Scenario

Your team is starting to use AI agents to work through a growing backlog. Copilot CLI brings that capability into the terminal, where many developers already live. This lesson gets you installed, authenticated, and ready to use it for the rest of the workshop.

## Install Copilot CLI

You can install Copilot CLI through [npm][install-cli], WinGet, and Homebrew. Since GitHub Codespaces comes with Node.js preinstalled, you'll use npm.

1. Return to your Codespace and open a terminal.
2. Install Copilot CLI globally:

   ```bash
   npm install -g @github/copilot
   ```

3. Verify the installation:

   ```bash
   copilot --version
   ```

## Authenticate with GitHub

On first launch, Copilot CLI prompts you to authenticate with your GitHub account.

1. Start Copilot CLI:

   ```bash
   copilot
   ```

2. If prompted, follow the device-code instructions to authenticate and authorize Copilot CLI.
3. When Copilot CLI asks whether you trust the files in this folder, verify that the path is your Tailspin Toys repository, then choose the option that remembers trust for this folder.

> [!NOTE]
> In a Codespace, you may already be authenticated through your GitHub session. If Copilot CLI starts without prompting for authentication, you're good to go!

## Get oriented

Commands at the normal shell prompt run directly in your Codespace. After Copilot CLI starts, natural language goes to the agent and slash commands control the conversation.

1. Enter `/help` to see the commands available in your installed version.
2. Ask Copilot a simple question to verify everything is working:

   ```plaintext
   What files are in this project?
   ```

3. Read the response and notice how Copilot explores the repository before answering.
4. Enter `/mcp list` and confirm the built-in GitHub MCP server is available.
5. Ask Copilot to find the filtering issue:

   ```plaintext
   Using GitHub MCP, find the issue in this repository titled "Allow users to filter games by category and publisher." Give me its URL and a short summary. Don't change anything.
   ```

6. Open the URL and read the issue. You'll use it after completing a quick first change.

> [!TIP]
> A normal Copilot CLI session works in the branch currently checked out in your terminal; it does not automatically create a worktree. You'll create a feature branch before each change.

## Use the workshop shortcut

Copilot CLI normally asks before using tools outside its established permissions. For this workshop, you'll relaunch it with `--yolo`, a user-approved shortcut that removes those approval prompts inside the Codespace so you can focus on the exercises.

`--yolo` allows Copilot to use all tools, paths, and URLs available to the session. The Codespace limits access to your local computer, but authenticated GitHub resources are still real. Review changes before publishing or merging them.

1. Exit Copilot CLI with `/exit`.
2. Relaunch it from the repository root:

   ```bash
   copilot --yolo
   ```

3. Ask another quick question about the project to confirm the conversation is working, then exit with `/exit`.

Copilot saves conversations automatically. Later, after changing instructions or adding an agent, you'll use `copilot --resume` to return to the same feature conversation and branch.

## Summary and next steps

Congratulations! In this lesson, you:

- installed GitHub Copilot CLI using npm.
- authenticated with your GitHub account.
- trusted the workshop repository and tried a quick conversation.
- found the filtering issue through the built-in GitHub MCP server.

Next, you'll [start your first focused change][next-lesson] and use Copilot CLI to show a star rating on the game cards.

## Resources

- [Install GitHub Copilot CLI][install-cli]
- [About GitHub Copilot CLI][about-copilot-cli]
- [Copilot CLI command reference][cli-reference]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-cli]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
