<!--
  GENERATED FILE — do not edit.
  Source: docs/src/content/docs/vscode/2-custom-instructions.mdx
  Run `python scripts/render-markdown.py` to regenerate.
-->

# Exercise 1 - Custom instructions (VS Code)

[← Previous lesson: MCP with VS Code][previous-lesson] · [Next lesson: Agent mode →][next-lesson]

Context is key when working with generative AI. If a task needs to be done a particular way — or there's background information Copilot should know — you want to make sure that context is reachable. There are several ways to share specific context with Copilot. Key among these is [instruction files][instruction-files], which are how you provide that guidance about code generation.

In this exercise, you will:

- explore how project-specific context, coding guidelines, and documentation standards reach Copilot through repository custom instructions and path-scoped instruction files,
- send a code-generation prompt with the *current* instructions in place,
- add a new repository-wide standard to `.github/copilot-instructions.md`,
- re-run the same prompt and watch the generated code adopt the new standard,
- commit the instructions update to `main` Copilot can use the updated guidance.

> [!WARNING]
> Generated code may diverge from some of the standards you set. Copilot is non-deterministic. The point of this exercise is to see the *trend* in behavior change after updating the instructions, not to match output character-for-character.

## Instruction files

### Scenario

As any good dev shop, Tailspin Toys has a set of guidelines and requirements for development practices. These include:

- API always needs unit tests.
- UI should be in dark mode and have a modern feel.
- Documentation should be added to code in the form of docstrings.
- A block of comments should be added to the head of each file describing what the file does.

Through the use of instruction files you'll ensure Copilot has the right information to perform the tasks in alignment with the practices highlighted.

### Custom instructions

Custom instructions allow you to provide context and preferences to Copilot, so that it can better understand your coding style and requirements. This is a powerful feature that can help you steer Copilot to get more relevant suggestions and code snippets. You can specify your preferred coding conventions, libraries, and even the types of comments you like to include in your code. You can create instructions for your entire repository, or for specific types of files for task-level context.

There are two types of instructions files:

- `.github/copilot-instructions.md`, a single instruction file sent to Copilot for **every** request for the repository. This file should contain project-level information — context relevant for most chat or CLI requests sent to Copilot. This could include the tech stack being used, an overview of what's being built, best practices, and other global guidance.
- `.github/instructions/*.instructions.md` files can be created for specific tasks or file types. You can use them to provide guidelines for particular languages (like Python or TypeScript), or for tasks like creating a React component or a new set of unit tests.

> [!NOTE]
> When working in your IDE, instructions files are only used for code generation in Copilot Chat — not for code completions or next-edit suggestions.
>
> Copilot Chat, Copilot CLI and Copilot cloud agent use both repository-level and `*.instructions.md` files (with `applyTo` front matter) when generating code.
>
> Finally, Copilot [supports instructions files using other standards][custom-instructions-support], including AGENTS.md and CLAUDE.md files.

### Best practices for managing instructions files

A full conversation about creating instructions files is beyond the scope of the workshop. However, the examples provided in the sample project show a representative approach. At a high level:

