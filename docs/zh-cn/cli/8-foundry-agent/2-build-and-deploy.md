---
title: "模块 2 - 构建并部署智能体"
description: "使用 GitHub Copilot CLI 和 Microsoft Foundry 技能，为 Backer Concierge 生成脚手架、进行测试并部署。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

在[模块 1][previous-lesson]中，已经准备好目录并测试了已部署的模型。本模块是[可选礼宾助手系列][overview]的第二个模块，将在此基础上构建托管智能体。

在本模块中，将完成以下任务：

- 生成智能体脚手架，并为其提供可随服务部署的独立目录副本。
- 在本地测试回答是否依据目录，以及对话是否连贯。
- 部署智能体并进行远程调用。

## 场景

Tailspin Toys 需要的不只是模型的一次性回答。支持者希望礼宾助手记住刚刚推荐的游戏，并回答关于这些游戏的后续问题。团队还需要确保，当礼宾助手从开发者的计算机迁移到托管服务后，回答仍然可靠。

## 继续使用现有项目

本模块基于模块 1 中已经可用的模型展开。将继续使用同一个项目和部署，而不是再创建一组 Azure 资源。

1. 返回 Tailspin Toys 存储库的 `foundry-agent-cli` 分支，以及模块 1 中的 Copilot CLI 会话。
2. 确认 `db/catalog.json` 可用，并且仍保留模型测试时使用的 Foundry 项目、所选模型部署和 Azure 登录状态。如果尚未完成这些设置，请先完成[准备项目和模型][previous-lesson]。

> [!IMPORTANT]
> 托管智能体目前处于公共预览阶段，会创建计费的 Azure 资源。如果在本模块后停止，也应按照[清理说明][cleanup]操作。

## 生成 Backer Concierge 智能体脚手架

现在将让 Microsoft Foundry 技能在现有 Tailspin Toys 存储库中生成托管智能体脚手架，然后在运行前检查其打包和配置。

1. 在 Copilot CLI 中输入以下提示：

    ```text
    Use the Microsoft Foundry Skill to scaffold a hosted Backer Concierge in this existing repository using the project and model deployment we selected. Start from the Python 3.13 Basic hosted-agent sample, use Microsoft Agent Framework with the Responses API and code deployment, and keep the agent in agent/backer-concierge. Keep one azure.yaml at the repository root with a service using host: azure.ai.agent.

    Ground every answer in db/catalog.json. Never invent games, publishers, ratings, funding totals, backer counts, pledge tiers, prices, player counts, play times, or release dates. Ask one short clarifying question when a request is vague and preserve conversation context. Ensure the catalog is copied into the deployable service during preparation so the deployed agent never depends on a file outside its service directory. Add focused tests for catalog loading and grounding behavior.

    Scaffold and test locally, but do not deploy the hosted agent yet. Stop and ask me to authenticate if needed.
    ```

2. 关注会话中关于 Foundry 项目、模型部署、智能体名称或环境的问题。
3. Copilot 完成后，查看更改：

    ```text
    /diff
    ```

    确认以下内容：

    - `azure.yaml` 包含一个使用 `host: azure.ai.agent` 的服务。
    - 该服务指向 `agent/backer-concierge`。
    - 部署的服务包包含自动生成的独立目录副本。
    - 通过一个脚本或构建步骤从 `db/catalog.json` 更新该副本，而不是手动维护两个目录文件。
    - 智能体使用所选模型部署和 Responses API。
    - 说明明确禁止使用目录中不存在的事实。
    - 没有凭据、访问令牌、`.env` 文件或 `.azure` 环境文件被暂存以待提交。

    生成脚手架后，以以下结构为检查标准：

    ```text
    tailspin-toys/
    ├── azure.yaml
    ├── agent/
    │   └── backer-concierge/
    │       ├── catalog.json
    │       └── requirements.txt
    ├── db/
    │   └── catalog.json
    └── src/
    ```

> [!IMPORTANT]
> `azd deploy` 会打包托管智能体的服务目录。如果运行时从 `agent/backer-concierge` 引用存储库级别的 `db/catalog.json`，可能在本地有效，但部署后失败。部署之前，生成的副本必须位于 `agent/backer-concierge/` 目录中。

