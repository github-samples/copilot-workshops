---
title: "Optional: Incorporate Foundry"
slug: app/8-foundry-canvas
description: "Build a catalog-grounded Backer Concierge with Microsoft Foundry Canvas, with safe stopping points along the way."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/app/9-review/
  label: Review and next steps
next:
  link: /copilot-workshops/app/8-foundry-canvas/1-project-and-model/
  label: Prepare project and model
---

This optional journey adds a **Backer Concierge** to Tailspin Toys using Microsoft Foundry Canvas in the GitHub Copilot app. It moves from a catalog-grounded model experiment to a hosted agent and then a local website integration.

## The journey

Each module ends with a checkpoint and a safe stopping point. The same Tailspin Toys repository, worktree branch, issue-linked session, Foundry project, and model deployment carry through the journey.

- [Prepare project and model][module-1] establishes the catalog boundary, creates the project and model deployment, and checks them in Canvas.
- [Build and deploy the agent][module-2] scaffolds the Backer Concierge, tests it locally, and deploys and retests the hosted agent.
- [Connect the agent to the site][module-3] adds a local credential-safe proxy, an accessible chat widget, end-to-end tests, and Agent merge.

> [!IMPORTANT]
> Microsoft Foundry Canvas and hosted agents are in public preview.
>
> This journey creates billable Azure resources, including a model deployment and, from module 2, a hosted agent. Subscription, region, quota, and estimated cost need approval before resource creation. Cleanup applies even when stopping after only the project and model.

1. Begin with [Prepare project and model][module-1], keeping the work in your Tailspin Toys repository rather than this workshop content repository.
2. At your chosen stopping point—project and model, hosted deployment, or full integration—record the module's checkpoint and follow the shared cleanup below when you are finished experimenting. Continuing later after cleanup requires restoring the deleted resources and rechecking their configuration.

## Clean up your resources

Cleanup depends on how far you went. A project-and-model-only run has no requirement for `azure.yaml`, an `azd` environment, or a hosted agent.

> [!WARNING]
> Resource deletion is destructive. Only resources dedicated to this workshop are eligible for deletion here. A shared resource group must never be deleted; individually removing workshop resources with the resource owner is the safe alternative.

1. Stop any local Agent Inspector, Azure Function, and Astro development server processes you started, using their terminals. Record any checkpoint details you need before deleting Azure resources.
2. In the Azure portal, confirm the active subscription ID, the exact workshop resource group name, and every resource it contains. Check that the Foundry project and model deployment belong to this run. If the subscription, ownership, or contents are unclear, stop cleanup until you have resolved them.
3. Choose the cleanup path for your stopping point. If you completed only module 1, skip the next step and use step 5; do not create `azure.yaml` or initialize `azd` just to clean up. If you deployed with Canvas in module 2 or 3, continue with step 4.
4. For a hosted deployment, open a terminal in the same Tailspin Toys worktree containing the root `azure.yaml`. Confirm that the selected `azd` environment targets this run's subscription and resources, review the resources to be deleted, and run the following only when all targets are dedicated to your workshop:

   ```bash
   azd down --purge
   ```

5. For a project-and-model-only run, or after `azd down` if the dedicated workshop resource group still exists, recheck the subscription, group name, and complete resource list in the portal. If the entire group is dedicated to this run and its name is exactly `rg-tailspin-toys`, run the following. If the name differs, use the verified dedicated name instead; if the group is shared, do not run this command and coordinate individual resource cleanup with its owner.

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. Verify in the Azure portal that deletion finishes; `--no-wait` returns before deletion is complete. Confirm that the workshop model deployment and any hosted-agent resources are gone, and resolve any remaining billable workshop resources without deleting shared resources.
7. Return to [Review and next steps][core-review] when your chosen checkpoint and cleanup are complete.

## Resources

The Microsoft documentation describes Canvas, hosted deployments, and their permissions.

- [What is Microsoft Foundry Canvas?][foundry-canvas]
- [Deploy your first hosted agent with Foundry Canvas][hosted-agent-quickstart]
- [Hosted agent permissions][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
