---
title: "Lesson 5 - Create and use a quality-checks skill"
description: "Ask Copilot to create reusable shell-bundled quality checks, inspect the skill, and execute it on the filtering branch."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Your filtering feature is implemented and checked with the existing npm commands. Now you'll package those checks as a reusable **agent skill**. Stay in the same filtering session and branch through Lessons 4–8; this lesson does not create a pull request.

In this lesson, you will:

- return to **Interactive** mode before creating customizations.
- ask Copilot to create and then stop for inspection of `quality-checks`.
- execute all four checks through its bundled scripts and prove a single-file test argument selects only that file.
- checkpoint the skill alongside the filtering feature.

## Scenario

Tailspin Toys needs the same quality checks whenever filtering changes. Instead of explaining the commands and prerequisites in every conversation, the team wants a reusable skill. You'll create it, inspect its scripts, and verify that another request can run the checks correctly.

## Instructions, scripts, and resources

Skills package reusable task instructions, executable scripts, and supporting resources that an agent loads on demand. Custom agents define specialist roles, instructions, and available tools. These are complementary: a custom agent can execute scripts, including those bundled with a skill.

A repository skill lives in `.github/skills/<skill-name>/SKILL.md`, with `name` and `description` frontmatter and Markdown instructions. Scripts and other resources live beside it. You'll ask Copilot to generate `.github/skills/quality-checks/SKILL.md` and its bundled scripts, rather than copy a prebuilt answer. The [Agent Skills specification][skill-spec] describes the format.

Copilot uses a discovered skill's description to decide when to load it. Don't assume a new skill is immediately discovered in an already open session; the run section includes an explicit-read fallback. A portable format does not remove shell or project prerequisites.

## Create the skill

Switch the filtering session back to **Interactive** mode using the mode selector before sending the prompt. Keep the current checkout and branch. If you started with an older template that already has this skill, inspect and extend it rather than overwrite your customizations.

```plaintext
Create .github/skills/quality-checks/SKILL.md and four scripts wrapping npm run lint, npm run test:unit, npm run test:e2e, and npm run typecheck:all. Read package.json, README, test configuration, and repository instructions first.

Detect this environment. Create ONLY Bash .sh scripts for macOS/Linux/WSL OR PowerShell .ps1 scripts for native Windows; ask if uncertain. Do not create both. Keep wrappers limited to resolving the repository root from their own location, verifying this project's package.json there, and invoking npm. Fail clearly for an invalid root. Support any working directory and paths with spaces. Preserve output and failure exit codes, including PowerShell native failures. Insert npm's -- exactly once; callers supply tool arguments directly without another --. No port or process management.

Give SKILL.md name/description frontmatter, instructions to run all four wrappers, prerequisites, troubleshooting, and portable examples including one existing unit-test file. Every Bash example must invoke bash explicitly; never bypass PowerShell execution policy. Explain Playwright server reuse: stop only servers you actually started; otherwise ask.

Only create the skill and necessary scripts. Do not run checks or probes, install anything, change application code, commit, or open a PR. Stop for inspection.
```

## Inspect the skill

1. Open **Changes** to review the generated files. You can also use the review panel's **+**, **File**, then search for `SKILL.md` or the script filenames.
2. Check that `name` and `description` describe the skill and when it applies. Read the instructions, not just the metadata.
3. Confirm the execution sequence actually invokes bundled scripts under `.github/skills/quality-checks/` for lint, unit tests, E2E, and type checking.
4. Inspect each wrapper for script-relative root resolution and an explicit check that the derived directory contains this checkout's intended `package.json`. A command that succeeds because npm searches ancestor directories does not prove the root is correct. Check quoted paths, argument forwarding, visible output, and failure exits; PowerShell must propagate native npm failures.
5. Check the documented single-unit-test-file example. The wrapper inserts npm's `--` separator, so callers pass target-tool arguments directly without another separator. Keep reusable instructions free of machine-specific absolute checkout paths. Ask Copilot to correct gaps before running anything.
6. Keep the scripts limited to root/manifest validation and running the existing npm checks. Port and process decisions belong in SKILL.md, not shell process-management code. Confirm that only servers actually started by the agent may be stopped; a matching working directory or process name does not establish ownership. The delivered files should contain only the skill, required wrappers, and any needed shared helper, without temporary probe or debug files.

> [!NOTE]
> Current Tailspin Toys requires Node.js 22.13 or later, project dependencies, and Playwright Chromium for E2E checks. Confirm prerequisites in your checkout's README and `package.json`. Missing prerequisites or a blocked PowerShell execution policy need an approved resolution, not an automatic installation, policy bypass, or silent switch to direct npm.

## Run the skill

Confirm the development server from the previous lesson has stopped. Playwright builds and serves a preview for E2E, but its local configuration can reuse a server on port `4321`. A server from another checkout is not valid evidence for your feature.

If the app offers `/quality-checks`, select it to explicitly invoke the discovered skill and include the request below. If it is not discovered, send the same request directly in this session; reading the skill is a supported fallback for this exercise.

```plaintext
Read .github/skills/quality-checks/SKILL.md and follow its instructions to validate the filtering feature in this checkout. First inspect each wrapper's code to verify that it derives the directory containing this checkout's intended package.json and explicitly fails for an invalid root, rather than relying on npm's ancestor-package discovery. Do not move, rename, delete, or modify repository files to simulate failures. Actually run its bundled scripts for lint, unit tests, end-to-end tests, and type checks. Also run the documented single-unit-test-file example, passing target-tool arguments directly because the wrapper owns npm's -- separator. Verify from the test runner's results that ONLY the named file ran, and report that filename and the executed test-file count. Echoing arguments or returning exit code 0 alone is not proof of correct selection.

Report each script invocation and result, including failures, skipped checks, or missing prerequisites. Do not silently substitute direct npm commands for an unusable skill script. Identify the checkout and server under test, stop only servers you started, and ask before installing anything or stopping another process. Do not change application code, change branches, commit, push, or open a pull request.
```

Inspect the tool calls and output. All four scripts must actually execute; a description of the checks or a skipped check is not a pass. For the single-file example, compare the requested filename with the runner's actual file results and reported count: only that file should run. Echoed arguments or exit code 0 are insufficient if other files also ran. A failure is useful evidence: correct the skill or resolve the setup blocker with approval, then rerun the affected checks. Don't stop unrelated processes or force a port conflict away.

## Save a checkpoint

Once you have reviewed the skill and its results, authorize a local checkpoint:

```plaintext
Review the current diff and create a checkpoint commit for the quality-checks skill files only. Keep the existing filtering branch. Do not push or create a pull request.
```

## Summary and next steps

You've created, inspected, and run a reusable quality-checks skill, including its single-file test example. The skill files will accompany filtering, the QA profile, and associated tests in the feature PR in Lesson 8. Continue in this same session to [Lesson 6 - Validate functionality with Playwright MCP][next-lesson].

## More skill examples

These community examples are references, not additional tasks. Review their prerequisites and behavior before adopting them:

- [Contribution workflow: `make-repo-contribution`][contribution-example].
- [Requirements documents: `prd`][prd-example].
- [Diagrams and a bundled export script: `drawio`][drawio-example].
- [Browser testing: `webapp-testing`][browser-example].

The upstream contribution example is named `make-repo-contribution`; older Tailspin templates used a different name, `make-contribution`. This workshop does not depend on either contribution skill.

[previous-lesson]: ../4-build-filtering/
[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