- Keep instructions in `copilot-instructions.md` focused on project-level guidance, such as a description of what's being built, the structure of the project, and global coding standards.
- Use `*.instructions.md` files to provide specific instructions for file types (unit tests, React components, API endpoints), or for specific tasks.
- Use natural language. Keep guidance clear. Provide examples of how code should (and shouldn't) look.

There isn't one specific way to create instructions files, just as there isn't one specific way to use AI. You will find through experimentation what works best for your project.

> [!TIP]
> Every project using GitHub Copilot should have a robust collection of instruction files. As you explore the ones in this project, you may notice there are files for numerous types of tasks, including [UI updates][ui-instructions] and [Astro][astro-instructions].
>
> Copilot can also help generate instruction files for you. Each surface exposes this differently (for example, **Configure Chat → Generate Agent Instructions** in VS Code, or `/init` in Copilot CLI) — the lesson for the surface you're on will call it out where it's relevant.
>
> Looking for templates or a starting point? Explore [awesome-copilot][awesome-copilot], a repository full of instruction files, custom agents, and other resources.

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support

## Explore the custom instructions files in this project

Take a moment to read the instruction files this repository ships with — there's one core `copilot-instructions.md` and a collection of `*.instructions.md` files for various tasks. Open these in your codespace or the GitHub web UI.

1. Open `.github/copilot-instructions.md`.
2. Explore the file, noting the brief description of the project and sections for **Code standards**, **Scripts**, and **GitHub Actions Workflows**. These are applicable to any interactions you'd have with Copilot.
3. Open the `.github/instructions` folder and look around. Note there are instructions for Astro files, Svelte files, tests, and more.
4. Open `.github/instructions/python-tests.instructions.md`. Note the `applyTo` field at the top — this sets a glob (relative to the repo root) that determines which files the instructions apply to. Here, any Python file in `server/tests` whose name starts with `test_` will match.
5. Note the instructions specific to creating Python tests for this project.
6. Finally, open `.github/instructions/flask-endpoint.instructions.md` and scroll to the bottom. Note the links to other instruction files and existing files in the project. This lets you break larger instruction sets into smaller, reusable files, and point Copilot at examples to follow when generating code. (Paths there are relative to the instruction file rather than the repo root.)

> [!NOTE]
> The **Code formatting requirements** section in `copilot-instructions.md` already includes the rule about Python type hints. In the next steps, you'll add additional rules about docstrings and comment headers.

## Create a branch for our changes

Let's follow some best practices here and create a branch for our changes.

1. Return to your codespace from the previous exercise.
2. Open a new terminal by selecting <kbd>Ctrl</kbd>+<kbd>`</kbd>.
3. Create and switch to a new branch:

   ```bash
   git checkout -b custom-instructions
   ```

## Use Copilot Chat *before* updating the instructions

> [!TIP]
> **Open Copilot Chat**
>
> Before you start the exercises below, return to your codespace, open the Copilot Chat panel, and select **New Chat** to start a clean conversation. Mode and model selection vary per exercise — each step calls those out where it matters.

To see the impact of custom instructions, start by sending a prompt with the current instruction file in place. Later, you'll update it and re-send the same prompt to see the difference.

1. Close any open editor tabs from previous exercises so Copilot picks up only the context you want.
2. Open `server/routes/publishers.py` (an empty file) so Copilot knows where the endpoint would live.
3. Select **Ask** from the agents dropdown in the Chat view. The **Ask** agent answers questions about coding concepts, your codebase, or VS Code itself without making file changes.

   ![Screenshot showing the agent picker in the Chat view.](../images/shared-chat-mode-selector.png)

4. Send the following prompt:

   ```plaintext
   Show me the code for a new endpoint in server/routes/publishers.py that returns a list of all publishers, with the name and id for each. Display the code in chat only — don't apply or write any files.
   ```

5. Copilot explores the project and proposes code in the chat panel, often spanning `publishers.py`, `app.py`, and tests.
6. Notice the proposed function signatures use [type hints][python-type-hints] — that's coming from a directive already in `.github/copilot-instructions.md`.
7. Notice the proposed code **is missing** docstrings and a file-level comment header.

> [!WARNING]
> Because Copilot is probabilistic, there's a chance it'll add docstrings even without being told to. If that happens, that's fine — the *consistency* improvement after the instruction update is still the point.

## Add a new repository standard

As highlighted previously, `.github/copilot-instructions.md` is designed to provide project-level information to Copilot. Let's ensure repository coding standards are documented to improve code suggestions.

1. Re-open `.github/copilot-instructions.md`.
2. Locate the **Code formatting requirements** section, which should be near line 27. Note how it contains a directive to use type hints — that's why you saw those in the code generated previously.
3. Add the following lines of markdown right below the note about type hints to instruct Copilot to add comment headers to files and docstrings:

   ```markdown
   - Every function should have docstrings or the language equivalent.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. Save `copilot-instructions.md`.

> [!TIP]
> As you saw in the previous lesson, instruction files can be created at the repository level (`.github/copilot-instructions.md`) for global guidance, or as `*.instructions.md` files for specific languages, file types, or tasks. The repository-level file is the right home for project-wide standards like the docstring rule you just added.

## Re-run the prompt and observe the change

1. Return to Copilot Chat and select **New Chat** to clear the buffer.
2. Click back into `server/routes/publishers.py` so Copilot focuses on the right file.
3. Send the **same prompt** as before:

   ```plaintext
   Show me the code for a new endpoint in server/routes/publishers.py that returns a list of all publishers, with the name and id for each. Display the code in chat only — don't apply or write any files.
   ```

4. Notice that the proposed file now opens with a comment block similar to:

   ```python
   """
   Publisher API routes for the Tailspin Toys Crowd Funding platform.
   This module provides endpoints to retrieve publisher information.
   """
   ```

5. Notice that the proposed function now includes a docstring similar to:

   ```python
   """
   Returns a list of all publishers with their id and name.

   Returns:
       Response: JSON response containing an array of publisher objects
   """
   ```

You just steered Copilot to follow a new project standard with a single line of markdown — no code changes, no tool configuration. That's the power of repository custom instructions.

## Commit the instructions and push the branch

Instructions files are just like any asset in the repository, meaning they're managed using the same source control approach you'd take with any other item. So let's commit and push the branch to our repository.

1. Open a new terminal window in your codespace by selecting <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
2. From the terminal, confirm `.github/copilot-instructions.md` is the only modified file by running the following command:

   ```bash
   git status
   ```

> [!TIP]
> If `git status` shows additional changes to `server/routes/publishers.py` or other files, **Ask** mode wasn't selected when the prompt ran. Discard those changes with `git restore server/routes/publishers.py` before committing so the commit stays focused on the instructions update.

2. From the terminal, stage and commit the instructions update:

   ```bash
   git add .github/copilot-instructions.md
   git commit -m "Add docstring and file-header standards to custom instructions"
   ```

3. From the terminal, push the branch to the repository:

   ```bash
   git push -u origin custom-instructions
   ```

## Create and merge a pull request

With our branch pushed, we should create a pull request and tie it to the issue we created earlier about updating our instructions with our coding standards. We could manually do that, but Copilot, through MCP, can do that our our behalf! Let's prompt Copilot to find the issue, to create the PR to close the issue, then we can merge the PR.

1. Open Copilot Chat inside of your codespace.
2. Select <kbd>Control</kbd>+<kbd>Command</kbd>+<kbd>I</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>I</kbd> (Windows/Linux) to open the Copilot Chat view, and ensure **Agent** is selected from the agent picker.
3. Ask Copilot to find the issue related to updating instructions files and ask it to create the PR using our current branch, and reference the issue in its comment, by using the following prompt:

   ```
   Find the issue related to updating the instructions file. Create a new PR from the current branch, and highlight that the PR closes that issue. Ensure there's a good description of the updates made in the PR.
   ```

4. Copilot will begin work on finding the issue and creating the PR.
5. As prompted to **Allow** Copilot to perform tasks through the MCP server, review the command and select **Allow** as appropriate.
6. Once the PR is created, ask Copilot to merge the PR and to return your branch to main by using the following prompt:

   ```
   Merge the PR into main. Then return to main locally, and pull the latest code so we are up to date.
   ```

7. As prompted to **Allow** Copilot to perform tasks through the MCP server and the shell, review the command and select **Allow** as appropriate.

You have now created and merged a pull request with the help of GitHub Copilot!

## Summary and next steps

You explored how Copilot picks up context from instruction files in this project, then used Copilot Chat in VS Code to:

- send a code-generation prompt and observe what Copilot produces with the *existing* instructions,
- add a new repository-wide standard to `.github/copilot-instructions.md`,
- re-run the same prompt and watch the proposed code adopt the new standard,
- commit the instructions update to `main` Copilot can use the updated guidance.

Next, you'll put those instructions to work in [agent mode][next-lesson] as Copilot adds a new feature across the codebase.

## Resources

- [Instruction files for GitHub Copilot customization][instruction-files]
- [Best practices for creating custom instructions][instructions-best-practices]
- [5 tips for writing better custom instructions for Copilot][copilot-instructions-five-tips]
- [Personal custom instructions for GitHub Copilot][personal-instructions]
- [Awesome Copilot — a collection of instruction files and other resources][awesome-copilot]

[previous-lesson]: 1-mcp.md
[next-lesson]: 3-agent-mode.md
[instruction-files]: https://code.visualstudio.com/docs/copilot/copilot-customization
[python-type-hints]: https://docs.python.org/3/library/typing.html
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[personal-instructions]: https://docs.github.com/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
[awesome-copilot]: https://github.com/github/awesome-copilot
