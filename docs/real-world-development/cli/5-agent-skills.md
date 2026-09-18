---
title: "Lesson 5 - Customize and use a quality-checks skill"
description: "Explore the existing quality-checks skill, customize its report format, and use it to validate filtering."
authors:
  - geektrainer
lastUpdated: 2026-09-18
---

There's more to writing code than just writing code. We've been able to validate the code works manually and used instruction files to ensure it follows our standards. But how about testing? Linting? All the other parts of continuous integration (CI)?

For these types of tasks, **agent skills** are the best fit! Skills help Copilot understand how to properly run operations like these.

In this lesson, you will:

- explore the existing `quality-checks` skill.
- customize the format of its results.
- reload and run the skill.

## Scenario

Tailspin Toys has a collection of unit and end to end tests which always need to be run before any pull request (PR) is made. As you might expect, ensuring these are run correctly and consistently is important. The team has already created an agent skill to run these tests, but they want to enhance the output for better readability.

## Instructions, scripts, and resources

Agent skills package reusable task instructions, executable scripts, and supporting resources that an agent loads on demand. At their core, they're a folder with the name of the skill, with a Markdown file named `SKILL.md`. The Markdown contains frontmatter with a name and description to define what the skill is, an overview of what it does, and guidance on when it should be called. The folder can also contain subfolders with scripts and other resources for the skill to use when called.

> [!NOTE]
> Additional folders and files are not required for a skill. The Tailspin Toys `quality-checks` skill contains only `SKILL.md` because it uses the project's existing commands.

Skills can reside in a project's `.github/skills` folder to become a repository asset shared and reused by the team, or in the user skills folder at `~/.copilot/skills`.

## Explore the skill

Let's explore the skill the Tailspin Toys team created for running tests and linters, named `quality-checks`.

1. In the Codespaces editor, open `.github/skills/quality-checks/SKILL.md`.
2. Read the `name` and `description` at the top. The description helps Copilot understand when to call the skill.
3. Read the instructions and note how they guide Copilot through the testing and linting process.
4. Notice that the skill does not yet contain a **Results output formatting** section.

## Run the skill before making a change

Skills are callable directly through Copilot CLI or by using natural language. Let's run the skill by asking Copilot to run our tests!

1. Return to the filtering conversation in Interactive mode.
2. Use the following prompt:

   ```plaintext
   Run the tests and linters.
   ```

3. Note the report at the end.

## Customize the report

OK, we'd like a better report that tells us what ran, whether it succeeded, and what the tools actually reported. Let's update our skill to create that report for us!

1. Return to `.github/skills/quality-checks/SKILL.md`.
2. Add the following section near the end of the file:

   ```markdown
   ## Results output formatting

   Upon completion, report each command that ran and whether it passed, failed, or was blocked. Include test counts, durations, errors, warnings, and other metrics only when the tool reports them. Identify the next action for any failure or blocker, and never describe a skipped or incomplete check as passed.
   ```

3. Save the file.

## Run the updated skill

With our change made, let's see it in action! Copilot CLI can reload edited skills without restarting the conversation.

1. Enter:

   ```plaintext
   /skills reload
   ```

2. Use the exact same prompt as before:

   ```plaintext
   Run the tests and linters.
   ```

3. Note the report at the end and compare it with the first report. Confirm every metric comes from the tools rather than an invented percentage.

## Summary and next steps

You've customized and used an existing agent skill. In this lesson, you:

- explored the existing `quality-checks` skill.
- customized the format of its results.
- reloaded and ran the skill.

That change will accompany filtering in the feature PR. Next, you'll allow Copilot to interact with the site directly [via the Playwright MCP server][next-lesson].

## More skill examples

These community examples are references, not additional tasks:

- [Agent Skills specification][skill-spec]
- [Contribution workflow: `make-repo-contribution`][contribution-example]
- [Requirements documents: `prd`][prd-example]
- [Diagrams and a bundled export script: `drawio`][drawio-example]
- [Browser testing: `webapp-testing`][browser-example]

[previous-lesson]: ../4-custom-instructions/
[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
