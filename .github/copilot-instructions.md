# Copilot Workshops — Workshop Authoring Guide

This repo hosts the **workshop content** for **Copilot Workshops**, published as an Astro + Starlight site at <https://github-samples.github.io/copilot-workshops/>. The demo application learners build during the workshop lives in a separate repository: <https://github.com/github-samples/tailspin-toys>.

**This is a content-only repo.** Do not add the demo app's application code (Astro SSR endpoints, the Drizzle data layer, UI components, Tailwind styles, or tests) here. Application changes belong in `tailspin-toys`.

## Repository structure

- `docs/` — **Source Markdown for all lessons. Edit here.** Browsable directly on github.com; no build required.
  - `README.md` — Workshop landing page (also the site home via `slug: index` frontmatter).
  - `cli/`, `vscode/`, `cloud/`, `app/` — Per-harness lessons (Copilot CLI / VS Code / Cloud agent / GitHub Copilot app). Each folder's landing page is a `README.md` (routed via a `slug:` matching the folder path). Each harness opens with its own `0-prerequisites.md` setup lesson; the CLI and VS Code harnesses set up a codespace, while the app and cloud harnesses cover the setup their flow needs (for the app, installing Node.js locally and creating the project from the template).
  - `es-es/`, `ja-jp/`, `ko-kr/`, `pt-br/`, `zh-cn/` — Localized content at the locale-root paths required by Starlight. Translated pages mirror the English path beneath each locale directory; untranslated pages use Starlight's English fallback.
  - `_images/` — Screenshots and diagrams (shared across all locales).
- `website/` — Optional Astro + Starlight site that publishes `docs/` to GitHub Pages (loader `base: '../docs'`). Only needed to self-host or preview the rendered site.
  - `astro.config.mjs` — Site config including the manually maintained sidebar and the `locales` block. The legacy `/shared/0-prereqs/` → home (`/`) redirect is a full-HTML redirect page at `src/pages/shared/0-prereqs.astro` (not an `astro.config.mjs` `redirects` entry, which would emit a stub with no `<html>` element that Pagefind can't index). Prerequisites are now per-harness (`/<harness>/0-prerequisites/`), so the old shared-prereqs URL forwards to the home page.
  - `src/content.config.ts` — Custom content loader (`base: '../docs'`) that excludes underscore-prefixed support directories so `_images/` is not routed as content.
- `AUTHORING.md` — Author entry point (recipes for adding lessons and images).
- `CONTRIBUTING.md` — Short pointer to AUTHORING.md + PR/CI rules.
- `.github/`
  - `copilot-instructions.md` — This file.
  - `instructions/` — Scoped instruction files (`applyTo` frontmatter targets specific file globs).
  - `agents/` — Custom agents available to Copilot.
  - `skills/` — Skills available to Copilot (see [`skills/README.md`](skills/README.md) for the index of what each one does).
  - `workflows/pages.yml` — Builds and deploys the site.
  - `workflows/content-alignment.md` — Agentic workflow that checks PRs for duplicated content needing aligned updates.

## Authoring conventions

### Reusing prose across paths

When the same prose applies to multiple harnesses (CLI, VS Code, cloud), copy it inline into each per-harness `.md` lesson. There is no import-based shared content system; the host page owns frontmatter, headings, navigation, and body prose.

Because inline copies can drift, run the `check-content-alignment` skill after editing duplicated sections. The `.github/workflows/content-alignment.md` agentic workflow performs the same analysis on PRs as a safety net, but do not rely on it as a substitute for updating all affected lessons.

### Admonitions

- **Use GitHub admonition syntax everywhere** — published lessons *and* repository Markdown. Put the `[!NOTE]` / `[!TIP]` / `[!IMPORTANT]` / `[!WARNING]` / `[!CAUTION]` marker on its own `>`-prefixed line, with the body on subsequent `>`-prefixed lines.
- In published lessons under `docs/**`, the `remark-github-admonitions-to-directives` plugin (wired in `website/astro.config.mjs`) converts these to Starlight asides at build time (NOTE/IMPORTANT to note, TIP to tip, WARNING/CAUTION to caution). Do **not** author Starlight `:::` directives.
- GitHub syntax has no custom-title or nesting form: put a callout heading on a **bold lead-in line** (`> **Title**`, then a blank `>` line, then the body), and emit "nested" callouts as sibling blockquotes separated by a blank line. Full mapping and patterns live in [`.github/instructions/markdown.instructions.md`](instructions/markdown.instructions.md).

### Linking

- **Inside the workshop:** Markdown ref-style links (`[Exercise 1][exercise-1]` with `[exercise-1]: ../1-foo/` defined at the bottom).
- **External docs:** Full URLs to `docs.github.com` and other authoritative sources.
- **Cross-repo (template repo, sample code):** Full URLs to `github.com/github-samples/tailspin-toys/...`. Do **not** link to files inside *this* repo as if they were the template — `tailspin-toys` is the learner template.

## Building, previewing, and verifying

The tooling for building, previewing, and verifying the site — dev server, clean build, the page-count invariant, and the lychee link check — lives in the [`build-and-verify-docs`](skills/build-and-verify-docs/SKILL.md) skill. Run that verification sequence before every commit, and don't commit if any step fails.

Before opening or updating a PR, also make the **PR-time consistency pass** documented in that skill — a structural-drift sweep (renamed paths, stale skill/instruction references, CI claims, repository-structure trees, and copied prose alignment) that the build and link check can't catch.

## Commit hygiene

- Conventional commit prefixes preferred (`docs:`, `chore:`, `fix:`).
- Always include the trailer:
  ```
  Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
  ```

## Things NOT to do here

- Don't add the demo app's application code — Astro SSR endpoints, the Drizzle data layer, `.astro` UI components, Tailwind classes, or Vitest/Playwright tests. That belongs in `github-samples/tailspin-toys`.
- Don't author against application source paths — the demo app is a single Astro project that lives in `tailspin-toys`, not here.
- Don't generate summary markdown files at the end of a task.
- Don't add `mkdocs.yml` or other parallel docs tooling — Astro + Starlight is the site.
