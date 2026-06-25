# Agents in SDLC — Workshop Authoring Guide

This repo hosts the **workshop content** for *Agents in SDLC*, published as an Astro + Starlight site at <https://github-samples.github.io/agents-in-sdlc/>. The demo application learners build during the workshop lives in a separate repository: <https://github.com/github-samples/tailspin-toys>.

**This is a content-only repo.** Do not add Python, Flask, Svelte, Tailwind, or other application code here. Application changes belong in `tailspin-toys`.

## Repository structure

- `docs/` — Astro + Starlight site that publishes the workshop to GitHub Pages.
  - `src/content/docs/` — **Source MDX for all lessons. Edit here.**
    - `index.mdx` — Workshop landing page.
    - `prereqs.mdx` — Shared setup lesson (Exercise 0).
    - `cli/`, `vscode/`, `cloud/` — Per-path lessons (Copilot CLI / VS Code / Cloud agent).
    - `_shared/` — Reusable MDX fragments imported via the `@shared/*` alias (see partials conventions below). Underscore-prefixed dirs are excluded from routing.
    - `_images/` — Screenshots and diagrams.
  - `astro.config.mjs` — Site config including the manually maintained sidebar and a redirect from the legacy `/shared/0-prereqs/` URL to `/prereqs/`.
- `scripts/` — Author tooling for the partials system (`lint_partials.py`, `sync_partial_metadata.py`, `_partials_lib.py`).
- `AUTHORING.md` — Author entry point (recipes for adding lessons, partials, images).
- `CONTRIBUTING.md` — Short pointer to AUTHORING.md + PR/CI rules.
- `.github/`
  - `copilot-instructions.md` — This file.
  - `instructions/` — Scoped instruction files (`applyTo` frontmatter targets specific file globs).
  - `agents/` — Custom agents available to Copilot.
  - `skills/` — Skills available to Copilot (see [`skills/README.md`](skills/README.md) for the index of what each one does).
  - `workflows/pages.yml` — Builds and deploys the site.

## Authoring conventions

### Partials naming convention

Every file in `docs/src/content/docs/_shared/` uses a category prefix:

- `callout-*` — Short callouts (e.g., `<Aside>` blocks, warnings, tips).
- `section-*` — Multi-paragraph reusable content sections (intros, recaps, overviews).
- `exercise-*` — Self-contained hands-on steps that drop into a numbered list.

Import partials via the `@shared/*` alias and bind them to a name starting with the PascalCase form of the prefix (`Callout…`, `Section…`, `Exercise…`):

```mdx
import SectionMcpOverview from '@shared/section-mcp-overview.mdx';

<SectionMcpOverview />
```

Partials must be **self-contained**: any link reference (`[label]`) used inside a partial must be defined inside that same partial. Don't rely on the importing page to provide ref definitions.

Don't extract a partial unless it's used in 2+ places (or the same place across both the CLI and VS Code paths).

### Reusing a lesson across paths

When the same prose applies to multiple paths (CLI, VS Code, cloud), pull the body into a `section-…` partial under `_shared/` and `import` it from each per-path lesson. The host page owns frontmatter, H2s, and prev/next nav; the partial owns the reusable prose.

### Linking

- **Inside the workshop:** Markdown ref-style links (`[Exercise 1][exercise-1]` with `[exercise-1]: ../1-foo/` defined at the bottom).
- **External docs:** Full URLs to `docs.github.com` and other authoritative sources.
- **Cross-repo (template repo, sample code):** Full URLs to `github.com/github-samples/tailspin-toys/...`. Do **not** link to files inside *this* repo as if they were the template — `tailspin-toys` is the learner template.

### Numbered lists across partials

When a partial drops into the middle of an ordered list, the list resumes numbering automatically as long as the partial's items use plain Markdown numerals starting at `1.`. See `exercise-instructions-add-docstring.mdx` for the working pattern.

## Building, previewing, and verifying

The tooling for building, previewing, and verifying the site — dev server, clean build, the page-count invariant, the lychee link check, and the local partial guardrails — lives in the [`build-and-verify-docs`](skills/build-and-verify-docs/SKILL.md) skill. Run that verification sequence before every commit, and don't commit if any step fails.

Before opening or updating a PR, also make the **PR-time consistency pass** documented in that skill — a structural-drift sweep (renamed paths, stale skill/instruction references, CI claims, repository-structure trees) that the build and link check can't catch.

## Commit hygiene

- Conventional commit prefixes preferred (`docs:`, `chore:`, `fix:`).
- Always include the trailer:
  ```
  Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
  ```

## Things NOT to do here

- Don't add Python, Flask, SQLAlchemy, Svelte, Astro components, Tailwind classes, or any other application code. That belongs in `github-samples/tailspin-toys`.
- Don't author against `client/` or `server/` paths — they were removed when the app was extracted.
- Don't generate summary markdown files at the end of a task.
- Don't add `mkdocs.yml` or other parallel docs tooling — Astro + Starlight is the site.
