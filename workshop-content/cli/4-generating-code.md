# Exercise 4 - Adding project features with GitHub Copilot CLI

| [← Previous lesson: MCP Servers][previous-lesson] | [Next lesson: Agent Skills →][next-lesson] |
|:--|--:|

As you might expect, the core tasks you'll perform with GitHub Copilot CLI is to add features, functionality, and code to a project. As you've already explored, you can add instructions files and MCP servers to help guide Copilot and ensure you're getting the code you expect, following the best practices laid out by the team and community. Let's take one of the issues we generated previously and ask Copilot to help us implement it.

## Scenario

The time has come to finally implement filtering in the project. You've already got the issue in GitHub. Let's have Copilot retrieve the details from the issue and put together a plan to implement it. Then we'll get Copilot on the job to create the code and run the tests.

In this exercise, you will:

- utilize plan mode to generate a plan for implementing the filtering functionality.
- generate the code necessary to add filtering to the website with Copilot.

By the end of this exercise, you will have added new functionality to the project.

## Warm-up: see custom instructions in action

Before we dive into building filtering, let's see firsthand how the instruction files you explored in Exercise 1 shape Copilot CLI's output.

1. Return to your codespace and open a fresh terminal window. Start Copilot CLI by issuing the following command:

    ```bash
    copilot --allow-all-tools
    ```

    If Copilot CLI is already running, clear Copilot's context by sending the `/clear` command in the prompt.

2. Open **server/routes/publishers.py**, which is currently an empty file, so you can see Copilot's output land there. You can use `code server/routes/publishers.py` if you're in a codespace, or whatever editor you prefer.
3. Send the following prompt to Copilot CLI:

    ```
    Create a new endpoint to return a list of all publishers. It should return the name and id for all publishers.
    ```

4. Review the generated code. You should notice that it includes type hints because those are already in **.github/copilot-instructions.md**, but it's missing a docstring and comment header.
5. Open **.github/copilot-instructions.md**. In the **Code formatting requirements** section, right under the type-hints note, add the following guidance:

    ```markdown
    - Every function should have docstrings or the language equivalent.
    - Before imports or any code, add a comment block to the file that explains its purpose.
    ```

6. Return to Copilot CLI, send `/clear`, and then send the same publishers prompt again. This time, the new output should include a comment header and a docstring.
7. Don't keep the warm-up changes. Undo them in your editor, or run the following command:

    ```bash
    git checkout -- server/routes/publishers.py
    ```

    You'll do the real project work in the next section.

> [!IMPORTANT]
> AI output is non-deterministic, so your generated code may vary slightly. Focus on the pattern: updating the instructions changes the shape of Copilot CLI's next response.

## Utilize plan mode

One of the best uses of AI is planning. Oftentimes you'll have a good concept of what you want to build, but just need to bounce some ideas off of something. AI tools can help you crystalize your thoughts by asking you follow up questions and working through different pitfalls or missing components. To support this process, Copilot CLI offers a plan mode.

You'll start the process of creating the new functionality by utilizing plan mode in Copilot CLI.

1. Return to your codespace.
2. If not already open, open a terminal window by utilizing <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. If not already running, start Copilot CLI by issuing the following command in the terminal window:

    ```bash
    copilot --allow-all-tools
    ```

4. If already running, clear Copilot's context by sending the `/clear` command in the prompt.
5. Switch Copilot CLI into plan mode by selecting <kbd>Shift</kbd>+<kbd>Tab</kbd> until you see **Plan mode** just below the prompt window.
6. Enter the following prompt into Copilot CLI to have it retrieve the issue from your repository and put forth a plan for implementing the functionality:

    ```
    Retrieve the issue on the repository related to adding filtering. Help me build a good plan to implement this functionality.
    ```

7. Copilot may ask follow-up questions as it builds out its plan. As those arise, answer them based on how you'd build out the functionality.
8. Once the plan is generated, review the blueprint. You should notice it recommends changes to the backend and frontend, as well as generating tests. You can utilize <kbd>Ctrl</kbd>+<kbd>Y</kbd> to view the full details as a markdown file in VS Code.
9. If you wish to make any suggestions to the plan Copilot generated, feel free to do so!
10. Once you're satisfied, switch out of plan mode by selecting <kbd>Shift</kbd>+<kbd>Tab</kbd>.
11. Tell Copilot to start the work by sending a `start` prompt (or another similar phrase like "Let's do it!") to Copilot.
12. Copilot will get to work generating the files!

> [!NOTE]
> This operation will likely take several minutes. You will see Copilot edit and create files, update and generate tests, and run all of the tests to ensure everything succeeds. Now's a good time to reflect on what you've explored thus far, or to enjoy a beverage.

## Review the code

All AI code needs to be reviewed before being merged into production. Let's take the time now to explore the files Copilot created and modified in implementing the new feature.

1. Review the changed files using whichever workflow fits your environment:

    - **Option A: Terminal**. If you're working from the terminal, you can use git directly:

        ```bash
        git status
        git diff
        ```

        Use `git status` to see the changed files and `git diff` to see the specific changes. Open any files you want to inspect with your editor of choice, such as `code <file>` if you're in a codespace, or `$EDITOR <file>` otherwise.

    - **Option B: VS Code GUI**. If you have VS Code open, hide the terminal window in your codespace by selecting <kbd>Ctrl</kbd>+<kbd>\`</kbd>, then select **Source Control** in your codespace.

2. Note the files changed. You should see updates to files such as **games.py**, the Games API, and **test_games.py**, the tests for that API. You should also see new files created, such as Svelte components for the new filter functionality, and Playwright tests to validate the frontend.
3. Open the files and explore the changes. In particular, notice the comment sections which have been added. All of this comes from the instructions files you worked on previously in this workshop.

## Summary and next steps

You've now added filtering functionality to the website with the help of Copilot CLI! Specifically, you:

- utilized plan mode to generate a plan for implementing the filtering functionality.
- generated the code necessary to add filtering to the website with Copilot.

Of course, the next step from here is to [create the PR][next-lesson], which we'll do with the help of a skill.

## Resources

- [Using Copilot CLI][using-copilot-cli]
- [About Copilot CLI][about-copilot-cli]
- [Context management in Copilot CLI][context-management]

---

| [← Previous lesson: MCP Servers][previous-lesson] | [Next lesson: Agent Skills →][next-lesson] |
|:--|--:|

[previous-lesson]: ./3-mcp.md
[next-lesson]: ./5-agent-skills.md
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
