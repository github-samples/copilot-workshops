---
title: "第 10 课 - 总结与后续步骤"
description: "回顾 App 的九个核心模块、四个 PR 里程碑和可复用质量工作流，再探索更多资源。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

在过去几节课程中，你使用 GitHub Copilot app 将一项功能从构想推进到合并，包括：

- 连接存储库，并熟悉应用工作区和模板创建的待办事项。
- 从直接任务和议题启动会话，并使用 Plan 和 Autopilot 模式控制智能体的工作方式。
- 使用自定义指令引导智能体，再让它创建包含 shell 脚本的可复用技能，审查并运行这些脚本，完成 lint、单元测试、端到端测试和类型检查。
- 使用 Playwright MCP 服务器在真实浏览器中测试工作。
- 创建并选择 QA 自定义智能体，以评估需求、覆盖情况、技能脚本结果和浏览器证据。
- 在共享画布上与智能体协作。
- 明确执行早期 PR 的合并，再在功能和画布 PR 工作流中授权 **Agent Merge**。

完成设置课程第 0–1 课后，你学习了九个核心模块，即第 2–10 课。现在回顾产出和后续方向；本总结不再启动新的动手任务。

## 交付的内容

本研讨会有四个 PR 里程碑，每个里程碑都从更新后的 `main` 开始，使用各自的分支：

1. **星级评分**：在游戏卡片上显示现有的 `starRating`，以及明确的未评分状态。
2. **指令及示例改动**：添加文档约定，并通过一个小型的真实代码改动验证其效果。
3. **筛选功能及质量工作流**：实现议题需求，创建包含 shell 脚本的 `quality-checks` 技能和 QA 配置文件，并包含相关测试。
4. **保存在存储库中的分类画布**：共享一个添加议题上下文的看板，而不自动实现其他功能。

第 4–8 课使用同一筛选会话、工作树和分支。检查点提交在 PR 3 内保留进度；技能、MCP 配置和 QA 无需单独的功能分支。每个后续里程碑都在前一个 PR 合并，且新会话分支从 `origin/main` 更新后才开始。

## 不同类型的验证

早期功能使用现有 npm 检查。筛选功能增加了手动浏览器检查。技能通过随附脚本让四项检查可重复执行，MCP 增加了智能体的直接浏览器观察，QA 则将需求和覆盖情况与最终验证结合起来。PR 仅在 QA 证据仍适用于所提交的修订版本时才复用它。

新增测试应填补真实缺口；不需要新增测试的 QA 运行也可能完全正确。缺少工具、跳过检查和失败都是需要明确报告的阻塞项，而不是通过。授权合并前审查代码和证据，并在改动后更新受影响的证据。

## 最佳实践

使用任何 AI 工具时，其周边基础设施都会影响输出质量。本研讨会中，你创建了指令、技能和 QA 配置文件；应审查它们，并在会话间复用。自定义智能体定义专业角色和指令，可用工具由配置和操作环境权限决定；技能则将可复用的任务指令、可执行脚本和辅助资源打包，供按需加载。自定义智能体也能执行脚本，包括技能随附的脚本。确认脚本实际执行且自定义智能体确已选中，而不是仅凭令人信服的描述作出判断。

根据任务选择适合的**模式和模型**。使用 **Plan** 在构建前思考方法；使用 **Interactive** 参与范围明确的更改；仅对范围清晰且彼此隔离的任务使用 **Autopilot**。日常编辑可选择更快的模型，复杂工作则选择推理能力更强的模型并提高推理强度。

上下文与基础设施同样重要。清楚说明要构建*什么*、*为什么*构建，以及*如何*构建，会显著影响输出。在决定创建完整会话前，可以先通过快速聊天下一步界定想法范围。

## 更多探索内容

你已经了解核心工作流。以下功能也值得探索：

- **Quick chats**：适合不需要完整会话的一次性问题。
- [**Automations**][using-automations]：用于重复性或按需任务，例如汇总近期工作。采用前审查计划、权限和范围；创建自动化任务属于后续方向，不是本研讨会的一部分。
- **Rubber duck**：用于分析问题，并在构建前获得高信噪比反馈。
- [**Custom agents**][custom-agents]：将角色、工具和指令打包，以便重复执行专业工作。
- [`/chronicle`][chronicle]：生成会话过程的叙述。
- [Bring your own key (BYOK)][byok]：使用自己提供商的模型，包括通过 Ollama、Foundry Local 或 LM Studio 使用本地模型。
- [Cloud sandboxes][sandboxes]：在 GitHub 托管的隔离环境中运行会话。
- [Deep links][deep-links]：直接在应用中打开存储库、会话或提示词。

## 后续步骤

熟练使用任何工具的最佳方式都是持续使用。可将它用于生产代码、业余项目，或那个构思多年却始终没有动手构建的小应用。与团队分享经验，也向团队学习。并且一如既往地探索文档。

要探索 GitHub Copilot 生态系统的更多内容，请查看 [VS Code 学习路径][vscode-harness]、[Copilot CLI 学习路径][cli-harness]或 [Cloud agent 学习路径][cloud-harness]。

## 资源

- [关于 GitHub Copilot app][about-copilot-app]
- [GitHub Copilot app 入门][getting-started]
- [自定义 GitHub Copilot app][customize]
- [使用自动化][using-automations]
- [使用画布扩展][canvas-docs]
- [关于云沙盒和本地沙盒][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links