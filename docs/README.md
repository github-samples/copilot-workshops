# Docs site (Astro + Starlight)

Source for the published workshop site at <https://github-samples.github.io/agents-in-sdlc/>.

This is a **separate** Astro project from `client/`. `client/` is the Tailspin Toys
crowdfunding application that learners build during the workshop. This project (`docs/`)
is the workshop site itself.

## Authoring

Workshop content lives in `../workshop-content/` at the repo root. Edit the `.mdx`
files there. The dev server here picks up changes automatically.

Reusable content:

- **Prose partials** — `_*.mdx` files in `../workshop-content/_partials/`. Imported into
  pages as MDX components.
- **Typed callouts and prereqs** — `.astro` components in `src/components/`. Imported
  via the `@components/*` alias.

## Local development

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs to dist/
npm run preview  # preview the production build
```

## Deployment

Deployed by `.github/workflows/pages.yml` to GitHub Pages on pushes to `main`.
