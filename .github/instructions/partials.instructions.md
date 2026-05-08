---
description: 'Conventions for reusable MDX partials in docs/src/content/docs/_partials/'
applyTo: 'docs/src/content/docs/_partials/**'
---

# Partials Conventions

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

## No `<Aside>` imports inside callout partials

When the partial *is* a single `<Aside>`, the import for `Aside` lives in the host MDX page. The partial just contains the JSX. (Imports inside partials are allowed but the convention is to keep partials minimal.)
