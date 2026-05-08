---
description: 'Astro + Starlight site wrapper conventions'
applyTo: 'docs/**/*.{astro,mjs,ts,js}'
---

# Astro + Starlight Wrapper

`docs/` is the Astro + Starlight project that publishes the workshop to GitHub Pages. It is **not** an application; it is a thin site shell. Lesson content lives under `docs/src/content/docs/` — author there, not in the project root files.

## Site config

- Base path: `/agents-in-sdlc` (the repo's GitHub Pages slug).
- Site URL: `https://github-samples.github.io/agents-in-sdlc/`.
- **Sidebar: manually maintained** in `astro.config.mjs`. The `sidebar` array drives both the order learners see and which pages appear in navigation. New lessons must be added explicitly.
- **Content collection** lives at `src/content/docs/` (Starlight's default location). The custom `glob()` loader in `src/content.config.ts` excludes underscore-prefixed files and directories so partials (`_partials/**`) don't get routed as pages.

## Don't add app-style components

This is a docs wrapper. Don't add interactive Svelte islands, Tailwind utility-class styling layers, custom routing, or other application-style code. Anything beyond Starlight defaults should be justified.

## When changing site config

After modifying `astro.config.mjs` or anything in `docs/src/`:

```bash
cd docs && rm -rf dist && npm run build
```

Verify the page count is still **29** unless you intentionally added or removed lessons. A build that produces a different count without an MDX change is a sign of a routing or content-collection misconfiguration — most likely partials being routed as pages (check the loader's exclude pattern).
