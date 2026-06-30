---
description: 'Markdown and MDX conventions for repository docs, READMEs, and workshop lessons'
applyTo: '**/*.{md,mdx}'
---

# Markdown and MDX conventions

This file covers both plain Markdown (`.md`) and MDX (`.mdx`). The first sections apply to both formats; the [MDX-only conventions](#mdx-only-conventions) section at the end is specific to workshop lesson files under `docs/src/content/docs/`.

## No hard-wrapping

Do not hard-wrap paragraphs. Keep each paragraph, list item, and blockquote on a single line and let editors soft-wrap. Line breaks are reserved for actual structural breaks (between paragraphs, list items, headings, code fences, table rows, etc.).

## GitHub admonitions

Preserve GitHub admonition syntax exactly:

```markdown
> [!NOTE]
> Body text on subsequent quoted lines.

> [!TIP]
> Body text.

> [!IMPORTANT]
> Body text.

> [!WARNING]
> Body text.

> [!CAUTION]
> Body text.
```

The `[!TYPE]` marker must be on its own `>`-prefixed line, with the body on subsequent `>`-prefixed lines.

In MDX lesson content, prefer Starlight's `<Aside>` component over GitHub admonitions — see [MDX-only conventions](#mdx-only-conventions).

## Headings

- Repository docs (README, CONTRIBUTING, etc.): start with `# Title` then `##` for sections.
- Lesson MDX (`docs/src/content/docs/**/*.mdx`): no `# H1` in body — the title comes from frontmatter. Body headings start at `##`.

## Code fences

Always tag code fences with their language:

````markdown
```bash
echo "hello"
```

```python
def f(): pass
```
````

## Lists

- Unordered: `-` (not `*` or `+`).
- Ordered: `1.`, `2.`, ... — Markdown auto-numbers, but use real ordinals for readability.

## Filenames, UI elements, and literal values

Follow the [GitHub Docs style guide][github-style]. In short:

- **Backticks** for filenames, directory names, code, configuration keys, and any literal text the user types or that appears verbatim in code/config. Examples: `` `.github/agents/accessibility.md` ``, `` `package.json` ``, `` `src/server/app.py` ``, `` `Code lacks documentation` `` (a literal value the learner types into a field).
- **Bold** for UI elements the user interacts with — buttons, tabs, menu items, field labels, dialog names. Examples: `**Issues**` tab, `**New issue**` button, `**Title**` field, `**Assign to Copilot**`.
- **Bold** for emphasis on a concept on its first introduction, used sparingly.

Rule of thumb: if the reader is going to select it, it's bold; if they're going to type it, read it in the filesystem, or see it in code, it's backticks.

## Accessibility

Accessibility conventions — descriptive link text, alt text, heading hierarchy, plain language, input-agnostic action verbs (**select** not "click") — live in [`markdown-accessibility.instructions.md`](./markdown-accessibility.instructions.md).

## Keyboard shortcuts

Use `<kbd>` tags with `+` joining keys (no spaces) and spell out Mac modifiers per the [GitHub Docs style guide][github-style-keyboard]. Mac shortcut first, then Windows/Linux:

```markdown
Press <kbd>Command</kbd>+<kbd>B</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>B</kbd> (Windows/Linux).
```

Mac modifiers: spell out **Command**, **Option**, **Control** — don't use ⌘, ⌥, ⌃, Cmd, or Opt. Windows/Linux: use **Ctrl**, **Alt** (abbreviated).

## Links

- Use reference-style links. Define refs at the bottom of the file (or the bottom of the partial that owns them).
- Strip locale codes (`/en/`, `/en-us/`, etc.) from URLs so readers land in their own locale.
- For descriptive link text (no "click here"; no link-only sentences), see [`markdown-accessibility.instructions.md`](./markdown-accessibility.instructions.md).

## MDX-only conventions

The rest of this file applies only to `.mdx` files (workshop lessons under `docs/src/content/docs/`).

### Frontmatter

Every MDX page (not partial) needs frontmatter:

```yaml
---
title: "Exercise N - Lesson title"
description: "One-sentence summary (optional, used for SEO/meta)."
---
```

### Starlight components

Import from `@astrojs/starlight/components`. Prefer `<Aside>` over GitHub admonitions in lesson body content:

```mdx
import { Aside } from '@astrojs/starlight/components';

<Aside type="note">A note.</Aside>
<Aside type="tip">A helpful tip.</Aside>
<Aside type="caution">Something to watch out for.</Aside>
<Aside type="danger">Don't do this.</Aside>
```

When the same callout repeats across lessons, extract it to a `callout-*.mdx` partial instead of duplicating the `<Aside>`.

### Importing partials

Use the `@shared/` alias (not relative paths):

```mdx
import CalloutStartCopilotCliAllowAll from '@shared/callout-start-copilot-cli-allow-all.mdx';
import ExerciseAddDocstring from '@shared/exercise-instructions-add-docstring.mdx';

<CalloutStartCopilotCliAllowAll />

<ExerciseAddDocstring />
```

Keep imports grouped at the top of the file under the frontmatter. Binding names follow PascalCase and start with the partial's category prefix (`Section…`, `Exercise…`, `Callout…`).

See [`partials.instructions.md`](./partials.instructions.md) for the full partials authoring guide.

### Numbered lists across partials

When dropping an exercise partial into a numbered list, write the partial's items as plain Markdown numerals starting at `1.`. The host page's list resumes correctly. Don't try to manually continue numbering inside the partial.

### Images

Use Markdown image syntax with paths relative to the MDX file:

```mdx
![Alt text describing the image](../_images/some-screenshot.png)
```

For an image referenced from a `_shared/` partial, use the same `../_images/...` relative path — `_shared/` sits one level under `docs/src/content/docs/`, just like `cli/`, `vscode/`, `cloud/`, and `app/`, so the path resolves identically for the partial and its consumer pages.

### Path conventions

- Per-path lessons: `cli/`, `vscode/`, `cloud/`, `app/`. Files numbered by lesson order: `1-installing.mdx`, `2-custom-instructions.mdx`, etc.
- Shared content: reusable fragments live in `_shared/` (e.g. `section-mcp-overview.mdx`) and are imported into lesson pages via the `@shared/` alias. They are body-only partials inlined at build time, not standalone routed pages — see [`partials.instructions.md`](./partials.instructions.md).

### Cross-repo links

The learner's template repo is `github.com/github-samples/tailspin-toys`. Never link to files inside *this* repo as if they were the template — those paths don't exist here anymore.

[github-style]: https://docs.github.com/contributing/style-guide-and-content-model/style-guide
[github-style-keyboard]: https://docs.github.com/contributing/style-guide-and-content-model/style-guide#keyboard-shortcuts
