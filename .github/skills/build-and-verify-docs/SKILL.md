---
name: build-and-verify-docs
description: Build, preview, and verify the Agents in SDLC Astro + Starlight workshop site before committing or opening a PR. Use whenever an author or agent is about to build the site, run a local preview/dev server, check links with lychee, confirm the page-count invariant, run the pre-commit verification sequence for any change under `docs/`, or make a PR-time consistency pass to catch structural drift (renamed paths, stale skill/instruction references, inaccurate CI claims, out-of-date structure trees).
---

# Build and verify the docs site

The workshop is an Astro + Starlight site under `docs/`. This skill is the single source of truth for **how to build, preview, and verify** that site. The instruction files (`.github/instructions/*`, `.github/copilot-instructions.md`) describe *what content should look like*; this skill describes *how to run the tooling*.

Run every command from the **repo root** unless a step says otherwise.

## When to use

Trigger this skill whenever you:

- are about to build the site (`npm run build`) or start the dev server,
- need to preview content locally,
- are running the pre-commit / pre-PR verification pass on any change under `docs/`,
- want to confirm the page-count invariant or check links,
- are about to open or update a PR that touches `docs/`.

For an optional **deeper, browser-based** pass that confirms pages actually render (console errors, broken images, mounted components), use the [`validate-site-playwright`](../validate-site-playwright/SKILL.md) skill after the static checks here.

## Local preview

The Astro dev server is the primary preview surface (hot reload):

```bash
cd docs && npm install && npm run dev
```

Open <http://localhost:4321/agents-in-sdlc/>. Content lives inside `docs/src/content/docs/`, so packages resolve natively — no symlinks required for preview.

## Verification sequence (run before every commit)

Run all three. Don't commit if any fails.

### 1. Build (clean)

```bash
cd docs && rm -rf dist && npm run build
```

### 2. Page-count invariant

The built page count should equal the 36 routable `.md` files under `docs/src/content/docs/` plus the one legacy redirect (`/shared/0-prereqs/`, authored as a full-HTML redirect page at `docs/src/pages/shared/0-prereqs.astro`). The expected count is 37 `index.html` files when excluding the 404 page. Astro reports 38 HTML files because it includes the 404 page.

```bash
# routable Markdown pages (expected pages, minus the redirect)
find docs/src/content/docs -name '*.md' | wc -l
# built pages (excludes the 404)
find docs/dist -name index.html | grep -v 404 | wc -l
```

`built pages` should equal `routable Markdown pages + 1`. If the build emits **more** pages than that without a matching `.md` change, check the underscore-directory exclude in `docs/src/content.config.ts`; it is still needed so support directories such as `_images/` are not routed as pages.

### 3. Link check (lychee, offline)

The site builds with `base=/agents-in-sdlc/`, so internal hrefs are absolute (`/agents-in-sdlc/foo/`). Symlink that prefix to `docs/dist` so lychee can follow internal links:

```bash
mkdir -p /tmp/lychee-root && ln -sfn "$PWD/docs/dist" /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```

Lychee runs offline and won't catch broken **external** GitHub URLs. When you change absolute `https://github.com/...` links, click through them manually.

## What CI enforces vs. what is local-only

`.github/workflows/pages.yml` runs on PRs and on push to `main`. It runs **only**:

1. `npm ci`
2. `npm run build` (Astro build) — must succeed
3. lychee offline link check against `docs/dist/` — must pass

After a push to `main`, `pages.yml` deploys `docs/dist` to GitHub Pages. Browser validation and content-alignment analysis are separate optional/safety-net workflows, not part of the Pages build job.

## PR-time consistency pass

The build and link check above catch *mechanical* breakage. They do **not** catch *structural drift* — prose and reference material that silently falls out of sync when files move or conventions change. Before opening or updating a PR, make a consistency pass over everything your change touched:

- **Renamed or moved a file or folder?** Grep the whole repo for the old path and update every hit — `.md`, instruction files, skills, and the repository-structure trees in `README.md`, `docs/README.md`, `AUTHORING.md`, and `.github/copilot-instructions.md`. Example: when `images/` became `_images/`, every `../images/...` reference and every structure tree had to change.
- **Added or removed a skill, agent, instruction file, or workflow?** Grep for references to the old name and remove them. Add a new `.github/instructions/*.instructions.md` file to the **Deeper conventions** list in `AUTHORING.md`, and to the structure block in `.github/copilot-instructions.md` if it's structural.
- **Changed duplicated lesson prose?** Run the `check-content-alignment` skill to identify other inline copies that need the same update. The `.github/workflows/content-alignment.md` agentic workflow runs the same analysis on PRs as a safety net.
- **Described what CI does anywhere?** Confirm it matches `.github/workflows/pages.yml`, which runs the build and the lychee link check.
- **Changed the build or verify steps?** This skill is the single source of truth. `README.md`, `AUTHORING.md`, and `CONTRIBUTING.md` should *point here*, not re-document the commands. Keep any summary in those files consistent with this skill.
- **Repository-structure trees** in `README.md`, `docs/README.md`, `AUTHORING.md`, and `.github/copilot-instructions.md` should all reflect the real tree. If you add or rename a top-level content directory, update all four.
- **Page-count invariant** (section 2 above) should still hold after the build.

When in doubt, `grep -rn "<old-name>" --include='*.md' .` (excluding `node_modules` and `docs/dist`) is the fastest way to surface stale references.

## Quick reference

```bash
# from repo root
cd docs && rm -rf dist && npm run build && cd ..
mkdir -p /tmp/lychee-root && ln -sfn "$PWD/docs/dist" /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```
