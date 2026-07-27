---
title: "练习 7 - GitHub Copilot CLI 中的斜杠命令"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

像其他优秀的 CLI 工具一样，GitHub Copilot CLI 也提供了许多斜杠命令供交互使用。这些命令会暴露高级功能、“幕后”信息或额外的配置选项。前面已经体验过 `/clear`（清理上下文）和 `/mcp`（查看 MCP 服务器）。接下来再探索几个强大的命令，包括 `/context`、`/model`、`/share` 和 `/delegate`。

## 场景

核心 CLI 流程已经体验完毕。现在再看看一些附加能力——共享会话、切换模型，以及把任务委托给 [Copilot cloud agent][about-cloud-agent]。

在本练习中，将使用：

- `/share` 创建一个 GitHub gist，与团队共享会话。
- `/context` 查看 Copilot CLI 当前使用的上下文。
- `/model` 查看可用模型列表，并在需要时选择新的模型。
- `/delegate` 可选地把任务移交给 cloud agent。这需要 cloud agent，Copilot Student、Pro、Pro+、Business 和 Enterprise 都支持——只有 Copilot Free 不支持。

## 共享会话

无论使用什么工具，包括 AI 工具，本身都是一种技能。与团队一起工作、彼此分享经验，是帮助所有人提升体验并生成更高质量代码的最佳方式。为此，Copilot CLI 提供了 `/share` 命令。`/share` 可以生成 markdown 文件或 GitHub gist，其中包含会话详情、使用过的提示以及 Copilot 采取的逻辑。

现在创建一个可以分享给团队的 GitHub gist。

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

1. 在 Copilot CLI 的提示窗口中发送以下命令：

    ```
    /share gist
    ```

2. 稍等片刻后，Copilot 会创建一个 gist 并显示链接。
3. 复制该链接文本。
4. 在新的浏览器标签页中粘贴链接并查看 gist。注意其中如何突出显示已发送的提示、使用过的技能和智能体、Copilot 的思考过程，甚至包括本地运行命令的代码和结果。

`/share` 生成的 gist 和 markdown 文件，既可以作为代码生成过程的文档，也可以用于向团队分享某些操作是如何完成的，以及这些操作如何帮助 Copilot 生成期望结果。

## 探索 Copilot CLI 的上下文

处理较大或较复杂的任务时，可能会触及模型的最大上下文窗口。窗口的具体大小取决于所使用的模型和 Copilot CLI 版本。当上下文窗口达到上限时，Copilot CLI 会自动压缩上下文，总结信息并移除它认为与当前任务无关的内容。可以使用斜杠命令查看当前上下文状态，也可以手动压缩上下文。现在来看看上下文窗口。

1. 在 Copilot CLI 的提示窗口中发送以下命令：

    ```
    /context
    ```

2. 稍等片刻后，Copilot CLI 会生成当前上下文的可视化表示：

    ![Copilot CLI 上下文窗口截图](../../_images/cli-7-context-window.png)

3. 注意显示的模型（可能与图片中不同）以及当前已使用的 token 百分比。其余信息展示了以下内容：

    | 标题 | 说明 |
    | ------------ | ------------------------------------------------------ |
    | System/Tools | 说明文件、文件内容和工具定义 |
    | Messages     | 与 Copilot 的对话历史 |
    | Buffer       | Copilot CLI 为生成响应预留的空间 |
    | Free space   | 剩余可用空间 |

4. 向 Copilot CLI 发送以下斜杠命令，压缩对话历史：

    ```
    /compact
    ```

5. 完成后，再次发送以下命令，显示当前上下文统计：

    ```
    /context
    ```

6. 注意上下文的变化。由于当前上下文窗口可能还比较小，变化未必十分明显。

> [!NOTE]
> 当上下文变满时，Copilot CLI 会自动压缩。接近 100% 容量时，它会在提示窗口上方显示百分比。通常它会异步压缩，因此在处理过程中仍可继续与 Copilot 交互。不过，它也可能在执行压缩时阻塞当前操作几秒钟。

