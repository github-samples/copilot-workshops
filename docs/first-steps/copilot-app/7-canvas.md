---
title: "Lesson 7 - Explore a Canvas"
description: "Install a Repository Issues Kanban Canvas and start a session from an issue card."
authors:
  - jamesmontemagno
lastUpdated: 2026-09-16
---

A **Canvas** is a shared, bidirectional surface where you and an agent can update the same plan, board, checklist, or dashboard. Explore a Kanban Canvas that turns repository issues into a visual workflow.

In this lesson, you will:

- install a Canvas extension.
- connect the Canvas to the Space Quiz repository.
- move an issue into active work.
- inspect the session created from the issue.

## Install the Repository Issues Kanban Canvas

1. Browse the [Canvas extensions gallery][canvas-gallery].
2. Open the [Repository Issues Kanban extension][kanban-extension].
3. Select **Install in GitHub Copilot app** and approve the installation.
4. In the app, open **Customize**, then **Canvas**.
5. Confirm that the extension is installed.

## Start work from the Canvas

1. Select **New session** for the Canvas.
2. Choose the `space-quiz` project.
3. Explore the issue board.
4. Move an issue card into the active-work column.
5. Open the automatically generated session.
6. Confirm that the selected issue is available as session context.

> [!NOTE]
> The current Repository Issues Kanban extension moves cards with pointer-based drag and drop. If you cannot use that interaction, note the issue number on the board, open the issue in **My work**, then select **New session**. This creates the same issue-grounded session without moving the card.

The Canvas provides a visual way to select and begin work while keeping the agent grounded in the issue.

## Summary and next steps

You used a shared visual surface to start an agent session. Continue to [Lesson 8: Review and next steps][next-lesson].

[canvas-gallery]: https://awesome-copilot.github.com/extensions/
[kanban-extension]: https://awesome-copilot.github.com/extension/accessibility-kanban/
[next-lesson]: ../8-review/
