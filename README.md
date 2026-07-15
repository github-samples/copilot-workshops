# Copilot Workshops — Workshop Content

Workshop content for **Copilot Workshops**, a guided exploration of GitHub Copilot's agentic capabilities (Copilot CLI, VS Code agent mode, the Copilot app, and the Copilot cloud agent) across the software development lifecycle.

The published site lives at **<https://github-samples.github.io/copilot-workshops/>**.

> [!NOTE]
> The demo application learners build through during the workshop — Tailspin Toys, a pure-Astro crowdfunding site (SSR, API endpoints, and a Drizzle data layer) — lives in a separate repository: **<https://github.com/github-samples/tailspin-toys>**. This repo holds only the *content*: lesson Markdown, images, and the Astro + Starlight site that publishes them.

## Start the workshop

Visit the published site: <https://github-samples.github.io/copilot-workshops/>.

## Authoring

If you want to add or edit content, start with **[AUTHORING.md](./AUTHORING.md)**. It has the mental model, file map, and step-by-step recipes for adding lessons and images.

For PR/CI rules, see **[CONTRIBUTING.md](./CONTRIBUTING.md)**.

## Repository structure

- **`docs/`** — **Lesson source (plain Markdown). Edit here.** Browsable directly on github.com, no build required.
  - `README.md` — Workshop landing page (also the published site's home via `slug: index`).
  - `cli/`, `vscode/`, `cloud/`, `app/` — Per-harness lessons (Copilot CLI / VS Code / cloud agent / GitHub Copilot app). Each codespace-based harness opens with its own `0-prerequisites.md` setup lesson, and a folder `README.md` (routed via a `slug:` matching the folder) is its landing page.
  - `es-es/`, `ja-jp/`, `ko-kr/`, `pt-br/`, `zh-cn/` — Translated locale trees (currently the app harness).
  - `_images/` — Screenshots and diagrams (shared across all locales).
- **`website/`** — Optional Astro + Starlight site that publishes `docs/` to GitHub Pages. Only needed to self-host or preview the rendered site.
  - `astro.config.mjs` — Site URL, base path, `locales` block, sidebar.
  - `src/content.config.ts` — Content loader (`base: '../docs'`).
  - `src/pages/shared/0-prereqs.astro` — Full-HTML redirect forwarding the legacy `/shared/0-prereqs/` URL to the home page.
- **`AUTHORING.md`** — Author entry point (recipes for adding/editing content).
- **`CONTRIBUTING.md`** — PR flow + CI requirements.
- **`.github/`**
  - `copilot-instructions.md` + `instructions/*.md` — Authoring guidance for Copilot.
  - `agents/`, `skills/` — Custom agents and skills available to Copilot in this repo.
  - `workflows/pages.yml` — Builds and deploys the site on pushes to `main`.

## Local development

From the repo root:

```bash
cd website
npm install
npm run dev
```

The site runs at <http://localhost:4321/copilot-workshops/>.

## Verification

Before opening a PR, build the site and run the full verification sequence — clean build, page-count check, and offline link check (lychee). The canonical commands live in **[AUTHORING.md → Building and verifying](./AUTHORING.md#building-and-verifying)** and the [`build-and-verify-docs`](./.github/skills/build-and-verify-docs/SKILL.md) skill. CI (`pages.yml`) runs the build and the lychee link check.

## License

MIT — see [LICENSE](./LICENSE).

## Maintainers

See [CODEOWNERS](./.github/CODEOWNERS).

## Support

Provided as-is. Open an issue if you have questions.
