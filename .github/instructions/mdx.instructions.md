---
description: 'MDX authoring conventions for workshop lessons'
applyTo: '**/*.mdx'
---

# MDX Authoring

## Frontmatter

Every MDX page (not partial) needs frontmatter:

```yaml
---
title: "Exercise N - Lesson title"
description: "One-sentence summary (optional, used for SEO/meta)."
---
```

Don't use `# H1` inside the body — Starlight renders the title from frontmatter.

Headings inside lesson body start at `##`.

## Starlight components

Import from `@astrojs/starlight/components`. Most common:

```mdx
import { Aside } from '@astrojs/starlight/components';

<Aside type="note">A note.</Aside>
<Aside type="tip">A helpful tip.</Aside>
<Aside type="caution">Something to watch out for.</Aside>
<Aside type="danger">Don't do this.</Aside>
```

When the same callout repeats across lessons, extract it to a `callout-*.mdx` partial instead of duplicating the `<Aside>`.

## Importing partials

```mdx
import StartCli from '../_partials/callout-start-copilot-cli.mdx';
import AddDocstring from '../_partials/exercise-instructions-add-docstring.mdx';

<StartCli />

<AddDocstring />
```

Path is relative to the importing file. Keep imports grouped at the top of the file under the frontmatter.

## Numbered lists across partials

When dropping an exercise partial into a numbered list, write the partial's items as plain Markdown numerals starting at `1.`. The host page's list resumes correctly. Don't try to manually continue numbering inside the partial.

## Images

Use Markdown image syntax with paths relative to the MDX file:

```mdx
![Alt text describing the image](../images/some-screenshot.png)
```

For shared lesson pages under `shared/<topic>/`, image paths are typically `../../images/...`.

## Path conventions

- Per-path lessons: `cli/`, `vscode/`, `cloud/`. Files numbered by lesson order: `1-installing.mdx`, `2-custom-instructions.mdx`, etc.
- Shared content: `shared/<topic>/<lesson>.mdx`. Per-path stubs redirect to the shared page and include a "Return to your path" footer.

## Cross-repo links

The learner's template repo is `github.com/github-samples/tailspin-toys`. Never link to files inside *this* repo as if they were the template — those paths don't exist here anymore.
