# Website (Astro + Starlight publisher)

Optional publishing layer that renders the workshop content as a documentation site and deploys it to GitHub Pages at <https://github-samples.github.io/copilot-workshops/>.

The lessons themselves are plain Markdown in the repo-root [`../docs/`](../docs/) directory — browsable directly on github.com with no build required. This `website/` project is only needed if you want to self-host or preview the rendered pages site. For author-focused guidance, see [`../AUTHORING.md`](../AUTHORING.md).

## Local development

From this directory:

```sh
npm install
npm run dev      # http://localhost:4321/copilot-workshops/
npm run build    # outputs to dist/
npm run preview  # preview the production build
```

## Site config

- `astro.config.mjs` — Site URL, base path, `locales` block, sidebar (manually maintained).
- `src/content.config.ts` — Content collection loader. Its `base` points at `../docs`, so lesson Markdown is sourced from the repo-root content directory. Excludes underscore-prefixed directories so support assets such as `_images/` aren't routed as pages.
- `src/components/` — Site-shell components (`.astro`). Lesson content does **not** live here.
- `src/pages/` — Standalone Astro routes outside the content collection. Currently just `shared/0-prereqs.astro`, the full-HTML redirect that forwards the legacy `/shared/0-prereqs/` URL to the home page (prerequisites are now per-harness at `/<harness>/0-prerequisites/`).

The workshop home (`/`) is generated from `../docs/README.md` (its `slug: index` frontmatter maps it to the site root), so the same file serves both GitHub's folder view and the Starlight landing page.

## Deployment

Deployed by [`../.github/workflows/pages.yml`](../.github/workflows/pages.yml) to GitHub Pages on pushes to `main`.
