# Contributing

Thanks for your interest in contributing to **Copilot Workshops**! This repository hosts the workshop content (Markdown source and the Astro + Starlight site that publishes it).

## Code of Conduct

This project is released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

Contributions are released under the [project's open source license](./LICENSE).

## What to read first

If you want to **author or edit content**, start with [`AUTHORING.md`](./AUTHORING.md). It covers the mental model, file layout, step-by-step recipes for adding/editing lessons and images, the local preview workflow, and style conventions.

## Submitting a pull request

1. [Fork](https://github.com/github-samples/copilot-workshops/fork) and clone the repository.
2. Create a topic branch (`git checkout -b my-change`).
3. Make your change. Keep PRs focused — one logical change per PR.
4. Push to your fork and [open a pull request](https://github.com/github-samples/copilot-workshops/compare).
5. Wait for CI and review.

## Before merge

CI (`pages.yml`) must be green on your PR. It runs:

- **`pages.yml` build** — `npm run build` (Astro site build).
- **Lychee** — offline link check of the built `website/dist/`.

Before you push, run the full local verification sequence described in [AUTHORING.md → Building and verifying](./AUTHORING.md#building-and-verifying): clean build, page-count check, and lychee link check.

## Commit messages

Conventional commit prefixes preferred: `docs:`, `chore:`, `fix:`, `ci:`, `feat:`.

Include a `Co-authored-by` trailer when AI-assisted:

```
Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## Resources

- [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [Using pull requests](https://help.github.com/articles/about-pull-requests/)
