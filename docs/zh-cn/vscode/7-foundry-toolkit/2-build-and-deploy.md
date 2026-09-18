---
title: "构建并部署代理"
description: "在 VS Code 中生成 Backer Concierge 框架并调试，然后将其部署为 Foundry 托管代理并测试。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 上一模块：准备项目和模型][previous-lesson] |
|:--|

本模块使用[准备项目和模型][previous-lesson]中的目录和已测试模型。Microsoft Foundry Toolkit 及其 **AIAgentExpert** 自定义代理将在 VS Code 中引导本地构建和托管部署。

## 目标

- 在现有 Tailspin Toys 工作区中，生成以目录数据为依据的代理框架。
- 使用 Agent Inspector 调试本地行为。
- 部署到现有 Foundry 项目，并验证托管代理。

## 场景

可信的推荐不能只在一次对话中成立。当支持者提出模糊问题，或坚持索取缺失的筹款详情时，Tailspin Toys 需要推荐助手始终遵守目录的信息边界。托管的推荐助手应当与私下测试时一样可靠。

## 继续使用工作区

代理使用现有模型部署，无需新建 Foundry 项目。

1. 在 VS Code 中打开同一个 Tailspin Toys 存储库，切换到 `foundry-agent-vscode` 分支。确认 `db/catalog.json` 存在，且 **Foundry Toolkit** > **My Resources** 下显示 `tailspin-toys` 项目和已测试的模型部署。
2. 确认已完成[上一个检查点][previous-lesson]。如果资源已清理，请先重新完成项目和模型的准备工作，再继续。
3. 如果尚未安装 Azure Developer CLI（`azd`），先安装它。托管代理部署需要使用此工具；仅选择适合当前操作系统的命令：

   ```bash
   # macOS / Linux
   curl -fsSL https://aka.ms/install-azd.sh | bash

   # Windows (PowerShell)
   winget install microsoft.azd
   ```

4. 登录现有项目所用的订阅：

   ```bash
   azd auth login
   ```

> [!IMPORTANT]
> 托管代理和 Foundry Toolkit 目前处于公共预览阶段。部署会创建计费资源。批准命令前，确认订阅、权限、区域、配额和预计费用。

## 创建并调试代理

工具包会在当前存储库中生成代码框架，并打开专用的 Copilot Chat。Agent Inspector 可以在部署前展示本地请求、事件和工具调用。

1. 选择 **Foundry Toolkit**，展开 **Developer Tools**，再展开 **+ Build**，然后选择 **+ Create Agent**。在 **Create Agent** 上，选择 **Code an agent with Copilot**。

   ![创建代理页面的截图。](../../../_images/vscode-create-agent.png)

2. 在新聊天中，确认已切换为 **AIAgentExpert**。将生成的提示替换为以下定制提示并提交：

   ```text
   /foundrytk-quick-start Create a backer concierge AI agent called 'Backer Concierge'. The agent should use the model I deployed to answer catalog questions and recommend games grounded strictly in db/catalog.json. Review the acceptance criteria in the issue titled 'Add a Backer Concierge assistant for catalog questions' and ensure the agent meets them. Generate the code into agent/backer-concierge in the current workspace and ask me if anything is unclear.
   ```

3. 审阅 `agent/backer-concierge` 下生成的代码。确认可部署的代理中包含目录、针对性测试通过，且不会提交凭据或本地环境文件。
4. 在活动栏中选择 **Run and Debug**，按 <kbd>F5</kbd> 启动调试器。确认 **Agent Inspector** 已加载并连接到代理服务器。
5. 复用[测试已部署的模型][model-tests]中的全部六个提示。根据完整的 `db/catalog.json` 检查回答，不要将九款游戏子集的排名当作完整目录的排名。
6. 在 **Input & Output**、**Events** 和 **Tools** 之间切换，检查请求与响应数据、会话事件和工具调用。如果行为违反验收标准，让 Copilot 修复，并在部署前重新运行针对性测试和 Inspector 检查。

   ![本地代理调试工作流截图。](../../../_images/vscode-agent-debug.png)

## 部署并测试托管代理

**Go production** 交接操作会将现有代理打包，以便部署到 Foundry。它不会使后续的网站代理服务成为可用于生产环境的公共服务。

1. 在创建代理的 Copilot Chat 中选择 **Go production**，将默认提示替换为以下内容并提交：

   ```text
   /foundrytk-quick-start Review this agent for deployment readiness, run its tests, then deploy it to my existing tailspin-toys Foundry project. Show me the deployment status and test the deployed agent.
   ```

   ![AIAgentExpert 代理提供的交接选项截图。](../../../_images/vscode-go-production-handoff.png)

2. 在聊天和终端中检查参数及命令批准请求。确认部署目标为现有的 `tailspin-toys` 项目，并在批准前检查计费资源。
3. 如果 Copilot 提供评估套件，可以选择接受并执行，作为额外检查。
4. 选择 **Foundry Toolkit**，展开 **My Resources**，再选择 **Agents**。在 **Agents** 选项卡中，切换到 **Hosted Agent**。

   ![已部署的托管代理截图。](../../../_images/vscode-agent-deployed.png)

5. 选择代理名称，确认部署状态为 **Running**。切换到 **Playground**，根据已部署的目录，重复检查回答的数据依据、缺失数据、目录外内容、模糊请求和排名。

   ![已部署的托管代理返回回答的截图。](../../../_images/vscode-agent-response.png)

6. 如果部署或回答未通过检查，与 Copilot 一起检查报告的状态和日志，在现有项目中修复问题，然后重复检查。不要在部署未经验证的情况下继续。

## 完成检查点

你已生成 Backer Concierge 的代码框架，在 Agent Inspector 中调试了它基于目录的回答，通过 **Go production** 交接将其部署到 Foundry，并在 Playground 中重新测试了托管版本。本模块的检查点是一个正在运行、遵守目录边界且不会编造缺失信息的托管代理。

接下来，你将使用同一个 `tailspin-toys` 项目、模型部署和托管代理，将代理连接到网站。如果在此停止，请[清理 Azure 资源][cleanup]，以免持续产生费用。

| [下一模块：将代理连接到网站 →][next-lesson] |
|--:|

[previous-lesson]: ../1-project-and-model/
[model-tests]: ../1-project-and-model/#测试已部署的模型
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#清理资源
