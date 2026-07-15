---
name: localizations
description: A skill that localizes contents into given locales.
---

# Localize contents into given locales

A skill that localizes contents into given locales.

## How it works

The skill takes input content and a list of target locales. It then translates the content into each specified locale, providing localized versions for each.

### Content structure

```text
.
└── docs/                         ← workshop content (source + locale outputs)
    ├── README.md                 ← landing page (source; slug: index)
    ├── <harness>/                ← English lessons (source)
    │   ├── README.md             ← harness landing (source; slug: <harness>)
    │   └── *.md
    ├── _images/                  ← shared assets (not localized)
    └── <locale>/                 ← localized output, direct child of docs/
        ├── README.md             ← locale landing (slug: <locale>)
        └── <harness>/
            ├── README.md         ← localized harness landing (slug: <locale>/<harness>)
            └── *.md
```

### Input contents

Here are the contents in scope for localization:

- All English Markdown files under `docs/` **and its subdirectories** — the workshop landing (`docs/README.md`) and the per-harness lessons (`docs/<harness>/**/*.md`).

Do **not** treat `_images/` (shared assets) or any configured locale-root directory as source input.

Files already under `docs/<locale>/` are **outputs**, not inputs—never treat configured locale-root directories as source content to be localized again.

### Target locales

Target locales are defined in the `rules` directory as markdown files in this skill (`rules/ko-kr.md`, for example). **To determine which locales to process, list the files in `rules/`: each `<locale>.md` file corresponds to exactly one supported target locale.** Each locale has its own set of rules and guidelines for translation, ensuring that the localized content is appropriate for the target audience.

Locale identifiers use lowercase with a hyphen (for example, `ko-kr`). This is the canonical casing for both the rules filename and the output directory in this skill; keep them consistent.

### Output contents

All localized workshop content is stored directly under the repo-root `docs/` content directory, with each locale having its own subdirectory. For example, Korean content is stored in `docs/ko-kr/`.

Locale directories must be direct children of `docs/` so Starlight (configured in `website/astro.config.mjs`) recognizes them and renders its language selector. Do not add an intermediate `localizations/` directory.

## Localization process

There are three cases for localization. To detect which case applies, compare the **source tree** against the existing `docs/<locale>/` tree, and use the **git history of the source files** to detect changes:

- **Original exists, no localized version for the locale:** Create a new localized document.
- **Both original and localized versions exist:** Compare the source tree against `docs/<locale>/`, then run `git diff` (or `git log`) on the **source** file to find what changed since the localized version was last produced. Update only the affected sections of the localized document; do not re-translate unchanged sections unnecessarily.
- **Localized version exists, but the original has been deleted:** Delete the orphaned localized document (and prune now-empty locale subdirectories).

The process runs in two passes. First, the content is analyzed to identify key phrases and context. Then the `translator` agent performs the initial localization, followed by a review-and-refinement pass by the `evaluator` agent to ensure quality and consistency.

> The `translator` and `evaluator` "agents" are **roles/personas**, not external tools. If no dedicated sub-agents are available, perform them as sequential personas: first adopt the translator role to produce the draft, then adopt the evaluator role to critique and refine that draft against the locale rules. Repeat the refinement loop until the evaluator's criteria pass.

### Markdown and formatting preservation

Regardless of locale, the following must be preserved exactly and **not** translated:

- YAML frontmatter **keys** (translate values only where appropriate, e.g. a `title`). **Exception — the `slug` key on landing pages (`README.md`):** the site routes each folder landing via its `slug`, so a localized landing must carry a **locale-prefixed** slug rather than the English one. Rewrite it: a locale root (`docs/<locale>/README.md`) uses `slug: <locale>`, and a localized harness landing (`docs/<locale>/<harness>/README.md`) uses `slug: <locale>/<harness>`. Never copy the English `slug: index` / `slug: <harness>` verbatim into a localized file — that would collide with the English route.
- Fenced and inline code, including variable, function, and command names.
- URLs and external link targets.
- HTML tags, Markdown structure, tables, and admonition markers.

Translate human-language prose, including comments inside code blocks where they are explanatory (per the locale rules). Keep heading order and document structure stable.

**Heading anchors follow the localized text.** When a heading is translated, its auto-generated anchor/slug changes with it—this is expected. The requirement is that **same-document anchor links keep resolving**: whenever you translate a heading, update every in-page link that targets it (`](#...)`) to the localized heading's new slug. Do not leave a link pointing at the original English slug once the heading is translated, and do not preserve an English anchor that no longer matches its heading. Anchors that point into **non-localized** files (or external URLs) keep their original target.

**Image and asset paths point to the original assets unless a localized asset exists.** Because localized files live under `docs/<locale>/`, rewrite source-relative paths as needed so they still resolve to the shared asset (for example, an app lesson at `docs/<locale>/app/2-foo.md` uses `../../_images/x.png` to reach `docs/_images/`). Only point at a localized asset when a corresponding translated image actually exists under the locale tree. Either way, the link must resolve to a real file.

### Translator agent

Use the `translator` agent to perform the localization. It should follow the rules and guidelines defined for each target locale document in the `rules` directory.

### Evaluator agent

Use the `evaluator` agent to assess the quality of the localized content. The evaluator checks for accuracy, cultural relevance, and overall quality, following the rules and guidelines defined for the target locale in the `rules` directory.

The evaluator scores the localized document against the locale's **Evaluator Scoring Rubric** (defined in the locale's `rules/<locale>.md`). The rubric uses two tiers: **Tier A** hard-fail criteria that must score 5, and **Tier B** graded criteria (1–5) that must score 4 or 5. A document passes only when **every applicable Tier A criterion scores 5 and every applicable Tier B criterion scores ≥ 4**. If anything falls short, return the document to the translator with specific notes and re-run the translate → evaluate loop until it passes, escalating to a human after the rubric's iteration cap.

## DOs and DON'Ts

- **Do** perform localization only for the target locales defined in the `rules` directory (one `<locale>.md` per supported locale). Do not localize into unsupported locales.
- **Do** preserve Markdown structure, code, external link/URL targets, and frontmatter keys exactly (see *Markdown and formatting preservation*).
- **Do** let heading anchors follow the localized heading text, and update same-document anchor links to match the new slugs so they keep resolving (see *Markdown and formatting preservation*).
- **Do** point image and asset paths at the original assets (rewriting the relative path as needed so it resolves from `docs/<locale>/`), unless a corresponding localized asset exists (see *Markdown and formatting preservation*).
- **Do** mirror the source directory layout under `docs/<locale>/`.
- **Don't** treat configured locale-root directories as source input.
- **Don't** reorder or restructure content; keep headings and their order stable.
- **Don't** translate code, commands, or identifiers; translate explanatory prose and code comments only.

