---
slug: zh-cn/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** 将 GitHub Copilot 作为代理式编码助手带入终端。它可以探索代码库、生成代码、运行命令，并连接外部工具——全部通过命令行完成，无需切换到图形化编辑器即可保持工作流畅。

完成练习 0–1 的设置后，你将学习练习 2–10 中的九个核心模块。从添加星级评分快速上手，建立文档指令，再使用 **Plan** 和 **Autopilot** 模式构建筛选功能。随后创建可复用的 quality-checks 技能，使用 Playwright MCP 验证行为，创建 QA 智能体，并交付功能。最后探索 CLI 控件，回顾已构建的内容。

## 练习

| 练习 | 主题 | 说明 |
|----------|-------|-------------|
| [0. 先决条件][ex0] | 设置 | 创建存储库和 codespace |
| [1. 安装 Copilot CLI][ex1] | 安装 | 安装并验证 Copilot CLI |
| [2. 添加星级评分：快速上手][ex2] | 首次更改 | 显示现有评分，完成验证，并合并 PR 1 |
| [3. 使用自定义指令引导 Copilot][ex3] | 上下文 | 添加文档约定，展示其效果，并合并 PR 2 |
| [4. 使用 Plan 和 Autopilot 构建筛选功能][ex4] | 实现 | 审查计划，批准 Autopilot，测试并保存检查点 |
| [5. 创建并使用 quality-checks 技能][ex5] | 技能 | 生成、审查并运行随附的 shell 检查脚本 |
| [6. 使用 Playwright MCP 验证功能][ex6] | 浏览器工具 | 在真实浏览器中观察筛选行为 |
| [7. 创建并使用 QA 智能体][ex7] | 智能体 | 审查需求和覆盖情况，收集最终证据 |
| [8. 创建并合并功能 PR][ex8] | 交付 | 在 PR 3 中一并审查筛选功能和可复用自定义配置 |
| [9. 探索斜杠命令和 CLI 选项][ex9] | CLI 控件 | 检查上下文、模型、会话和共享目标 |
| [10. 总结与后续步骤][ex10] | 总结 | 回顾共同产出和三个 PR 里程碑 |

## 分支和拉取请求

你将合并三个拉取请求：星级评分；指令及小型示例改动；最后是筛选功能及 quality-checks 技能、QA 配置文件和相关测试。前两个 PR 都必须先完成合并，再从更新后的 `main` 开始下一个里程碑。

练习 4–8 共用一个功能分支和检出目录。过程中使用检查点提交保存进度；创建技能、设置 MCP 和选择 QA 不会开启新的功能分支。练习 9 只探索控件，不启动其他功能或 PR。

## 先决条件

参加本工作坊前，请确保已具备以下条件：

- [ ] 拥有 GitHub 账户，并已启用 **Copilot Student、Pro、Pro+、Business 或 Enterprise** 计划
- [ ] 对终端/命令行操作有基本了解
- [ ] 已安装并配置 Git

> [!TIP]
> 没有付费计划？已验证学生可通过 [GitHub Education][callout-student-plan-education] 免费使用 GitHub Copilot。**Copilot Student** 计划包含本工作坊所用的智能体、MCP、代码审查和 Copilot CLI 功能，因此可以完整完成所有路径。

[callout-student-plan-education]: https://github.com/education/students

> [!NOTE]
> 如果使用的是 Copilot Business 或 Copilot Enterprise，请确认管理员已启用 Copilot CLI。

## 开始

**[从练习 0：先决条件开始 →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
