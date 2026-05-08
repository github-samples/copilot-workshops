---
description: 'Markdown conventions for repository-level docs and READMEs'
applyTo: '**/*.md'
---

# Markdown Conventions

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

## Headings

- Repository docs (README, CONTRIBUTING, etc.): start with `# Title` then `##` for sections.
- Lesson MDX (`workshop-content/**/*.mdx`): no H1 in body — title comes from frontmatter. See `mdx.instructions.md`.

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
