---
title: "Exercise 1 - Installing GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[GitHub Copilot CLI][about-copilot-cli] is a powerful agentic coding assistant that runs in your terminal, enabling you to explore codebases, generate code, run commands, and interact with external tools - all from the command line. It allows you to offload tasks, request changes, and stay in the zone. The first step, as you might imagine, is to install the tool! Fortunately this can be done using tools you're already familiar with.

In this exercise, you will learn how to:

- install GitHub Copilot CLI using npm.
- authenticate with your GitHub account.
- verify the installation.

## Scenario

Your team is starting to use AI agents to work through a growing backlog. Copilot CLI brings that capability into the terminal, where many developers already live. This exercise gets you installed, authenticated, and ready to use it for the rest of the workshop.

## Open a terminal in your codespace

Before installing Copilot CLI, you need to open a terminal window in your codespace.

1. Return to your codespace and wait for its setup to finish.
2. Open a terminal window by pressing <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. You should see a terminal panel appear at the bottom of your VS Code window.

## Confirm the learner environment

In the codespace terminal, confirm you are in your own Tailspin Toys repository, not the workshop-content repository. Read its `README.md` and `package.json` for setup and check commands. Current Tailspin Toys requires Node.js 22.13 or later, project dependencies, and Playwright Chromium for E2E testing.

```bash
pwd
git remote -v
node --version
gh auth status
```

GitHub CLI (`gh`) will help inspect PRs and CI. If authentication is missing, use `gh auth login` and follow its browser instructions. Confirm your account can push branches and create and merge PRs in this repository; organizational policies may require another reviewer. Resolve missing prerequisites using the repository setup instructions before starting code changes, and review any installation before authorizing it.

The CLI runs against the checkout where you start it; starting a conversation does not automatically create an isolated worktree. This workshop uses one branch per PR milestone. You'll merge star ratings and the instructions demonstration first, then keep the same filtering branch through Exercises 4–8.

## Install Copilot CLI

You can install Copilot CLI through [npm][install-npm], [WinGet][install-winget], and [Homebrew][install-homebrew]. Since GitHub Codespaces come with Node.js pre-installed you'll use npm to install Copilot CLI.

1. In the terminal, verify Node.js is installed and meets the version requirement:

   ```bash
   node --version
   ```

   Tailspin Toys requires version 22.13 or higher, even if the CLI's own requirement differs. Follow the learner repository's setup instructions if your version is too old.

2. Install Copilot CLI globally in the codespace using npm:

   ```bash
   npm install -g @github/copilot
   ```

3. Verify the installation by checking the version:

   ```bash
   copilot --version
   ```

   You should see the version number displayed (e.g., `v1.0.XX`).

> [!NOTE]
> If installation fails with a permission error, inspect your npm configuration or ask your workshop leader for help rather than rerun an unfamiliar command with elevated privileges.

## Authenticate with GitHub

On first launch, Copilot CLI will prompt you to authenticate with your GitHub account.

1. Start Copilot CLI:

   ```bash
   copilot
   ```

2. If you're not currently logged in, you'll see a prompt to authenticate. Copilot CLI will display a device code and ask you to visit a URL.
3. Follow the on-screen instructions:
   - Open the provided URL in your browser
   - Enter the device code when prompted
   - Authorize Copilot CLI to access your GitHub account
4. Once authenticated, you'll see the Copilot CLI prompt, ready to accept your questions and commands.

> [!NOTE]
> In a codespace, you may already be authenticated through your GitHub session. If Copilot CLI starts without prompting for authentication, you're good to go!

## Trust the directory and verify everything is working

Now that you're at the Copilot CLI prompt for the first time, let's trust this workshop repository and make sure Copilot CLI is properly installed and connected.

1. When Copilot CLI asks you to confirm that you trust the files in this folder, you'll see three options:
   - **Yes, proceed**: Trust for this session only
   - **Yes, and remember this folder for future sessions**: Trust permanently
   - **No, exit (Esc)**: Don't allow file access
2. For this workshop, select **Yes, and remember this folder for future sessions** since you'll be working in this repository throughout.
3. Ask Copilot a simple question to verify it's working:

   ```plaintext
   What files are in this project?
   ```

4. Copilot should explore the repository and provide a summary of the project structure.
5. Try the `/help` command to see available slash commands:

   ```text
   /help
   ```

6. Exit this session by entering the following command at the Copilot prompt. You'll start a fresh session for the first change.

   ```text
   /exit
   ```

## Understand modes and permissions

Copilot CLI works in the directory and Git branch where you launch it. Trusting a directory lets it use repository context; it is not the same as approving every tool action. Review permission requests for file changes, shell commands, and GitHub operations.

Start the code exercises from your learner repository root with:

```bash
copilot --enable-all-github-mcp-tools
```

The GitHub MCP server is built in. This flag exposes its full tool set for issue and PR work; authentication, repository permissions, and tool approvals still apply. It does not authorize a commit or PR on its own.

Use <kbd>Shift</kbd>+<kbd>Tab</kbd> to cycle between standard **Interactive**, **Plan**, and **Autopilot** modes. Check the mode indicator before sending a request. You'll stay Interactive for the early changes, plan filtering before building it, and explicitly return to Interactive before creating and reviewing customizations.

> [!CAUTION]
> Mode and permission settings are different. Autopilot continues working autonomously; `--allow-all` and its alias `--yolo` grant all tool, path, and URL permissions. This workshop does not require starting every session with unrestricted permissions. Review the scope before granting access, even inside a codespace.

## Summary and next steps

Congratulations! You've successfully installed and authenticated GitHub Copilot CLI. You learned how to:

- install Copilot CLI using npm.
- authenticate with your GitHub account.
- trust a directory for Copilot CLI to work with.
- verify the installation is working correctly.

Now that Copilot CLI is installed, make a small, reviewable change in [Exercise 2 - Add star ratings: a quick win][next-lesson].

## Resources

- [Installing GitHub Copilot CLI][install-copilot-cli]
- [About Copilot CLI][about-copilot-cli]
- [Using Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
