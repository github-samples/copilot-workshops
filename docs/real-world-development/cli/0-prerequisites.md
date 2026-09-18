---
title: "Lesson 0 - Prerequisites"
description: "Create your own copy of Tailspin Toys and prepare a GitHub Codespace for the Copilot CLI workshop."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

Before you start the Copilot CLI lessons, you need to get everything ready. You'll create your own copy of the Tailspin Toys repository and spin up a [codespace][codespaces], whose integrated terminal you'll use to install and run Copilot CLI in the next lesson.

In this lesson, you will:

- create your own copy of the Tailspin Toys project from the template.
- create a Codespace and confirm the project is ready.

## Set up the lab repository

You'll work against your own copy of the Tailspin Toys project. Create it now from the [template repository][tailspin-template]. The new repository contains every file the lab needs.

1. In a new browser window, navigate to the [Tailspin Toys template][tailspin-template].
2. Create your own copy of the repository by selecting **Use this template**, then **Create a new repository**.
3. If you are completing the workshop as part of an event being led by GitHub or Microsoft, follow the instructions provided by the mentors. Otherwise, create the new repository in an organization where you have access to GitHub Copilot.
4. Make a note of the repository path you created (`organization-or-user-name/repository-name`), as you will refer to it later in the workshop.

> [!NOTE]
> When you create your repository from the template, a backlog of GitHub issues is created for you automatically. You'll work from these issues throughout the workshop — there's nothing to file yourself.

Use a fresh copy of the workshop template. It includes repository instructions, application code, tests, a `quality-checks` skill, and the backlog you'll use. If you use an older copy, check with your facilitator that it has the files you'll need.

## Create a Codespace

Next up, you'll use a Codespace to complete the workshop.

[GitHub Codespaces][codespaces] is a cloud-based development environment that allows you to write, run, and debug code directly in your browser. It provides a fully featured editor with support for multiple programming languages, extensions, and tools.

1. Navigate to your newly created repository.
2. Select **Code**.
3. Select the **Codespaces** tab, then select **Create codespace on main**.
4. Wait for the Codespace setup to finish. The template installs the project dependencies, Playwright Chromium, and the local database for you.
5. Open a terminal in the repository root and start the application:

   ```bash
   npm run dev
   ```

6. When Codespaces reports that port `4321` is available, select **Open in Browser** and confirm the Tailspin Toys site loads.
7. Return to the terminal and stop the development server with <kbd>Ctrl</kbd>+<kbd>C</kbd>.

> [!NOTE]
> This workshop is built to run inside a Codespace or local [dev container][dev-containers]. Both provide the prerequisites for a smooth experience. If you'd prefer to run it locally, open the cloned repository in Visual Studio Code and select **Reopen in Container** when prompted.

## Summary and next steps

You're set up! In this lesson, you:

- created your own copy of the Tailspin Toys project from the template.
- created a Codespace and confirmed the project was ready.

Next, you'll [install GitHub Copilot CLI][next-lesson] in your Codespace and authenticate it with your GitHub account.

## Resources

- [GitHub Codespaces overview][codespaces]
- [Creating a repository from a template][template-repository]
- [Getting started with Codespaces][codespaces-quickstart]

[tailspin-template]: https://github.com/github-samples/tailspin-toys
[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
