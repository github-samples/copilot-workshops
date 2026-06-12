---
name: sync-partial-metadata
description: Regenerate the partial metadata artifacts (lint output and `docs/src/types/_shared/<name>.mdx.d.ts` declaration files that power VS Code hover tooltips) for the docs partials system. Use this skill whenever a partial under `docs/src/content/docs/_shared/` is created, edited, renamed, or removed; whenever a consumer page changes which partials it imports; or whenever an author asks an agent to "generate the partial types", "sync the partial metadata", "update the .d.ts files", or otherwise refresh the generated declaration files.
---

# Sync Partial Metadata

Regenerate the lint and TypeScript declaration artifacts that back the docs partials system in this repository.

## When to use

Trigger this skill automatically whenever **any** of the following happens:

- A file under `docs/src/content/docs/_shared/*.mdx` is created, edited (including changes to the `@summary`/`@sections` metadata block, headings, or component name), renamed, or deleted.
- A consumer `.mdx` page (anywhere under `docs/src/content/docs/`) adds, removes, or renames a `import … from '@shared/…'` line.
- An author explicitly asks for the partial types / `.mdx.d.ts` files to be (re)generated, or asks to "sync partials".

CI runs `scripts/sync_partial_metadata.py --check` and `scripts/lint_partials.py` on every PR; running this skill locally before pushing avoids CI failures.

## Process

1. **Lint first**. Run `python scripts/lint_partials.py` from the repo root. It validates:
    - partials contain no `## H2` headings (host pages own H2),
    - every partial has a metadata block whose `@sections` list matches the actual headings,
    - imports use the `@shared/` alias (not relative `../_partials/...`),
    - import bindings start with the PascalCase form of the filename prefix (`Section`, `Exercise`, `Callout`).

    Fix any reported issues in the partial or the consumer page before continuing.
2. **Sync**. Run `python scripts/sync_partial_metadata.py` from the repo root. This regenerates:
    - `docs/src/types/_shared/<name>.mdx.d.ts` for every partial (these provide JSDoc that powers VS Code hover tooltips at every `<Component />` use site),
    - migrates any stale `'../_shared/…'` imports in consumer pages to `'@shared/…'`.
3. **Verify clean state**. Run `python scripts/sync_partial_metadata.py --check`. It must exit `OK: partial metadata is in sync.` with no diff. If it reports drift, re-run step 2 and inspect what changed.
4. **Stage the regenerated files**. Include any modified files under `docs/src/types/_shared/` in the same commit as the partial change. Never hand-edit those files — they carry a `// GENERATED FILE — do not edit` header and are marked read-only in `.vscode/settings.json`.

## Expected output

- `lint_partials.py` → `OK: N partial(s), M consumer page(s).`
- `sync_partial_metadata.py` → either silent success or a list of files it (re)wrote.
- `sync_partial_metadata.py --check` → `OK: partial metadata is in sync.`

If any command exits non-zero, surface the full error to the author and do not stage the partial commit until lint and sync both pass.

## Reference

- Conventions: `.github/instructions/partials.instructions.md` (frontmatter, metadata block, naming rules, alias).
- Authoring guide: `AUTHORING.md` ("Adding a partial" section).
- Scripts:
    - `scripts/lint_partials.py`
    - `scripts/sync_partial_metadata.py`
    - `scripts/_partials_lib.py` (shared parser used by the two above)
