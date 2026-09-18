---
title: "Lesson 5 - Customize and use a quality-checks skill"
description: "Explore the existing quality-checks skill, customize its report format, and use it to validate filtering."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

There's more to writing code that just writing code. We've been able to validate the code works manually, and used instructions files to ensure it follows our standards. But how about testing? Linting? All the other parts of continuous integration (CI)?

For these types of tasks, **agent skills** are the best fit! Skills help Copilot understand how to properly run operations like these.

In this lesson, you will:

- explore the existing `quality-checks` skill and its bundled scripts.
- customize the format of its results.
- run the skill and review its output.

## Scenario

Tailspin Toys has a collection of unit and end to end tests which always need to be run before any pull request (PR) is made. As you might expect, ensuring these are run correctly and consistently is important. The team has already created an agent skill to run these tests, but they want to enhance the output for better readability.

## Instructions, scripts, and resources

Agent skills package reusable task instructions, executable scripts, and supporting resources that an agent loads on demand. At their core, they're a folder with the name of the skill, with a markdown file named `SKILL.md`. The markdown contains frontmatter with a name and description to define what the skill is, an overview of what it does, and guidance on when it should be called. The folder can also contain subfolders which contain scripts and other resources for the skill to use when called.

> [!NOTE]
> Additional folders and files are not required for a skill! In our example, our skill will be running `npm` commands to run our tests and linters. As a result, we don't need additional supporting files.

Skills can reside in a projects `.github/skills` folder to become a repository asset to be shared and reused by the rest of the team, or in the root folder for Copilot, typically `~/.copilot/skills`.

## Explore the skill

Let's explore the skill the Tailspin Toys team created for running tests and linters, named `quality-checks`.

1. If you don't already have a **Files** canvas open, in the review panel, select **+**, then **File**
2. Search for `.github/skills/quality-checks/SKILL.md`.
3. Read the `name` and `description` at the top. Note the description, which helps Copilot understand when to call the skill.
4. Read the instructions and note how it guides Copilot through the testing and linting process.

## Run the skill before making a change

Skills are callable directly via a slash (`/`) command, or by using natural language to call the skill. If you notice the description, it highlights the fact the skill is to be used whenever a request is made to run tests or linting. Let's run the skill by asking Copilot to run our tests!

1. Ensure Copilot is in **Interactive** mode by selecting it from the mode dropdown.
2. Use the following prompt to ask Copilot to run the tests and linter, which will call the skill:

    ```plaintext
    Run the tests and linters.
    ```

3. Note the report at the end.

## Customize the report

OK, we'd like to get a better report that shows us the tests that ran, success/failure rates, and how long they took to run. Let's update our skill to have Copilot create that report for us!

1. Return to the **Files** canvas.
2. If not already open, open `.github/skills/quality-checks/SKILL.md`.
3. Find the header at the bottom of the file that reads **Results output formatting**.
4. Just below that header, add the following to ensure our results are displayed to our specifications:

    ```markdown
    Upon completion of all tests, generate a report that provides a quick overview of both success and failure of the tests, and how long they took to ran. In particular, we need sections for:

    - Unit tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - End to end tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - Linting, number of lines scanned, number of violations, and the percentage of lines of code that meet the linting requirements.
    ```

The file will automatically be saved.

## Run the updated skill

With our change made, let's see it in action! We'll use the exact same prompt as before.

1. Ensure Copilot is in **Interactive** mode by selecting it from the mode dropdown.
2. Use the following prompt to ask Copilot to run the tests and linter, which will call the skill:

    ```plaintext
    Run the tests and linters.
    ```

3. Note the report at the end.

## Summary and next steps

You've customized and used an existing agent skill. In this lesson, you:

- explored the `quality-checks` skill and its bundled scripts.
- customized the format of its results.
- ran the skill and reviewed its output.

That change will accompany filtering in the feature PR. Next, you'll allow Copilot to interact with the site directly [via the Playwright MCP server][next-lesson].

## More skill examples

These community examples are references, not additional tasks. Review their prerequisites and behavior before adopting them:

- [Agent Skills specification][skill-spec].
- [Contribution workflow: `make-repo-contribution`][contribution-example].
- [Requirements documents: `prd`][prd-example].
- [Diagrams and a bundled export script: `drawio`][drawio-example].
- [Browser testing: `webapp-testing`][browser-example].

The upstream contribution example is named `make-repo-contribution`; older Tailspin templates used a different name, `make-contribution`. This workshop does not depend on either contribution skill.

[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
