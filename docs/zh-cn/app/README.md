---
slug: zh-cn/app
title: "GitHub Copilot app"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[**GitHub Copilot app**](https://docs.github.com/copilot/concepts/agents/github-copilot-app) 是一款基于 Copilot CLI 构建的桌面应用，可将智能体驱动的开发集中到一个专注的工作区。它支持并行智能体会话、可切换的会话模式、共享画布，以及原生的 GitHub 议题和拉取请求管理功能。其中包括 **Agent Merge**，可处理拉取请求的变基、审查反馈、CI 修复与合并。

设置课程第 0–1 课帮助你准备项目和 App 工作区。九个核心模块，即第 2–10 课，从添加星级评分快速上手，再通过真实代码展示文档约定。随后规划并构建筛选功能，创建并执行包含 shell 脚本的 quality-checks 技能，通过 Playwright MCP 观察功能，再创建 QA 自定义智能体来评估需求和覆盖情况。你将审查完整的功能 PR 并授权 Agent Merge，最后创建并合并共享分类画布。

本研讨会有四个 PR 里程碑：星级评分；指令及示例改动；筛选功能及技能、QA 配置文件和测试；最后是画布。每个里程碑都从更新后的 `main` 开始，每个 PR 使用一个分支，而不是每个模块一个分支。第 4–8 课沿用同一筛选会话、工作树和分支。重新打开画布只添加议题上下文，不启动其他功能或第五个 PR。自动化任务作为后续方向提供链接，而不是额外练习。

## 课程

| 课程 | 主题 | 说明 |
|--------|-------|-------------|
| [0. 先决条件][ex0] | 设置 | 安装 Node.js，并创建自己的 Tailspin Toys 项目副本 |
| [1. 安装 Copilot app][ex1] | 设置 | 安装应用、连接项目并熟悉工作区 |
| [2. 添加星级评分：快速上手][ex2] | 首次更改 | 显示现有评分和空值回退状态，再合并 PR 1 |
| [3. 使用自定义指令引导 Copilot][ex3] | 上下文 | 添加文档标准和真实示例改动，再合并 PR 2 |
| [4. 使用 Plan 和 Autopilot 构建筛选功能][ex4] | 实现 | 批准计划，实现并检查筛选功能，保存检查点 |
| [5. 创建并使用 quality-checks 技能][ex5] | 可重复检查 | 创建、审查并执行随附的 shell 脚本 |
| [6. 使用 Playwright MCP 验证功能][ex6] | 浏览器观察 | 通过 Customize 配置 MCP，并检查筛选行为 |
| [7. 创建并使用 QA 智能体][ex7] | 需求与覆盖 | 选择专业配置文件，收集最终验证证据 |
| [8. 创建并合并功能 PR][ex8] | 审查与合并 | 审查筛选功能、技能、QA 配置文件和测试，再为 PR 3 授权 Agent Merge |
| [9. 创建分类画布][ex9] | 协作 | 通过 PR 4 共享保存在存储库中的画布，并添加议题上下文 |
| [10. 总结与后续步骤][ex10] | 总结 | 回顾工作流、产出及更多资源 |

## 先决条件

参加本次研讨会前，请确保具备：

- [ ] 拥有有效 **Copilot Student、Pro、Pro+、Business 或 Enterprise** 计划的 GitHub 帐户
- [ ] 一台运行 **macOS、Linux 或 Windows** 的计算机
- [ ] 计算机上已[安装 Git][install-git]

> [!TIP]
> 没有付费计划？经过验证的学生可通过 [GitHub Education][callout-student-plan-education] 免费获取 GitHub Copilot。**Copilot Student** 计划包含本研讨会所需的智能体、MCP、代码审查和 Copilot CLI 功能，因此可以完成所有学习路径。

> [!NOTE]
> Copilot app 在本地计算机而非 codespace 中运行，因此[第 0 课][ex0]会先指导你安装 Node.js 并创建项目副本，然后再安装应用。

> [!NOTE]
> 如果使用 Copilot Business 或 Copilot Enterprise，管理员必须先启用 **Copilot CLI** 策略，你才能使用该应用。

## 开始学习

[**从第 0 课“先决条件”开始 →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students