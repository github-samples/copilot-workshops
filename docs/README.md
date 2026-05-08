# Docs site (Astro + Starlight)

Site shell that publishes the workshop content from [`../workshop-content/`](../workshop-content/) to GitHub Pages at <https://github-samples.github.io/agents-in-sdlc/>.

This project is a **thin wrapper** — lesson authoring happens in `../workshop-content/`, not here.

## Authoring

Edit the `.mdx` files under `../workshop-content/`. The dev server picks up changes automatically.

Reusable content:

- **Prose partials** — files in `../workshop-content/_partials/` (prefixes: `callout-*`, `section-*`, `exercise-*`). Imported into lesson pages as MDX components.
- **Typed callouts and prereqs** — `.astro` components in `src/components/`. Imported via the `@components/*` alias.

See [`../.github/instructions/astro.instructions.md`](../.github/instructions/astro.instructions.md) and [`../.github/copilot-instructions.md`](../.github/copilot-instructions.md) for conventions.

## Local development

From this directory:

```sh
npm install
ln -sfn $PWD/node_modules ../workshop-content/node_modules   # so MDX outside docs/ resolves Starlight imports
npm run dev      # http://localhost:4321/agents-in-sdlc/
npm run build    # outputs to dist/
npm run preview  # preview the production build
```

The `workshop-content/node_modules` symlink mirrors what `pages.yml` does in CI.

## Deployment

Deployed by [`../.github/workflows/pages.yml`](../.github/workflows/pages.yml) to GitHub Pages on pushes to `main`.
