---
title: "练习 3 - 使用 GitHub Copilot CLI 添加项目功能"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

正如预期，使用 GitHub Copilot CLI 执行的核心任务之一，就是向项目添加功能、特性和代码。现在从积压工作中选取一个 issue，请 Copilot 帮助实现它。

## 场景

现在到了完成项目过滤功能的时候。积压工作中已经有这个过滤 issue，上一节练习还提供了一个基础 helper。接下来让 Copilot 获取 issue 详情，考虑现有工作，并补齐剩余功能。

在本练习中，将：

- 使用计划模式生成实现过滤功能的计划。
- 使用 Copilot 生成向网站添加过滤功能所需的代码。

完成本练习后，项目中将新增这项功能。

## 使用计划模式

AI 最适合做的事情之一就是规划。很多时候，对要构建的内容已经有大致想法，只是需要一个对象来帮助梳理思路。AI 工具可以通过追问和分析潜在问题或遗漏项，帮助把想法变得更清晰。为支持这一过程，Copilot CLI 提供了计划模式。此外，花在规划上的时间也会帮助 Copilot 生成更符合要求的代码。

接下来将通过 Copilot CLI 的计划模式，开始创建这项新功能。

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

1. 在 Copilot CLI 中输入以下提示，根据过滤 issue 创建计划：

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

2. Copilot 在生成计划时可能会提出后续问题。出现时，可根据希望实现功能的方式进行回答。
3. 计划生成后，查看这份蓝图。应能看到它建议在数据层和 UI 中进行剩余变更，并生成测试。
4. Copilot CLI 会提供继续反馈计划的能力。可将光标移到指定区域，然后输入建议。Copilot 会把这些建议整合进新版本计划。
5. 满意后，选择 Copilot 提供的选项，开始构建这个新功能。

> [!NOTE]
> 由于 Copilot 是概率性的，提供的具体文本和选项会有所不同。但会看到一个开始构建的选项，内容大致类似：
>
> `Yes, and switch to autopilot mode`.
>
> Copilot 可能会像上面的示例一样，提供启用 [autopilot mode](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot) 的选项。autopilot mode 允许 Copilot CLI 在每一步后无需等待输入，自主完成整个任务。给出初始指令后，Copilot CLI 会自动执行各个步骤，直到判断任务完成。由于当前运行在受控环境中，可以放心启用 autopilot 并允许所有工具。

6. Copilot 会开始生成文件。

> [!NOTE]
> 这个操作很可能需要几分钟。会看到 Copilot 编辑和创建文件、更新和生成测试，并运行全部测试以确保成功。此时可以顺便回顾前面学到的内容，或者喝点东西休息一下。

## 查看代码

所有 AI 生成的代码在合并到生产环境前都需要审查。现在就来查看 Copilot 为实现新功能而创建和修改的文件。

1. 在 Copilot CLI 中使用以下命令显示“diff”或代码变更：

    ```
    /diff
    ```

2. 注意已更改的文件。使用方向键左右切换查看不同文件。应能看到游戏列表页面（新过滤控件和客户端过滤逻辑所在位置）、`src/lib/games.ts`，以及 `games.test.ts` 等测试文件的更新。如果 Copilot 为了与完整实现保持一致而优化了现有 helper，也可能会看到 `publishers.ts` 的更新。

## 总结和后续步骤

现在已经借助 Copilot CLI 为网站添加了过滤功能。具体来说，完成了以下事项：

- 使用计划模式生成了实现过滤功能的计划。
- 生成了向网站添加过滤功能所需的代码。

当然，下一步就是确认它确实可用。在打开 pull request 之前，先[使用 Playwright MCP 服务器测试这个功能][next-lesson]。

## 资源

- [使用 Copilot CLI][using-copilot-cli]
- [关于 Copilot CLI][about-copilot-cli]
- [Copilot CLI 中的上下文管理][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
