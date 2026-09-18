---
title: "练习 6 - 在 GitHub Copilot CLI 中使用自定义智能体"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## 什么是自定义智能体？

GitHub Copilot 中的[自定义智能体][custom-agents-concept]允许创建适用于开发工作流中特定任务或领域的专用 AI 助手。通过在存储库的 `.github/agents` 文件夹中使用 markdown 文件定义智能体，可以为 Copilot 提供聚焦的说明、最佳实践、编码模式和领域知识，从而引导它更高效地完成特定类型的工作。团队可以把自身经验固化为可复用智能体——例如强制遵循 [WCAG][wcag] 的无障碍智能体、遵循安全编码实践的安全智能体，或保持一致测试模式的测试智能体。

自定义智能体通过项目 `.github/agents` 文件夹中的 markdown 文件定义，也可以全局定义在 `~/.copilot/agents` 中。每个文件都有 YAML frontmatter，至少包含 `name` 和 `description`，后面跟着一个 markdown prompt，用于定义智能体的行为、专长和说明。

### 自定义智能体与智能体技能的对比

自定义智能体与[智能体技能][agent-skills-concept]在逻辑上有一些重叠。两者主要都通过 markdown 文件定义，也都在告诉 AI 如何执行操作。最清晰的区分方式是：**自定义智能体**是执行工作的角色，而 **skills** 是工具。

自定义智能体拥有自己的上下文窗口，并且设计上就用于在工作过程中编排技能（甚至其他智能体）。在这个实验中，无障碍自定义智能体会根据无障碍准则审查并更新网站；在执行这项工作时，它可以调用诸如 pull request 工作流技能，或用于运行和管理测试的技能。

> [!NOTE]
> 编写自定义智能体并不存在唯一“正确”的方式。和 AI 中的大多数事情一样，需要测试并迭代，找到最适合环境和场景的做法。

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/

## 场景

许多 Web 应用在无障碍方面都做得不够，而正在使用的网站也不例外。接下来将使用一个自定义智能体来识别并解决无障碍缺陷。

Tailspin Toys 致力于确保其众筹平台对所有用户都可访问，无论其视觉能力或偏好如何。最近的用户反馈指出，由于文本与背景颜色之间的对比度不足，一些用户认为当前的深色主题难以阅读。为了解决这一无障碍问题，设计团队要求实现一种可开关的高对比度模式。

由于无障碍非常关键，希望尽快实现这项功能。因此将使用一个自定义智能体来生成功能。
在本练习中，将：

- 探索自定义智能体。
- 启用一个自定义智能体，并通过 Copilot CLI 为其分配任务。

## 查看无障碍自定义智能体

项目中已经预先创建了一个用于无障碍的自定义智能体。先查看其内容，了解它将如何引导 Copilot。

1. 打开 `.github/agents/accessibility.md`。
2. 注意其中带有 `name` 和 `description` 字段的 YAML frontmatter。

> [!CAUTION]
> 自定义智能体必须包含带 `name` 和 `description` 的 frontmatter。

3. 接着浏览后续部分，查看其中强调的内容：
   - 为无障碍网站生成代码时的核心职责。
   - 无障碍最佳实践。
   - HTML、CSS 和 JavaScript 的代码示例。
   - 常见陷阱和错误列表。

## 在 Copilot CLI 中使用自定义智能体

可以通过 `/agent` 命令在 Copilot CLI 中启动自定义智能体。现在对网站执行一次无障碍检查。

> [!TIP]
> **启动 Copilot CLI 会话**
>
> 开始下面的练习前，先返回 codespace 并打开一个终端（如果还没打开，可按 <kbd>Ctrl</kbd>+<kbd>\`</kbd>）。然后使用 `--yolo` 和 `--enable-all-github-mcp-tools` 启动 Copilot CLI：
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 如果希望接续这个项目最近一次会话，而不是重新开始，请运行 `copilot --yolo --enable-all-github-mcp-tools --continue`。如果 Copilot CLI 仍在运行之前练习中的会话，请发送 `/clear` 开始一段新的对话。
>
> `--enable-all-github-mcp-tools` 会为当前会话启用 GitHub MCP 读写工具，因此在工作坊流程中 Copilot 可以读取积压工作并打开 pull request。

> [!CAUTION]
> `--yolo` 会启用完整的自动权限（`--allow-all-tools`、`--allow-all-paths` 和 `--allow-all-urls`）。只能在 Codespace 或 VM 这类隔离环境中使用，绝不要把它设成日常开发的默认别名。详情见[允许和拒绝工具使用][allow-all-warning]。

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. 在 Copilot CLI 的提示窗口中输入 `/agent` 并选择 <kbd>Enter</kbd>，调出智能体列表。
2. 从可用智能体列表中选择 **Accessibility agent**。
3. 使用以下提示，请无障碍智能体执行审查，并为无障碍积压工作项生成修复：

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. Copilot 会开始处理这项任务。它会先检索 issue，然后执行审查、生成更新，最后创建 PR。创建 PR 时，还会注意到它使用了项目中专门处理 PR 的技能。

> [!NOTE]
> 这个过程可能需要几分钟。正好可以回顾一下到目前为止学到的所有内容、休息片刻，或者提前看一下下一模块——其中会介绍 Copilot CLI 中更多可用命令。

## 总结和后续步骤

本课探索了 GitHub Copilot 中的[自定义智能体][custom-agents]：它们是面向特定任务和领域定制的专用 AI 助手。通过自定义智能体，可以把团队的经验和标准固化为可复用智能体，引导 Copilot 更高效地完成特定类型的工作。

本课探索了以下概念：

- 自定义智能体是如何定义的。
- 如何在 Copilot CLI 中使用自定义智能体。

接下来将探索[一些斜杠命令][next-lesson]，学习更多 Copilot CLI 的使用技巧。

## 资源

- [自定义智能体][custom-agents]
- [为存储库创建自定义智能体][creating-custom-agents]
- [awesome-copilot 上的自定义智能体][awesome-copilot-agents]
- [在组织中启用自定义智能体的准备工作][org-custom-agents]
- [在企业中启用自定义智能体的准备工作][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
