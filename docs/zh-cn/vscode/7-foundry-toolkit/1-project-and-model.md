---
title: "准备项目和模型"
description: "导出 Tailspin 目录，并根据 Backer Concierge 的验收标准测试已部署的模型。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 可选：集成 Foundry][overview] |
|:--|

第一个模块使用 VS Code 和 Microsoft Foundry Toolkit，为 Backer Concierge 准备数据和模型。在必修工作坊中创建的个人 Tailspin Toys 存储库中完成操作。

## 目标

- 导出目录并识别其信息边界。
- 准备 Foundry 项目，并根据验收标准和配额选择模型。
- 编写代理代码前，在 Model Playground 中验证回答是否以给定数据为依据。

## 场景

Tailspin 的支持者希望获得可信的推荐。解谜游戏爱好者期待的是真实的游戏名称和准确的评分，而不是虚构的筹款总额。推荐助手需要明确目录的信息边界，并养成提出一个有用问题的习惯，而不是猜测支持者的需求。

## 准备工作区

该工具包将模型发现、部署、提示工程、评估和代理部署带入 VS Code。Azure 访问权限和干净的功能分支为后续工作做好准备。

> [!IMPORTANT]
> Foundry Toolkit 和托管代理目前处于公共预览阶段。本模块会创建计费的 Azure 资源。批准创建前，确认订阅权限、区域、配额和预计费用。即使在构建代理前停止，也可以执行[清理][cleanup]。

