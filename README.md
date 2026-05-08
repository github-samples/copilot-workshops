# Agents in SDLC — Workshop Content

Workshop content for **Agents in SDLC**, a guided exploration of GitHub Copilot's agentic capabilities (Copilot CLI, VS Code agent mode, and the Copilot cloud agent) across the software development lifecycle.

The published site lives at **<https://github-samples.github.io/agents-in-sdlc/>**.

> [!NOTE]
> The demo application learners build through during the workshop — Tailspin Toys, a Flask + Astro/Svelte crowdfunding site — lives in a separate repository: **<https://github.com/github-samples/tailspin-toys>**. This repo holds only the *content*: lesson MDX, partials, images, and the Astro + Starlight site that publishes them.

## Start the workshop

Begin at the [workshop landing page](https://github-samples.github.io/agents-in-sdlc/) on the published site, or open [`workshop-content/index.mdx`](./workshop-content/index.mdx) locally.

## Repository structure

- **`workshop-content/`** — Lesson source (MDX).
  - `cli/`, `vscode/`, `cloud/` — Per-path lessons (Copilot CLI / VS Code / cloud agent).
  - `shared/` — Lessons shared across paths (referenced via redirect-stub pages in the per-path folders).
  - `_partials/` — Reusable MDX fragments (`callout-*`, `section-*`, `exercise-*` prefixes).
  - `images/` — Screenshots and diagrams.
- **`docs/`** — Astro + Starlight site that publishes `workshop-content/` to GitHub Pages.
- **`.github/`**
  - `copilot-instructions.md` + `instructions/*.md` — Authoring guidance for Copilot.
  - `agents/`, `skills/` — Custom agents and skills available to Copilot in this repo.
  - `workflows/pages.yml` — Builds and deploys the site on pushes to `main`.

## Local development

From the repo root:

```bash
cd docs
npm install
ln -sfn $PWD/node_modules ../workshop-content/node_modules   # MDX outside docs/ needs to resolve @astrojs/starlight/components
npm run dev
```

The site runs at <http://localhost:4321/agents-in-sdlc/>.

The `workshop-content/node_modules` symlink mirrors what `pages.yml` does in CI. It is gitignored.

## Verification

Before opening a PR, run both checks:

**Build (target: 29 pages):**

```bash
cd docs && rm -rf dist && npm run build
```

**Link check (offline):**

```bash
mkdir -p /tmp/lychee-root && ln -sfn $PWD/docs/dist /tmp/lychee-root/agents-in-sdlc \
  && lychee --offline --no-progress --root-dir /tmp/lychee-root 'docs/dist/**/*.html'
```

Lychee runs offline and won't catch broken external GitHub URLs — click those manually after changes.

## Authoring conventions

See [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) for the full playbook (partials naming, shared-module pattern, link conventions, commit hygiene).

Per-file-type guidance lives in [`.github/instructions/`](./.github/instructions/) and is auto-applied based on each file's `applyTo` glob:

- `mdx.instructions.md` — Workshop MDX patterns.
- `markdown.instructions.md` — Repo-level Markdown (no hard-wrap; GitHub admonitions).
- `partials.instructions.md` — `workshop-content/_partials/` conventions.
- `astro.instructions.md` — `docs/` site wrapper.

## License

MIT — see [LICENSE](./LICENSE).

## Maintainers

See [CODEOWNERS](./.github/CODEOWNERS).

## Support

Provided as-is. Open an issue if you have questions.
