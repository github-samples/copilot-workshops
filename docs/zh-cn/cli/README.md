---
slug: zh-cn/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** 将 GitHub Copilot 作为代理式编码助手带入终端。它可以探索代码库、生成代码、运行命令，并连接外部工具——全部通过命令行完成，无需切换到图形化编辑器即可保持工作流畅。

在这些练习中，将先安装并验证 Copilot CLI，然后通过自定义说明为它提供项目上下文，再使用计划模式有目的地生成一个功能。接着连接 Playwright MCP 服务器，在真实浏览器中测试该功能；然后通过可复用的智能体技能和自定义智能体扩展 Copilot。最后，将探索用于管理上下文、模型和共享的斜杠命令，并回顾已完成的内容。

## 练习

| 练习 | 主题 | 说明 |
|----------|-------|-------------|
| [0. 先决条件][ex0] | 设置 | 创建存储库和 codespace |
| [1. 安装 Copilot CLI][ex1] | 安装 | 安装并验证 Copilot CLI |
| [2. 自定义说明][ex2] | 上下文 | 添加一条说明，并观察 Copilot CLI 如何遵循它 |
| [3. 生成代码][ex3] | 代码生成 | 使用计划模式生成功能 |
| [4. 使用 Playwright MCP 测试][ex4] | 外部工具 | 添加 Playwright MCP 服务器，并在浏览器中测试功能 |
| [5. 智能体技能][ex5] | 技能 | 用专门的技能增强 Copilot |
| [6. 自定义智能体][ex6] | 智能体 | 查看并使用自定义智能体 |
| [7. 斜杠命令][ex7] | CLI 功能 | 探索上下文、模型、共享，以及可选的委托给 cloud agent |
| [8. 回顾][ex8] | 总结 | 回顾关键概念和后续步骤 |

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
[ex2]: 2-custom-instructions/
[ex3]: 3-generating-code/
[ex4]: 4-mcp/
[ex5]: 5-agent-skills/
[ex6]: 6-custom-agents/
[ex7]: 7-slash-commands/
[ex8]: 8-review/
