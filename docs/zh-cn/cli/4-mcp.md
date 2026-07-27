---
title: "练习 4 - 使用 Playwright MCP 服务器测试功能"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

刚刚已经使用 Copilot CLI 生成了过滤功能。在打开 pull request 之前，应该先确认它在浏览器中能够正常工作。与其手动点选应用，不如连接 **Playwright MCP 服务器**，让 Copilot 驱动真实浏览器代为测试。

在本练习中，将：

- 了解什么是 Model Context Protocol (MCP)，以及 MCP 服务器如何扩展 Copilot CLI。
- 将 Playwright MCP 服务器添加到 Copilot CLI。
- 要求 Copilot 使用它在浏览器中手动测试过滤功能。

## 什么是 Model Context Protocol (MCP)？

[Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) 为 AI 智能体提供了一种与外部工具和服务通信的方式。借助 MCP，AI 智能体可以实时连接外部工具和服务，从而获取最新信息（通过资源），并代表执行操作（通过工具）。

这些工具和资源通过 MCP 服务器访问，它充当 AI 智能体与外部工具和服务之间的桥梁。MCP 服务器负责管理 AI 智能体与外部工具之间的通信（例如现有 API 或 NPM package 这类本地工具）。每个 MCP 服务器都代表一组不同的工具和资源，供 AI 智能体访问。

几个常见的 MCP 服务器包括：

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**：该服务器提供一组 API，用于管理 GitHub 存储库。它允许 AI 智能体执行创建新存储库、更新现有存储库、管理 issue 和 pull request 等操作。
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**：该服务器提供基于 Playwright 的浏览器自动化能力。它允许 AI 智能体执行导航到网页、填写表单和选择按钮等操作。

还有许多其他 MCP 服务器可提供对不同工具和资源的访问。GitHub 托管了一个 [MCP registry](https://github.com/mcp)，以提升生态系统中的可发现性和协作贡献。

> [!CAUTION]
> 从安全角度看，应像对待项目中的其他依赖项一样对待 MCP 服务器。使用前，请仔细审查其源代码、验证发布者，并评估安全影响。只使用可信的 MCP 服务器，并谨慎授予对敏感资源或操作的访问权限。

> [!NOTE]
> [GitHub MCP 服务器][github-mcp-server] 是 Copilot CLI 的**内置**能力——无需任何设置即可使用，这也是为什么在整个工作坊中 Copilot 能持续读取和写入存储库。本练习将添加*第二个*服务器，即 Playwright，为 Copilot 提供浏览器能力。

## 添加 Playwright MCP 服务器

添加服务器最快的方法是使用交互式 `/mcp add` 命令。这里将注册 [Playwright MCP 服务器][playwright-mcp-server]，让 Copilot 获得一个可控浏览器。

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

1. 在 Copilot CLI 会话中输入：

    ```text
    /mcp add
    ```

2. 此时会出现一个配置表单。使用 <kbd>Tab</kbd> 在字段之间切换，并按如下内容填写：

    - **Server Name**：`playwright`
    - **Server Type**：选择 **Local**（也标记为 **STDIO**）
    - **Command**：`npx @playwright/mcp@latest --headless`
    - **Tools**：保持为 `*`，允许使用该服务器的全部工具

3. 按 <kbd>Ctrl</kbd>+<kbd>S</kbd> 保存。服务器会立即添加并可用——无需重启。

`--headless` 标志表示让 Playwright 在无可见窗口的模式下运行，这对于没有桌面界面的 codespace 是必需的。在后台，这会把服务器写入 `~/.copilot/mcp-config.json` 文件：

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. 通过列出 MCP 服务器，确认该服务器已注册并处于活动状态：

    ```text
    /mcp show
    ```

5. 应该会看到 `playwright` 与内置的 `github` 服务器一起列出。

> [!NOTE]
> Tailspin Toys 项目本身已经使用 Playwright 进行端到端测试，因此 Playwright 所需的浏览器通常已经安装好。如果之后 Copilot 提示缺少浏览器，让它运行 `npx playwright install chromium`，然后重试。

## 启动网站

Playwright MCP 服务器需要一个正在运行的应用作为测试目标。请在**单独**的终端中启动 Astro 开发服务器，这样在使用 Copilot CLI 时它才能持续运行。

1. 在 codespace 中选择 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 打开一个新终端。
2. 启动网站：

    ```bash
    npm run dev
    ```

3. 保持这个终端持续运行。看到 `Astro server: http://localhost:4321` 横幅后，说明应用已就绪。

## 测试过滤功能

返回 Copilot CLI 会话，并请 Copilot 测试这个功能。

[Playwright MCP 服务器][playwright-mcp-server] 会为 Copilot 提供一个可以驱动的真实浏览器。无需手动点选应用来检查结果，智能体可以打开页面、导航、应用过滤条件，并把结果读回给你——然后总结其观察结果。这是在不离开当前对话的情况下，快速确认功能是否符合预期的最佳方式。

在底层，Playwright MCP 服务器依赖页面的[无障碍树][playwright-mcp-server]而不是截图来工作。这意味着智能体会基于结构化、带标签的元素（按钮、链接、列表项）进行推理，方式与辅助技术类似——因此一次快速的功能检查，也兼具轻量级的无障碍合理性检查。

在服务器已连接且应用已运行的情况下，请 Copilot 演练刚刚构建的过滤功能：

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

Copilot 会通过 Playwright MCP 服务器启动浏览器，依次执行每一步，并反馈它发现的内容。将它的总结与 issue 中的验收标准对照——如果有任何异常，可以继续追问，或在打开 pull request 之前让它回头修复代码。

> [!NOTE]
> 本测试要求应用运行在 `http://localhost:4321`。如果已经停止开发服务器，请在发送提示前重新启动。Copilot 第一次使用 Playwright MCP 服务器时，可能需要下载浏览器——如果提示缺少浏览器，让它运行 `npx playwright install chromium` 后再试一次。

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp

## 总结和后续步骤

恭喜，已经使用 Playwright MCP 服务器配合 Copilot CLI 手动测试了这个功能。回顾一下，完成了以下事项：

- 了解了什么是 Model Context Protocol (MCP)，以及 MCP 服务器如何扩展 Copilot CLI。
- 使用 `/mcp add` 添加了 Playwright MCP 服务器。
- 要求 Copilot 驱动浏览器，在发布前验证过滤功能。

现在既然已经确认功能正常，可以继续下一节练习，在那里将[借助智能体技能打开一个 pull request][next-lesson]。

## 资源

- [MCP 到底是什么，为什么大家都在讨论它？][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [为 Copilot CLI 添加 MCP 服务器][cli-add-mcp]
- [GitHub MCP Server][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
