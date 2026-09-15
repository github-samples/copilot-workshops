---
title: "练习 1 - 安装 GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[GitHub Copilot CLI][about-copilot-cli] 是一个功能强大的代理式编码助手，可在终端中运行，让开发者通过命令行探索代码库、生成代码、运行命令并与外部工具交互。它可以帮助分担任务、请求变更，并保持专注。第一步自然是安装这个工具，好在可以使用已经熟悉的工具来完成。

在本练习中，将学习如何：

- 使用 npm 安装 GitHub Copilot CLI。
- 使用 GitHub 账户完成验证。
- 验证安装结果。

## 场景

团队开始使用 AI agent 处理不断增长的积压工作。Copilot CLI 将这种能力带入终端，而终端本就是许多开发者的主要工作环境。本练习会完成安装和验证，为后续工作坊中的使用做好准备。

## 在 codespace 中打开终端

安装 Copilot CLI 前，需要先在 codespace 中打开终端窗口。

1. 返回 codespace，等待设置完成。
2. 按 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 打开终端窗口。
3. 应该会在 VS Code 窗口底部看到终端面板。

## 确认练习环境

在 codespace 终端中，确认当前位于自己的 Tailspin Toys 存储库，而不是研讨会内容存储库。阅读其中的 `README.md` 和 `package.json`，了解设置和检查命令。当前 Tailspin Toys 需要 Node.js 22.13 或更高版本、项目依赖项，以及用于 E2E 测试的 Playwright Chromium。

```bash
pwd
git remote -v
node --version
gh auth status
```

GitHub CLI（`gh`）可帮助检查 PR 和 CI。如果尚未完成身份验证，使用 `gh auth login` 并遵循浏览器指引。确认当前账户能够在此存储库中推送分支、创建及合并 PR；组织策略可能要求其他审查者参与。开始代码更改前，按存储库设置说明解决缺失的先决条件，并在授权安装前进行审查。

CLI 使用启动时所在的检出目录；开始对话不会自动创建隔离的工作树。本研讨会为每个 PR 里程碑使用一个分支。先合并星级评分和指令示例，再在练习 4–8 中保持同一筛选分支。

## 安装 Copilot CLI

可以通过 [npm][install-npm]、[WinGet][install-winget] 和 [Homebrew][install-homebrew] 安装 Copilot CLI。由于 GitHub Codespaces 已预装 Node.js，本练习使用 npm 安装 Copilot CLI。

1. 在终端中确认 Node.js 已安装，并满足版本要求：

   ```bash
   node --version
   ```

   Tailspin Toys 需要 22.13 或更高版本，即使 CLI 自身的要求有所不同。如果版本过旧，请遵循练习存储库的设置说明。

2. 使用 npm 在 codespace 中全局安装 Copilot CLI：

   ```bash
   npm install -g @github/copilot
   ```

3. 通过查看版本验证安装：

   ```bash
   copilot --version
   ```

   应看到显示的版本号（例如 `v1.0.XX`）。

> [!NOTE]
> 如果安装因权限错误而失败，应检查 npm 配置或向研讨会导师求助，而不是提升权限后重新运行不熟悉的命令。

## 使用 GitHub 完成验证

首次启动时，Copilot CLI 会提示使用 GitHub 账户完成验证。

1. 启动 Copilot CLI：

   ```bash
   copilot
   ```

2. 如果当前尚未登录，会看到验证提示。Copilot CLI 会显示一个设备代码，并要求访问一个 URL。
3. 按照屏幕上的说明操作：
   - 在浏览器中打开提供的 URL
   - 在提示时输入设备代码
   - 授权 Copilot CLI 访问 GitHub 账户
4. 验证完成后，会看到 Copilot CLI 提示符，可以开始输入问题和命令。

> [!NOTE]
> 在 codespace 中，可能已经通过 GitHub 会话完成验证。如果 Copilot CLI 启动时没有提示验证，就表示可以直接使用。

## 信任目录并确认一切正常

首次进入 Copilot CLI 提示符后，先信任这个工作坊存储库，并确认 Copilot CLI 已正确安装并连接成功。

1. 当 Copilot CLI 要求确认是否信任此文件夹中的文件时，会看到三个选项：
   - **Yes, proceed**：仅信任当前会话
   - **Yes, and remember this folder for future sessions**：永久信任
   - **No, exit (Esc)**：不允许访问文件
2. 对于本工作坊，请选择 **Yes, and remember this folder for future sessions**，因为后续会持续在这个存储库中工作。
3. 向 Copilot 提一个简单问题，确认它运行正常：

   ```plaintext
   这个项目中有哪些文件？
   ```

4. Copilot 应该会探索存储库，并给出项目结构摘要。
5. 试用 `/help` 命令查看可用的斜杠命令：

   ```text
   /help
   ```

6. 在 Copilot 提示符处输入以下命令，退出此会话。你将为第一次更改启动新会话。

   ```text
   /exit
   ```

## 了解模式和权限

Copilot CLI 在启动时所在的目录和 Git 分支中工作。信任目录使其能够使用存储库上下文，但不等于批准所有工具操作。应审查文件更改、shell 命令和 GitHub 操作的权限请求。

从练习存储库根目录启动代码练习：

```bash
copilot --enable-all-github-mcp-tools
```

GitHub MCP 服务器是内置的。此标志提供完整工具集，供处理议题和 PR；身份验证、存储库权限和工具批准仍然适用。该标志本身并不授权提交或创建 PR。

使用 <kbd>Shift</kbd>+<kbd>Tab</kbd> 在标准 **Interactive**、**Plan** 和 **Autopilot** 模式之间切换。发送请求前检查模式指示器。早期更改保持 Interactive，构建筛选功能前先规划，创建和审查自定义配置前明确切回 Interactive。

> [!CAUTION]
> 模式和权限设置是两回事。Autopilot 会自主持续工作；`--allow-all` 及其别名 `--yolo` 则授予全部工具、路径和 URL 权限。本研讨会不要求每个会话都使用无限制权限启动。即使在 codespace 中，授予访问权限前也应审查范围。

## 总结和后续步骤

恭喜，已成功安装并验证 GitHub Copilot CLI。现在已经学会如何：

- 使用 npm 安装 Copilot CLI。
- 使用 GitHub 账户完成验证。
- 信任一个目录，以便 Copilot CLI 可以处理其中内容。
- 确认安装运行正常。

现在 Copilot CLI 已安装完成，前往[练习 2 - 添加星级评分：快速上手][next-lesson]，完成一项便于审查的小改动。

## 资源

- [安装 GitHub Copilot CLI][install-copilot-cli]
- [关于 Copilot CLI][about-copilot-cli]
- [使用 Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
