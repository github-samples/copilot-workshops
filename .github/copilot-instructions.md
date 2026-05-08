# Agents in SDLC — Workshop Authoring Guide

This repo hosts the **workshop content** for *Agents in SDLC*, published as an Astro + Starlight site at <https://github-samples.github.io/agents-in-sdlc/>. The demo application learners build during the workshop lives in a separate repository: <https://github.com/github-samples/tailspin-toys>.

**This is a content-only repo.** Do not add Python, Flask, Svelte, Tailwind, or other application code here. Application changes belong in `tailspin-toys`.

## Repository structure

- `workshop-content/` — Source MDX for all lessons.
  - `cli/`, `vscode/`, `cloud/` — Per-path lessons (Copilot CLI / VS Code / Cloud agent).
  - `shared/` — Lesson content used by multiple paths (referenced via redirect-stub pages in the per-path folders).
  - `_partials/` — Reusable MDX fragments (see partials conventions below).
  - `images/` — Screenshots and diagrams.
  - `index.mdx` — Workshop landing page.
- `docs/` — Astro + Starlight wrapper that publishes `workshop-content/` to GitHub Pages. Don't author lessons here; this is the site shell.
- `.github/`
  - `copilot-instructions.md` — This file.
  - `instructions/` — Scoped instruction files (`applyTo` frontmatter targets specific file globs).
  - `agents/` — Custom agents available to Copilot.
  - `skills/` — Skills available to Copilot.
  - `workflows/pages.yml` — Builds and deploys the site.

## Authoring conventions

### Partials naming convention

Every file in `workshop-content/_partials/` uses a category prefix:

- `callout-*` — Short callouts (e.g., `<Aside>` blocks, warnings, tips).
- `section-*` — Multi-paragraph reusable content sections (intros, recaps, overviews).
- `exercise-*` — Self-contained hands-on steps that drop into a numbered list.

Partials must be **self-contained**: any link reference (`[label]`) used inside a partial must be defined inside that same partial. Don't rely on the importing page to provide ref definitions.

Don't extract a partial unless it's used in 2+ places (or the same place across both the CLI and VS Code paths).

### Path / shared module pattern

When the same lesson applies to multiple paths (CLI, VS Code, cloud), put the real content in `workshop-content/shared/<topic>/<lesson>.mdx` and create thin **redirect-stub** pages in each per-path folder. Stubs have a "Return to your path" footer so learners get back to their track.

See `shared/cloud-agent/cloud-agent.mdx` and the `cloud/2-cloud-agent.mdx` / `vscode/4-cloud-agent.mdx` stubs for the established pattern.

### Linking

- **Inside the workshop:** Markdown ref-style links (`[Exercise 1][exercise-1]` with `[exercise-1]: ../1-foo/` defined at the bottom).
- **External docs:** Full URLs to `docs.github.com` and other authoritative sources.
- **Cross-repo (template repo, sample code):** Full URLs to `github.com/github-samples/tailspin-toys/...`. Do **not** link to files inside *this* repo as if they were the template — `tailspin-toys` is the learner template.

### Numbered lists across partials

When a partial drops into the middle of an ordered list, the list resumes numbering automatically as long as the partial's items use plain Markdown numerals starting at `1.`. See `exercise-instructions-add-docstring.mdx` for the working pattern.

## Verification before commit

Run both checks. Don't commit if either fails.

**Build (target: 29 pages):**

```bash
cd docs && rm -rf dist && npm run build
```

**Link check (offline; catches broken cross-page links):**

```bash
mkdir -p /tmp/lychee-root && ln -sfn $PWD/docs/dist /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```

Lychee runs offline and won't catch broken external GitHub URLs. When changing absolute `https://github.com/...` links, click through manually.

## Local development

From repo root:

```bash
cd docs && npm install
ln -sfn $PWD/node_modules ../workshop-content/node_modules   # MDX outside docs/ needs to resolve @astrojs/starlight/components
npm run dev
```

The `workshop-content/node_modules` symlink mirrors what `pages.yml` does in CI. It's gitignored.

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
