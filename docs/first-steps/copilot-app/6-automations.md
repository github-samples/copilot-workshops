---
title: "Lesson 6 - Automate issue triage"
description: "Create and run a weekly automation that summarizes recent open issues."
authors:
  - jamesmontemagno
lastUpdated: 2026-09-16
---

Use an automation to turn a recurring issue-triage task into a scheduled agent workflow.

In this lesson, you will:

- create a weekly automation.
- connect the automation to the Space Quiz project.
- run the automation immediately and review its result.

## Create the automation

1. Open **Automations**.
2. Choose the template for a new weekly automation.
3. Enter the following prompt:

   ```plaintext
   Review the latest GitHub issues created and still open in the last week, and provide a summary table ranked by severity and priority.
   ```

4. Set the session mode to **Autopilot**.
5. Set the model to **Auto**.
6. Select the `space-quiz` project.
7. Open the **Create** dropdown, then select **Create and run**.

Review the generated summary and confirm that it references the recent open issues in your repository.

## Summary and next steps

You created a reusable agent workflow that runs on a schedule. Continue to [Lesson 7: Explore a Canvas][next-lesson].

[next-lesson]: ../7-canvas/
