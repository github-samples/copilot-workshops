---
slug: zh-cn/vscode
title: "VS Code"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

VS Code 中的 **[GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)** 将 GitHub Copilot 带入了日常使用的代码编辑器。在 Visual Studio Code（以及 GitHub Codespaces）中，可以使用代理模式操作 Copilot Chat，通过 MCP 连接外部工具，并使用自定义代理，全程无需离开 IDE。在这里，Copilot 可以完整查看文件、终端和问题。

首先添加自定义指令，观察 Copilot 如何遵循这些指令，然后使用代理模式构建涵盖 UI、数据层和测试的筛选功能。接下来，连接 Playwright MCP 服务器，让 Copilot 操作浏览器测试功能，再创建拉取请求。最后，审阅并使用自定义代理完成无障碍改进，然后监控、引导并迭代 Copilot 的更改，全程无需离开编辑器。

## 练习

| 练习 | 主题 | 说明 |
|----------|-------|-------------|
| [0. 先决条件][ex0] | 设置 | 创建存储库和 codespace |
| [1. 自定义指令][ex1] | 上下文 | 在 VS Code 中添加并验证自定义指令 |
| [2. 代理模式][ex2] | 代码生成 | 使用代理模式构建筛选功能 |
| [3. 结合 Playwright 使用 MCP][ex3] | 外部工具 | 使用 Playwright MCP 服务器在浏览器中测试功能 |
| [4. 自定义代理][ex4] | 专用代理 | 审阅并使用自定义代理 |
| [5. 管理代理][ex5] | 监控 | 监控并引导代理会话 |
| [6. 迭代][ex6] | 审阅 | 在本地审阅 Copilot 的工作并选择后续步骤 |
| [可选：集成 Foundry][foundry-toolkit] | AI 代理 | 通过三个模块，使用 VS Code 和 Foundry Toolkit 准备模型、部署代理并将其连接到网站 |

## 先决条件

参加本工作坊前，需要具备：

- [ ] 拥有有效 **Copilot Student、Pro、Pro+、Business 或 Enterprise** 计划的 GitHub 账户
- [ ] GitHub Codespaces 访问权限

> [!TIP]
> 没有付费计划？通过验证的学生可以通过 [GitHub Education][callout-student-plan-education] 免费使用 GitHub Copilot。**Copilot Student** 计划包含本工作坊使用的代理、MCP、代码审查和 Copilot CLI 功能，因此可以用它完成所有学习路径。

[callout-student-plan-education]: https://github.com/education/students
## 开始学习

**[从练习 0：先决条件开始 →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-custom-instructions/
[ex2]: 2-agent-mode/
[ex3]: 3-mcp/
[ex4]: 4-custom-agents/
[ex5]: 5-managing-agents/
[ex6]: 6-iterating/
[foundry-toolkit]: 7-foundry-toolkit/
