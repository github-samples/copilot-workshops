---
title: "Lesson 3 - Guiding Copilot with custom instructions"
description: "Add a documentation standard, demonstrate it on a small existing helper or component, and merge both as the second pull request."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Context is key when working with generative AI. If a task needs to be done a particular way — or there's background information Copilot should know — you want that context available. One of the most powerful tools for this is [instruction files][instruction-files], which describe not just *what* code you want but *how* it should be structured. In this lesson you'll add a documentation standard to your repository, and you'll do it the way you'll do most work from here on: starting from an issue in your backlog and letting the agent make the change.

In this lesson, you will:

- explore how repository instructions and path-scoped instruction files reach the agent.
- start a session from the instructions issue in your backlog.
- ask the agent to add a focused documentation standard to the appropriate repository instruction files.
- demonstrate the standard with a small real code change, validate it, and merge PR 2.

## Scenario

As any good dev shop, Tailspin Toys has a set of guidelines and requirements for development practices. These include:

- Comments should explain intent and non-obvious decisions rather than restate code.
- Exported functions in `db/` and `src/lib/` should document their purpose, parameters, and return values with TSDoc/JSDoc, including an injectable `db` argument where present.
- Reusable Astro components should document their `Props` contracts, and comments should stay current when related code changes.
- Existing formatting and lint guidance should be preserved.

Through the use of instruction files you'll ensure Copilot has the right information to perform the tasks in alignment with the practices highlighted.

## Instruction files

Custom instructions allow you to provide context and preferences to Copilot, so that it can better understand your coding style and requirements. This is a powerful feature that can help you steer Copilot to get more relevant suggestions and code snippets. You can specify your preferred coding conventions, libraries, and even the types of comments you like to include in your code. You can create instructions for your entire repository, or for specific types of files for task-level context.

The project uses two kinds of instruction files:

- `.github/copilot-instructions.md`, a single instruction file sent to Copilot for **every** request for the repository. This file should contain project-level information — context relevant for most chat or CLI requests sent to Copilot. This could include the tech stack being used, an overview of what's being built, best practices, and other global guidance.
- `.github/instructions/*.instructions.md` files can be created for specific tasks or file types. You can use them to provide guidelines for particular languages (like TypeScript or Astro), or for tasks like creating a UI component or a new set of unit tests.

> [!NOTE]
> Other instruction formats and support vary by harness. Consult the [custom instructions support reference][custom-instructions-support] before relying on a particular format.

### Best practices for managing instructions files

A full conversation about creating instructions files is beyond the scope of the workshop. However, the examples provided in the sample project show a representative approach. At a high level:

