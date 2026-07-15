---
name: validate-site-playwright
description: Render-validate the built Copilot Workshops site in a real browser using the Playwright MCP server. Use as an optional deeper QA pass — after the static checks in build-and-verify-docs — to confirm pages actually render: navigate the built routes, assert HTTP 200, catch console/hydration errors, find broken images, confirm Starlight Markdown features rendered, and optionally screenshot key pages. Trigger when asked to "validate the built site", "check the pages render", "do a browser/visual QA pass", or before opening a PR that changes rendered output.
---

# Validate the built site with Playwright

`build-and-verify-docs` checks the site *statically* — it builds, confirms the page-count invariant, and link-checks the HTML with lychee. It never opens a page in a browser, so it cannot see runtime failures: console/hydration errors, images that 404 at load time, or rendered Markdown that looks wrong.

This skill is the **optional, deeper, browser-based pass**. It drives the **Playwright MCP server** against a local preview of the built site. It is **interactive/local only** — CI (`pages.yml`) has no browser step, so this is never a merge gate. Run it before a PR that changes how pages render (new site-shell components, image-heavy lessons, layout changes), or whenever you want to confirm the real rendered output.

Run every command from the **repo root** unless a step says otherwise.

## Prerequisites

- The Playwright MCP server must be available (the agent has `browser_*` tools).
- A clean build must exist. If you haven't just built, run the build from [`build-and-verify-docs`](../build-and-verify-docs/SKILL.md) first:

  ```bash
  cd website && rm -rf dist && npm run build && cd ..
  ```

## 1. Serve the built site

Serve the production build (not the dev server) so you validate exactly what ships. `npm run preview` serves `website/dist/` at the real base path:

```bash
cd website && npm run preview
```

The site is served at <http://localhost:4321/copilot-workshops/>. Start it as a **detached background process** so it survives while you navigate, and capture its PID for teardown. Wait until the server logs that it's listening before navigating.

## 2. Derive the routes to check

Don't hard-code URLs. The built `dist/` is the source of truth for what routes exist:

```bash
# every built route, as site-absolute paths under the base
find website/dist -name index.html | grep -v 404 | sed 's#website/dist#/copilot-workshops#; s#/index.html#/#'
```

Validate a **representative sample** that covers every layout and harness: the landing page (`/copilot-workshops/`), a per-harness prerequisites page (e.g. `cli/0-prerequisites/`), and at least one lesson from each of `cli/`, `vscode/`, `cloud/`, and `app/`. For a release pass or a change that touches shared layout/components, validate **all** routes.

## 3. Validate each route

For each chosen route, use the Playwright MCP tools:

1. **Navigate** — `browser_navigate` to `http://localhost:4321/copilot-workshops/<route>`.
2. **Confirm it rendered** — `browser_snapshot` and check the page has its heading/title and real content (not an error page or raw, unrendered Markdown).
3. **Check the console** — `browser_console_messages` with `level: "error"`. There should be **zero** errors. Hydration warnings and 404s for assets surface here.

   *Known benign exception:* the legacy redirect route `/copilot-workshops/shared/0-prereqs/` is a minimal full-HTML redirect page (it immediately forwards to the home page `/copilot-workshops/` via a meta refresh) and declares no favicon, so the browser auto-requests `/favicon.ico` and logs a single `404 (Not Found)`. That one favicon 404 **on the redirect page only** is expected. Validate that route by confirming it lands on the home page, not by console cleanliness. A favicon 404 on any *real* page is a genuine finding (real pages link `favicon.svg`).
4. **Find broken images** — `browser_evaluate` with an async function that **force-loads lazy images first**, then flags only the ones that truly fail. Starlight/Astro mark below-the-fold images `loading="lazy"`, so a naive `naturalWidth === 0` check reports false positives for images that simply haven't scrolled into view yet:

   ```js
   async () => {
     const imgs = Array.from(document.images);
     const results = await Promise.all(imgs.map(img => new Promise(resolve => {
       img.loading = 'eager'; // defeat lazy-loading so the asset actually fetches
       if (img.complete) return resolve(img.naturalWidth === 0 ? (img.currentSrc || img.src) : null);
       const done = ok => resolve(ok ? null : (img.currentSrc || img.src));
       img.addEventListener('load', () => done(true), { once: true });
       img.addEventListener('error', () => done(false), { once: true });
       setTimeout(() => done(img.naturalWidth > 0), 5000); // timeout guard
     })));
     return results.filter(Boolean);
   }
   ```

   An empty array is a pass. Any entry is a genuinely broken/missing image — most often an `_images/` path that didn't survive a rename (cross-check with the [`build-and-verify-docs`](../build-and-verify-docs/SKILL.md) consistency pass). If you ever get a hit, confirm it with `curl -o /dev/null -w '%{http_code}'` against the asset URL before treating it as a real failure — a `200` means it was a lazy-load timing artifact, not a broken image.
5. **Confirm Markdown rendered cleanly** — GitHub admonitions should render as styled Starlight callouts, not literal text. In the snapshot, verify there is no visible `[!NOTE]`, `[!TIP]`, `[!CAUTION]`, `[!WARNING]`, `[!IMPORTANT]`, leftover `:::` directive, or raw frontmatter in the body.
6. **Screenshot (optional)** — `browser_take_screenshot` for a visual record of key pages. Save screenshots outside the repo as throwaway artifacts, not content.

## 4. Tear down

Close the browser and stop the preview server when finished:

- `browser_close` to release the browser.
- `kill <PID>` for the preview server you started in step 1.

## What to report

Summarize per route: rendered (yes/no), console errors (count), broken images (list), Markdown rendered cleanly (yes/no). A clean pass is **every route rendered, zero console errors, zero broken images, all Markdown rendered cleanly**. Flag anything else with the specific route and the failing URL/selector so it can be fixed before the PR.

## Scope notes

- This validates **rendering**, not link correctness — lychee (in `build-and-verify-docs`) owns link checking. Run both.
- It is **not** an accessibility audit. For accessibility *authoring* conventions, see [`markdown-accessibility.instructions.md`](../../instructions/markdown-accessibility.instructions.md).
- It is local-only and does not gate merges; treat failures as must-fix-before-PR, not as CI status.