4. 启动服务之前，让 Copilot 运行针对性测试并检查生成的配置：

    ```text
    Run the focused Backer Concierge tests. Then verify that the selected model deployment, Responses API protocol, service path, startup command, catalog preparation step, and azure.ai.agent host configuration are consistent. Fix only problems in this hosted-agent project and rerun the failed checks.
    ```

    只有针对性测试通过后，才能继续。

    ![验证智能体脚手架](../../../_images/cli-8-verify-generated-agent.png)

## 在本地测试智能体

现在将通过智能体的本地 Responses API，检查其回答是否依据目录，以及对话行为是否符合预期。本地智能体服务运行时会占用终端，因此请在当前终端中保持 Copilot CLI 打开，并从第二个终端启动智能体。

1. 按 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 打开另一个终端。
2. 在 Tailspin Toys 存储库根目录中运行：

    ```bash
    azd ai agent run
    ```

    首次在本地运行时，会创建 Python 环境、安装依赖项并启动托管智能体。保持此终端中的服务运行。

3. 返回第一个终端中的 Copilot CLI 并输入：

    ```text
    Test the running Backer Concierge through its Responses API. Run each acceptance prompt below, preserve the response ID for the two-turn conversation test, and compare every response with the expected behavior. Show a concise pass or fail table and the evidence for any failure. Do not change code yet.

    1. "I love puzzle games about tracking down bugs. What should I back?" Expected: only real catalog titles with correct details.
    2. "How much has Pipeline Conquest raised so far, and how many backers does it have?" Expected: explains that the catalog doesn't track funding or backers, then offers known information.
    3. "I need something for four players, about an hour long." Expected: explains that player count and play time are missing, then asks one actionable follow-up question.
    4. "Do you have Wingspan? If not, what's the closest thing you've got?" Expected: says Wingspan isn't in the catalog, doesn't describe it from outside knowledge, and pivots to catalog titles.
    5. "Recommend me something good." Expected: asks one short clarifying question and doesn't recommend a title yet.
    6. "What are your three highest rated games?" Expected: the three highest-rated catalog entries in the correct order with correct ratings.
    7. In one conversation, send "Show me two highly rated strategy games." followed by "Which of those has the higher rating?" Expected: the second response compares only the two earlier titles using catalog ratings.
    ```

    ![托管智能体部署测试通过](../../../_images/cli-8-passing-acceptance-scenarios.png)

4. 查看结果。如果无法连接智能体，请确认第二个终端中的服务仍在运行。如果测试失败，让 Copilot 仅修复本地缺陷、运行针对性测试，并告知何时需要重启 `azd ai agent run`。每次更改后，都要重启服务并重新运行失败的验收测试。

## 部署托管智能体

本地验收测试通过后，就可以将智能体部署到 Microsoft Foundry。将继续使用由技能引导的工作流程，检查部署准备情况并测试远程终结点。

1. 所有验收测试通过后，按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 停止本地服务。
2. 返回 Copilot CLI 并输入以下提示。在批准部署之前，检查建议的资源和预估费用：

    ```text
    Continue with the Microsoft Foundry Skill workflow. Review the hosted agent for deployment readiness, then deploy it to Microsoft Foundry, show the deployment status and playground link, and invoke it remotely with: "I love puzzle games about tracking down bugs. What should I back?"
    ```

3. 如果系统提示选择评估套件来源，请选择 **No, set it up later**（否，稍后设置）。

    ![托管智能体部署状态和操练场链接](../../../_images/cli-8-hosted-agent-deployment.png)

4. 查看部署状态和远程回答。确认智能体正在运行，且仅推荐目录中真实存在的游戏。如果部署或调用失败，请让 Copilot 诊断故障，并在继续之前重复远程测试。

通过显示的操练场链接，可以在 Microsoft Foundry 门户中与已部署的托管智能体交互。

由技能引导的工作流程使用 `azd deploy` 打包服务源代码、解析依赖项、执行远程构建，并发布到 Microsoft Foundry。它通过 Foundry 调用流程测试已部署的终结点。

## 总结和后续步骤

本模块生成了包含可部署目录副本的智能体脚手架，测试了回答的信息依据和对话连贯性，并验证了 Microsoft Foundry 的远程回答。现在已经拥有一个可用的托管 Backer Concierge。

接下来，将继续使用同一个存储库、分支、Copilot CLI 会话和已部署的智能体，[将礼宾助手连接到网站][next-lesson]。如果托管智能体已足以满足探索需求，可以到此为止，并[清理 Azure 资源][cleanup]。

[overview]: ../
[previous-lesson]: ../1-project-and-model/
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#清理资源
