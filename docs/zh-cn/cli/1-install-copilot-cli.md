---
title: "练习 1 - 安装 GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
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

1. 如果当前不在 codespace 中，请先返回。
2. 按 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 打开终端窗口。
3. 应该会在 VS Code 窗口底部看到终端面板。

## 安装 Copilot CLI

可以通过 [npm][install-npm]、[WinGet][install-winget] 和 [Homebrew][install-homebrew] 安装 Copilot CLI。由于 GitHub Codespaces 已预装 Node.js，本练习使用 npm 安装 Copilot CLI。

1. 在终端中确认 Node.js 已安装，并满足版本要求：

   ```bash
   node --version
   ```

   应看到版本 22 或更高（例如 `v22.x.x`）。

2. 使用 npm 在 codespace 中全局安装 Copilot CLI：

   ```bash
   npm install -g @github/copilot
   ```

3. 通过查看版本验证安装：

   ```bash
   copilot --version
   ```

   应看到显示的版本号（例如 `v1.0.XX`）。

> [!TIP]
> 如果遇到权限错误，在某些系统中可能需要使用 `sudo npm install -g @github/copilot`。不过在 GitHub Codespaces 中通常不需要这样做。

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

   ```
   What files are in this project?
   ```

4. Copilot 应该会探索存储库，并给出项目结构摘要。
5. 试用 `/help` 命令查看可用的斜杠命令：

   ```
   /help
   ```

6. 在终端中输入以下命令退出 Copilot CLI。后续练习还会回到 Copilot CLI。

   ```
   exit
   ```

## 总结和后续步骤

恭喜，已成功安装并验证 GitHub Copilot CLI。现在已经学会如何：

- 使用 npm 安装 Copilot CLI。
- 使用 GitHub 账户完成验证。
- 信任一个目录，以便 Copilot CLI 可以处理其中内容。
- 确认安装运行正常。

现在 Copilot CLI 已安装完成，接下来为 Copilot 提供一些项目上下文。继续前往[练习 2 - 通过 CLI 使用自定义说明][next-lesson]。

## 资源

- [安装 GitHub Copilot CLI][install-copilot-cli]
- [关于 Copilot CLI][about-copilot-cli]
- [使用 Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-custom-instructions/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
