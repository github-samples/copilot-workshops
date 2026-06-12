# Agents in SDLC — Workshop Content

Workshop content for **Agents in SDLC**, a guided exploration of GitHub Copilot's agentic capabilities (Copilot CLI, VS Code agent mode, and the Copilot cloud agent) across the software development lifecycle.

The published site lives at **<https://github-samples.github.io/agents-in-sdlc/>**.

> [!NOTE]
> The demo application learners build through during the workshop — Tailspin Toys, a Flask + Astro/Svelte crowdfunding site — lives in a separate repository: **<https://github.com/github-samples/tailspin-toys>**. This repo holds only the *content*: lesson MDX, partials, images, and the Astro + Starlight site that publishes them.

## Start the workshop

Visit the published site: <https://github-samples.github.io/agents-in-sdlc/>.

## Authoring

If you want to add or edit content, start with **[AUTHORING.md](./AUTHORING.md)**. It has the mental model, file map, and step-by-step recipes for adding lessons, partials, and images.

For PR/CI rules, see **[CONTRIBUTING.md](./CONTRIBUTING.md)**.

## Repository structure

- **`docs/`** — Astro + Starlight site that publishes the workshop to GitHub Pages.
  - `src/content/docs/` — **Lesson source (MDX). Edit here.**
    - `index.mdx` — Workshop landing page.
    - `prereqs.mdx` — Shared setup lesson (Exercise 0).
    - `cli/`, `vscode/`, `cloud/` — Per-path lessons (Copilot CLI / VS Code / cloud agent).
    - `_shared/` — Reusable MDX fragments (`callout-*`, `section-*`, `exercise-*` prefixes), imported via the `@shared/*` alias.
    - `images/` — Screenshots and diagrams.
- **`AUTHORING.md`** — Author entry point (recipes for adding/editing content).
- **`CONTRIBUTING.md`** — PR flow + CI requirements.
- **`.github/`**
  - `copilot-instructions.md` + `instructions/*.md` — Authoring guidance for Copilot.
  - `agents/`, `skills/` — Custom agents and skills available to Copilot in this repo.
  - `workflows/pages.yml` — Builds and deploys the site on pushes to `main`.

## Local development

From the repo root:

```bash
cd docs
npm install
npm run dev
```

The site runs at <http://localhost:4321/agents-in-sdlc/>.

## Verification

Before opening a PR:

**Build:**

```bash
cd docs && rm -rf dist && npm run build
```

**Link check (offline):**

```bash
mkdir -p /tmp/lychee-root && ln -sfn $PWD/docs/dist /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```

Lychee runs offline and won't catch broken external GitHub URLs — click those manually after changes.

**Partial metadata lint:**

```bash
python scripts/lint_partials.py
```

## License

MIT — see [LICENSE](./LICENSE).

## Maintainers

See [CODEOWNERS](./.github/CODEOWNERS).

## Support

Provided as-is. Open an issue if you have questions.
