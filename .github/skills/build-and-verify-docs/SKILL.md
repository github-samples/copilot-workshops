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

For the partial-specific lint + `.mdx.d.ts` regeneration on its own, use the [`sync-partial-metadata`](../sync-partial-metadata/SKILL.md) skill; it is also included as step 4 of the verification sequence below.

For an optional **deeper, browser-based** pass that confirms pages actually render (console errors, broken images, mounted components), use the [`validate-site-playwright`](../validate-site-playwright/SKILL.md) skill after the static checks here.

## Local preview

The Astro dev server is the primary preview surface (hot reload):

```bash
cd docs && npm install && npm run dev
```

Open <http://localhost:4321/agents-in-sdlc/>. Content lives inside `docs/src/content/docs/`, so packages resolve natively — no symlinks required for preview.

## Verification sequence (run before every commit)

Run all four. Don't commit if any fails.

### 1. Build (clean)

```bash
cd docs && rm -rf dist && npm run build
```

### 2. Page-count invariant

The built page count should equal the number of routable `.mdx` files — everything under `docs/src/content/docs/` **except** `_shared/` — plus the one legacy redirect (`/shared/0-prereqs/`, authored as a full-HTML redirect page at `docs/src/pages/shared/0-prereqs.astro`). You never hard-code the number; you confirm the relationship:

```bash
# routable .mdx (expected pages, minus the redirect)
find docs/src/content/docs -name '*.mdx' -not -path '*/_shared/*' | wc -l
# built pages (excludes the 404)
find docs/dist -name index.html | grep -v 404 | wc -l
```

`built pages` should equal `routable .mdx + 1`. If the build emits **more** pages than that without a matching `.mdx` change, a `_shared/` partial is most likely being routed as a page — check the underscore-directory exclude in `docs/src/content.config.ts`.

### 3. Link check (lychee, offline)

The site builds with `base=/agents-in-sdlc/`, so internal hrefs are absolute (`/agents-in-sdlc/foo/`). Symlink that prefix to `docs/dist` so lychee can follow internal links:

```bash
mkdir -p /tmp/lychee-root && ln -sfn "$PWD/docs/dist" /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```

Lychee runs offline and won't catch broken **external** GitHub URLs. When you change absolute `https://github.com/...` links, click through them manually.

### 4. Partial guardrails (local-only)

```bash
python scripts/lint_partials.py
python scripts/sync_partial_metadata.py --check
```

`lint_partials.py` validates partial heading levels, metadata blocks, the `@shared/` alias, and binding-name prefixes. `sync_partial_metadata.py --check` confirms the generated `docs/src/types/_shared/<name>.mdx.d.ts` files are in sync. If the latter reports drift, run `python scripts/sync_partial_metadata.py` (no `--check`) to regenerate, then stage the updated `.d.ts` files alongside the partial change. See the [`sync-partial-metadata`](../sync-partial-metadata/SKILL.md) skill for detail.

## What CI enforces vs. what is local-only

`.github/workflows/pages.yml` runs on PRs and on push to `main`. It runs **only**:

1. `npm ci`
2. `npm run build` (Astro build) — must succeed
3. lychee offline link check against `docs/dist/` — must pass

It does **not** run `lint_partials.py` or `sync_partial_metadata.py --check`, and `npm run build` does not chain them. The partial guardrails (step 4 above) are **local checks you must run yourself** — otherwise stale `.mdx.d.ts` tooltips or `@shared/` alias drift can merge unnoticed. After a push to `main`, `pages.yml` deploys `docs/dist` to GitHub Pages.

## PR-time consistency pass

The build, link check, and partial guardrails above catch *mechanical* breakage. They do **not** catch *structural drift* — prose and reference material that silently falls out of sync when files move or conventions change. Before opening or updating a PR, make a consistency pass over everything your change touched:

- **Renamed or moved a file or folder?** Grep the whole repo for the old path and update every hit — `.md`, `.mdx`, instruction files, skills, and the repository-structure trees in `README.md`, `docs/README.md`, `AUTHORING.md`, and `.github/copilot-instructions.md`. Example: when `images/` became `_images/`, every `../images/...` reference and every structure tree had to change.
- **Added or removed a skill, agent, or instruction file?** Grep for references to the old name and remove them. Add a new `.github/instructions/*.instructions.md` file to the **Deeper conventions** list in `AUTHORING.md`, and to the structure block in `.github/copilot-instructions.md` if it's structural.
- **Described what CI does anywhere?** Confirm it matches `.github/workflows/pages.yml`, which runs **only** the build and the lychee link check. The partial guardrails are local-only — never describe them as CI checks or as "rejecting PRs."
- **Changed the build or verify steps?** This skill is the single source of truth. `README.md`, `AUTHORING.md`, and `CONTRIBUTING.md` should *point here*, not re-document the commands. Keep any summary in those files consistent with this skill.
- **Repository-structure trees** in `README.md`, `docs/README.md`, `AUTHORING.md`, and `.github/copilot-instructions.md` should all reflect the real tree. If you add or rename a top-level content directory, update all four.
- **Page-count invariant** (section 2 above) should still hold after the build.

When in doubt, `grep -rn "<old-name>" --include='*.md' --include='*.mdx' .` (excluding `node_modules` and `docs/dist`) is the fastest way to surface stale references.

## Quick reference

```bash
# from repo root
cd docs && rm -rf dist && npm run build && cd ..
mkdir -p /tmp/lychee-root && ln -sfn "$PWD/docs/dist" /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
python scripts/lint_partials.py && python scripts/sync_partial_metadata.py --check
```
