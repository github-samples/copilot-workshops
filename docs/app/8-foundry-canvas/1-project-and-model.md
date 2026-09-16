---
title: "Prepare project and model"
description: "Export the Tailspin catalog, create a Foundry project and model deployment, and validate them in Canvas."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/app/8-foundry-canvas/
  label: "Optional: Incorporate Foundry"
next:
  link: /copilot-workshops/app/8-foundry-canvas/2-build-and-deploy/
  label: Build and deploy the agent
---

This first module establishes the data and Azure resources for the Backer Concierge. No agent code or hosted deployment is needed yet.

By the end, you will have:

- A catalog export with explicit grounding limits.
- A Foundry project and a model deployment chosen for the feature requirements.
- A Canvas-validated deployment and a simple catalog-bounded model smoke check.

## Scenario

Tailspin Toys backers can filter games by category and publisher, but questions such as *Which games would suit someone who loves Git puns?* don't have dropdown answers. A Backer Concierge should recommend only games in the Tailspin catalog and never invent games, publishers, ratings, funding totals, backer counts, prices, player counts, play times, or release dates. A reliable catalog and a suitable model are the foundation for those answers.

## Prepare your tools and issue session

The setup connects the GitHub Copilot app to Azure while keeping all feature work together.

> [!IMPORTANT]
> Microsoft Foundry Canvas and hosted agents are in public preview. This module creates billable Azure resources. Subscription, region, quota, and estimated cost need checking before resource creation.

1. Confirm you have an Azure subscription, such as a [free Azure subscription with $200 credit][azure-free] or [Azure for Students with $100 credits][azure-students], and permission to create the workshop resources.
2. Install the [Azure CLI][install-azure-cli] for your OS, then verify the installation using `az version`. Azure Developer CLI setup is deferred until the hosted-agent module.
3. Open the GitHub Copilot app, open **Customize**, then select **Plugins**. Search for `microsoft-foundry` and select **Install** for the Microsoft Foundry plugin, which bundles Canvas and the Foundry skills.

   ![Install Microsoft Foundry plugin](../../_images/app-8-install-foundry-plugin.png)

4. In **Customize**, select **Plugins**, search for `azure` or select it from the **Featured** list, then select **Install** for the Azure plugin.
5. On the **My work** tab, find and open the issue titled **Add a Backer Concierge assistant for catalog questions** in your Tailspin Toys repository. Select **New session** to start an issue-linked session in a new worktree. Keep this repository, worktree branch, and issue session for all three modules.
6. Type `/microsoft-foundry`, then `/azure` to confirm both skills are installed and available; don't send any prompts yet. If a plugin does not appear immediately, restart the app, return to this same issue session, and check again.

## Generate the catalog export

The sample repository includes an export script that gives the agent a file it can read.

7. In this issue-linked worktree session, replace the default `/fix-issue` prompt in the prompt box with:

   ```plaintext
   Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
   ```

8. Review the command output. Copilot should run the equivalent of:

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

   ![Generate catalog export](../../_images/app-8-generate-catalog-export.png)

9. Open `db/catalog.json` and confirm it contains 21 games with a title, description, category, publisher, and star rating. Check its `note` field: the catalog doesn't contain funding totals, backer counts, pledge tiers, or release dates. Treat missing prices, player counts, and play times as unavailable too, rather than filling gaps from outside knowledge. If the export fails or differs, ask Copilot to investigate and rerun it before continuing.

   ![Catalog export open in the Copilot app](../../_images/app-8-view-catalog.png)

## Set up a Foundry project and model

Creating the project and deployment in chat first means Canvas connects only to resources that already exist.

10. Select **+**, select **Terminal**, and sign in to Azure:

    ```bash
    az login
    ```

11. Confirm the selected subscription, region, quota, and estimated cost before approving resource creation. Check in the Azure portal that `rg-tailspin-toys` is available for a dedicated workshop group. If that name belongs to unrelated or shared resources, stop and resolve a dedicated naming choice before using the following prompt; consistently use your approved names throughout the journey.
12. In the same issue session, enter:

    ```plaintext
    Use the Microsoft Foundry skill to create a resource group named rg-tailspin-toys and a Foundry project named tailspin-toys.
    ```

    ![Create Foundry project](../../_images/app-8-foundry-project-created.png)

13. Ask Copilot to recommend a model. The issue's acceptance criteria are already in context because the session started from the issue:

    ```plaintext
    Use the Microsoft Foundry skill to recommend two or three current chat models in the tailspin-toys project that meet this issue's acceptance criteria. Explain the tradeoffs and wait for me to choose.
    ```

14. Confirm Copilot loads the `microsoft-foundry` skill, then choose an available model based on its tradeoffs. The Microsoft Foundry hosted-agent quickstart currently uses `gpt-5.4-mini`, but availability and quota vary by region.

    ![Select model](../../_images/app-8-select-model.png)

15. Ask Copilot to deploy your selection, reviewing the target project and cost before approval:

    ```plaintext
    Deploy the model I selected to the tailspin-toys Foundry project, using the model name as the deployment name.
    ```

> [!TIP]
> Model availability changes over time. The model Copilot confirms is available in your project is the appropriate choice, rather than a hardcoded model from this module.

## Validate and smoke-test the model in Canvas

This check verifies the project and model before any agent code exists. A model smoke check is not a substitute for the hosted agent's grounding tests in module 2.

16. Select **+**, then **Canvas**, then **Microsoft Foundry (Preview)**.
17. Open the **More options** menu in the top-right corner of Canvas, then select **Sign in**.
18. Select the **tailspin-toys** Foundry project. Expand **Models** and confirm your deployment appears with the expected name and status.

    ![Validate project and model in Canvas](../../_images/app-8-validate-project-model.png)

19. In the same GitHub Copilot app issue session, ask Copilot to run a small authenticated request to the model deployment you confirmed in Canvas, using your existing local Azure sign-in. Have it supply two actual entries from `db/catalog.json` plus the catalog's `note`, request one recommendation using only that excerpt, and ask whether the excerpt supplies prices. Check that the recommendation uses the supplied entries and the response acknowledges that prices are unavailable. Keep credentials local or server-side, never in browser code or chat output; no agent scaffold is needed.
20. Compare the answer's title, publisher, and rating with the supplied entries. If the deployment cannot be tested, check the project, deployment status, access, and quota in Canvas and send the error to Copilot. If it invents details, make the excerpt-only instruction explicit and retry. Record the result without treating it as proof of full agent acceptance.

> [!NOTE]
> Canvas remembers the selected project when reopened. Its stages are **Create new hosted agents** for scaffolding, **Build current hosted agent** for connecting models, toolboxes, skills, and guardrails, and **Deploy and test** for local runs and deployment to Foundry Agent Service.

## Checkpoint and next steps

The handoff is a catalog export plus a tested model deployment, not a scaffolded agent.

21. Record the Tailspin Toys repository, current worktree branch, issue-linked session, subscription ID, dedicated resource group, Foundry project, model deployment name, catalog export result, and smoke-check evidence in this session. Confirm the selected project before every later cost-bearing change.
22. Continue to [Build and deploy the agent][next-module] in this same repository, worktree branch, issue session, Foundry project, and model deployment—do not create another project. If stopping here, follow [Clean up your resources][cleanup]; this stopping point needs neither `azure.yaml` nor `azd`.

[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azure-cli]: https://learn.microsoft.com/cli/azure/install-azure-cli
[next-module]: ../2-build-and-deploy/
[cleanup]: ../#clean-up-your-resources
