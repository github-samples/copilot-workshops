---
title: "Lesson 2 - Add star ratings: a quick win"
description: "Start your first agent session in the GitHub Copilot app, make a small change to the game cards, and merge it as your first pull request."
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

In the previous lesson you toured the workspace and used a quick chat. Now it's time to start an **agent session** and make your first change to the project. You'll keep it small: the games already have a star rating in their data, but the game cards on the home page don't show it yet. You'll ask the agent to surface it, review the change, and merge it as your first pull request.

In this lesson, you will:

- start an agent session and learn how a session is structured.
- ask the agent to make a small, focused change to the project.
- review the change in the workspace diff view.
- run the app locally to confirm the change in the browser.
- open and merge your first pull request.

## Scenario

Each game in Tailspin Toys can have a star rating, and it already appears on the game details page. The game cards on the home page, though, only show the title, category, publisher, and description. As a warm-up, you'll have the agent display the existing rating on each card — a tiny, self-contained change that's perfect for your first session.

## Anatomy of a session

A **session** is a conversation with an agent. In this workshop you choose a **new working tree**, giving the session a dedicated checkout and branch. This isolates each PR milestone without a separate branch for every lesson. Your sessions appear in the sidebar grouped by repository; select any one to switch to it.

Inside a session you'll see three things: the **conversation** with the agent, the agent's **tool activity** as it explores and edits files, and the list of **changed files** with their diffs.

## Start a session and request our change

Let's start a new session to begin exploring the project and implementing our feature. In a [prior lesson][prior-lesson] you added your project from its GitHub repository. We'll create a new session for that repository and request our change.

1. Return to (or open) the GitHub Copilot app.
2. Select the **Home screen**.
3. Ensure `tailspin-toys` is selected for the repo.

   ![The GitHub Copilot app prompt box with the repository selector set to tailspin-toys and the model selector shown beneath the prompt](../_images/app-2-start-session.png)

4. Choose a **new working tree** and **Interactive** mode below the prompt box. Use the following prompt to request the change:

   ```plaintext
   Before editing, identify this checkout and branch, confirm it is a clean new worktree, fetch origin, and fast-forward this session branch to origin/main. Confirm HEAD matches origin/main. Stop and explain if it is dirty, diverged, or cannot be updated; do not reset or discard work.

   On the game cards, show each game's star rating. The Game type already includes a starRating field — it's a number out of 5, or null when a game hasn't been rated yet. Display it on each card in src/components/GameCard.astro, and when starRating is null show "No rating yet" instead. Keep the change small and don't restructure the card layout or change the data model.

   Follow repository instructions, add or update appropriate tests, and run the relevant existing npm checks. Inspect prerequisites and ask before installing anything. Report the changed files and check results, then stop for my review. Do not commit, push, open a pull request, or implement another feature.
   ```

> [!NOTE]
> Notice how the prompt contained the name of the file for Copilot to update. While it's not required at all to specify which files Copilot should include in its work, pointing it in the right direction both helps Copilot quickly generate code and reduce token usage.

5. Press <kbd>Enter</kbd> to send the prompt to Copilot.

Copilot app begins work by first creating a new worktree, an isolated copy of the project. It then explores the project, locating the necessary files to update to add the new feature. It will then create the necessary code. You've now added a new feature with Copilot app!

## Review the diff

All AI-generated changes deserve a review before they're merged, even small ones. Let's explore the changes, right here in Copilot app.

1. In the upper right-hand corner of the app, select **Toggle review panel**. This will open the diff screen with all the outstanding changes made by Copilot.

   ![The GitHub Copilot app top toolbar with an arrow pointing to the Toggle review panel button to the right of Create PR](../_images/app-2-review-panel.png)

