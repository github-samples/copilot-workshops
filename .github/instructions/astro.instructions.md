---
description: 'Astro + Starlight site wrapper conventions'
applyTo: 'docs/**/*.{astro,mjs,ts,js}'
---

# Astro + Starlight Wrapper

`docs/` is the Astro + Starlight project that publishes `workshop-content/` to GitHub Pages. It is **not** an application; it is a thin site shell. Do not author lesson content here — author it in `workshop-content/`.

## Site config

- Base path: `/agents-in-sdlc` (the repo's GitHub Pages slug).
- Site URL: `https://github-samples.github.io/agents-in-sdlc/`.
- Sidebar: auto-generated from `workshop-content/` directory structure. Don't hand-maintain a sidebar config unless you need to override ordering.
- Content collection sources `workshop-content/` (outside `docs/src/`); Starlight is configured to resolve MDX and partials from that path.

## Local resolution of MDX outside docs/

MDX files under `workshop-content/` import from `@astrojs/starlight/components`. Those imports resolve only if `workshop-content/node_modules` exists. The `pages.yml` workflow creates a symlink during build; locally, do the same:

```bash
cd docs && npm install
ln -sfn $PWD/node_modules ../workshop-content/node_modules
```

The symlink is gitignored.

## Don't add app-style components

This is a docs wrapper. Don't add interactive Svelte islands, Tailwind utility-class styling layers, custom routing, or other application-style code. Anything beyond Starlight defaults should be justified.

## When changing site config

After modifying `astro.config.mjs` or anything in `docs/src/`:

```bash
cd docs && rm -rf dist && npm run build
```

Verify the page count is still **29** unless you intentionally added or removed lessons. A build that produces a different count without an MDX change is a sign of a routing or content-collection misconfiguration.
