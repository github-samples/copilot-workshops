---
title: "可选：集成 Foundry"
slug: zh-cn/app/8-foundry-canvas
description: "使用 Microsoft Foundry Canvas 构建以目录为依据的 Backer Concierge，并在各阶段设置可安全暂停的位置。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/zh-cn/app/9-review/
  label: 回顾与后续步骤
next:
  link: /copilot-workshops/zh-cn/app/8-foundry-canvas/1-project-and-model/
  label: 准备项目和模型
---

在这一可选学习流程中，将使用 GitHub Copilot app 中的 Microsoft Foundry Canvas，为 Tailspin Toys 添加 **Backer Concierge**。整个流程从以目录为依据的模型实验开始，逐步构建托管代理，最后集成到本地网站。

## 学习流程

每个模块最后都设有检查点，可在此安全暂停。整个流程始终使用同一个 Tailspin Toys 存储库、工作树分支、关联议题的会话、Foundry 项目和模型部署。

- [准备项目和模型][module-1]：明确回答所依据的目录数据范围，创建项目和模型部署，并在 Canvas 中检查。
- [构建并部署代理][module-2]：生成 Backer Concierge 的初始框架，在本地测试，然后部署并重新测试托管代理。
- [将代理连接到网站][module-3]：添加保护凭据的本地代理服务、支持无障碍访问的聊天组件、端到端测试，并使用 Agent merge。

> [!IMPORTANT]
> Microsoft Foundry Canvas 和托管代理目前处于公开预览阶段。
>
> 此流程会创建计费的 Azure 资源，包括模型部署，以及从模块 2 开始创建的托管代理。创建资源之前，必须确认订阅、区域、配额和预计费用并获得批准。即使只完成项目和模型阶段就停止，也需要清理资源。

1. 从[准备项目和模型][module-1]开始，所有操作都应在自己的 Tailspin Toys 存储库中完成，而不是在本研讨会的内容存储库中。
2. 在选定的停止位置（项目和模型、托管部署或完整集成），记录该模块的检查点，并在结束实验后按下方的通用步骤清理资源。清理后如需继续，必须恢复已删除的资源，并重新检查其配置。

## 清理资源

清理方式取决于已完成的阶段。如果只完成项目和模型阶段，则不需要 `azure.yaml`、`azd` 环境或托管代理。

> [!WARNING]
> 删除资源具有破坏性。此处只允许删除本研讨会专用的资源。绝不能删除共享资源组；安全的替代方式是与资源所有者协调，逐一移除研讨会资源。

1. 在相应终端中停止自己启动的本地 Agent Inspector、Azure Function 和 Astro 开发服务器进程。删除 Azure 资源前，记录所需的检查点详情。
2. 在 Azure 门户中确认当前订阅 ID、研讨会资源组的准确名称及其包含的每个资源。检查 Foundry 项目和模型部署是否属于本次实验。如果订阅、归属或资源内容不明确，先暂停清理，直到核实清楚。
3. 根据停止位置选择清理方式。如果只完成模块 1，请跳过下一步，直接执行第 5 步；不要为了清理而创建 `azure.yaml` 或初始化 `azd`。如果在模块 2 或 3 中通过 Canvas 完成了部署，请继续执行第 4 步。
4. 对于托管部署，在同一个 Tailspin Toys 工作树中打开终端，该工作树的根目录中应包含 `azure.yaml`。确认所选 `azd` 环境指向本次实验的订阅和资源，审查将要删除的资源，并且仅在所有目标都是本次研讨会专用资源时运行以下命令：

   ```bash
   azd down --purge
   ```

5. 如果只完成项目和模型阶段，或者运行 `azd down` 后研讨会专用资源组仍然存在，请在门户中重新检查订阅、资源组名称和完整资源列表。如果整个资源组专用于本次实验，且名称恰好为 `rg-tailspin-toys`，则运行以下命令。如果名称不同，请改用已核实的专用资源组名称；如果资源组为共享资源组，不要运行此命令，应与其所有者协调逐一清理资源。

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. 在 Azure 门户中验证删除操作已完成；`--no-wait` 会在删除完成前返回。确认研讨会的模型部署及所有托管代理资源均已删除，并清理其余仍在计费的研讨会资源，但不要删除共享资源。
7. 完成选定的检查点和清理后，返回[回顾与后续步骤][core-review]。

## 资源

Microsoft 文档介绍了 Canvas、托管部署及其权限。

- [什么是 Microsoft Foundry Canvas？][foundry-canvas]
- [使用 Foundry Canvas 部署第一个托管代理][hosted-agent-quickstart]
- [托管代理权限][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
