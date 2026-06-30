# Skills

Skills are reusable, self-contained playbooks that Copilot (and human contributors) can follow for recurring tasks in this repo. Each skill lives in its own folder as a `SKILL.md` with `name` + `description` frontmatter; Copilot loads it automatically when a task matches the description.

This file is an **index** so a person can see what exists at a glance. It is not itself a skill (no `SKILL.md`), so it is never auto-loaded — keep it in sync when you add, rename, or remove a skill (see the PR-time consistency pass in [`build-and-verify-docs`](./build-and-verify-docs/SKILL.md)).

## Repo-specific skills

These encode conventions unique to this Astro + Starlight workshop content repo.

| Skill | What it does | Use it when |
|---|---|---|
| [`build-and-verify-docs`](./build-and-verify-docs/SKILL.md) | Canonical build/preview/verify process: dev server, clean build, page-count invariant, lychee link check, and the **PR-time consistency pass** for structural drift. | Building, previewing, or verifying any change under `docs/`; before every commit/PR. |
| [`check-content-alignment`](./check-content-alignment/SKILL.md) | Scans a diff (staged/unstaged or a branch range) for content changes, then finds other lessons that duplicate or parallel the changed prose — formerly-shared passages now copied across pages, and the same concept taught across the VS Code / CLI / App / Cloud harnesses — so duplicated copies don't drift out of sync. Reports candidate files and line ranges; does not edit content. | After editing lesson content under `docs/`, before committing/opening a PR, to find other pages that should change too. |
| [`validate-site-playwright`](./validate-site-playwright/SKILL.md) | Optional deeper **browser** QA: drives the Playwright MCP server against a local preview to confirm pages render, catch console/hydration errors, find broken images, and confirm Starlight components mounted. | A deeper render/visual pass before a PR that changes how pages render. Complements (doesn't replace) `build-and-verify-docs`. |

## General-purpose skills

Portable skills that aren't specific to this repo's content model.

| Skill | What it does | Use it when |
|---|---|---|
| [`make-repo-contribution`](./make-repo-contribution/SKILL.md) | Enforces the correct issue → branch → commit → PR workflow, including repository conventions and commit-message rules. | Filing an issue, branching, committing, pushing, or opening a PR. |
| [`publish-to-pages`](./publish-to-pages/SKILL.md) | Publishes presentations or web content (PPTX, PDF, HTML, Google Slides) to a live GitHub Pages URL. | Publishing or sharing a presentation/HTML artifact via GitHub Pages. |
| [`update-markdown-file-index`](./update-markdown-file-index/SKILL.md) | Updates a section of a Markdown file with an index/table of files from a folder. | Keeping a generated file index in a Markdown doc current. |

## Adding a skill

1. Create `.github/skills/<skill-name>/SKILL.md` with `name` and `description` frontmatter. Write the `description` so it states *what the skill does* **and** *when to trigger it* — that's how Copilot decides to load it.
2. Keep the body focused on the procedure. If the skill drives repo tooling, point at the single source of truth rather than re-documenting commands.
3. Add a row to the correct table above.
4. If the skill is structural enough to belong in the repo map, mention it in [`../copilot-instructions.md`](../copilot-instructions.md) and [`../../AUTHORING.md`](../../AUTHORING.md).