2. You should notice code added to `GameCard.astro`, the core file used to display game details. It should be similar to the following — a small block that renders the rating when present and falls back to "No rating yet" when `starRating` is `null`:

   ```astro
   {game.starRating !== null ? (
       <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-900/60 text-amber-300" data-testid="game-rating">
           ★ {game.starRating} / 5
       </span>
   ) : (
       <span class="text-xs font-medium text-slate-500" data-testid="game-rating-empty">
           No rating yet
       </span>
   )}
   ```

> [!NOTE]
> Because Copilot, like all generative AI tools, is probabilistic rather than deterministic, the exact code may vary from the above. But it should be relatively similar.

## Check the changes

Review the agent's automated check results before opening a browser. Confirm that tests cover a numeric `starRating` and the `null` fallback, using the project's existing npm scripts rather than a skill that does not exist yet. A missing prerequisite or skipped check is not a pass.

Then inspect the app manually using the session's built-in terminal. Identify the worktree before starting the server, and do not reuse a server belonging to another checkout.

1. In the review panel on the right side of Copilot app, select **Terminal**. If there is no **Terminal** button, select the **+** (labeled as **Open in panel**), then select **Terminal**.

   ![The Terminal button in the review panel of the GitHub Copilot app](../_images/app-terminal-screenshot.png)

2. Enter the following command in the terminal window to start the web app's dev server:

   ```shell
   npm run dev
   ```

3. Once the server starts (this will just take a moment), open a browser window.
4. Open the local URL printed by the server, normally `http://localhost:4321`. If the port is occupied, identify the owner instead of stopping an unrelated process.
5. Confirm rated game cards display their value out of five. Where unrated data is available, confirm **No rating yet** appears; otherwise use the automated test to verify the null case rather than claiming you observed it.
6. Return to the terminal window.
7. Press <kbd>Control</kbd>+<kbd>C</kbd> (Mac) or <kbd>Ctrl</kbd>+<kbd>C</kbd> (Windows/Linux) to stop the dev server you started.

## Open and merge your first pull request

Your change looks good — now it's time to ship PR 1. First authorize the commit and PR separately from implementation:

```plaintext
Review the full diff for the star-rating change and its tests, summarize the verification, and commit the reviewed changes on this session branch. Push the branch and create a pull request targeting main using the repository's PR template. Do not merge it.
```

1. Follow the created PR link in the session. If the app presents a **Create PR** confirmation, select it to approve the request rather than creating a second PR.
2. If prompted, select **Sign in with your browser** and follow the prompts to authenticate.
3. Copilot gets to work on creating the PR.

Once the PR is created, inspect the full PR diff and the checks in **My work**. Read the learner repository's workflow results; wait for required checks and reviews, and resolve failures before merging. **Ready to merge** is not a substitute for reviewing the change or your local evidence.

4. Select the **PR** bubble just above chat to open your PR in the review pane to see your pull request. You can review the PR as needed here.
5. Once ready, select **Ready to merge**.
6. Select **Merge pull request** on the new dialog window to merge your pull request!

Confirm PR 1 is merged into `main` before continuing. Merging the learner repository does not by itself deploy a website. The next lesson starts a fresh worktree and updates it from `origin/main` so it includes this PR.

## Summary and next steps

You've started your first agent session and shipped your first change! Specifically, you:

- started an agent session and learned how sessions are structured.
- directed the agent to make a small, focused change to the game cards.
- reviewed the change in the workspace diff view.
- ran the app locally to confirm the star rating in the browser.
- opened PR 1, reviewed its checks, and explicitly merged it.

Next, you'll use the app to add a custom instructions standard to the repository — starting from one of the issues in your backlog. Continue to [Lesson 3 - Guiding Copilot with custom instructions][next-lesson].

## Resources

- [Working with agent sessions in the GitHub Copilot app][agent-sessions]
- [About the GitHub Copilot app][about-copilot-app]
- [Managing issues and pull requests with the GitHub Copilot app][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#install-and-configure-the-github-copilot-app
[previous-lesson]: ../1-install-copilot-app/
[next-lesson]: ../3-custom-instructions/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
