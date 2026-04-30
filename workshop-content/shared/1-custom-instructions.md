# Exercise 1 - Providing context to Copilot with instruction files

| [← Previous lesson: Prerequisites][previous-lesson] | [Next lesson →][next-lesson] |
|:--|--:|

Context is key across many aspects of life, and when working with generative AI. If you're performing a task which needs to be completed a particular way, or if a piece of background information is important, you want to ensure Copilot has access to that information. You can use [instruction files][instruction-files] to provide guidance so that Copilot not only understands what you want it to do but also how you want it to be done.

In this exercise, you will learn how to:

- provide Copilot with project-specific context, coding guidelines and documentation standards using [repository custom instructions][repository-custom-instructions] **.github/copilot-instructions.md**.
- provide path instruction files to guide Copilot for repetitive or templated tasks on specific types of files.
- implement both repository-wide instructions and task-specific instructions.

> [!IMPORTANT]
> Note that the code generated may diverge from some of the standards you set. AI tools like Copilot are non-deterministic, and may not always provide the same result. The other files in the codebase do not contain docstrings or comment headers, which could lead Copilot in another direction. Consistency is key, so making sure that your code follows the established patterns is important. You can always follow-up in chat and ask Copilot to follow your coding standards, which will help guide it in the right direction.

## Scenario

As any good dev shop, Tailspin Toys has a set of guidelines and requirements for development practices. These include:

- API always needs unit tests.
- UI should be in dark mode and have a modern feel.
- Documentation should be added to code in the form of docstrings.
- A block of comments should be added to the head of each file describing what the file does.

Through the use of instruction files you'll ensure Copilot has the right information to perform the tasks in alignment with the practices highlighted.

## Custom instructions

Custom instructions allow you to provide context and preferences to Copilot, so that it can better understand your coding style and requirements. This is a powerful feature that can help you steer Copilot to get more relevant suggestions and code snippets. You can specify your preferred coding conventions, libraries, and even the types of comments you like to include in your code. You can create instructions for your entire repository, or for specific types of files for task-level context.

There are two types of instructions files:

- **.github/copilot-instructions.md**, a single instruction file sent to Copilot for **every** chat prompt for the repository. This file should contain project-level information, context which is relevant for most chat requests sent to Copilot. This could include the tech stack being used, an overview of what's being built and best practices, and other global guidance for Copilot.
- **\*.instructions.md** files can be created for specific tasks or file types. You can use **\*.instructions.md** files to provide guidelines for particular languages (like Python or TypeScript), or for tasks like creating a React component or a new set of unit tests.

> [!NOTE]
> When working in your IDE, instructions files are only used for code generation in Copilot Chat, and not used for code completions or next edit suggestions.
>
> Copilot coding agent and Copilot CLI will utilize both repository level and `*.instructions` files with `applyTo` header matter when generating code.

## Best practices for managing instructions files

A full conversation about creating instructions files is beyond the scope of the workshop. However, the examples provided in the sample project provide a representative example of how to approach their management. At a high level:

