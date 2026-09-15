---
title: "第 3 课 - 使用自定义指令引导 Copilot"
description: "添加文档标准，在一个现有的小型辅助函数或组件上展示其效果，并通过第二个拉取请求一并合并。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

使用生成式 AI 时，上下文至关重要。如果任务需要以特定方式完成，或 Copilot 应了解一些背景信息，就应提供这些上下文。[指令文件][instruction-files]是实现此目的最强大的工具之一，它不仅说明需要什么代码，还说明代码应如何组织。本课将向存储库添加文档标准，并采用后续大多数工作的方式：从待办议题开始，让智能体完成更改。

本课将介绍如何：

- 探索存储库指令和路径范围指令文件如何传递给智能体。
- 从待办事项中的指令议题启动会话。
- 要求智能体向适当的存储库指令文件添加范围明确的文档标准。
- 通过一个小型的真实代码改动展示标准的效果，完成验证，并合并 PR 2。

## 场景

与所有优秀的开发团队一样，Tailspin Toys 针对开发实践制定了一组准则和要求，其中包括：

- 注释应说明意图和不明显的决策，而不是复述代码。
- `db/` 和 `src/lib/` 中导出的函数应使用 TSDoc/JSDoc 记录用途、参数和返回值；如果存在可注入的 `db` 参数，也应记录。
- 可复用的 Astro 组件应记录其 `Props` 契约，并在相关代码变化时同步更新注释。
- 应保留现有格式和 lint 指导。

通过指令文件，可以确保 Copilot 获得正确的信息，按照这些实践完成任务。

## 指令文件

自定义指令可向 Copilot 提供上下文和偏好，使其更好地理解编码风格与要求。这项强大功能可引导 Copilot 提供更相关的建议和代码片段。你可以指定首选编码约定、库，甚至希望代码中包含的注释类型。可以为整个存储库创建指令，也可以针对特定文件类型提供任务级上下文。

项目使用两类指令文件：

- `.github/copilot-instructions.md`：每次针对存储库的请求都会发送给 Copilot 的单个指令文件。此文件应包含项目级信息，即与大多数发送给 Copilot 的聊天或 CLI 请求相关的上下文，例如所用技术栈、正在构建的内容概述、最佳实践和其他全局指导。
- `.github/instructions/*.instructions.md`：可针对特定任务或文件类型创建。可以用它们为特定语言（如 TypeScript 或 Astro）提供准则，也可以为创建 UI 组件或一组新单元测试等任务提供指导。

> [!NOTE]
> 其他指令格式及支持情况因操作环境而异。依赖某种格式前，请查阅[自定义指令支持参考][custom-instructions-support]。

### 管理指令文件的最佳实践

深入讨论如何创建指令文件超出了本研讨会的范围。不过，示例项目提供了具有代表性的方法。总体而言：

- `copilot-instructions.md` 中的指令应专注于项目级指导，例如所构建内容的说明、项目结构和全局编码标准。
- 使用 `*.instructions.md` 文件为文件类型（单元测试、Astro 组件、数据层）或特定任务提供具体指令。
- 使用自然语言。保持指导清晰，并提供代码应采用和不应采用的示例。

创建指令文件没有唯一方法，使用 AI 同样如此。通过不断试验，可以找到最适合项目的方式。

> [!TIP]
> 每个使用 GitHub Copilot 的项目都应拥有一套完善的指令文件。探索本项目中的文件时，可以看到针对多种代码文件类型的指令文件。
>
> 要查找模板或起点，请探索 [awesome-copilot][awesome-copilot]，其中包含大量指令文件、自定义智能体和其他资源。

## 探索此项目中的自定义指令文件

花一点时间阅读此存储库附带的指令文件：一个核心 `copilot-instructions.md`，以及一组用于不同任务的 `*.instructions.md` 文件。在编辑器或 GitHub Web UI 中打开这些文件。

1. 如果审查面板尚不可见，请选择右上角的 **Toggle review panel** 将其打开。

   ![GitHub Copilot app 顶部工具栏，箭头指向 Create PR 右侧的 Toggle review panel 按钮](../../_images/app-2-review-panel.png)

