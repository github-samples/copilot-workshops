---
slug: cli/8-foundry-agent
title: "Optional: Incorporate Foundry"
description: "A three-module series to prepare a model, build and deploy a catalog-grounded agent, and connect it to Tailspin Toys."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

This optional series uses GitHub Copilot CLI and the Microsoft Foundry Skill to turn the Tailspin Toys catalog into a conversational assistant. The three modules take you from project and model setup to a hosted agent and a working website integration.

In this series, you will:

- prepare an Azure environment and test a model against the catalog.
- scaffold, test, and deploy a hosted Backer Concierge agent.
- connect the agent to the website through a local server-side proxy and chat widget.

## Scenario

Tailspin Toys backers can browse games by category and publisher, but those filters don't help everyone find their next game. Some backers have questions such as *Which games would suit someone who loves Git puns?* Those questions don't have dropdown answers.

Tailspin Toys wants a **Backer Concierge** that helps backers discover games through conversation. It should recommend games from the Tailspin catalog, ask a short clarifying question when someone's preferences are vague, and remember earlier recommendations when they ask a follow-up question.

Backers need answers they can trust. The concierge should use only information in the catalog and be clear when a detail isn't available, rather than inventing games, publishers, ratings, funding totals, backer counts, prices, player counts, play times, or release dates.

## Choose your next step

The modules build on one another in the same Tailspin Toys repository, branch, and Foundry project. Each ends with a working checkpoint.

| Module | What you'll do | Completion point |
| --- | --- | --- |
| [1. Prepare the project and model][project-model] | Set up the tools, export the catalog, and select and test a model | A deployed model that answers catalog questions correctly |
| [2. Build and deploy the agent][build-deploy] | Scaffold the agent, test its behavior, and deploy it to Foundry | A working hosted Backer Concierge |
| [3. Connect the agent to the website][connect-site] | Build a local proxy and chat widget, then test the complete flow | A concierge available through your local website |

> [!IMPORTANT]
> Microsoft Foundry hosted agents are in public preview.
>
> This series creates billable Azure resources, including a model deployment and a hosted agent. Resource creation requires a review of the selected subscription, region, quota, and estimated cost. The [cleanup instructions][cleanup] apply even if you stop after the first or second module.

1. To begin the optional series, continue to [Prepare the project and model][project-model]. Setup instructions are included there.
2. If you'd rather finish the core workshop, continue to [Review and next steps][review].

## Clean up your resources

When you're done experimenting at any checkpoint, remove the Azure resources to avoid unwanted costs. Cleanup removes resources needed by later modules, so continuing afterward requires recreating them.

> [!CAUTION]
> Only delete `rg-tailspin-toys` if it is dedicated to this exercise and contains no resources you need to keep. Deleting a shared resource group would remove unrelated resources too.

1. Stop any local agent, Function, or Astro dev server you started by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd> in its terminal.
2. Exit Copilot CLI. If you scaffolded the agent in Module 2, run the following from the Tailspin Toys repository root using the same `azd` environment:

    ```bash
    azd down --purge
    ```

3. Check the selected subscription with `az account show`. Inspect `rg-tailspin-toys` in that subscription and verify that all remaining resources belong to this exercise. If you stopped after Module 1, the Foundry project and model still need cleanup even though you haven't scaffolded an `azd` service.
4. If the dedicated workshop resource group still exists and contains only resources you intend to remove, run:

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. Confirm in the Azure portal that resource group deletion finishes. The `--no-wait` command returns before deletion completes.

## Resources

- [Azure Skills Plugin][azure-skills]
- [Use the Microsoft Foundry Skill in coding agents][foundry-skill]
- [Deploy your first hosted agent with the Microsoft Foundry Skill][hosted-agent-quickstart]
- [Hosted agent permissions][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #clean-up-your-resources
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
