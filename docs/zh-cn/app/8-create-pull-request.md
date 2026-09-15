---
title: "第 8 课 - 创建并合并功能 PR"
description: "一并审查筛选功能、技能、QA 配置文件和测试，创建 PR 3，并明确授权 Agent Merge。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

筛选实现、quality-checks 技能、QA 配置文件及相关测试已通过检查点提交保存在同一分支上。一并审查这些内容，并使用当前 QA 证据准备 PR 3。你已经明确合并了星级评分和指令 PR。这次将在 PR 工作流中使用 **Agent Merge**，而不是为其创建单独的功能或分支。

本课将介绍如何：

- 了解 Agent Merge 及其如何自动执行合并生命周期。
- 检查完整的功能 PR 和验证证据。
- 审查后再授权 Agent Merge，并确认 PR 已合并。

## 场景

在前几课中，你探索了不同程度的自动化，从创建代码到让 Copilot 直接验证 UI。为了进一步加快开发速度，Tailspin Toys 希望了解是否可以自动合并经过审查和验证的拉取请求。

## Agent Merge 简介

通过 **Agent Merge**，可以使用 Copilot app 自动执行拉取请求落地前的最后阶段。启用后，应用会话会读取拉取请求并处理阻塞项，包括修复失败的 CI 检查、响应审查意见，以及在需要时变基。GitHub 允许后，它会立即合并。该功能在后台运行，应用重启后仍会继续，并在拉取请求合并后自动关闭。

此前，你一直自行选择 **Merge pull request**。Agent Merge 可以承担这项工作，但它编辑代码和合并的能力仍需要明确授权。授予合并权限前，先审查它允许执行的操作及工作内容。

## 审查完整的里程碑

留在第 4–7 课的筛选会话中。检查相对于 `main` 的完整分支差异，而不只是最新检查点：其中应包含筛选功能、`.github/skills/quality-checks/SKILL.md`、随附脚本、`.github/agents/qa.agent.md` 和相关测试。

请求提交或 PR 操作前，使用智能体选择器从 **QA** 切回通用 Copilot 智能体，并保持 **Interactive** 模式。QA 配置文件的职责是验证，而不是交付。更换所选智能体不得改变筛选会话、检出目录或分支。

本研讨会有意将功能工作和可复用质量基础设施放在同一个 PR 中。生产团队可能会将两者拆分；这里使用检查点提交保留便于审查的步骤，无需堆叠分支或额外创建 PR。

审查第 7 课的 QA 报告。只有报告涵盖待提交的最终修订版本，且已完成全部四项检查和相关浏览器观察，才能复用其中的证据。如果代码改动、冲突解决或 CI 修复改变了被测内容，应重新运行受影响的检查和浏览器观察，并更新证据。失败或受阻的 **NO-GO** 报告不代表批准合并。

差异和证据准备就绪后，发送：

```plaintext
审查筛选分支相对于 main 的完整差异，包括筛选功能、quality-checks 技能及脚本、QA 智能体定义和相关测试。汇总议题标准、批准的澄清内容及当前 QA 证据。仅在验证仍适用于最终修订版本时复用；继续前报告过时、缺失或失败的证据。

如果已审查的更改和验证已就绪，提交剩余的已批准里程碑更改，推送当前分支，并使用存储库的 PR 模板和实际筛选议题 URL，创建一个以 main 为目标的功能 PR。保留当前分支上的检查点历史。不要使用贡献技能、创建其他分支或 PR，也不要合并。
```

在 **My work** 中打开 PR，检查 **Files changed**、描述、审查和检查结果。查看 Tailspin Toys 自己的工作流文件和必需检查；不要假设每项本地检查或浏览器观察都会在 CI 中运行。研讨会发布站点的 Astro 构建和链接检查器属于另一个存储库，不能验证此功能。

## 使用 Agent Merge 管理 PR

审查现有 PR 后，在同一会话中配置 Agent Merge。不要创建第二个 PR。

1. 返回筛选会话，确认其已关联 PR 3。
2. 打开右上角的 PR 操作下拉菜单。PR 创建前，它位于 **Create PR** 旁；关联 PR 后，标签可能变化。
3. 选择 **Agent merge** 以启用 agent merge。
4. 审查可用权限，包括 **Address reviews**、**Fix CI failures**、**Resolve conflicts** 和 **Merge pull request**。发现的问题或验证尚未解决时，保持合并权限关闭。
5. 启动前，发送以下范围和授权说明，再选择 **Agent merge**：

   ```plaintext
   使用 Agent Merge 管理此现有筛选 PR。仅在该 PR 范围内处理审查或 CI 阻塞项。不要弱化测试或需求，并在无关更改或安装前先询问。只要被测修订版本发生改动，就需要更新相关检查和浏览器证据；不要将旧 QA 结果当作更改后代码的证明。

   在我审查最终差异和证据并明确启用 Merge pull request 前，不要合并。不要创建其他 PR 或开始画布任务。
   ```

6. 审查后续更改和更新后的结果。最终差异获批、必需的 CI 和审查通过，且 QA 证据适用于该修订版本后，选择 **Agent merge** 旁的下拉菜单，再选择 **Merge pull request**，明确授权合并。

   ![Agent merge 下拉菜单显示智能体获准执行的操作：Address reviews、Fix CI failures 和 Resolve conflicts，箭头指向 Merge pull request](../../_images/app-agent-merge-merge.png)

7. 确认 GitHub 显示 PR 3 为 **Merged**，而不只是可合并或已排队。Agent Merge 不会绕过存储库保护或缺失的权限；解决这些阻塞项后再继续。

只有合并完成后，才能开始画布里程碑。第 9 课会创建新工作树，并将其会话分支快进到最新的 `origin/main`，确保画布工作从完整合并后的功能状态开始。

## 总结与后续步骤

你已自动执行开发流程中的多个环节，包括生成代码、测试和验证代码，以及拉取请求流程。你：

- 了解了 Agent Merge 及其如何自动执行合并生命周期。
- 将筛选功能、技能、QA 配置文件和测试的完整差异作为 PR 3 进行了审查。
- 复用了当前 QA 证据，检查了 CI，并明确授权了 Agent Merge。

接下来，你将探索**画布**，这是一种与智能体共同规划和可视化工作的更丰富方式。继续学习[第 9 课 - 创建分类画布][next-lesson]。

## 资源

- [使用 GitHub Copilot app 管理议题和拉取请求][managing-issues-prs]
- [关于 GitHub Copilot app][about-copilot-app]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-canvases/
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app