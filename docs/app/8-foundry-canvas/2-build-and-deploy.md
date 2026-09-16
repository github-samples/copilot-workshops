---
title: "Build and deploy the agent"
description: "Scaffold the Backer Concierge in Canvas, inspect it locally, and deploy and retest it in Foundry."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/app/8-foundry-canvas/1-project-and-model/
  label: Prepare project and model
next:
  link: /copilot-workshops/app/8-foundry-canvas/3-connect-to-site/
  label: Connect the agent to the site
---

This module turns the project, model deployment, and catalog from [Prepare project and model][previous-module] into a hosted Backer Concierge through Microsoft Foundry Canvas.

By the end, you will have:

- A scaffolded agent with packaged catalog data and focused tests.
- Local evidence for each catalog and conversation acceptance criterion.
- A deployed agent version retested in Foundry.

## Scenario

Tailspin Toys needs a concierge that can answer real catalog questions, admit when information is missing, and remember the games discussed in a conversation. The service must earn that trust before it becomes part of the storefront.

## Resume the project and prepare deployment tools

Hosted-agent inspection and deployment use Azure Developer CLI through Canvas; the existing Foundry project and model are reused.

1. Resume the same Tailspin Toys repository, worktree branch, and **Add a Backer Concierge assistant for catalog questions** issue session from module 1. Confirm `db/catalog.json`, your recorded subscription, dedicated resource group, Foundry project, and model deployment are intact. If resources were cleaned up, repeat the relevant [project-and-model setup][previous-module] first; otherwise do not recreate them.
2. Install the [Azure Developer CLI][install-azd], then verify that version 1.27.1 or later is installed:

   ```bash
   azd version
   ```

3. Select **+**, select **Terminal**, and sign in to Azure Developer CLI, completing authentication in the browser when prompted:

   ```bash
   azd auth login
   ```

4. Run `azd config show` to verify your Azure subscription. If it is empty or incorrect, update it with `azd config set defaults.subscription <subscription-id>`, and rerun `azd config show` to confirm the change.
5. Reopen Microsoft Foundry Canvas in this session and confirm the same **tailspin-toys** project and deployment under **Models**. Check the subscription, region, quota, and estimated cost before each cost-bearing change.

> [!IMPORTANT]
> Microsoft Foundry Canvas and hosted agents are in public preview. Local model calls and hosted Azure resources can incur costs; the [shared cleanup][cleanup] also applies when stopping at a hosted deployment.

## Scaffold the Backer Concierge

Canvas scaffolds the code, folder structure, and root `azure.yaml` that connect the Backer Concierge to your existing model deployment.

6. In **Create new hosted agents** preview, enter:

   ```plaintext
   Scaffold a hosted agent named Backer Concierge in agent/backer-concierge, connected to the tailspin-toys project and the model deployment I just confirmed. Use Microsoft Agent Framework with the Responses API. Ground it in db/catalog.json and ensure it meets the acceptance criteria in this issue. Keep a single azure.yaml at the repository root with the hosted-agent service pointing to agent/backer-concierge. Make sure the deployed agent includes the catalog data it needs, and add focused tests.
   ```

   Canvas sends the prompt and current subscription and Foundry project context to Copilot. It looks for Agent Framework + Responses API samples; a selection such as **Agent with Local Tools (Responses, Agent Framework, Python)** may appear.

   ![Scaffold Backer Concierge agent in Canvas](../../_images/app-8-scaffold-backer-concierge.png)

7. Review Copilot's changes in the **Files** tab against this checkpoint. Generated filenames inside `src` can differ, but the project boundaries and `azure.yaml` location should match:

   - The agent lives in `agent/backer-concierge`.
   - A single `azure.yaml` at the repository root contains a service with `host: azure.ai.agent`.
   - The deployable agent includes its own generated copy of the catalog.
   - Focused tests cover catalog grounding requirements.
   - No credentials or local environment files are included.

   ```text
   tailspin-toys/
   ├── azure.yaml
   ├── agent/
   │   └── backer-concierge/
   │       └── requirements.txt
   ├── db/
   │   └── catalog.json
   └── src/
   ```

