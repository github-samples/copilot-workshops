---
title: "练习 3 - 使用自定义指令引导 Copilot"
description: "添加范围明确的文档约定，在现有代码上展示其效果，并合并第二个拉取请求。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

上下文帮助 Copilot 不仅理解要构建*什么*，也理解团队期望*如何*编写代码。你将添加范围明确的文档约定，观察其对真实代码的影响，并将指令和示例改动通过 PR 2 一并合并。

在本练习中，将：

- 探索存储库范围和路径范围的指令。
- 添加文档标准，不提前实现筛选功能。
- 在一个现有的小型辅助函数或组件上展示标准的效果。
- 验证并合并指令里程碑。

## 探索指令

存储库已包含两类有用的指令：

- `.github/copilot-instructions.md` 提供存储库范围的上下文，例如技术栈、结构和通用实践。
- `.github/instructions/*.instructions.md` 提供限定范围的指导。frontmatter 中的 `applyTo` glob 指明这些指令适用的文件。

在编辑器中打开这些文件：

1. 阅读 `.github/copilot-instructions.md`，找到当前编码和验证标准。
2. 探索 `.github/instructions/`，包括 Astro、数据层和测试指导。
3. 在 `unit-tests.instructions.md` 中检查 `applyTo` 模式和测试约定。
4. 在 `drizzle.instructions.md` 中检查数据访问模式及示例引用。

保持存储库范围指令简洁，将文件特定的细节放入相关范围指令文件，并避免同一规则的多个副本相互矛盾。[GitHub 指令支持参考][instruction-support]说明了各操作环境支持的指令格式。

> [!NOTE]
> 指令会影响生成结果，但不保证始终遵循。审查时既要检查指令文本，也要检查其对代码的影响。如果 Copilot 已生成良好注释，本课的目的就是让约定明确且可重复，而不是强行制造前后对比中的失败。

## 从已合并的 PR 1 开始

确认星级评分 PR 已合并。在练习存储库终端中，从更新后的 `main` 开始下一个里程碑：

```bash
git status
git switch main
git pull --ff-only
git switch -c update-custom-instructions
copilot --enable-all-github-mcp-tools
```

如果工作树不干净或拉取失败，应先解决再继续。保持 **Interactive** 模式。

在存储库的 **Issues** 选项卡中，找到 **Update our repository coding standards**，复制其实际 URL。该议题提供更广泛的上下文：说明意图、记录导出的数据层函数和组件契约，并持续更新注释。本练习只处理其中范围明确的文档工作，不进行全库重构，也不承诺完成每项议题标准。

## 添加文档约定

将占位符替换为实际议题 URL，然后发送：

```plaintext
阅读此编码标准议题以了解上下文：<coding-standards-issue-URL>。检查现有存储库指令和范围指令。添加范围明确的文档约定：说明意图，而不是复述代码；使用 TSDoc/JSDoc 记录 db/ 和 src/lib/ 中导出函数的用途、参数和返回值；记录可复用 Astro 组件的 Props 契约；并在相关代码变化时同步更新注释。

将每条规则放入适当的现有指令文件，避免重复或矛盾。保留现有格式和 lint 标准；在适当位置从 README 链接到或概述该文档约定。将此次更改限定为文档标准，不要迁移格式工具或重写整个存储库。不要创建技能或智能体、实现筛选功能、提交、推送或打开 PR。停止，让我在进行示例改动前检查指令。
```

检查差异。约定应鼓励有用的注释，而不是要求每个文件都有样板标头，或添加只重复显而易见代码的注释。继续前先请求修正。

## 在真实代码上展示约定

检查存储库后，选择一个现有的小型导出辅助函数或可复用组件。它不必是发行商辅助函数，也不要求 `src/lib/publishers.ts` 已存在。

发送：

```plaintext
根据更新后的指令，选择一个文档可以更清晰的现有小型导出辅助函数或可复用 Astro 组件。直接在该文件中应用约定，不改变运行时行为，也不添加筛选功能。说明哪条指令指导了改动，并在提交或打开 PR 前停止。
```

打开实际更改的文件。对于辅助函数，检查注释是否准确描述参数、返回值和注入的数据库参数；对于组件，检查是否记录了 `Props` 契约。确认说明与代码一致，而不只是寻找注释块。

> [!TIP]
> 聊天中的示意代码片段不算示例改动，应检查真实的存储库更改。如果所选代码已满足约定，应选择另一个确有改进必要的小型现有目标，而不是添加冗余注释。

## 验证并合并 PR 2

让 Copilot 验证已审查的更改：

```plaintext
审查指令更改和小型文档示例改动。确认运行时行为未改变。检查 package.json，运行 npm run lint 和 npm run typecheck:all，并在代码改动确有需要时运行受影响的现有测试。报告确切命令和结果。暂时不要安装任何内容、创建技能、提交、推送或打开 PR。
```

解决失败项，检查最终差异，然后授权此里程碑：

```plaintext
仅提交已审查的文档指令、直接相关的 README 更新和小型代码示例。推送当前分支，并按照存储库的 PR 模板创建以 main 为目标的 PR。包含验证结果，并将编码标准议题作为部分贡献进行引用；除非确已满足每项议题标准，否则不要使用关闭议题的关键字。不要合并或开始筛选功能。
```

打开 PR URL，检查 **Files changed** 并审查 CI。全部必需检查和审查通过后，在 GitHub 上合并，并确认 PR 2 为 **Merged**。使用 `/exit` 退出 CLI 会话。此 PR 合并前，不要开始下一个里程碑。

## 总结与后续步骤

文档约定和真实示例改动现已进入 `main`。接下来，在基于该合并状态的新分支中，[使用 Plan 和 Autopilot 构建筛选功能][next-lesson]。

## 资源

- [添加存储库自定义指令][repository-instructions]说明存储库范围和路径范围的指导。
- [Awesome Copilot][awesome-copilot] 提供可审查并调整的示例，不应盲目采用。

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[repository-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[awesome-copilot]: https://github.com/github/awesome-copilot
