---
description: 'How to write and maintain instruction files (`.github/instructions/*.instructions.md`) for this workshop content repo'
applyTo: '**/*.instructions.md'
---

# Authoring instruction files

Guidance for creating and maintaining the scoped instruction files that steer Copilot in this repo. This is a **content-only** Astro + Starlight workshop repo, so instruction files govern *Markdown authoring conventions* — never application code (that lives in `github-samples/tailspin-toys`).

This file covers what is specific to instruction files. For mechanical Markdown formatting (no hard-wrapping, admonition syntax, headings, link style), instruction files also follow [`markdown.instructions.md`](./markdown.instructions.md) — don't restate those rules here.

## Where instruction files live

- Location: `.github/instructions/`.
- Naming: lowercase with hyphens, ending `.instructions.md` (e.g. `markdown-accessibility.instructions.md`).
- One concern per file. The existing set: `markdown` (formatting), `markdown-accessibility` (a11y), `astro` (the `docs/` site wrapper). Add a new file only for a genuinely new concern; otherwise extend an existing one.

## Required frontmatter

Every instruction file opens with YAML frontmatter:

```yaml
---
description: 'One sentence stating the purpose and scope'
applyTo: '**/*.md'
---
```

- **description** — single-quoted, one sentence. This is how an author (and Copilot) tells files apart, so make it specific.
- **applyTo** — glob(s) selecting the files the instructions bind to. Patterns used in this repo:
  - `'**/*.md'` — all Markdown files (formatting, accessibility).
  - `'docs/**/*.{astro,mjs,ts,js}'` — the site wrapper.
  - `'**/*.instructions.md'` — this meta-guide.

## Structure

- Start with a single `#` H1 title, then `##` sections. (Instruction files are repository docs, so — unlike lesson Markdown — they *do* carry a body H1.)
- Keep sections short and scannable. Lead with the rule; follow with a tight example only when it removes ambiguity.
- If two files would cover the same ground, pick one home and have the other point to it. Duplicated guidance drifts.

## Instruction altitude (the Goldilocks zone)

Aim for the smallest rule set that fully defines the outcome. Add a rule after a real failure, not for a hypothetical one. Prefer a high-signal example over an exhaustive decision table.

| Altitude | Failure mode | Result |
| --- | --- | --- |
| Over-specified | Brittle if-this-then-that prose | Breaks on any case you didn't list |
| Under-specified | Assumes shared context | Generic, off-convention output |
| Right altitude | Heuristics + one example | Stable, generalizes to new content |

## Writing style

- Imperative mood: "Use", "Define", "Avoid" — not "you should" / "it might be good to".
- Be specific and actionable. Replace vague advice with a concrete instruction plus, where helpful, a `Good`/`Avoid` pair.
- Use backticks for filenames, paths, and literal syntax; bold for UI labels (per `markdown.instructions.md`).

## Examples

Show the convention, not just describe it. Label the contrast.

**Good** — names the syntax and shows the callout:

```markdown
Use GitHub admonition syntax for callouts in published lesson content:

> [!TIP]
> Run the dev server before editing.
```

**Avoid** — abstract, unactionable:

```markdown
Callouts should be done properly using the right syntax.
```

## Patterns to avoid

- **Hypothetical-rule inflation** — don't encode rules for failures that haven't happened.
- **Restating other files** — defer mechanical formatting to `markdown.instructions.md` and the build/verify process to the [`build-and-verify-docs`](../skills/build-and-verify-docs/SKILL.md) skill.
- **Documenting tooling here** — instruction files describe *what content should look like*; *how to build/verify/preview* belongs in the skill.
- **Ambiguous terms** — "should", "might", "possibly" leave the outcome undefined.
- **Copy-paste from upstream docs** — distill and contextualize for this repo instead.

## Maintenance

- When a convention, path, or file is renamed, update the instruction files that mention it (the PR-time consistency pass in [`build-and-verify-docs`](../skills/build-and-verify-docs/SKILL.md) catches this).
- Keep `applyTo` globs accurate as the project structure evolves.
- Remove rules that no longer reflect how the repo works rather than letting them accumulate.