8. Check **Build current hosted agent** for the existing project and model connection. Ask Copilot to run the focused tests and fix any failures before continuing to **Deploy and test**.

## Inspect the agent locally

**Inspect Locally** runs `azd ai agent run` in the Copilot integrated terminal, waits for the hosted agent to start, and opens the embedded Agent Inspector.

9. In **Deploy and test**, select **Inspect Locally** and wait for Agent Inspector to open.

> [!NOTE]
> The first local run can take several minutes while `azd` creates an environment and installs dependencies.

10. If the inspector cannot connect, confirm that no other process is using the required port, send the error to Copilot, and retry after the issue is fixed.
11. Test a **grounded recommendation** in Agent Inspector:

    ```text
    I love puzzle games about tracking down bugs. What should I back?
    ```

    Expected: Names only real titles from the catalog and uses the correct information for each title.

    ![Grounded recommendation in Agent Inspector](../../_images/app-8-grounded-recommendation.png)

12. Test a **hallucination trap**:

    ```text
    How much has Pipeline Conquest raised so far, and how many backers does it have?
    ```

    Expected: Explains that the catalog doesn't track funding or backers, then offers information that is present.

13. Test **out-of-catalog pressure**:

    ```text
    Do you have Wingspan? If not, what's the closest thing you've got?
    ```

    Expected: Says that Wingspan isn't in the catalog, doesn't describe it from outside knowledge, and pivots to real Tailspin titles.

14. Test a **vague request**:

    ```text
    Recommend me something good.
    ```

    Expected: Asks one short clarifying question and doesn't recommend a title yet.

15. Test **ranking accuracy**:

    ```text
    What are your three highest rated games?
    ```

    Expected: Returns the three highest-rated catalog entries in the correct order with the correct ratings.

16. Test **conversation continuity** by sending these prompts in the same conversation:

    ```text
    Show me two highly rated strategy games.
    ```

    ```text
    Which of those has the higher rating?
    ```

    Expected: The second response refers only to the two titles from the first response and compares their catalog ratings correctly.

17. Compare every response with `db/catalog.json` and the issue's acceptance criteria. Confirm the agent never invents games, publishers, ratings, funding totals, backer counts, prices, player counts, play times, or release dates. If Agent Inspector reports an error or a response crosses the grounding boundary, copy the result into the Canvas prompt area and ask Copilot to fix it. Restart local inspection and rerun the failed test after every change, then confirm all six checks pass before deploying.

## Deploy and retest the hosted agent

Canvas uses `azd` to deploy the tested agent. Foundry packages the service source, resolves dependencies, builds it remotely, and publishes it to Foundry Agent Service.

18. Confirm the selected subscription, existing project, model deployment, and dedicated resource targets. On Canvas, in **Deploy and test**, select **Deploy to Foundry**. Review the prompt it drops into chat and approve deployment only after checking its targets and cost.

    ![Deploy to Foundry prompt on the canvas](../../_images/app-8-deploy-to-foundry.png)

19. Check for a deployment confirmation, agent version, status, and link to the agent playground in Foundry. If deployment fails, send the error to Copilot and resolve it in the same project before retrying through Canvas.
20. Select **Test in Foundry Portal** from Canvas to open the deployed agent playground. Rerun all six acceptance checks from steps 11–16 against this deployed version, retaining the paired prompts in one conversation for continuity. Compare its responses with the catalog; if any check fails, ask Copilot to fix it, rerun local tests, redeploy through Canvas, and retest the hosted version.

## Checkpoint and next steps

The handoff is a tested hosted agent, with no website integration required yet.

21. Record the passing focused tests, local inspection results, hosted retest results, agent version, status, and server-side connection details in the same issue session, without recording credentials. Retain the same Tailspin Toys repository, worktree branch, issue session, Foundry project, and model deployment from module 1.
22. Continue to [Connect the agent to the site][next-module] using this exact checkpoint, or stop at the hosted deployment and follow [Clean up your resources][cleanup] when finished. The site proxy and widget are not prerequisites for cleanup.

[previous-module]: ../1-project-and-model/
[next-module]: ../3-connect-to-site/
[cleanup]: ../#clean-up-your-resources
[install-azd]: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