- Keep instructions in `copilot-instructions.md` focused on project-level guidance, such as a description of what's being built, the structure of the project, and global coding standards.
- Use `*.instructions.md` files to provide specific instructions for file types (unit tests, Astro components, the data layer), or for specific tasks.
- Use natural language. Keep guidance clear. Provide examples of how code should (and shouldn't) look.

There isn't one specific way to create instructions files, just as there isn't one specific way to use AI. You will find through experimentation what works best for your project.

> [!TIP]
> Every project using GitHub Copilot should have a robust collection of instruction files. As you explore the ones in this project, you may notice there are instructions files for numerous types of code files.
>
> Looking for templates or a starting point? Explore [awesome-copilot][awesome-copilot], a repository full of instruction files, custom agents, and other resources.

## Explore the custom instructions files in this project

Take a moment to read the instruction files this repository ships with — there's one core `copilot-instructions.md` and a collection of `*.instructions.md` files for various tasks. Open these in your editor or the GitHub web UI.

1. If the review panel is not already visible, open it by selecting **Toggle review panel** in the upper right.

   ![The GitHub Copilot app top toolbar with an arrow pointing to the Toggle review panel button to the right of Create PR](../_images/app-2-review-panel.png)

2. Select the **+** to add a new item to the review panel.
3. Select **File**.
4. Search for `copilot-instructions.md`.
5. Select  `copilot-instructions.md` from the list of files to open it.
6. Explore the file, noting the brief description of the project plus sections such as **Agent notes**, **Code standards**, **Scripts**, and **Repository Structure**. Under **Code standards**, note the nested **GitHub Actions Workflows** guidance. These are applicable to any interactions you'd have with Copilot.
7. Select **Show folder view** to open the folder navigator.

   ![The Show folder view button in the review panel with a file open in the GitHub Copilot app](../_images/app-show-folder-view.png)

8. Navigate to the `.github/instructions` folder and explore the files. Note there are instructions for Astro files, the Drizzle data layer, tests, and more.
9. Open `.github/instructions/unit-tests.instructions.md`. Note the `applyTo` field at the top — this sets a glob (relative to the repo root) that determines which files the instructions apply to. Here, any TypeScript test file (for example, one matching `**/*.test.ts`) will match.
10. Note the instructions specific to creating unit tests for this project.
11. Finally, open `.github/instructions/drizzle.instructions.md` and scroll to the bottom. Note the links to other instruction files (like `unit-tests.instructions.md`) and existing files in the project. This lets you break larger instruction sets into smaller, reusable files, and point Copilot at examples to follow when generating code. (Paths there are relative to the instruction file rather than the repo root.)

> [!NOTE]
> Compare the existing guidance with the actual coding-standards issue before adding rules. This lesson focuses on intent-based comments, exported data-layer function documentation, and Astro `Props` contracts, not blanket file headers or comments that restate code.

## Start from the instructions issue

Confirm PR 1 is merged before creating this session. Start a fresh worktree for PR 2; do not continue on the star-rating branch. Most work starts with an issue, so use the coding-standards issue to supply the requirements.

> [!NOTE]
> Because instructions files have a large impact on the code generated by Copilot, care should be taken in ensuring they clearly guide Copilot. Having Copilot create a first version, like you'll do in this lesson is a great approach, followed by a review by you to ensure the updates meet your requirements.

1. Select **My work** in the sidebar
2. Select the issue titled **Update our repository coding standards** to open the issue.
3. Select **New session** in the upper right, choose a **new working tree**, and select **Interactive** mode.

   ![The issue view in the GitHub Copilot app with an arrow pointing to the New session button in the upper right](../_images/app-new-session-from-issue.png)

4. Use the following prompt. Updating the new session branch before editing makes the latest merged `main` the actual starting point, even if the app's local checkout was stale:

   ```plaintext
   Before editing, identify this checkout and branch, confirm it is a clean new worktree, fetch origin, and fast-forward this session branch to origin/main. Confirm HEAD matches origin/main and includes the merged star-rating PR. Stop if it is dirty, diverged, or missing that merge; do not reset, discard work, or create another branch.

   Read the issue "Update our repository coding standards" and the existing repository instructions. Add a focused documentation convention: explain intent rather than mechanics; document exported functions in db/ and src/lib/ with TSDoc/JSDoc covering purpose, parameters, returns, and injectable db arguments where present; document reusable Astro components' Props contracts; and keep comments current when related code changes.

   Put each rule in the appropriate existing instruction file without duplication or contradictions, and link to or summarize the updated standard in README. Preserve existing formatting and lint guidance. Do not require blanket file headers, migrate formatting tools, rewrite documentation across the application, or implement filtering. Show me the instruction diff, then stop for review. Do not create a skill or agent, commit, push, or create a PR.
   ```

Copilot will make the updates!

## Review the change

Read the updated guidance, then demonstrate its effect on a real file. A proposed snippet alone does not show that repository instructions affected a code change.

1. Select **Changes** in the upper right to open the code changes.

   ![The session panel tabs in the GitHub Copilot app with an arrow pointing to the Changes tab](../_images/app-select-changes.png)

2. Review the updated instruction files and README reference. Confirm the rules match the issue's comment philosophy, exported-function documentation, and component contracts without inventing a blanket file-header requirement.

> [!NOTE]
> Because AI is probabilistic rather than deterministic, the exact text will vary.

3. After reviewing the instructions, request a bounded demonstration in this same session:

   ```plaintext
   Demonstrate the updated documentation convention on one small existing exported TypeScript helper in db/ or src/lib/, or one reusable Astro component. Inspect the repository to choose a suitable existing file; do not assume a publishers helper exists. Make a small behavior-preserving readability improvement and apply the relevant function-documentation or Props-contract guidance. Explain non-obvious intent without adding comments that merely restate code.

   Keep the change bounded to that demonstration and any directly relevant tests. Do not implement filtering or create a new feature. Run the relevant existing npm checks, report what changed and how the instruction affected the code, and stop for review. Ask before installing anything. Do not commit, push, or create a PR.
   ```

4. Review the actual file diff, not only the chat response. Check that the documentation explains the real behavior and that the readability change preserves it. Review the relevant test, lint, and type-check results; resolve failures before continuing.

You've now updated the instructions files in the project and seen the impact it will have!

## Open and merge the pull request

Instructions files become assets in the repository, meaning they're shared with the rest of the team. Let's create a PR with our work, just like we would any other asset!

First authorize the reviewed instructions and demonstration together:

```plaintext
Review the full diff for the coding-standard instructions, README reference, and bounded code demonstration, including any related tests. Summarize the verification and commit these reviewed changes on this session branch. Push the branch and create one pull request targeting main, using the repository's PR template and linking the coding-standards issue. Describe this as a partial contribution unless every issue acceptance criterion is satisfied; do not use closing keywords for incomplete work. Do not merge it.
```

1. Follow the PR link in the session. If the app presents a **Create PR** confirmation, select it without creating a duplicate PR.
2. If prompted, select **Sign in with your browser** and follow the prompts to authenticate.
3. Copilot gets to work on creating the PR.

Inspect the full PR diff in **My work**, including both the instruction and code changes. Review the learner repository's CI results and any required reviews. Resolve failures before selecting **Ready to merge**; CI does not replace the demonstration or your review.

4. Select **Ready to merge**.
5. Select **Merge pull request** on the new dialog window to merge your pull request!

> [!NOTE]
> Confirm PR 2 is merged into `main` before beginning filtering. A new worktree alone does not guarantee current code: in Lesson 4 you will fetch and fast-forward the fresh session branch to `origin/main`, then verify both earlier merges are present before planning.

## Summary and next steps

You explored how the app picks up context from instruction files, then used a session to add and merge a repository-wide standard. Specifically, you:

- explored the repository's `copilot-instructions.md` and path-scoped `*.instructions.md` files.
- started a session from the instructions issue in your backlog.
- asked the agent to add focused documentation rules to the appropriate instruction files and reference them from README.
- inspected the standard's effect on a real code change, validated the result, and merged both as PR 2.

Next, you'll build the filtering feature in a fresh session — and check that it follows the standard you just merged. Continue to [Lesson 4 - Build filtering with Plan and Autopilot][next-lesson].

## Resources

- [Instruction files for GitHub Copilot customization][instruction-files]
- [Customizing the GitHub Copilot app][customize-app]
- [Best practices for creating custom instructions][instructions-best-practices]
- [Awesome Copilot — a collection of instruction files and other resources][awesome-copilot]

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
