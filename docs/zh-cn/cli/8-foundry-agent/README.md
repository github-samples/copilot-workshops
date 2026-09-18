---
slug: zh-cn/cli/8-foundry-agent
title: "可选：集成 Foundry"
description: "通过三个模块准备模型、构建并部署基于目录的智能体，以及将其连接到 Tailspin Toys。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

本可选系列使用 GitHub Copilot CLI 和 Microsoft Foundry 技能，将 Tailspin Toys 目录变为对话助手。三个模块将从项目和模型设置开始，逐步构建托管智能体，并完成可用的网站集成。

在本系列中，将完成以下任务：

- 准备 Azure 环境，并使用目录测试模型。
- 为托管的 Backer Concierge 智能体生成脚手架，进行测试并部署。
- 通过本地服务端代理和聊天组件，将智能体连接到网站。

## 场景

Tailspin Toys 支持者可以按类别和发行商浏览游戏，但这些筛选条件无法帮助所有人找到下一款游戏。有些支持者会问：*喜欢 Git 双关语的人适合哪些游戏？* 下拉选项无法回答这类问题。

Tailspin Toys 希望打造一个 **Backer Concierge** 礼宾助手，通过对话帮助支持者发现游戏。它应推荐 Tailspin 目录中的游戏，在偏好不明确时提出一个简短的澄清问题，并在支持者追问时记住之前的推荐。

支持者需要可信的回答。礼宾助手应仅使用目录中的信息，并在某个细节不可用时明确说明，而不是编造游戏、发行商、评分、筹款总额、支持者人数、价格、玩家人数、游戏时长或发布日期。

## 选择下一步

这些模块在同一个 Tailspin Toys 存储库、分支和 Foundry 项目中逐步推进。每个模块结束时都会得到一个可用的阶段成果。

| 模块 | 将完成的任务 | 完成标志 |
| --- | --- | --- |
| [1. 准备项目和模型][project-model] | 设置工具、导出目录，以及选择和测试模型 | 一个能够正确回答目录问题的已部署模型 |
| [2. 构建并部署智能体][build-deploy] | 生成智能体脚手架、测试其行为，并部署到 Foundry | 一个可用的托管 Backer Concierge |
| [3. 将智能体连接到网站][connect-site] | 构建本地代理和聊天组件，然后测试完整流程 | 可通过本地网站使用的礼宾助手 |

> [!IMPORTANT]
> Microsoft Foundry 托管智能体目前处于公共预览阶段。
>
> 本系列会创建计费的 Azure 资源，包括模型部署和托管智能体。创建资源前，需要检查所选订阅、区域、配额和预估费用。即使在第一个或第二个模块后停止，也应按照[清理说明][cleanup]操作。

1. 要开始本可选系列，请继续学习[准备项目和模型][project-model]，其中包含设置说明。
2. 如果更想完成核心工作坊，请继续学习[回顾与后续步骤][review]。

## 清理资源

在任意阶段结束实验后，移除 Azure 资源以避免不必要的费用。清理会移除后续模块所需的资源，因此之后若要继续学习，就需要重新创建这些资源。

> [!CAUTION]
> 只有当 `rg-tailspin-toys` 专用于本练习，且不包含任何需要保留的资源时，才可将其删除。删除共享资源组也会移除与本练习无关的资源。

1. 在各自的终端中按 <kbd>Ctrl</kbd>+<kbd>C</kbd>，停止此前启动的所有本地智能体、Function 或 Astro 开发服务器。
2. 退出 Copilot CLI。如果在模块 2 中生成了智能体脚手架，请在 Tailspin Toys 存储库根目录中，使用同一个 `azd` 环境运行以下命令：

    ```bash
    azd down --purge
    ```

3. 使用 `az account show` 检查所选订阅。查看该订阅中的 `rg-tailspin-toys`，确认所有剩余资源都属于本练习。如果在模块 1 后停止，即使尚未生成 `azd` 服务脚手架，也仍需清理 Foundry 项目和模型。
4. 如果工作坊专用资源组仍然存在，且仅包含打算移除的资源，请运行：

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. 在 Azure 门户中确认资源组删除已完成。`--no-wait` 命令会在删除完成前返回。

## 资源

- [Azure Skills 插件][azure-skills]
- [在编码智能体中使用 Microsoft Foundry 技能][foundry-skill]
- [使用 Microsoft Foundry 技能部署第一个托管智能体][hosted-agent-quickstart]
- [托管智能体权限][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #清理资源
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