2. 选择 **+**，向审查面板添加新项目。
3. 选择 **File**。
4. 搜索 `copilot-instructions.md`。
5. 从文件列表中选择 `copilot-instructions.md` 将其打开。
6. 探索该文件，注意项目的简要说明，以及 **Agent notes**、**Code standards**、**Scripts** 和 **Repository Structure** 等部分。在 **Code standards** 下，注意嵌套的 **GitHub Actions Workflows** 指导。这些内容适用于与 Copilot 的所有交互。
7. 选择 **Show folder view** 打开文件夹导航器。

   ![GitHub Copilot app 审查面板中打开了一个文件，并显示 Show folder view 按钮](../../_images/app-show-folder-view.png)

8. 转到 `.github/instructions` 文件夹并探索其中的文件。注意，其中包含针对 Astro 文件、Drizzle 数据层和测试等内容的指令。
9. 打开 `.github/instructions/unit-tests.instructions.md`。注意顶部的 `applyTo` 字段，它设置了一个相对于存储库根目录的 glob，用于确定指令适用的文件。此处会匹配任何 TypeScript 测试文件，例如匹配 `**/*.test.ts` 的文件。
10. 注意此项目中有关创建单元测试的具体指令。
11. 最后，打开 `.github/instructions/drizzle.instructions.md` 并滚动到底部。注意其中指向其他指令文件（如 `unit-tests.instructions.md`）和项目现有文件的链接。这样可以将较大的指令集拆分为较小的可复用文件，并让 Copilot 在生成代码时参考示例。（其中的路径相对于指令文件，而非存储库根目录。）

> [!NOTE]
> 添加规则前，将现有指导与实际编码标准议题进行比较。本课关注说明意图的注释、导出的数据层函数文档和 Astro `Props` 契约，而不是统一要求文件标头或复述代码的注释。

## 从指令议题开始

创建此会话前，确认 PR 1 已合并。为 PR 2 创建新工作树，不要继续使用星级评分分支。大多数工作都从议题开始，因此使用编码标准议题提供需求。

> [!NOTE]
> 指令文件对 Copilot 生成的代码影响很大，因此应确保它们能清晰地引导 Copilot。让 Copilot 创建第一版（正如本课将要做的），再由你审查更新是否满足要求，是一种有效方法。

1. 在侧边栏中选择 **My work**。
2. 选择标题为 **Update our repository coding standards** 的议题，将其打开。
3. 选择右上角的 **New session**，选择 **new working tree**，再选择 **Interactive** 模式。

   ![GitHub Copilot app 的议题视图，箭头指向右上角的 New session 按钮](../../_images/app-new-session-from-issue.png)

4. 使用以下提示词。即使应用的本地检出内容已过时，编辑前更新新会话分支，也能确保实际起点是最新合并后的 `main`：

   ```plaintext
   编辑前，确定当前检出目录和分支，确认这是一个干净的新工作树，获取 origin，并将当前会话分支快进到 origin/main。确认 HEAD 与 origin/main 一致，并包含已合并的星级评分 PR。如果工作树不干净、已发生分叉或缺少该合并，停止；不要重置、丢弃工作或创建其他分支。

   阅读议题 "Update our repository coding standards" 和现有存储库指令。添加范围明确的文档约定：说明意图而不是机械过程；使用 TSDoc/JSDoc 记录 db/ 和 src/lib/ 中导出函数的用途、参数、返回值，以及存在时可注入的 db 参数；记录可复用 Astro 组件的 Props 契约；并在相关代码变化时同步更新注释。

   将每条规则放入适当的现有指令文件，避免重复或矛盾，并在 README 中链接到或概述更新后的标准。保留现有格式和 lint 指导。不要统一要求文件标头、迁移格式工具、重写整个应用的文档或实现筛选功能。向我展示指令差异，然后停止，供我审查。不要创建技能或智能体、提交、推送或创建 PR。
   ```

Copilot 会进行更新。

## 审查更改

阅读更新后的指导，再通过真实文件展示其效果。仅提供建议代码片段，无法证明存储库指令影响了代码改动。

