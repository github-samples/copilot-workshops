# Contributing

Thanks for your interest in contributing to *Agents in SDLC*! This repository hosts the workshop content (MDX source and the Astro + Starlight site that publishes it).

## Code of Conduct

This project is released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

Contributions are released under the [project's open source license](./LICENSE).

## What to read first

If you want to **author or edit content**, start with [`AUTHORING.md`](./AUTHORING.md). It covers the mental model, file layout, step-by-step recipes for adding/editing lessons, partials, and images, the local preview workflow, and style conventions.

## Submitting a pull request

1. [Fork](https://github.com/github-samples/agents-in-sdlc/fork) and clone the repository.
2. Create a topic branch (`git checkout -b my-change`).
3. Make your change. Keep PRs focused — one logical change per PR.
4. Push to your fork and [open a pull request](https://github.com/github-samples/agents-in-sdlc/compare).
5. Wait for CI and review.

## Before merge

All CI checks must be green:

- **`pages.yml`** — builds the Astro site.
- **Lychee** — offline link checks the built `docs/dist/`.
- **Partial lint + sync check** — `lint_partials.py` and `sync_partial_metadata.py --check` enforce the `_shared/` partial conventions.

## Commit messages

Conventional commit prefixes preferred: `docs:`, `chore:`, `fix:`, `ci:`, `feat:`.

Include a `Co-authored-by` trailer when AI-assisted:

```
Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## Resources

- [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [Using pull requests](https://help.github.com/articles/about-pull-requests/)
