---
title: "Exercise 3 - Guide Copilot with custom instructions"
description: "Add a focused documentation convention, demonstrate it on existing code, and merge the second pull request."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

Context helps Copilot understand not just *what* to build but *how* your team expects code to be written. You'll add a focused documentation convention, observe its effect on real code, and merge the instructions and demonstration together as PR 2.

In this exercise, you will:

- explore repository-wide and path-scoped instructions.
- add a documentation standard without implementing filtering early.
- demonstrate the standard on a small existing helper or component.
- validate and merge the instructions milestone.

## Explore the instructions

The repository already contains two useful kinds of instructions:

- `.github/copilot-instructions.md` supplies repository-wide context, such as the stack, structure, and common practices.
- `.github/instructions/*.instructions.md` supplies scoped guidance. An `applyTo` frontmatter glob identifies the files the instructions apply to.

Open these files in your editor:

1. Read `.github/copilot-instructions.md` and locate the current coding and verification standards.
2. Explore `.github/instructions/`, including the Astro, data-layer, and test guidance.
3. In `unit-tests.instructions.md`, inspect the `applyTo` pattern and the testing conventions.
4. In `drizzle.instructions.md`, inspect the data-access patterns and references to examples.

Keep repository-wide instructions concise, place file-specific detail in the relevant scoped file, and avoid conflicting copies of the same rule. [GitHub's instruction support reference][instruction-support] explains which instruction formats each harness supports.

> [!NOTE]
> Instructions influence generation; they do not guarantee compliance. Your review will check both the instruction text and its effect on code. If Copilot already produces good comments, the lesson is about making the convention explicit and repeatable, not forcing a before-and-after failure.

## Start from merged PR 1

Confirm the star-rating PR is merged. From the learner repository terminal, start the next milestone from updated `main`:

```bash
git status
git switch main
git pull --ff-only
git switch -c update-custom-instructions
copilot --enable-all-github-mcp-tools
```

If the working tree is not clean or the pull fails, resolve that state before continuing. Stay in **Interactive** mode.

In the repository's **Issues** tab, find **Update our repository coding standards** and copy its actual URL. The issue provides the broader context: explain intent, document exported data-layer functions and component contracts, and keep comments current. This exercise takes a bounded documentation slice, not a repository-wide refactor or a promise to complete every issue criterion.

## Add the documentation convention

Replace the placeholder with the actual issue URL and send:

```plaintext
Read this coding-standards issue for context: <coding-standards-issue-URL>. Inspect the existing repository and scoped instructions. Add a focused documentation convention: explain intent rather than restating code, document exported functions in db/ and src/lib/ with TSDoc/JSDoc covering purpose, parameters, and return values, document reusable Astro component Props contracts, and keep comments current when related code changes.

Put each rule in the appropriate existing instruction file and avoid duplication or contradictions. Preserve the existing formatting and linting standards; link to or summarize the documentation convention in README where appropriate. Limit this change to the documentation standard, not a formatting-tool migration or repository-wide rewrite. Do not create a skill or agent, implement filtering, commit, push, or open a PR. Stop so I can inspect the instructions before the demonstration.
```

Inspect the diff. The convention should encourage useful comments, not demand a boilerplate header on every file or comments that merely repeat obvious code. Ask for corrections before proceeding.

## Demonstrate the convention on real code

Choose a small existing exported helper or reusable component after inspecting the repository. It does not need to be a publisher helper, and there is no requirement that `src/lib/publishers.ts` already exists.

Send:

```plaintext
Using the updated instructions, select one small existing exported helper or reusable Astro component that would benefit from clearer documentation. Apply the convention directly to that file without changing runtime behavior or adding filtering functionality. Explain which instruction guided the change, and stop before committing or opening a PR.
```

Open the actual changed file. For a helper, check that the comments accurately describe its parameters, return value, and any injected database argument. For a component, check that its `Props` contract is documented. Confirm the explanation matches the code rather than just looking for a comment block.

> [!TIP]
> An illustrative snippet in the chat is not the demonstration: inspect a real repository change. If the selected code already meets the convention, choose another small existing target where an improvement is justified rather than add redundant comments.

## Validate and merge PR 2

Ask Copilot to validate the reviewed changes:

```plaintext
Review the instruction changes and the small documentation demonstration. Confirm runtime behavior is unchanged. Inspect package.json, run npm run lint and npm run typecheck:all, and run affected existing tests where the code change warrants them. Report exact commands and results. Do not install anything, create a skill, commit, push, or open a PR yet.
```

Resolve failures and inspect the final diff. Then authorize the milestone:

```plaintext
Commit only the reviewed documentation instructions, directly related README update, and small code demonstration. Push the current branch and create a PR into main following the repository's PR template. Include the verification results and reference the coding-standards issue as a partial contribution; do not use a closing keyword unless every issue criterion is actually satisfied. Do not merge or start filtering.
```

Open the PR URL, inspect **Files changed**, and review CI. After all required checks and reviews pass, merge on GitHub and confirm PR 2 is **Merged**. Exit the CLI session with `/exit`. Do not start the next milestone until this PR is merged.

## Summary and next steps

Your documentation convention and a real demonstration are now on `main`. Next, you'll [build filtering with Plan and Autopilot][next-lesson] in a fresh branch based on that merged state.

## Resources

- [Adding repository custom instructions][repository-instructions] explains repository-wide and path-scoped guidance.
- [Awesome Copilot][awesome-copilot] offers examples to review and adapt, not blindly adopt.

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[repository-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[awesome-copilot]: https://github.com/github/awesome-copilot
