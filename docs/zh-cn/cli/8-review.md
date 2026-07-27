---
title: "练习 8 - 回顾与后续步骤"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

在前几节练习中，已经探索了 GitHub Copilot CLI 的一些最常见用例，包括：

- 与 GitHub 和其他 MCP 服务器交互。
- 使用说明文件指导代码生成。
- 实现技能，为 Copilot CLI 工具箱添加工具。
- 调用自定义智能体处理更高级、更复杂的任务。
- 使用斜杠命令管理会话，并可选择通过 `/delegate` 衔接回 cloud agent。

下面再谈谈一些斜杠命令、最佳实践和后续步骤。

## 斜杠命令

Copilot CLI 提供了一系列斜杠命令用于交互，其中包括一些可用于配置它或查看幕后情况的命令。前面已经使用过 `/clear` 来开始新聊天并清除当前上下文，也使用过 `/mcp` 来查看和管理 MCP 服务器。以下是一些可能也很有用的命令：

| 命令               | 说明                                                          |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir`         | 将目录添加到 Copilot 的受信任列表 |
| `/clear`, `/new`   | 清除对话历史并重新开始 |
| `/compact`         | 总结对话历史，以减少上下文窗口占用 |
| `/context`         | 显示上下文窗口 token 使用情况和可视化信息 |
| `/diff`            | 查看当前目录中的变更 |
| `/model`           | 选择要使用的 AI 模型（Claude Sonnet、GPT-5 等） |
| `/plan <prompt>`   | 在编码前创建实现计划 |
| `/review <prompt>` | 运行代码审查代理分析变更 |
| `/delegate`        | 将任务委托给 Copilot cloud agent 进行异步处理 |
| `/session`         | 显示会话信息和工作区摘要 |
| `/share`           | 将会话共享为 markdown 文件或 GitHub gist |
| `/skills`          | 管理技能以增强能力 |
| `/usage`           | 显示会话使用指标和统计信息 |

> [!TIP]
> 使用 `/help` 查看完整的可用命令列表和键盘快捷键。

## 最佳实践

使用任何 AI 工具时，底层基础设施都会影响最终效果。完善的说明文件、自定义智能体和智能体技能都很重要——本工作坊已经逐一体验过。[awesome-copilot][awesome-copilot] 是一个很好的模板来源，而 Copilot 本身也可以为这些内容生成脚手架，作为起点。

和基础设施同样重要的，仍然是上下文。清楚描述想构建*什么*、*为什么*构建、以及*如何*构建，都会显著影响输出结果。凡是有助于 Copilot 的信息，都应该主动提供。

## 后续步骤

提升任何工具使用能力的最好方式，就是持续使用它。把它用在生产代码上、用在个人项目上，或者用在那个想了很多年却一直没开始实现的小应用上。把经验分享给团队，也从团队中学习。并且，一如既往地，多查阅文档。

如果想继续探索 GitHub Copilot 生态系统，可以查看 [VS Code 路径](../../vscode/) 或 [Cloud agent 路径](../../cloud/)。

## 资源

- [关于 Copilot CLI][about-copilot-cli]
- [使用 Copilot CLI][using-copilot-cli]
- [Awesome Copilot 存储库][awesome-copilot]
- [自定义说明指南][repo-instructions]
- [Agent Skills 文档][agent-skills]
- [自定义智能体文档][custom-agents]
- [MCP 规范][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
