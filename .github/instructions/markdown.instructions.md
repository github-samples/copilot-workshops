---
description: 'Markdown conventions for repository docs, READMEs, and workshop lessons'
applyTo: '**/*.md'
---

# Markdown conventions

This file covers Markdown authoring across the repo. Published lesson content under `docs/**` is plain `.md`; repository docs and instruction files are also Markdown but are read primarily on github.com. **Use GitHub admonition syntax (`> [!NOTE]`) everywhere** — see below.

## No hard-wrapping

Do not hard-wrap paragraphs. Keep each paragraph, list item, and blockquote on a single line and let editors soft-wrap. Line breaks are reserved for actual structural breaks (between paragraphs, list items, headings, code fences, table rows, etc.).

## Admonitions

Use **GitHub admonition syntax** for every callout in the repo — in published lesson content *and* in repository docs. The `[!TYPE]` marker goes on its own `>`-prefixed line, with the body on subsequent `>`-prefixed lines:

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

The five GitHub admonition types are `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, and `CAUTION`. On github.com they render natively. In published lesson content under `docs/**`, a remark plugin (`remark-github-admonitions-to-directives`, wired in `website/astro.config.mjs`) converts them to Starlight asides at build time using this mapping:

| GitHub type | Starlight aside |
| ----------- | --------------- |
| `NOTE`      | note            |
| `TIP`       | tip             |
| `IMPORTANT` | note            |
| `WARNING`   | caution         |
| `CAUTION`   | caution         |

Do **not** use Starlight `:::` aside directives anywhere — author only GitHub admonitions and let the plugin translate them.

### Custom titles

GitHub admonition syntax has no custom-title form. When a callout needs a heading, put it on a **bold lead-in line** as the first body line, then a blank quoted line, then the body:

```markdown
> [!TIP]
> **Open Copilot Chat**
>
> Body text.
```

### No nesting; separate adjacent callouts with a blank line

GitHub admonitions cannot nest. If you need a callout "inside" another, emit them as **sibling** blockquotes instead. Consecutive admonitions **must** be separated by a blank line — without it, Markdown merges them into one blockquote and the second `[!TYPE]` marker renders as literal text:

```markdown
> [!TIP]
> First callout.

> [!CAUTION]
> Second callout — note the blank line above.
```

## Headings

- Repository docs (README, CONTRIBUTING, instruction files, skills, etc.): start with `# Title` then `##` for sections.
- Lesson pages (`docs/**/*.md`): no `# H1` in body — the title comes from frontmatter. Body headings start at `##`.

## Frontmatter for lesson pages

Every lesson page needs frontmatter:

```yaml
---
title: "Exercise N - Lesson title"
description: "One-sentence summary (optional, used for SEO/meta)."
---
```

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

- Use reference-style links when practical. Define refs at the bottom of the file that owns the link.
- Strip locale codes (`/en/`, `/en-us/`, etc.) from URLs so readers land in their own locale.
- For descriptive link text (no "click here"; no link-only sentences), see [`markdown-accessibility.instructions.md`](./markdown-accessibility.instructions.md).

## Images

Use Markdown image syntax with paths relative to the Markdown file:

```markdown
![Alt text describing the image](../_images/some-screenshot.png)
```

## Path conventions

- Per-path lessons: `cli/`, `vscode/`, `cloud/`, `app/`. Files are numbered by lesson order: `1-installing.md`, `2-custom-instructions.md`, etc.
- Support images live in `_images/` directories and are excluded from routing by `website/src/content.config.ts`.

## Cross-repo links

The learner's template repo is `github.com/github-samples/tailspin-toys`. Never link to files inside *this* repo as if they were the template — those paths don't exist here anymore.

[github-style]: https://docs.github.com/contributing/style-guide-and-content-model/style-guide
[github-style-keyboard]: https://docs.github.com/contributing/style-guide-and-content-model/style-guide#keyboard-shortcuts
