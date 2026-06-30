# Authoring Guide

This is the entry point for **content authors and maintainers** of the *Agents in SDLC* workshop. If you arrived here looking to *take* the workshop, head to the published site at <https://github-samples.github.io/agents-in-sdlc/>.

## Project overview model

- **All content is created in MDX files** under `docs/src/content/docs/`. That's the source of truth.
- **One consumer.** The Astro + Starlight site in `docs/` builds the published GitHub Pages site from those MDX files.
- **Reusable fragments live in `_shared/`** and are imported via the `@shared/*` alias.

```
agents-in-sdlc/
├── docs/
│   └── src/content/docs/         ← MDX source. EDIT HERE.
│       ├── index.mdx             ← Workshop landing page
│       ├── cli/                  ← Copilot CLI lessons (0-prerequisites.mdx + numbered exercises)
│       ├── vscode/               ← VS Code lessons (0-prerequisites.mdx + numbered exercises)
│       ├── cloud/                ← Cloud agent lessons (0-prerequisites.mdx + numbered exercises)
│       ├── app/                  ← GitHub Copilot app lessons (setup folded into Exercise 1)
│       ├── _shared/              ← Reusable MDX fragments (callout-/section-/exercise-)
│       └── _images/              ← Screenshots and diagrams
└── .github/
    ├── copilot-instructions.md   ← AI authoring guide (humans can read it too)
    ├── instructions/             ← Per-file-type conventions (auto-applied to Copilot)
    └── workflows/                ← CI for site build + Pages deploy
```

## Step-by-step recipes

### Add a new lesson

1. **Pick a path and number.** Lessons live under `docs/src/content/docs/{cli,vscode,app,cloud}/N-name.mdx`. `N` is the next available integer in that path; the number drives the URL slug (`/cli/3-generating-code/`).
2. **Create the file** with frontmatter:
   ```mdx
   ---
   title: "Exercise N - Short descriptive title"
   ---

   import { Aside } from '@astrojs/starlight/components';

   Body starts here.
   ```
   Only `title` is required; it becomes the H1 and the page title. Don't add a body H1 — Starlight renders the title automatically.
3. **Write the body.** Use Markdown plus optional MDX `<Aside>` admonitions. See **Style essentials** below.
4. **Add prev/next navigation.** Define `[previous-lesson]` and `[next-lesson]` reference links at the bottom of the page, pointing at the adjacent lessons in the same path:
   ```markdown
   [previous-lesson]: ../2-custom-instructions/
   [next-lesson]: ../4-mcp/
   ```
   Then surface them in the body using **the same style as the other lessons in your path** — don't mix styles within a path:
   - **Woven into prose** (common in the CLI path): end the lesson with a sentence like ``the next step is to [create the PR][next-lesson]``.
   - **Explicit nav table** (common in the cloud and VS Code paths): a single-cell table just below the frontmatter/imports and again at the end of the body.
     ```markdown
     | [← Previous lesson: Custom instructions][previous-lesson] |
     |:--|
     ```
     ```markdown
     | [Next lesson: Custom agents →][next-lesson] |
     |--:|
     ```
   The first lesson in a path omits `[previous-lesson]`; the last omits `[next-lesson]`.
