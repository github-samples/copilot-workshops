---
title: "Lesson 4 - Work with issues and sessions"
description: "Create a focused backlog, select an issue, and implement it in an isolated worktree."
authors:
  - jamesmontemagno
lastUpdated: 2026-09-16
---

Ask the agent to suggest focused product improvements, turn those ideas into GitHub issues, and implement one issue in an isolated session.

In this lesson, you will:

- create three focused issues for the Space Quiz.
- compare their scope and acceptance criteria.
- start a session from an issue.
- implement and verify the issue in an isolated worktree.

## Create a backlog

Send the following prompt:

```plaintext
Review the space quiz and suggest three focused feature ideas that could each be completed in a short session. Create a separate GitHub issue for each idea with a clear title, user-focused description, and acceptance criteria. Do not implement them yet.
```

Open **My work**, review the three issues, and choose one that has clear value and a manageable scope.

## Implement an issue

1. Open the selected issue in **My work**.
2. Select **New session**.
3. Choose a **new worktree** when prompted.
4. Use **Interactive** mode and **GPT-5.3-Codex**, or choose **Auto** as the fallback.
5. Send the following prompt:

   ```plaintext
   Implement this issue completely. Keep the single-file, dependency-free design, test the behavior in the integrated browser, and summarize the changes when finished.
   ```

6. Review the diff.
7. Test the feature in the integrated browser and confirm that it meets the issue's acceptance criteria.

The new worktree keeps this feature isolated from your default branch until you are ready to review and merge it.

## Summary and next steps

You created a backlog and implemented one issue in an isolated session. Continue to [Lesson 5: Complete the Copilot review loop][next-lesson].

[next-lesson]: ../5-review/
