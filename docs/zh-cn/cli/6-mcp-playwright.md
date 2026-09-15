---
title: "练习 6 - 使用 Playwright MCP 验证功能"
description: "通过 MCP 连接浏览器，将观察到的筛选行为与议题和批准的计划进行比较。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

筛选实现和 quality-checks 技能已经过自动化验证。现在为 Copilot 提供浏览器，让它直接观察功能。本练习展示**模型上下文协议（MCP）**交互，而不是再次运行完整测试套件。

在同一筛选检出目录和分支上保持 **Interactive** 模式。配置 MCP 不会开始新的功能里程碑。

在本练习中，你将：

- 连接 Playwright MCP，确认其浏览器工具可用。
- 将实际筛选行为与议题及已批准的标准进行比较。
- 审查观察结果，并停止自己启动的开发服务器。

## 场景

自动化检查已通过，但 Tailspin Toys 还需要有关访客体验的证据。你将为 Copilot 提供浏览器工具，让它操作筛选器，并将显示的游戏与约定行为进行比较，而不是把控件能够响应当作筛选功能正确运行的证明。

## MCP 带来的能力

[MCP][mcp-overview] 通过服务器将智能体连接到外部工具和上下文。内置 GitHub MCP 服务器让 Copilot 能处理议题和 PR。[Playwright MCP 服务器][playwright-mcp]则提供打开页面、检查无障碍元素、导航及操作控件的浏览器工具。

浏览器的无障碍快照有助于智能体识别控件，但不能证明完全符合无障碍要求。应将实际操作和观察结果与议题要求进行比较，而不是接受笼统的“看起来不错”。

> [!CAUTION]
> 将 MCP 服务器视为项目依赖项：启用前审查发布者、源代码、权限和所有包下载。组织策略可能限制可运行的服务器。不要将凭据放入已提交的配置，也不要只为完成练习而批准未知工具。

## 配置 Playwright MCP

1. 在现有 CLI 会话中输入 `/mcp`，检查已配置的服务器。复用可用的 Playwright 配置，不要重复添加。
2. 如有需要，输入 `/mcp add`，使用 <kbd>Tab</kbd> 在表单中移动。
3. 将 **Server Name** 设为 `playwright`，**Server Type** 设为 **STDIO**（或 **Local**），**Command** 设为 `npx @playwright/mcp@latest --headless`。
4. 为此已审查的浏览器服务器，将 **Tools** 设为 `*`。这会使其工具可用，但不会替代 CLI 的权限控制。
5. 审查包及启动命令后，按 <kbd>Ctrl</kbd>+<kbd>S</kbd> 保存。注册会启动服务器，并可能下载包；应明确批准该设置，并回应包提示。
6. 输入 `/mcp show playwright`，确认服务器已连接且浏览器工具可用。

无头浏览器无需桌面窗口，适合 Codespaces。交互式添加流程将配置保存到 `~/.copilot/mcp-config.json`，无需重启 CLI 即可使用服务器。这是用户配置，不是应包含在功能 PR 中的文件。[MCP 设置指南][mcp-setup]说明了相关字段和配置来源。

> [!NOTE]
> 项目 E2E 依赖项与 MCP 浏览器有关，但可能需要不同设置。如果缺少浏览器或系统依赖项，应检查实际错误，并获批后解决具体的先决条件。不要自动安装浏览器，也不要假定服务器已连接就证明它能启动浏览器。

## 启动正确的应用

在同一筛选检出目录中打开单独的终端。确认目录和分支，再启动应用：

```bash
pwd
git branch --show-current
npm run dev
```

从服务器输出中读取实际本地 URL。在 codespace 中，MCP 服务器和应用处于同一环境，因此使用该本地 URL，通常是 `http://localhost:4321`，不要假定必须使用转发后的浏览器 URL。

如果端口已占用或 Astro 选择了其他端口，继续前先确定服务器归属。不要复用或终止未知服务器。使用刚启动进程的 URL，并在测试期间保持该终端打开。

## 观察筛选行为

将占位符替换为真实议题 URL、练习 4 中批准的澄清内容和应用 URL：

```plaintext
使用已配置的 Playwright MCP 服务器，根据此议题验证筛选功能：<filtering-issue-URL>。以下是规划时批准的澄清内容：<粘贴约定的澄清内容，或填写 none>。当前检出目录的应用运行于 <local-app-URL>。在依赖结果前，确认被测检出目录、分支和服务器。

打开游戏页面，记录未筛选状态，先选择一个类别，再选择多个类别，应用发行商筛选，并组合类别和发行商选择。根据批准的标准测试清除筛选和空结果行为。检查控件标签、键盘操作和可见焦点。将显示结果与所选筛选条件及源数据比较，不要仅因为控件发生变化就推断成功。

使用实际浏览器工具操作，逐项报告观察到的结果，并明确标出失败或缺失证据。不要仅为此浏览器练习再次运行完整测试套件，不要更改应用代码、创建测试或自定义配置、更改分支、提交、推送或打开 PR。在安装任何内容或停止其他进程前先询问。
```

检查浏览器工具调用和报告。Copilot 是否确实选择了多个类别并与发行商组合？返回的游戏是否符合约定行为？报告是否区分了可观察的浏览器行为、数据层覆盖和自动化测试覆盖？

如果失败，记录观察到的行为。单独授权针对性的应用修复，再重复受影响的浏览器检查和自动化检查。不要为了迁就实现而修改验收标准，也不要将旧证据算作更改后代码的验证。

## 停止自己启动的服务器并继续

在启动开发服务器的终端中按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 停止它。保持 Playwright MCP 配置可用。练习 7 将协调新的浏览器观察和自动化 E2E 检查，这些检查不得复用过时的开发服务器或其他检出目录的应用。

## 总结与后续步骤

创建 QA 配置文件前保持 **Interactive**。你已观察浏览器行为，没有额外创建 PR 或分支；接下来[创建并使用 QA 智能体][next-lesson]，将需求、覆盖情况、技能和最终证据结合起来。

## 资源

- [向 Copilot CLI 添加 MCP 服务器][mcp-setup]说明设置和管理方式。
- [Microsoft Playwright MCP][playwright-mcp] 说明浏览器配置和工具。
- [GitHub MCP 注册表][mcp-registry]列出其他可供评估的服务器。

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-overview]: https://docs.github.com/copilot/concepts/context/mcp
[mcp-setup]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
[playwright-mcp]: https://github.com/microsoft/playwright-mcp
[mcp-registry]: https://github.com/mcp