1. 确认有权访问 Azure 订阅。可选方案包括[提供 200 美元额度的免费 Azure 账户][azure-free]和[提供 100 美元额度的 Azure for Students][azure-students]，但需满足各自的资格条件和服务限制。
2. 在 VS Code 的活动栏中选择 **Extensions**，搜索 **Foundry Toolkit**，然后选择 **Install**。安装后，其图标会出现在活动栏中。
3. 选择 **Azure** 图标，再选择 **Sign in to Azure…**，然后选择用于 Foundry 项目的订阅。工具包完成身份验证后，Copilot 可以使用 [Microsoft Foundry Skill][foundry-skill]，通过对话准备资源。
4. 在 Tailspin Toys 工作区中，打开 **Terminal** > **New Terminal**，或按 <kbd>Control</kbd>+<kbd>\`</kbd>（Mac）或 <kbd>Ctrl</kbd>+<kbd>\`</kbd>（Windows/Linux）。确认之前的工作已提交并推送，然后创建功能分支：

   ```bash
   git checkout main
   git pull
   git checkout -b foundry-agent-vscode
   ```

5. 以 **Agent** 模式打开新的 Copilot Chat，并提问：

   ```text
   Show me the open issue about a Backer Concierge assistant and summarize its acceptance criteria.
   ```

6. 确认 Copilot 找到了 **Add a Backer Concierge assistant for catalog questions**。验收标准要求回答有数据依据、不虚构筹款金额、提出一个澄清问题，并提供具有端到端测试覆盖的无障碍 UI。

## 生成目录导出文件

目录导出脚本为代理提供回答所依据的数据源。

1. 在 Tailspin Toys 存储库的终端中，执行迁移、填充初始数据并写入 `db/catalog.json`：

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

2. 打开 `db/catalog.json`，确认其中包含二十一款游戏，每款都有名称、描述、类别、发行商和星级评分，另有一个 `note` 字段说明缺失的信息。目录不包含筹款总额、支持者人数、认捐档位和发布日期；代理必须遵守这一边界。

## 设置 Foundry 项目

项目用于容纳模型，以及之后的托管代理。继续本模块时，应使用同一个项目，而不是另建项目。

1. 在活动栏中选择 **Foundry Toolkit**，展开 **Help and Feedback**，然后选择 **Ask Copilot**。在下拉列表中确认所选模型，并发送生成的 `/foundrytk-quick-start` 提示。

   ![Foundry Toolkit 快速入门操作流程截图。](../../../_images/vscode-foundry-setup.png)

2. 在交互式工作流中，对 **Where are you starting from?** 选择 **Set up Foundry**，然后对 **What do you have already?** 选择 **I have an Azure subscription or Foundry resources**。
3. 检查工具批准请求。如果建议的命令及其作用范围合适，为本会话选择 **Allow azmcp …**，以减少重复的批准提示。
4. 在 **Microsoft Foundry: Create Project** 中，为 **Choose a resource group** 选择 **Create new resource group**，输入 `rg-tailspin-toys`，选择提供目标模型的区域，并在 **Enter project name** 中输入 `tailspin-toys`。`East US 2` 和 `Sweden Central` 支持的模型较多，可作为初始候选区域；实际选择取决于当前可用性和配额。如果是继续之前的工作，改为选择已有项目。
5. 等待部署成功通知。在工具包中展开 **My Resources**，确认该项目为默认项目。

## 发现并部署模型

在这里，遵循规则并以数据为依据，比选择最大或最新的模型更重要。议题提供了具体标准，可用于比较速度、回答与数据的一致性、区域可用性和配额。

1. 在 Copilot Chat 中选择 **+**，再选择 **GitHub Issues**，并附加 **Add a Backer Concierge assistant for catalog questions**。发送：

   ```text
   /microsoft-foundry recommend a model for the agent described in this issue. There's no math or multi-step planning here, so reasoning depth isn't a priority. Prioritize speed instead. Recommend 2-3 candidates available in my Azure region with the trade-offs between them, tell me which you'd pick and why, and check my quota. Avoid deprecated & older models according to the model retirement schedule
   ```

2. 阅读建议，选择最符合需求和可用配额的模型。让 Copilot 部署该模型：

   ```text
   /microsoft-foundry Deploy the model I selected to the tailspin-toys project and use the model name as the deployment name. Confirm the available quota and capacity with me before creating it.
   ```

3. 批准前确认项目、部署、容量和费用。检查作用范围后，如果合适，为本会话选择 **Allow az …**，以减少重复提示。
4. 选择 **Foundry Toolkit**，展开 **My Resources**，然后选择 **Models**。确认已部署的模型显示在 Foundry 下。截图仅为示例；所在区域可能提供不同模型。

   ![Foundry Toolkit 中的模型部署示例截图。](../../../_images/vscode-model-deployed.png)

## 测试已部署的模型

Model Playground 没有目录文件。在系统提示中提供精简的九款游戏子集，就足以测试模型是否遵守数据依据规则。

1. 在 **Models** 中选择已部署的模型名称，打开已预选该模型的 **Model Playground**。粘贴以下系统提示：

   ```text
   You're the Backer Concierge for Tailspin Toys. Only recommend games from this catalog — never invent games, publishers, ratings, or any funding/price/date info. If a request is vague, ask one short question first.

   CATALOG

   | Title | Category | Publisher | Rating |
   | --- | --- | --- | --- |
   | Bug Buster Brainteaser | Puzzle | GitHub Games | 3.0 |
   | Merge Conflict Mystery | Puzzle | DevMasters Inc. | 3.8 |
   | Stack Trace Secrets | Puzzle | Ops Interactive | 3.6 |
   | Deployment Dynasty | Simulation | Ops Interactive | 5.0 |
   | Script Strike | Action | CodeForge Studios | 5.0 |
   | Pipeline Conquest | Strategy | DevMasters Inc. | 3.9 |
   | Repo Rulers | Strategy | Ops Interactive | 4.1 |
   | Server Siege | Strategy | GitHub Games | 3.3 |
   | Code Quest Odyssey | Adventure | CodeForge Studios | 4.8 |
   ```

2. 使用 `I love puzzle games about tracking down bugs. What should I back?` 测试回答是否以数据为依据。预期结果是推荐列表中的真实游戏，并提供正确信息。
3. 使用 `How much has Pipeline Conquest raised so far, and how many backers does it have?` 测试缺失数据。预期结果是明确拒绝提供这些信息，说明目录未记录筹款金额或支持者人数，然后给出已知信息。
4. 使用 `I need something for four players, about an hour long.` 测试另一个边界。预期结果是说明无法获取玩家人数和游戏时长，然后提出一个有助于继续推荐的追问。
5. 使用 `Do you have Wingspan? If not, what's the closest thing you've got?` 测试对目录外内容的应对。预期结果是不声称目录中有 Wingspan，不使用外部知识描述它，并转向推荐真实的 Tailspin 游戏。
6. 使用 `Recommend me something good.` 测试模糊请求。预期结果是提出一个简短的澄清问题，在得知类别或主题前不作推荐。
7. 使用 `What are your three highest rated games?` 测试排名。预期结果是评分为 5.0 的 Deployment Dynasty 和 Script Strike，然后是评分为 4.8 的 Code Quest Odyssey，顺序和数值均正确。
8. 如果任何检查失败，与 Copilot 讨论失败的回答和对应规则，调整配置或模型选择，并在继续之前重复检查。

## 完成检查点

你已准备好 VS Code 工作区、导出目录、创建 Foundry 项目，并针对 Backer Concierge 的据实回答规则测试了已部署的模型。本模块的检查点是一个能推荐目录中真实游戏、且不会编造缺失信息的模型，此时尚未部署代理。

接下来，你将使用同一个 `tailspin-toys` 项目和所选的模型部署来构建并部署代理。如果在此停止，请[清理 Azure 资源][cleanup]，以免持续产生费用。

| [下一模块：构建并部署代理 →][next-lesson] |
|--:|

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#清理资源
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[foundry-skill]: https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/SKILL.md
