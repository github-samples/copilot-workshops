---
description: 'Conventions for reusable MDX partials in docs/src/content/docs/_shared/'
applyTo: 'docs/src/content/docs/_shared/**'
---

# Partials Conventions

## Heading levels (host owns H2)

Partials must contain only `### H3` and below. The host page owns every `## H2`.

- This keeps the use site descriptive: a reader scanning the host page sees what the partial is *about* before opening the partial body.
- It also keeps two consumer pages free to introduce the same partial under different H2 wording when context calls for it.
- `scripts/lint_partials.py` rejects any `^## ` line in a partial body.

```mdx
{/* host page (cli/2-custom-instructions.mdx) */}
## Instruction files

<SectionInstructionsOverview />
```

```mdx
{/* partial (section-instructions-overview.mdx) */}
### Scenario

…
```

## Single purpose (concept *or* exercise)

Each partial is either:

- a **concept section** (multi-paragraph explanation) — filename starts with `section-`,
- a **hands-on exercise** (numbered steps) — filename starts with `exercise-`,
- or a **standalone callout** (a single `<Aside>` or short note) — filename starts with `callout-`.

Don't mix. If a partial has both explanatory prose and numbered steps, split it into a `section-…` partial and an `exercise-…` partial. Each one then drops cleanly under its own host-page H2.

## Component naming (matches the filename prefix)

Always import a partial under a binding that begins with the PascalCase form of its filename prefix. The use site then signals intent at a glance:

```mdx
import SectionInstructionsOverview from '@shared/section-instructions-overview.mdx';
import ExerciseExploreInstructionsFiles from '@shared/exercise-explore-instructions-files.mdx';
import CalloutStartCopilotCliAllowAll from '@shared/callout-start-copilot-cli-allow-all.mdx';

<SectionInstructionsOverview />
<ExerciseExploreInstructionsFiles />
<CalloutStartCopilotCliAllowAll />
```

`scripts/lint_partials.py` rejects imports of `@shared/<prefix>-foo.mdx` whose binding doesn't start with `Section`, `Exercise`, or `Callout` to match.

## Metadata block (required)

Every partial **must** begin with an MDX comment block that documents what it contains. Authors who consume the partial rely on this metadata — both directly when editing the partial, and indirectly via tooltips at every use site (see "Editor tooltips" below).

```mdx
{/*
@summary One sentence describing what the partial drops into the host page.
@sections
  - H3 First heading the partial introduces
  - H3 Second heading
  - H4 Subheading under the second
*/}
```

Rules:

- The block is the **first non-blank line** of the file, before any `import`.
- `@summary` is a single sentence, max ~200 characters. It populates the JSDoc tooltip on every `<Component />` use site.
- `@sections` lists every `###` and deeper heading the partial introduces into the host page, in document order. Each entry is `- H<level> <heading text>` (e.g., `- H3 Custom instructions`). It may be empty if the partial has no headings (callouts and short single-purpose exercises typically do). **Partials must not contain H2** — see "Heading levels" above.
- Update this block whenever you meaningfully change the partial's content or headings. `scripts/lint_partials.py` fails when `@sections` doesn't match the actual headings, and `scripts/sync_partial_metadata.py --check` fails when the generated `.mdx.d.ts` files are stale — run both locally before committing.
- Starlight strips MDX `{/* */}` comments from rendered output, so the block is invisible to readers.

## Editor tooltips (`docs/src/types/_shared/<name>.mdx.d.ts`)

Every partial has a **generated** TypeScript declaration file in `docs/src/types/_shared/`. Hovering a `<Component />` use site (or the imported identifier) in any consumer `.mdx` shows the JSDoc — the partial's `@summary` and `@sections` — as a tooltip.

- These files are **regenerated** by `scripts/sync_partial_metadata.py` from each partial's metadata. Never edit them by hand — the file header says `// GENERATED FILE — do not edit` and `.vscode/settings.json` marks them read-only.
- Tooltips work in any editor that uses the workspace's TypeScript server. The repo wires this up two ways: `.vscode/extensions.json` recommends `unifiedjs.vscode-mdx`, and `docs/tsconfig.json` registers `@mdx-js/typescript-plugin` and sets `allowArbitraryExtensions: true` so TS treats `<name>.mdx.d.ts` as the declaration for `<name>.mdx`.

## Importing partials (use the `@shared/` alias)

Always import partials via the `@shared/` path alias, not a relative path:

```mdx
import InstructionsOverview from '@shared/section-instructions-overview.mdx';
```

The alias is configured in `docs/tsconfig.json`. TypeScript resolves it against `docs/src/types/_shared/` first (so it sees the JSDoc-bearing `.mdx.d.ts`), then falls through to `docs/src/content/docs/_shared/` for the real `.mdx` (which is what Vite/Astro inlines at build time). `scripts/lint_partials.py` flags any remaining `'../_shared/...'` import; `scripts/sync_partial_metadata.py` will migrate them automatically.

## Naming prefix

Every partial's filename uses a category prefix:

- `callout-*` — Short callouts (single `<Aside>` or short note).
- `section-*` — Multi-paragraph reusable content (intros, recaps, overviews).
- `exercise-*` — Self-contained hands-on steps that drop into a numbered list on the host page.

## When to extract

Extract a partial when the same content appears in **2+ places** (e.g., the same callout in both the CLI and VS Code paths). Don't extract single-use content; inline it.

A reasonable threshold: the duplicated block is at least 5 lines, or contains a non-trivial code sample.

## Self-contained links

Any link reference (`[label]`) used inside a partial **must** be defined inside that same partial, at the bottom:

```mdx
See the [Copilot CLI docs][cli-docs] for details.

[cli-docs]: https://docs.github.com/en/copilot/github-copilot-in-the-cli
```

Don't rely on the host page to provide ref definitions. A partial with undefined refs breaks the moment it's reused.

## No frontmatter

Partials are body-only — no `---` frontmatter block. The host page's frontmatter applies.

## Numbered list compatibility

If a partial drops into the middle of a numbered list, write its items as plain Markdown numerals starting at `1.`. The host page's list resumes numbering automatically.

```mdx
1. First step inside the partial.
1. Second step.
1. Third step.
```

## Imports inside callout partials

Callout partials should be **self-contained**: import any Starlight component they use (typically `Aside`) at the top of the partial itself, rather than expecting the host page to provide the import. This matches how every existing `callout-*.mdx` is written and means a host page can drop in a callout partial without remembering to also add an `import { Aside } ...` line.

```mdx
import { Aside } from '@astrojs/starlight/components';

<Aside type="tip" title="Start a Copilot CLI session">
  …
</Aside>
```
