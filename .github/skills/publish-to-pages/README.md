# About this skill in this repo

`publish-to-pages` is a general-purpose skill for converting and publishing arbitrary content (PPTX, PDF, HTML, Google Slides) to a **new** GitHub Pages repo.

**It is NOT the deployment workflow for this repo's site.** This repo's workshop site is built and deployed by [`.github/workflows/pages.yml`](../../workflows/pages.yml). That workflow runs automatically on pushes to `main` and publishes the Astro + Starlight build under `website/dist/` to <https://github-samples.github.io/copilot-workshops/>.

Use `publish-to-pages` when you want to spin up a *separate* Pages site for, say, a slide deck or a one-off HTML artifact. Don't use it to deploy this repo.

Source: imported from [`github/awesome-copilot@65b20ad`](https://github.com/github/awesome-copilot/tree/65b20ad912305cb9ac6e3cf2b0e65ea35db2d1f7/skills/publish-to-pages).
