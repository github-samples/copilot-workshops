---
name: build-and-verify-docs
description: Build, preview, and verify the workshop site using existing checks. Use before committing or updating a PR. Inspect affected content and translations separately rather than relying on fixed page counts.
---

# Build and verify the docs site

Lesson source lives in `docs/`; the Astro + Starlight publisher lives in `website/`. This skill owns the verification procedure. Other authoring guidance should link here instead of repeating commands.

## Run existing checks

Use the wrapper for your shell, from the repository root or by absolute script path from any directory:

```bash
bash .github/skills/build-and-verify-docs/scripts/verify.sh
```

```powershell
& ./.github/skills/build-and-verify-docs/scripts/verify.ps1
```

Use an installed Node.js/npm version supported by `website/`, existing site dependencies, and Lychee on `PATH`. Ask before installing missing software. Run PowerShell under your normal execution policy; do not bypass it. The Bash wrapper has been run on macOS; the PowerShell wrapper has not been executed or parser-validated because PowerShell was unavailable.

Both wrappers run `npm run check:all`, remove only `website/dist` (refusing a linked output directory), run `npm run build`, then run `lychee --offline --no-progress` against the built HTML. Package scripts remain the source of truth. Output is not suppressed, failures stop verification, and native command exit codes are returned. Each run creates and cleans its own temporary link root. Like the existing Pages workflow, the wrappers map `/copilot-workshops/` to the build; update that mapping alongside the workflow if the configured site base changes.

Stop on failure and resolve it before committing. The wrappers do not install dependencies, start servers, compare source text with HTML, or validate translation quality. Offline Lychee checks internal links and images, not external destinations.

## Inspect affected content

Use the diff, source paths and `slug` frontmatter, `website/src/content.config.ts`, and `website/astro.config.mjs` to select and inspect affected output. Do not use a fixed page total as proof of correctness.

- Confirm changed lessons appear at their intended routes with their titles, headings, prompts, and admonitions rendered correctly.
- Compare translated pages with their locale source and language; English fallback is expected only when a translation is absent.
- Check references and navigation after renames or removals, and confirm support assets are not published as lessons.
- Review semantic accuracy, teaching flow, translation quality, intentional harness differences, and whether navigation or redirects lead to the appropriate next task.

These inspections are not automated by the wrappers. Use the [browser validation skill][browser-validation] for layout, styling, client-side behavior, console errors, and visual image loading. Existing plain-div admonition styling is not fixed or certified by a successful build. Open changed external links separately and confirm their intended destinations. Report any blocked checks honestly.

## Local preview

```bash
(cd website && npm run dev)
```

Open the URL printed by the server, including the configured base path. Stop only the server you started when finished.

## Consistency before updating a PR

- Search for references to paths, names, or conventions changed by the diff, including repository guidance and navigation.
- Use the [content alignment skill][content-alignment] for duplicated lesson passages and translations that may need matching changes.
- Keep CI descriptions aligned with `website/package.json` and `.github/workflows/pages.yml`.

The Pages workflow remains unchanged: it runs type checks, the build, and offline link validation, with deployment restricted to pushes to `main`. Source-page inspection, browser validation, and content-alignment review remain separate.

[browser-validation]: ../validate-site-playwright/SKILL.md
[content-alignment]: ../check-content-alignment/SKILL.md
