---
slug: zh-cn/vscode/7-foundry-toolkit
title: "可选：集成 Foundry"
description: "通过三个聚焦的模块，使用 VS Code 和 Microsoft Foundry Toolkit 构建基于目录数据的 Backer Concierge。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 上一课：迭代 GitHub Copilot 的工作][previous-lesson] |
|:--|

完成练习 6 后，VS Code 学习路径的必修部分就结束了。本可选扩展使用 VS Code 中的 GitHub Copilot Chat 和 Microsoft Foundry Toolkit，将 Tailspin 目录转化为 Backer Concierge，将其部署为托管代理，并通过本地代理服务连接到网站。

## 场景

支持者提出的问题，往往不是筛选器能够回答的：哪款游戏适合喜欢 git 双关语的人？一款解谜游戏为什么比另一款更适合自己？Tailspin Toys 需要一位推荐助手，能够推荐目录中真实存在的游戏，在必要时提出澄清问题，并在缺少筹款金额或其他信息时坦诚说明，以此赢得信任。

## 模块

每个模块都以可运行的成果作为完成检查点。三个模块始终使用同一个学员存储库、功能分支和 Foundry 项目，模块之间无需重新创建项目。

| 模块 | 完成检查点 |
|--------|-----------------------|
| [1. 准备项目和模型][module-1] | 已导出目录，并根据数据依据规则测试已部署的模型 |
| [2. 构建并部署代理][module-2] | 已调试本地代理，并测试托管代理 |
| [3. 将代理连接到网站][module-3] | 已对本地代理服务和无障碍小组件进行端到端测试 |

> [!IMPORTANT]
> Microsoft Foundry Toolkit 和托管代理目前处于公共预览阶段。这些模块会创建计费的 Azure 资源，包括模型部署和托管代理。订阅权限、区域可用性、配额和费用可能限制参与。

## 开始之前

本扩展基于学员的 Tailspin Toys 存储库，而不是工作坊文档存储库。

1. 开始可选功能前，确认必修工作坊中的工作已保存、提交并推送。
2. 从[准备项目和模型][module-1]开始。如果是继续之前的工作，请在 `foundry-agent-vscode` 分支上重新打开 Tailspin Toys 存储库，并确认 **Foundry Toolkit** > **My Resources** 中仍有 `tailspin-toys` 项目及其模型部署。
3. 完成任一模块后如果要停止，请执行[清理资源][cleanup]，除非决定为下一个模块保留资源，并接受持续产生的费用。

## 清理资源

在任一检查点结束练习后，请删除 Azure 资源，以免产生不必要的费用。清理会删除后续模块所需的资源，之后若要继续，需要重新创建。

> [!WARNING]
> 只有当 `rg-tailspin-toys` 专用于本练习，且不包含需要保留的资源时，才删除该资源组。删除共享资源组会连带移除无关资源。
>
> 如果在模块 1 中批准了其他资源组名称，请在下面所有命令中将 `rg-tailspin-toys` 替换为该名称。

1. 在各自的终端中停止已启动的 Agent Inspector 调试会话、Azure Functions 主机和 Astro 开发服务器。
2. 如果在模块 2 中部署了托管代理，请在包含 `azure.yaml` 的生成代理目录中打开终端，选择同一个 `azd` 环境，然后运行：

   ```bash
   azd down --purge
   ```

3. 检查所选订阅以及工作坊资源组是否仍然存在：

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   如果命令返回 `false`，说明清理已完成。如果返回 `true`，请检查该资源组中的资源：

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   确认剩余资源全部属于本练习。如果在模块 1 后停止，即使没有部署 `azd` 服务，仍需要清理 Foundry 项目和模型。

4. 如果工作坊专用资源组仍然存在，且仅包含打算移除的资源，请运行：

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. 由于 `--no-wait` 会在删除完成前返回，请反复运行以下命令，直到返回 `false`：

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## 资源

- [适用于 Visual Studio Code 的 Foundry Toolkit][foundry-toolkit]
- [Microsoft Foundry 代理扩展概述][foundry-extension]

| [下一模块：准备项目和模型 →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #清理资源
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
