---
slug: vscode/7-foundry-toolkit
title: "Optional: Incorporate Foundry"
description: "Build a grounded Backer Concierge with VS Code and Microsoft Foundry Toolkit in three focused modules."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← Previous lesson: Iterating on GitHub Copilot's work][previous-lesson] |
|:--|

The required VS Code harness is complete after Exercise 6. This optional extension uses GitHub Copilot Chat and Microsoft Foundry Toolkit in VS Code to turn the Tailspin catalog into a Backer Concierge, deploy it as a hosted agent, and connect it to the site through a local proxy.

## Scenario

Backers ask questions that filters cannot answer: which game suits someone who loves git puns, or what makes one puzzle game a better fit than another? Tailspin Toys needs a concierge that recommends real catalog titles, asks a clarifying question when needed, and earns trust by admitting when funding numbers or other facts are unavailable.

## Modules

Each module ends with a working checkpoint. The same learner repository, feature branch, and Foundry project carry through all three; there is no project recreation between modules.

| Module | Completion checkpoint |
|--------|-----------------------|
| [1. Prepare a project and model][module-1] | Catalog exported and deployed model tested against grounding rules |
| [2. Build and deploy an agent][module-2] | Local agent debugged and hosted agent tested |
| [3. Connect the agent to the site][module-3] | Local proxy and accessible widget tested end to end |

> [!IMPORTANT]
> Microsoft Foundry Toolkit and hosted agents are in public preview. These modules create billable Azure resources, including a model deployment and a hosted agent. Subscription permissions, region availability, quota, and cost can limit participation.

## Before you begin

The extension builds on your Tailspin Toys repository, not the workshop documentation repository.

1. Confirm the required workshop work is saved, committed, and pushed before starting the optional feature.
2. Start with [Prepare a project and model][module-1]. If resuming, reopen your Tailspin Toys repository on the `foundry-agent-vscode` branch and confirm the `tailspin-toys` project and its model deployment still exist under **Foundry Toolkit** > **My Resources**.
3. When stopping after any module, follow [Clean up your resources][cleanup] unless you intentionally keep resources for the next module and accept ongoing costs.

## Clean up your resources

When you're done experimenting at any checkpoint, remove the Azure resources to avoid unwanted costs. Cleanup removes resources needed by later modules, so continuing afterward requires recreating them.

> [!WARNING]
> Only delete `rg-tailspin-toys` if it is dedicated to this exercise and contains no resources you need to keep. Deleting a shared resource group would remove unrelated resources too.
>
> If you approved a different resource-group name in module 1, substitute it for `rg-tailspin-toys` in every command below.

1. Stop any local Agent Inspector debug session, Azure Functions host, or Astro development server you started in its terminal.
2. If you deployed the hosted agent in module 2, open a terminal in the generated agent directory that contains `azure.yaml`, select the same `azd` environment, then run:

   ```bash
   azd down --purge
   ```

3. Check the selected subscription and whether the workshop resource group still exists:

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   If the command returns `false`, cleanup is complete. If it returns `true`, inspect the resources in the group:

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   Verify that all remaining resources belong to this exercise. If you stopped after module 1, the Foundry project and model still need cleanup even though you did not deploy an `azd` service.

4. If the dedicated workshop resource group still exists and contains only resources you intend to remove, run:

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. Because `--no-wait` returns before deletion completes, rerun the following command until it returns `false`:

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## Resources

- [Foundry Toolkit for Visual Studio Code][foundry-toolkit]
- [Microsoft Foundry agent extension overview][foundry-extension]

| [Next module: Prepare a project and model →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #clean-up-your-resources
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
