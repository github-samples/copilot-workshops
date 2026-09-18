---
title: "Lesson 0 - Prerequisites and setup"
description: "Verify the workshop prerequisites, install the GitHub Copilot app, and get familiar with its workspace."
authors:
  - jamesmontemagno
lastUpdated: 2026-09-16
---

Before you build the Space Quiz, verify your development tools, install the GitHub Copilot app, and get familiar with its main workspace.

In this lesson, you will:

- verify the workshop prerequisites.
- install and sign in to the GitHub Copilot app.
- identify the app's primary work areas.
- try a quick chat.

## Prerequisites

You need:

- a GitHub account with Copilot Student or a paid Copilot plan.
- [Git][git] installed. Run `git --version` to verify it.
- [Node.js 22 or later][nodejs] installed. Run `node --version` to verify it.
- a computer running macOS, Windows, or Linux.

> [!NOTE]
> If you use Copilot Business or Copilot Enterprise, your administrator must enable the **Copilot CLI** policy before the app will work.

## Install and configure the app

1. Open the [GitHub Copilot app download page][download-app].
2. Download the app for your operating system and follow the installation instructions.
3. Open the app.
4. Select **Sign in to GitHub** and authenticate. If you use GitHub Enterprise Server, select **Use GitHub Enterprise** and enter your server address.
5. If the app asks you to connect a repository or local folder, skip that step for now. You will create a new project in the next lesson.
6. Choose a theme, then select **Finish**.

For your first session, choose **GPT-5.3-Codex** if it is available. Otherwise, choose **Auto**.

## Explore the workspace

The app brings the development workflow into one place:

- **Home**: Choose a project, configure a session, and send a prompt.
- **Sessions**: Run agents in isolated workspaces, including several sessions in parallel.
- **Quick chats**: Ask questions and brainstorm without creating a branch or worktree.
- **My work**: Browse issues and pull requests, check CI, start sessions, and review changes.
- **Automations**: Save agent tasks to run on demand or on a schedule.

## Try a quick chat

Open a quick chat and send the following prompt:

```plaintext
How does the GitHub Copilot app use worktrees?
```

Quick chats are useful for questions that do not need a project workspace or code changes.

## Summary and next steps

You verified the prerequisites, installed the app, and explored its main work areas. Continue to [Lesson 1: Create the Space Quiz workspace][next-lesson].

[git]: https://git-scm.com/downloads
[nodejs]: https://nodejs.org/
[download-app]: https://gh.io/app
[next-lesson]: ../1-create-workspace/
