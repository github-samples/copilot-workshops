## Scenario

Tailspin Toys has some tech debt they'd like to address. The contractors initially hired to create the first version of the site left the documentation in an unideal state - and by that you'll notice it's completely lacking. As a first step, they'd like to see docstrings added to all functions in the application.

Additionally, the design team is ready to get to work on building the UX for managing games. They don't need a full implementation yet, but they at least need some endpoints they can use for testing. Specifically, they need endpoints for the games API which will allow them to create, update and delete games. This is currently a blocker, but there are other issues which are of higher priority at the moment.

These are both examples of tasks which can quickly find themselves deprioritized, and are great to assign to Copilot coding agent. Copilot coding agent can then work on them asynchronously, allowing the developer to focus on other tasks, then return to review Copilot's work and ensure everything is as expected.

## Setting up the dev environment for the Copilot coding agent

Creating code, regardless of who's involved, typically requires a specific environment and some setup scripts to be run to ensure everything is in a good state. This holds true when assigning tasks to Copilot, which is performing tasks in a similar fashion to a SWE.

Coding agent uses [GitHub Actions][github-actions] for its environment when doing its work. You can customize this environment by creating a [special setup workflow][setup-workflow], configured in the **.github/workflows/copilot-setup-steps.yml** file, to run before it gets to work. This enables it to have access to the required development tools and dependencies. This has been pre-configured ahead of the lab to help the lab flow and allow this learning opportunity. It makes sure that Copilot has access to Python, Node.JS, and the required dependencies for the client and server:

```yaml
name: "Copilot Setup Steps"

# Allows you to test the setup steps from your repository's "Actions" tab
on: workflow_dispatch

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # Backend setup - Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Python dependencies
        working-directory: ./server
        run: pip install -r requirements.txt

      # Frontend setup - Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"
          cache-dependency-path: "./client/package.json"

      - name: Install JavaScript dependencies
        working-directory: ./client
        run: npm ci
```

It looks like any other GitHub workflow file, but it has a few key points:

- It contains a single job called **copilot-setup-steps**. This job is executed in GitHub Actions before Copilot starts working on the pull request.
- Notice the **workflow_dispatch** trigger, which allows you to run the workflow manually from the Actions tab of your repository. This is useful for testing that the workflow runs successfully instead of waiting for Copilot to run it.

## Adding documentation

While everyone understands the importance of documentation, most projects have either outdated information or lack it altogether. This is the type of tech debt which often goes unaddressed, slowing productivity and making it more difficult to maintain the codebase or bring new developers into the team. Fortunately, Copilot shines at creating documentation, and this is a perfect issue to assign to Copilot coding agent. It'll work in the background to generate the necessary documentation. In a future exercise you'll return to review its work.

1. Navigate to your repository on github.com in a new browser tab.
2. Select the **Issues** tab.
3. Select **New issue** to open the new issue dialog.
4. Select **Blank issue** to create the new issue.
5. Set the **Title** to `Code lacks documentation`.
6. Set the **Description** to:
   
    ```plaintext
    Our organization has a requirement that all functions have docstrings or the language equivalent. Unfortunately, recent updates haven't followed this standard. We need to update the existing code to ensure docstrings (or the equivalent) are included with every function or method.
    ```

7. Select **Create** to create the issue.
8. On the right side, select **Assign to Copilot** to open the assignment dialog.

  ![Assigning Copilot to an issue](images/shared-assign-copilot.png)

9. Select **Assign**.

  ![Copilot assignment details](images/ex4-assign-copilot-details.png)

10. Select the **Pull Requests** tab.
11. Open the newly generated pull request (PR), which will be titled something similar to **[WIP]: Code lacks documentation**. If a new PR doesn't appear on the list, wait for a moment or two and refresh the browser window.
12. After a few minutes, you should see that Copilot has created a todo list.

> [!NOTE]
> It make take several minutes for the todo list from Copilot to appear in the PR. Copilot is creating its environment (running the workflow highlighted previously), analyzing the project, and determining the best approach to tackling the problem.

13. Review the list and the tasks it's going to complete.
14. Scroll down the pull request timeline, and you should see an update that Copilot has started working on the issue.
15. Select the **View session** button.

  ![Copilot session view](images/ex4-view-session.png)

> [!IMPORTANT]
> You may need to refresh the window to see the updated indicator.

16. Notice that you can scroll through the live session, and how Copilot is solving the problem. That includes exploring the code and understanding the state, how Copilot pauses to think and decide on the appropriate plan and also creating code.

This will likely take several minutes. One of the primary goals of Copilot coding agent is to allow it to perform tasks asynchronously, freeing us to focus on other tasks. We're going to take advantage of that very feature by both assigning another task to Copilot coding agent, then turning our attention to writing some code to add features to our application.

## Create new API endpoints

As has been highlighted, one of the great advantages of GitHub Copilot coding agent is the ability to divide work, where you can focus on one set of tasks while it focuses on another. While creating the endpoints for modifying games for the design team might not necessarily take a long time, it's still time which could be used for other tasks. Let's assign it to Copilot coding agent!

1. Return to your repository on github.com.
2. Select the **Issues** tab.
3. Select **New issue** to open the new issue dialogue.
4. Select **Blank issue** to use the blank template.
5. Set the **Title** to: `Add endpoints to create and edit games`
6. Set the **Description** to:

    ```markdown
    We're going to be creating functionality in the future to allow for the submission (and editing) of games. For now we just want the endpoints so we can explore how we want to create the UX and do some acceptance testing. Our requirements are:

   - Add new endpoints to the Games API to support creating, updating and deleting games
   - There should be appropriate error handling for all new endpoints
   - There should be unit tests created for all new endpoints
   - Before creating the PR, ensure all tests pass
    ```

7. Select **Create** to create the issue.
8. On the right side, select **Assign to Copilot** to open the assignment dialog.

  ![Assigning Copilot to an issue](images/shared-assign-copilot.png)

9. Select **Assign**.

Shortly after, you should see a set of 👀 on the first comment in the issue, indicating Copilot is on the job!

![Copilot uses the eyes emoji to indicate it's working on the issue](images/ex4-issue-eyes-emoji.png)

9. Select **Assign** to assign the issue to Copilot coding agent.

Copilot is now diligently working on your second request! Copilot coding agent works in a similar fashion to a SWE, so you don't need to actively monitor it, but instead review once it's completed. Let's turn your attention to writing code and adding other features.
