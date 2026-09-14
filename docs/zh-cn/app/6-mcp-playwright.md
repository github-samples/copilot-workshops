---
title: "第 6 课 - 使用 Playwright MCP 验证功能"
description: "通过 Customize 配置 Playwright MCP，在现有功能工作树中通过浏览器观察筛选功能。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

上一课通过 quality-checks 技能封装并运行了项目检查。现在让智能体访问浏览器，直接观察筛选 UI。保持同一筛选会话、工作树和分支。本课添加浏览器证据，而不是另一个功能、一次完整测试套件运行或一个 PR。

本课将介绍如何：

- 了解模型上下文协议 (MCP) 及 GitHub Copilot app 如何使用它。
- 通过 **Customize** 添加 Playwright MCP 服务器。
- 要求智能体操控浏览器并探索筛选功能。

## 场景

单元测试和端到端测试很重要，但验证 UI 更新需要实际与 UI 交互。你希望 Copilot 能像用户一样使用正在开发的网站，以进一步自动执行更改并提高对更新符合预期的信心。

## 什么是模型上下文协议 (MCP)？

[模型上下文协议 (MCP)][mcp-blog-post] 为 AI 智能体提供了与外部工具和服务通信的方式。借助 MCP，AI 智能体可以实时与外部工具和服务通信。这让它们既能访问最新信息（使用资源），也能代表你执行操作（使用工具）。

这些工具和资源通过 MCP 服务器访问。MCP 服务器是 AI 智能体与外部工具和服务之间的桥梁，负责管理双方的通信。外部工具可以是现有 API，也可以是 NPM 包等本地工具。每个 MCP 服务器代表 AI 智能体可访问的一组不同工具和资源。

以下是两种常用的现有 MCP 服务器：

- [**GitHub MCP Server**](https://github.com/github/github-mcp-server)：提供一组用于管理 GitHub 存储库的 API。AI 智能体可以创建新存储库、更新现有存储库，以及管理议题和拉取请求。
- [**Playwright MCP Server**][playwright-mcp-server]：使用 Playwright 提供浏览器自动化功能。AI 智能体可以转到网页、填写表单和选择按钮。

还有许多其他 MCP 服务器可用于访问不同的工具和资源。GitHub 托管了一个 [MCP registry](https://github.com/mcp)，以提高生态系统的可发现性并促进贡献。

> [!CAUTION]
> 应像对待项目中的任何其他依赖项一样对待 MCP 服务器。使用前请仔细审查其源代码、验证发布者并考虑安全影响。仅使用可信的 MCP 服务器，并谨慎授予对敏感资源或操作的访问权限。

## 添加 Playwright MCP 服务器

当前的 [App 自定义文档][customize-app]使用侧边栏中的 **Customize** 来发现和管理 MCP。在存储库或 Copilot CLI 中配置的 MCP 服务器可能已在 App 中可用；添加前先检查已安装的服务器，避免重复。

1. 在侧边栏中选择 **Customize**。
2. 选择 **MCP**，再检查 **Installed** 中是否已有 Playwright 服务器。
3. 如有需要，在可用服务器中找到 **Playwright**，或使用发布者文档说明的自定义服务器流程。
4. 批准前审查发布者、配置和所有安装提示。按提示添加服务器；组织策略或缺少先决条件可能阻止设置。
5. 返回现有筛选会话，保持 **Interactive** 模式。请求验证前，确认 Playwright MCP 浏览器工具可用。不要通过创建新的功能工作树来绕过设置问题。

如果设置失败，应解决配置或权限问题，不要接受智能体未使用工具却声称已浏览的说法。浏览器是否可见取决于服务器配置；实际工具活动和观察结果才是证据。

## 要求 Copilot 通过 Playwright 探索功能

使用第 4 课保存的实际议题 URL 和批准的澄清内容。在智能体启动自己的服务器前，停止之前课程中手动启动的开发服务器。智能体必须确定被测检出目录和服务器。

1. 使用以下提示词，要求 Copilot 验证新功能：

   ```plaintext
   使用已配置的 Playwright MCP 服务器，根据此议题观察筛选功能：<filtering-issue-URL>。以下是我批准的规划澄清内容：<粘贴约定的澄清内容，或填写 none>。保持当前筛选工作树和分支。

   确定检出目录，启动其开发服务器，并使用实际浏览器工具测试所要求的多类别选择、发行商筛选、组合筛选、无障碍控件，以及约定的清除筛选或空结果行为。根据验收标准报告观察结果，包括失败或受阻的检查。不要声称观察到了未实际观察的行为。

   此步骤是浏览器观察，不是再次运行完整自动化测试。不要更改应用代码、测试、技能或智能体配置文件，不要提交、推送或创建 PR。将缺少 MCP 工具或先决条件报告为受阻，并在安装任何内容前先询问。不要复用其他检出目录的服务器，也不要停止无关进程。完成后仅停止自己启动的服务器。
   ```

检查 Playwright MCP 工具调用、被测 URL 和报告中的浏览器观察结果。仅根据源代码或此前 E2E 结果撰写的描述，不能证明使用了 MCP。

2. 对照议题和批准的澄清内容阅读摘要。如果发现缺陷，单独授权针对性修复，审查更改的差异，并重复相关自动化检查和浏览器观察。修复前的证据不能证明修复后版本的状态。
3. 确认智能体已停止自己启动的服务器。保持筛选会话打开，并在第 7 课创建 QA 配置文件前保持 **Interactive** 模式。

此阶段提供直接观察，不能替代自动化覆盖。失败或受阻的观察结果应保留，供 QA 使用。

## 总结与后续步骤

你使用 Playwright MCP 服务器，从 GitHub Copilot app 在真实浏览器中探索了功能。总结来说，你：

- 了解了模型上下文协议 (MCP)，以及应用如何提供 MCP 工具。
- 通过 **Customize** 配置了 Playwright MCP 服务器。
- 要求智能体操控浏览器并探索筛选功能。

接下来，通过专业配置文件将需求、浏览器观察、覆盖情况和技能结合起来。在同一会话中继续学习[第 7 课 - 创建并使用 QA 智能体][next-lesson]。暂时不要创建功能 PR。

## 资源

- [MCP 是什么？为什么每个人都在谈论它？][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [在 GitHub Copilot app 中配置 MCP 服务器][customize-app]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app