1. 选择右上角的 **Changes**，打开代码更改。

   ![GitHub Copilot app 会话面板选项卡，箭头指向 Changes 选项卡](../../_images/app-select-changes.png)

2. 审查更新后的指令文件和 README 引用。确认规则符合议题的注释理念、导出函数文档要求和组件契约，不要自行添加统一的文件标头要求。

> [!NOTE]
> AI 具有概率性而非确定性，因此实际文本会有所不同。

3. 审查指令后，在同一会话中请求一个范围明确的示例改动：

   ```plaintext
   在 db/ 或 src/lib/ 中一个现有的小型导出 TypeScript 辅助函数，或一个可复用 Astro 组件上展示更新后的文档约定。检查存储库，选择合适的现有文件；不要假设已有 publishers 辅助函数。进行一项不改变行为的小型可读性改进，并应用相关函数文档或 Props 契约指导。解释不明显的意图，不添加仅复述代码的注释。

   将更改限制在该示例及直接相关的测试内。不要实现筛选功能或创建新功能。运行相关的现有 npm 检查，报告更改内容及指令如何影响代码，然后停止，供我审查。在安装任何内容前先询问。不要提交、推送或创建 PR。
   ```

4. 审查实际文件差异，而不只是聊天回复。检查文档是否说明了真实行为，以及可读性改动是否保留了原有行为。审查相关测试、lint 和类型检查结果，解决失败项后再继续。

现在，你已更新项目中的指令文件，并了解了更新带来的影响。

## 打开并合并拉取请求

指令文件会成为存储库中的资产，与团队其他成员共享。接下来像处理任何其他资产一样，为此次工作创建 PR。

先一并授权已审查的指令和示例改动：

```plaintext
审查编码标准指令、README 引用和范围明确的代码示例的完整差异，包括相关测试。汇总验证结果，并在当前会话分支上提交这些已审查的更改。推送分支，使用存储库的 PR 模板创建一个以 main 为目标的拉取请求，并关联编码标准议题。除非满足议题的每项验收标准，否则将其描述为部分贡献；不要为未完成的工作使用关闭议题的关键字。不要合并。
```

1. 打开会话中的 PR 链接。如果应用显示 **Create PR** 确认提示，选择它，不要创建重复的 PR。
2. 如果系统提示，请选择 **Sign in with your browser**，并按照提示完成身份验证。
3. Copilot 开始创建 PR。

在 **My work** 中检查完整的 PR 差异，包括指令和代码更改。审查练习存储库的 CI 结果及必需的审查。在选择 **Ready to merge** 前解决失败项；CI 不能替代示例改动或你的审查。

4. 选择 **Ready to merge**。
5. 在新对话框窗口中选择 **Merge pull request**，合并拉取请求。

> [!NOTE]
> 开始筛选功能前，确认 PR 2 已合并到 `main`。仅创建新工作树并不能保证代码是最新的：第 4 课会先获取更新，将新会话分支快进到 `origin/main`，并在规划前确认前两个合并都已包含在内。

## 总结与后续步骤

你探索了应用如何从指令文件获取上下文，然后使用会话添加并合并存储库范围的标准。具体而言，你：

- 探索了存储库中的 `copilot-instructions.md` 和路径范围 `*.instructions.md` 文件。
- 从待办事项中的指令议题启动了会话。
- 要求智能体向适当的指令文件添加范围明确的文档规则，并从 README 引用这些规则。
- 检查了标准对真实代码改动的影响，验证了结果，并通过 PR 2 一并合并。

接下来，你将在新会话中构建筛选功能，并检查它是否遵循刚合并的标准。继续学习[第 4 课 - 使用 Plan 和 Autopilot 构建筛选功能][next-lesson]。

## 资源

- [用于自定义 GitHub Copilot 的指令文件][instruction-files]
- [自定义 GitHub Copilot app][customize-app]
- [创建自定义指令的最佳实践][instructions-best-practices]
- [Awesome Copilot：指令文件和其他资源集合][awesome-copilot]

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests