# Docs site (Astro + Starlight)

Site shell that publishes the workshop content to GitHub Pages at <https://github-samples.github.io/agents-in-sdlc/>.

Lesson MDX lives in `src/content/docs/` (the standard Starlight content collection location). For author-focused guidance, see [`../AUTHORING.md`](../AUTHORING.md).

## Local development

From this directory:

```sh
npm install
npm run dev      # http://localhost:4321/agents-in-sdlc/
npm run build    # outputs to dist/
npm run preview  # preview the production build
```

## Site config

- `astro.config.mjs` — Site URL, base path, sidebar (manually maintained).
- `src/content.config.ts` — Content collection loader. Excludes `_partials/**` from routing so partials aren't published as pages.
- `src/components/` — Site-shell components (`.astro`). Lesson content does **not** live here.

## Deployment

Deployed by [`../.github/workflows/pages.yml`](../.github/workflows/pages.yml) to GitHub Pages on pushes to `main`.