### 上下文最佳实践

在大多数会话中，Copilot 本身就能高效管理上下文，通常不需要额外指导。不过，在某些情况下，可能会决定手动指示 Copilot 清空或压缩其历史记录：

- 如果要切换到应用的其他部分，或转到无关任务，可以使用 `/clear` 重新开始，避免旧的无关上下文让 Copilot 混淆。
- 如果即将接近最大上下文窗口，可以手动使用 `/compact`，自行控制压缩发生的时机。

> [!CAUTION]
> 再次强调，大多数时候 Copilot 都能在无需直接干预的情况下管理上下文。如果发现 Copilot 因较早的信息而有些混乱，或者即将切换到无关任务，再考虑使用这些手动命令即可。

## 选择模型

不同模型有不同的强项，不同开发者也会有不同偏好。Copilot CLI 允许列出并选择要使用的模型。

1. 向 Copilot CLI 发送以下斜杠命令，显示模型列表：

    ```
    /model
    ```

2. 查看模型列表。每个模型旁边都会显示其名称及单次请求成本修正值。
3. 如果需要，可以选择一个新模型；或者选择 <kbd>Esc</kbd> 退出模型列表。

> [!CAUTION]
> 在 Copilot CLI 中，模型选择会持久保留。

## 委托给 cloud agent（可选）

有时希望继续在终端中工作，但把耗时较长的任务交给 Copilot cloud agent。`/delegate` 命令会把当前 Copilot CLI 会话发送到 GitHub.com，由 cloud agent 接手，异步处理，并在完成后打开 pull request。

> [!NOTE]
> `/delegate` 需要 cloud agent，Copilot Student、Pro、Pro+、Business 和 Enterprise 都支持——只有 Copilot Free 不支持。如果没有访问权限，可以阅读这一部分，然后跳过动手步骤。

1. 先清空当前会话，避免把整个工作坊累积的上下文一并委托出去：

    ```
    /clear
    ```

2. 发送一个范围较小、定义清晰的提示。例如，可以委托积压工作中的延伸目标——分页功能：

    ```
    Implement pagination on the game list page so it shows a fixed number of games per page with Previous and Next controls, and add tests.
    ```

3. 发送以下斜杠命令，把会话交给 cloud agent，并确认要委托的提示：

    ```
    /delegate
    ```

4. 在浏览器中打开 [Copilot agents](https://github.com/copilot/agents) 以监控进度。
5. 在这个路径中，无需等待 pull request 完成；稍后可以再回来查看。如果想更深入了解如何管理异步 agent 工作，可继续学习 [Cloud agent 路径](../../cloud/)。

## 总结和后续步骤

在 Copilot CLI 中使用斜杠命令，可以对它进行配置、共享会话，并查看 Copilot 工作方式的内部信息。本课中，已经使用或了解了以下内容：

- 使用 `/share` 创建 GitHub gist，与团队共享会话。
- 使用 `/context` 查看 Copilot CLI 当前使用的上下文。
- 使用 `/model` 查看可用模型列表，并在需要时选择新的模型。
- 了解了 `/delegate` 作为连接 cloud agent 的可选桥梁。

当然，还有更多斜杠命令可用，也还有更多 Copilot CLI 功能值得探索。最后通过[回顾已学内容][next-lesson]以及后续学习方向，为这段旅程收尾。

## 资源

- [使用 Copilot CLI][using-copilot-cli]
- [关于 Copilot CLI][about-copilot-cli]
- [Copilot CLI 中的上下文管理][context-management]
- [使用 Copilot CLI 共享会话][share-sessions]
- [在 Copilot CLI 中选择模型][selecting-models]

[previous-lesson]: ../6-custom-agents/
[next-lesson]: ../8-review/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
[share-sessions]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#share-sessions
[selecting-models]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#select-an-llm
