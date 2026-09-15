---
title: "Lesson 0 - Prerequisites"
description: "Set up for the GitHub Copilot app lessons: install Node.js for the Tailspin Toys project and create your own copy of the repository from the template."
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

The GitHub Copilot app is a desktop app, serving as your central hub for both Copilot and GitHub. It provides quick access to issues and pull requests, and of course allows you to build using GitHub Copilot. During this workshop you'll be working locally, using both the Tailspin Toys app, built on Astro, and of course the GitHub Copilot app. Before you get started, let's ensure Node.js is installed locally, then install the Copilot app.

In this lesson, you will:

- install Node.js so the project's tests can run on your machine.
- create your own copy of the Tailspin Toys project from the template.

## Install Node.js

Several lessons ask an agent to build features and run the Tailspin Toys test suite locally, which needs **[Node.js][nodejs]**. Use **Node.js 22.13 or later**, and confirm the supported version in your checkout's `package.json` and README.

The simplest option on every platform is the official installer:

1. In your operating system, open a terminal window using Windows Terminal, macOS terminal, or whatever you typically use.
2. Run the following command to confirm you have Node.js 22.13 or later installed:

    ```shell
    node --version
    ```

3. If the reported version is at least `v22.13.0` and supported by the project, you can skip to the next section.

> [!TIP]
> You only need to complete these steps if you don't have Node installed, or you need to update.

4. Open the [Node.js download page][node-download].
5. Download the **LTS** build for your operating system.
6. Run the installer and accept the defaults. On Windows, keep the **Add to PATH** option selected.
7. Once installed, open a new terminal window.
8. Confirm the install in the new terminal window by running the following:

    ```bash
    node --version
    ```

9. Confirm the reported version is at least `v22.13.0` and supported by the project.

> [!IMPORTANT]
> This App path uses local worktrees. A runtime installed only in a container is not available to those local sessions. Each worktree also needs the project dependencies and Playwright Chromium for E2E checks. Follow the learner repository's README when preparing a worktree, and review any installation request before approving it.

## Set up the lab repository

You'll work against your own copy of the Tailspin Toys project. Create it now from the [template repository][template-repository]. The new repository contains every file the lab needs, and you'll connect it to the app in the next lesson.

1. In a new browser window, navigate to the GitHub repository for this lab: `https://github.com/github-samples/tailspin-toys`.
2. Create your own copy of the repository by selecting the **Use this template** button on the lab repository page. Then select **Create a new repository**.

    ![The Use this template button with Create a new repository selected from the dropdown](../_images/app-0-use-template.png)

3. If you are completing the workshop as part of an event being led by GitHub or Microsoft, follow the instructions provided by the mentors. Otherwise, you can create the new repository in an organization where you have access to GitHub Copilot.

    ![The Create a new repository form with github-samples/tailspin-toys set as the template and the repository name filled in](../_images/app-0-create-repository.png)

4. Make a note of the repository path you created (**organization-or-user-name/repository-name**), as you will be referring to this later in the lab.

> [!NOTE]
> When you create your repository from the template, a backlog of GitHub issues is created for you automatically. You'll work from these issues throughout the workshop — there's nothing to file yourself.

Use a fresh copy of the revised template: it includes repository instructions, application code, tests, and an existing canvas extension, but no supplied custom agents or skills. You will create your own quality-checks skill and QA profile during the workshop. If you use an older copy, inspect existing customizations rather than overwrite them.

## Summary and next steps

You're set up! You installed Node.js so the project can build and test on your machine, and you created your own copy of the Tailspin Toys repository from the template.

Next, you'll install the GitHub Copilot app, connect the repository you just created, and get oriented in the workspace. Continue to [Lesson 1 - Installing the GitHub Copilot app][next-lesson].

## Resources

- [Download Node.js][node-download]
- [Creating a repository from a template][template-repository]
- [About the GitHub Copilot app][about-copilot-app]

[next-lesson]: ../1-install-copilot-app/
[nodejs]: https://nodejs.org/
[node-download]: https://nodejs.org/en/download
[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
