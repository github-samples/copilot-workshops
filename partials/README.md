# Reusable Markdown partials for the workshop site

This directory holds reusable content fragments included into the published workshop site
(`https://github-samples.github.io/agents-in-sdlc/`) via the
[PyMdown Snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/) extension.

Snippets are referenced from pages in `workshop-content/` using:

```markdown
--8<-- "sections/coding-agent-intro.md"
```

The `base_path` for snippet resolution is configured to this folder in `mkdocs.yml`.

## Rules for partials

- **Inline links only** — do NOT use reference-style links (`[text][ref]` plus `[ref]: url`). Reference
  definitions become document-global once the snippet is included and can collide with the host page.
- **No image references** — keep images in the consuming page outside the include. Snippets are
  inserted before Markdown conversion and have no stable source path.
- **No H1** — partials drop into the middle of a page; use H2 (`##`) at most.
- **One concept per partial** — easier to reuse, easier to update.

## Layout

```
partials/
  scenarios/   # Repeatable scenario blocks (Tailspin-specific framing)
  sections/    # Multi-paragraph sections that recur verbatim across paths
```