- Keep instructions in **copilot-instructions.md** focused on project-level guidance, such as a description of what's being built, the structure of the project, and global coding standards.
- Use **\*.instructions.md** files to provide specific instructions for file types (unit tests, React components, API endpoints), or for specific tasks.
- Use natural language in your instructions files. Keep guidance clear. Provide examples of how code should (and shouldn't) look.

There isn't one specific way to create instructions files, just as there isn't one specific way to use AI. You will find through experimentation what works best for your project. The guidance provided here and the [resources](#resources) below should help you get started.

> [!TIP]
> Every project using GitHub Copilot should have a robust collection of instructions files to provide context and best guide code generation. As you explore the instructions files in the project, you may notice there are ones for numerous types of files and tasks, including [UI updates][ui-instructions] and [Astro][astro-instructions]. The investment made in instructions files will greatly enhance the quality of code suggestion from Copilot, ensuring it better matches the style and requirements your organization has.
> 
> You can even have Copilot aid in generating instructions files by selecting the gear icon for **Configure Chat** in Copilot chat and selecting **Generate Agent Instructions**. Or if using Copilot CLI, use the `/agent` command to engage an agent specialized for generating instruction files.
>
> And, if you're looking for templates or a starting point for instructions files, you can explore [awesome-copilot][awesome-copilot], a repository full of instructions files, custom agents, and other resources to help you out! 

## Ensure your codespace is ready

In a [prior exercise][prereqs-lesson] you launched the codespace you'll use for the remainder of the coding exercises in this lab. Let's put the final touches on it before you begin using it.

The setup process for the codespace installed and set up many [VS Code extensions][vscode-extensions]. As with any software, updates may be needed. When your codespace is created you'll need to ensure everything is up-to-date.

1. Return to the tab where you started your codespace. If you closed the tab, return to your repository, select **Code** > **Codespaces** and then the name of the codespace.
2. Select **Extensions** on the workbench on the left side of your codespace.

    ![Screenshot of the extensions window with multiple extensions showing either Update or Reload Window buttons](../images/ex1-extensions-updates.png)

3. Select **Update** on any extensions with an **Update** button. Repeat as necessary.
4. Select **Reload Window** on any extensions with a **Reload Window** button to reload the codespace.
5. When prompted by a dialog, select **Reload** to reload the window. This will ensure the latest version is being used.

## Explore the custom instructions files

Let's start by exploring the instructions files created for this project. You'll notice there's one core **copilot-instructions.md** file, and a collection of **.instructions** files for various tasks.

1. Return to your codespace.
2. Open **.github/copilot-instructions.md**.
3. Explore the file, noting the brief description of the project and sections for **Code standards**, **Scripts** and **GitHub Actions Workflows**. These are applicable to any interactions you'd have with Copilot, are robust, and provide clear guidance on what you're doing and how you want to accomplish it.
4. Open **.github/instructions**, and explore the files contained inside it. Note there are instructions for Astro files, Svelte files, the various tests, and others.
5. Open **.github/instructions/python-tests.instructions.md**. Make note of the `applyTo` section. This sets the path, relative to the root of the project, which determines which files the instructions apply to. In this case, any Python files in the **server/tests** folder with a name that starts with **test_** will match the slug.
6. Note the instructions specific to creating Python tests for this project.
7. Finally, open **.github/instructions/flask-endpoint.instructions.md**, and scroll to the bottom of the file. Note the links to other instructions files and existing files in the project. This allows you to both break down larger instruction sets into smaller, reusable files, and to point to examples Copilot should consider when generating code. Note these paths are relative to the instructions file rather than the root of the project.

## Examine the impact of custom instructions

To see the impact of custom instructions, you'll start by sending a prompt with the current version of the files, and see how Copilot pulls those files into context. Then you'll make some updates, send the same prompt again, and note the difference.

1. Return to your codespace.
2. Close any files open in the codespace.
3. Open `server/routes/publishers.py`, an empty file.
4. If **Copilot chat** is not already open, open it by selecting the Copilot icon towards the top of your codespace.
5. Create a new chat session by typing `/clear` into the chat window and selecting <kbd>Enter</kbd> (or <kbd>return</kbd> on a Mac).
6. Select **Ask** from the modes dropdown.
7. Send the following prompt to create a new endpoint to return all publishers:

   ```plaintext
   Create a new endpoint to return a list of all publishers. It should return the name and id for all publishers.
   ```

8. Copilot explores the project to learn how best to implement the code, and generates a list of suggestions, which may include code for `publishers.py`, `app.py`, and tests to ensure the new code runs correctly.
9. Explore the code, noticing the generated code includes [type hints][python-type-hints] because, as you'll see, the custom instructions includes the directive to include them.
10. Notice the generated code **is missing** either a docstring or a comment header - or both!

> [!IMPORTANT]
> As highlighted previously, GitHub Copilot and LLM tools are probabilistic, not deterministic. As a result, the exact code generated may vary, and there's even a chance it'll abide by your rules without you spelling it out! But to aid consistency in code you should always document anything you want to ensure Copilot should understand about how you want your code generated.

## Add new repository standards to copilot-instructions.md

As highlighted previously, `copilot-instructions.md` is designed to provide project-level information to Copilot. Let's ensure repository coding standards are documented to improve code suggestions from Copilot.

1. Return to your codespace.
2. Open `.github/copilot-instructions.md`.
3. Locate the **Code formatting requirements** section. Note how it contains a note to use type hints. That's why you saw those in the code generated previously.
4. Add the following lines of markdown right below the note about type hints to instruct Copilot to add comment headers to files and docstrings:

   ```markdown
   - Every function should have docstrings or the language equivalent.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

5. Close **copilot-instructions.md**.
6. Select **New Chat** in Copilot chat to clear the buffer and start a new conversation.
7. Return to **server/routes/publishers.py** to ensure focus is set correctly.
8. Send the same prompt as before to create the endpoint.

   ```plaintext
   Create a new endpoint to return a list of all publishers. It should return the name and id for all publishers.
   ```

9. Notice how the newly generated code includes a comment header at the top of the file which resembles the following:

   ```python
   """
   Publisher API routes for the Tailspin Toys Crowd Funding platform.
   This module provides endpoints to retrieve publisher information.
   """
   ```

10. Notice how the newly generated code includes a docstring inside the function which resembles the following:

   ```python
   """
   Returns a list of all publishers with their id and name.
    
   Returns:
      Response: JSON response containing an array of publisher objects
   """
   ```

11. Notice the generated code now includes a docstring as well as a comment block at the top!
12. Also note how the existing code isn't updated, but of course you could ask Copilot to perform that operation if you so desired!
13. **Don't implement the suggested changes**, as you'll be doing that in a later exercise.

> [!NOTE]
> If you accepted the changes, you can always select the **Undo** button towards the top right of the Copilot chat window.

## Summary and next steps

Congratulations! You explored how to ensure Copilot has the right context to generate code following the practices your organization has set forth. This can be done at a repository level with the **.github/copilot-instructions.md** file, or on a task basis with instruction files. You explored how to:

- provide Copilot with project-specific context, coding guidelines and documentation standards using custom instructions (.github/copilot-instructions.md).
- use instruction files to guide Copilot for repetitive or templated tasks.
- implement both repository-wide instructions and task-specific instructions.

Next, continue to the exercise for your chosen path!

## Resources

- [Instruction files for GitHub Copilot customization][instruction-files]
- [5 tips for writing better custom instructions for Copilot][copilot-instructions-five-tips]
- [Best practices for creating custom instructions][instructions-best-practices]
- [Personal custom instructions for GitHub Copilot][personal-instructions]
- [Awesome Copilot - a collection of instructions files and other resources][awesome-copilot]

---

| [← Previous lesson: Prerequisites][previous-lesson] | [Next lesson →][next-lesson] |
|:--|--:|

[previous-lesson]: ./0-prereqs.md
[next-lesson]: ../README.md
[instruction-files]: https://code.visualstudio.com/docs/copilot/copilot-customization
[repository-custom-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[python-type-hints]: https://docs.python.org/3/library/typing.html
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[personal-instructions]: https://docs.github.com/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
[awesome-copilot]: https://github.com/github/awesome-copilot
[ui-instructions]: ../../.github/instructions/ui.instructions.md
[astro-instructions]: ../../.github/instructions/astro.instructions.md
[vscode-extensions]: https://code.visualstudio.com/docs/configure/extensions/extension-marketplace
