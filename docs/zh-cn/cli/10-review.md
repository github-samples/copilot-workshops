---
title: "练习 10 - 总结与后续步骤"
description: "回顾共同的开发工作流、可复用产出和 CLI 的三个拉取请求里程碑。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

你已使用 Copilot CLI，从一个小改动推进到经过规划、具有可复用验证方式的功能。练习 0–1 的设置准备了环境；练习 2–10 的九个核心模块展示了完整开发工作流。

## 回顾三个 PR 里程碑

| 里程碑 | 合并后的结果 | 审查习惯 |
| --- | --- | --- |
| PR 1：星级评分 | 在游戏卡片上显示现有 `starRating`，包括在 `null` 时显示 `No rating yet` | 保持改动范围明确，验证两种情况 |
| PR 2：自定义指令 | 范围明确的文档约定和小型真实代码示例 | 检查指令是否改善实际代码，而不只是聊天示例 |
| PR 3：筛选功能及验证 | 筛选功能、quality-checks 技能、QA 配置文件和相关测试 | 合并前审查全部检查点、当前 QA 证据和 CI |

前两个 PR 都在下一个里程碑从更新后的 `main` 开始之前完成了合并。练习 4–8 共用一个分支和检出目录。检查点提交保留进度，无需为每个模块创建 PR。控件练习没有启动其他功能或 PR。

## 回顾共同产出

这些与 [Copilot app 研讨会][app-workshop]的核心成果相同，只是通过终端界面完成：

- **存储库指令**说明项目上下文和标准；路径范围指令为相关文件补充细节。
- **筛选实现和测试**满足议题及规划时批准的澄清内容。
- **quality-checks 技能**封装可复用指令和实际 shell 脚本，用于运行项目的四项检查。
- **Playwright MCP 配置**提供直接观察所需的浏览器工具。在此 CLI 流程中，它属于用户配置，而不是功能 PR。
- **QA 自定义智能体**定义可复用角色：从需求出发，检查覆盖情况，使用技能和浏览器工具，并如实报告结果。
- **PR 和验证证据**将已审查的更改与测试结果、浏览器观察、限制和 CI 联系起来。

技能不只是一份命令列表，配置文件也不只是一个文件名。在依赖报告前，你检查了生成的资产、确认了实际执行，并选择了自定义智能体。

## 区分各阶段的验证目的

规划在实现前明确了需求。Autopilot 执行范围明确的计划；切回 Interactive，则在编写自定义配置前恢复了明确的审查节点。

实现阶段在任何技能存在之前使用现有 npm 检查。技能练习证明了随附脚本和参数转发可用。MCP 展示直接浏览器交互，而不是重复完整套件。QA 将标准、覆盖情况、浏览器证据和全部四项技能驱动的检查结合起来。PR 复用当前 QA 结果，同时由 CI 检查提交的修订版本。

失败和阻塞项都是有用的结果。缺少浏览器工具、跳过测试、服务器内容过时或需求未明确，都意味着 **NO-GO**，而不是允许降低标准。新增测试必须针对真实缺口；现有覆盖充分时，不添加测试才是正确做法。

## 延续这些习惯

- 向 Copilot 提供议题、更改原因和明确边界。
- 批准自主工作前审查计划。
- 运行前检查生成的指令、技能和配置文件。
- 清楚结果对应哪个检出目录、分支、服务器和修订版本。
- 采用确有必要的最小修正，并在更改后更新证据。
- 明确授权安装、破坏性操作、共享和 PR 合并。

## 继续学习

[Copilot app 研讨会][app-workshop]通过图形界面实现共同成果，并增加画布里程碑。[VS Code 研讨会][vscode-workshop]和 [Cloud agent 研讨会][cloud-workshop]探索与智能体协作的其他方式。

使用 [Awesome Copilot][awesome-copilot] 查找指令、技能和自定义智能体示例。[练习 5 中的技能示例][skill-examples]包括贡献工作流、需求文档、图表和浏览器测试。采用社区内容前，审查先决条件和行为。

日常使用时可查阅 [CLI 命令参考][cli-reference]、[智能体技能文档][agent-skills]和[自定义智能体文档][custom-agents]。继续在范围明确的任务中尝试，并仅通过批准的渠道共享已审查材料。

[previous-lesson]: ../9-slash-commands/
[app-workshop]: ../../app/
[vscode-workshop]: ../../vscode/
[cloud-workshop]: ../../cloud/
[skill-examples]: ../5-agent-skills/#更多技能示例
[awesome-copilot]: https://github.com/github/awesome-copilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/concepts/agents/copilot-cli/about-custom-agents