5. **Register in the sidebar.** Open `docs/astro.config.mjs` and add an entry to the appropriate `items: []` block. The sidebar is *manually* maintained — order in the file is the order learners see.
6. **Preview and verify, then open a PR.** Preview locally and run the verification sequence before committing — see [Building and verifying](#building-and-verifying) below. CI runs the Astro build and the lychee link check; both must pass.

### Add a partial

Partials are reusable MDX fragments imported by lesson pages. They live in `docs/src/content/docs/_shared/` and are resolved via the `@shared/*` alias.

1. **Pick a category prefix.** Partial filenames must start with one of:
   - `callout-` — single short callout (e.g., one `<Aside>`).
   - `section-` — multi-paragraph reusable concept content (intros, recaps, overviews).
   - `exercise-` — self-contained hands-on steps that drop into a numbered list on the host page.

   Each partial is *single-purpose*: concept *or* exercise, never both. If you have explanation plus numbered steps, split it into a `section-…` partial and an `exercise-…` partial that the host page introduces under separate H2 headings.
2. **Create the file** at `docs/src/content/docs/_shared/<prefix>-name.mdx`. No frontmatter — the host page's frontmatter applies.
3. **Add the metadata block** as the very first lines of the file. `@summary` is one sentence; `@sections` lists every `##`/`###` heading the partial introduces (use `H2`/`H3` prefixes). Starlight strips `{/* */}` comments, so this is invisible at runtime.
   ```mdx
   {/*
   @summary One sentence describing what the partial drops into the host page.
   @sections
     - H3 First heading the partial introduces
     - H3 Second heading
     - H4 Subheading under the second
   */}
   ```
   Partials must not contain `## H2` — host pages own H2. List `### H3` and deeper only.
4. **Self-contained links.** Any reference-style link (`[label][ref]`) used inside the partial must define `[ref]: url` *inside the same partial*. Don't depend on the host page to provide refs.
5. **Import and use** in the host page (always via the `@shared/` alias and bound to a name starting with the PascalCase form of the filename prefix):
   ```mdx
   import CalloutStartCopilotCliAllowAll from '@shared/callout-start-copilot-cli-allow-all.mdx';

   <CalloutStartCopilotCliAllowAll />
   ```
   The lint enforces both the alias and the prefix-matching binding.
6. **Run sync** so the corresponding `docs/src/types/_shared/<name>.mdx.d.ts` (which powers VS Code hover tooltips at every `<CalloutStartCopilotCliAllowAll />` use site) is generated:
   ```bash
   python scripts/sync_partial_metadata.py
   ```
7. **Lint** to confirm everything is consistent:
   ```bash
   python scripts/lint_partials.py
   ```
8. **Threshold for extraction**: only extract a partial when the same content appears in 2+ places, or it's at least 5 lines and non-trivial. Single-use content stays inline.

`lint_partials.py` and `sync_partial_metadata.py --check` are **local** guardrails — CI does not run them, so run them yourself before committing. The generated `<name>.mdx.d.ts` files in `docs/src/types/_shared/` are marked read-only in `.vscode/settings.json`; never edit them by hand.

See [`.github/instructions/partials.instructions.md`](./.github/instructions/partials.instructions.md) for the full partial conventions.

### Add an image

1. **Drop the file** in `docs/src/content/docs/_images/` (or a path-scoped `cli/_images/` etc. when the image is path-specific). Use lowercase-with-hyphens filenames; prefix with `shared-` if the image is referenced from multiple harnesses.
2. **Reference it** with a relative path from the consuming MDX page:
   ```mdx
   ![Description of the screenshot](../_images/my-screenshot.png)
   ```
3. **Always include alt text.** Starlight treats the alt text as required.
4. **Preview locally** to confirm the image resolves.

### Edit an existing lesson

1. **Find the file** under `docs/src/content/docs/` (use the published URL as a hint — `/cli/3-generating-code/` lives at `cli/3-generating-code.mdx`).
2. **Edit the MDX.** Same conventions apply — see **Style essentials** below.
3. **Preview** with `npm run dev` in `docs/`.
4. **Commit, PR, merge.**

### Reuse a lesson across paths

When the same lesson applies to multiple harnesses (CLI, VS Code, Cloud), pull the body into a `section-…` partial under `_shared/` and `import` it from each per-harness lesson page. The host page owns the frontmatter, the H2s, and the prev/next nav; the partial owns the reusable prose.

## Building and verifying

Before opening a PR, preview the site and run the full verification sequence. The canonical commands live in the [`build-and-verify-docs`](./.github/skills/build-and-verify-docs/SKILL.md) skill — the summary below mirrors it.

**Preview** with the Astro dev server (hot reload):

```bash
cd docs
npm install
npm run dev
```

The site runs at <http://localhost:4321/agents-in-sdlc/>.

**Verify** before committing:

1. **Build** — `cd docs && rm -rf dist && npm run build`. Must succeed.
2. **Link check** — lychee (offline) against the built `docs/dist/`. Catches broken internal links/images.
3. **Partial guardrails** — `python scripts/lint_partials.py` and `python scripts/sync_partial_metadata.py --check`. These keep partial metadata, the `@shared/` alias, and the generated `.mdx.d.ts` tooltips in sync.

**What CI enforces vs. what you run locally:** CI (`pages.yml`) runs only the **build** and the **lychee** link check on every PR. The partial guardrails (`lint_partials.py`, `sync_partial_metadata.py --check`) are **not** run by CI — they're local checks you must run yourself before committing, otherwise stale `.mdx.d.ts` files or alias drift can land unnoticed. After merge to `main`, `pages.yml` deploys the site to GitHub Pages.

**Consistency pass.** When a change renames a file or folder, adds or removes a skill or instruction file, or touches how the build works, also sweep for stale references — the structure trees and cross-doc pointers in `README.md`, `AUTHORING.md`, and `.github/copilot-instructions.md` aren't checked by any tool. The [`build-and-verify-docs`](./.github/skills/build-and-verify-docs/SKILL.md) skill has the full checklist.

## Style essentials

A short cheat sheet. For deeper conventions, see [`.github/instructions/`](./.github/instructions/).

- **Reference-style links** for in-workshop pages and external docs. Define refs at the bottom of the page (or bottom of the partial — partials are self-contained):
  ```markdown
  See [Exercise 1][exercise-1] for context. The [Copilot CLI docs][cli-docs] explain.

  [exercise-1]: ../1-install-copilot-cli/
  [cli-docs]: https://docs.github.com/copilot/github-copilot-in-the-cli
  ```
- **Admonitions** use Starlight's `<Aside>` component:
  ```mdx
  <Aside type="note">Use `note`, `tip`, `caution`, or `danger`.</Aside>
  ```
- **No hard-wrapping** in repo-level Markdown files (READMEs, this file). Editors soft-wrap. Hard breaks are reserved for actual structural breaks.
- **Cross-repo links** (the demo app): always use `https://github.com/github-samples/tailspin-toys/...`. Don't link to files in *this* repo as if they were the template.

## Troubleshooting

- **"Module not found: `@astrojs/starlight/components`"** — run `npm install` inside `docs/`.
- **"No matching exports" or component renders as text** — check that the import in the host MDX page matches the component name and path exactly. Imports go at the top of the MDX file, after frontmatter.
- **Sidebar entry doesn't appear** — confirm you added it to `docs/astro.config.mjs` (it's manually maintained).
- **A lesson page renders but a partial inside it doesn't** — check that the partial import uses the `@shared/` alias (e.g. `import Foo from '@shared/foo.mdx'`) and that the file exists in `docs/src/content/docs/_shared/`.
- **Lychee reports a broken link** — most often a renamed lesson breaking a `[ref]: ../old-name/` definition. Update both the link target and any cross-page refs.

## Deeper conventions

The `.github/instructions/*.md` files have `applyTo` frontmatter that targets specific file globs. Read these when you need depth on a specific area:

- [`markdown.instructions.md`](./.github/instructions/markdown.instructions.md) — Markdown + MDX conventions: no hard-wrap, admonitions, headings, filenames/UI formatting, partials patterns.
- [`markdown-accessibility.instructions.md`](./.github/instructions/markdown-accessibility.instructions.md) — accessibility conventions: descriptive links, alt text, heading hierarchy, plain language, input-agnostic action verbs (**select** not "click").
- [`partials.instructions.md`](./.github/instructions/partials.instructions.md) — partial conventions (naming, self-containment, list resumption).
- [`astro.instructions.md`](./.github/instructions/astro.instructions.md) — `docs/` site wrapper.
- [`instructions.instructions.md`](./.github/instructions/instructions.instructions.md) — how to write and maintain the instruction files themselves.

Reusable task playbooks (build/verify, browser validation, partial sync, contribution flow) live as **skills** under `.github/skills/` — see the [skills index](./.github/skills/README.md) for what each one does and when to use it.

For the AI authoring playbook, see [`.github/copilot-instructions.md`](./.github/copilot-instructions.md).
