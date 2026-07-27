---
title: "练习 2 - 自定义说明（Copilot CLI）"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[← 上一课：安装 Copilot CLI][previous-lesson] · [下一课：使用 CLI 生成代码 →][next-lesson]

使用生成式 AI 时，上下文至关重要。如果某项任务需要按特定方式完成，或者存在 Copilot 应该知道的背景信息，就需要确保这些上下文可用。本工作坊会探索几种帮助 Copilot 的工具。这里先从[说明文件][instruction-files]开始，它们通常关注代码本身应如何组织。这能帮助 Copilot 不仅理解想要*什么*代码，也理解代码应当*如何*组织。

在本练习中，将：

- 了解项目专属上下文、编码准则和文档标准如何通过存储库自定义说明及按路径限定范围的说明文件传递给 Copilot；
- 在当前说明已生效的前提下，生成过滤功能的第一块数据切片（publisher helper）；
- 向 `.github/copilot-instructions.md` 添加一项新的全库标准；
- 运行后续提示，观察重新生成的代码如何采用这项新标准；
- 提交说明更新和 helper，为下一节练习做好准备。

> [!CAUTION]
> 生成的代码可能与设定的某些标准不完全一致。Copilot 是非确定性的。这里的目标是观察更新说明后行为变化的*趋势*，而不是逐字符匹配输出。

## 说明文件

### 场景

和优秀的开发团队一样，Tailspin Toys 也有一套开发实践准则和要求，包括：

- 数据层始终需要单元测试。
- UI 应使用深色模式，并具有现代感。
- 应以 TSDoc 文档注释的形式为代码添加文档。
- 每个文件顶部都应添加一段注释，说明该文件的作用。

通过使用说明文件，可以确保 Copilot 拥有正确的信息，从而按照这些实践要求完成任务。

### 自定义说明

自定义说明可用于向 Copilot 提供上下文和偏好，帮助它更好地理解编码风格和需求。这是一项非常强大的功能，能够引导 Copilot 给出更相关的建议和代码片段。可以指定偏好的编码约定、库，甚至希望包含的注释类型。既可以为整个存储库创建说明，也可以为特定文件类型创建说明，以提供任务级上下文。

说明文件分为两类：

- `.github/copilot-instructions.md`：这是一个针对整个存储库**每次**请求都会发送给 Copilot 的单一说明文件。这个文件应包含项目级信息——也就是大多数发送给 Copilot 的聊天或 CLI 请求都会用到的上下文。可以包括所用技术栈、构建内容概览、最佳实践以及其他全局指导。
- `.github/instructions/*.instructions.md`：可针对特定任务或文件类型创建。可以用来为特定语言（如 TypeScript 或 Astro）提供指导，也可以针对创建 UI 组件或新增一组单元测试等任务提供指导。

> [!NOTE]
> 在 IDE 中工作时，说明文件仅用于 Copilot Chat 的代码生成——不会用于代码补全或下一次编辑建议。
>
> Copilot Chat、Copilot CLI 和 Copilot cloud agent 在生成代码时都会使用存储库级说明文件以及 `*.instructions.md` 文件（带 `applyTo` front matter）。
>
> 此外，Copilot [还支持采用其他标准的说明文件][custom-instructions-support]，包括 `AGENTS.md` 和 `CLAUDE.md` 文件。

### 管理说明文件的最佳实践

关于如何创建说明文件的完整讨论超出了本工作坊范围。不过，示例项目中的例子展示了一种具有代表性的做法。从高层来看：

- 将 `copilot-instructions.md` 中的说明聚焦于项目级指导，例如构建内容说明、项目结构和全局编码标准。
- 使用 `*.instructions.md` 文件为特定文件类型（单元测试、Astro 组件、数据层）或特定任务提供具体说明。
- 使用自然语言。保持指导清晰。提供代码应该如何写以及不应该如何写的示例。

创建说明文件没有唯一正确的方法，就像使用 AI 也没有唯一正确的方法一样。通过不断实验，会逐渐找到最适合项目的方式。

> [!TIP]
> 每个使用 GitHub Copilot 的项目都应该具备一套完善的说明文件。查看本项目中的这些文件时，可能会注意到其中覆盖了许多任务类型，包括 [UI 更新][ui-instructions] 和 [Astro][astro-instructions]。
>
> Copilot 也可以帮助生成说明文件。不同界面对这一功能的暴露方式不同（例如 VS Code 中的 **Configure Chat → Generate Agent Instructions**，或 Copilot CLI 中的 `/init`）——所在路径的课程会在相关位置指出。
>
> 想找模板或起点？可以看看 [awesome-copilot][awesome-copilot]，这是一个汇集说明文件、自定义智能体和其他资源的存储库。

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support

## 探索本项目中的自定义说明文件

花一点时间阅读此存储库随附的说明文件——其中包含一个核心 `copilot-instructions.md`，以及一组面向不同任务的 `*.instructions.md` 文件。可以在编辑器中打开它们，也可以在 GitHub Web UI 中查看。

1. 打开 `.github/copilot-instructions.md`。
2. 浏览该文件，注意其中对项目的简要说明，以及 **Agent notes**、**Code standards**、**Scripts** 和 **Repository Structure** 等部分。在 **Code standards** 下，还要注意嵌套的 **GitHub Actions Workflows** 指导。这些内容适用于与 Copilot 的任何交互。
3. 打开 `.github/instructions` 文件夹并浏览。可以看到其中包含针对 Astro 文件、Drizzle 数据层、测试等内容的说明。
4. 打开 `.github/instructions/unit-tests.instructions.md`。注意顶部的 `applyTo` 字段——它设置了一个相对于存储库根目录的 glob，用于决定这些说明适用于哪些文件。在这里，任何 TypeScript 测试文件（例如匹配 `**/*.test.ts` 的文件）都会匹配。
5. 注意其中针对为本项目创建单元测试的专门说明。
6. 最后，打开 `.github/instructions/drizzle.instructions.md` 并滚动到底部。注意其中链接到了其他说明文件（如 `unit-tests.instructions.md`）以及项目中的现有文件。这样可以把较大的说明集拆分为更小、可复用的文件，并在生成代码时为 Copilot 指出可参考的示例。（其中路径是相对于说明文件本身，而不是存储库根目录。）

> [!NOTE]
> `copilot-instructions.md` 中的 **Code formatting requirements** 部分记录了项目的编码标准，但目前还没有要求在代码中编写文档。接下来的步骤会添加 TSDoc 文档注释和文件注释头规则。

## 创建分支

接下来会修改代码，因此先创建一个分支来工作。

1. 在 codespace 终端中，创建并切换到新分支：

   ```bash
   git checkout -b update-custom-instructions
   ```

2. 确认 Copilot CLI 已安装并完成验证：

   ```bash
   copilot --version
   ```

   如果找不到该命令，或者尚未登录，请返回[练习 1 - 安装 GitHub Copilot CLI](../1-install-copilot-cli/)。

## 在更新说明*之前*使用 Copilot CLI

为了看清自定义说明的影响，先在当前说明生效的情况下生成代码。稍后会更新该文件，并再次运行后续提示。

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

1. 确保 Copilot CLI 会话从**存储库根目录**启动，这样它才能自动读取 `.github/copilot-instructions.md`。
2. 在 Copilot CLI 提示符中，请它生成过滤 UI 将要使用的 publishers helper：

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

3. Copilot CLI 会探索项目、提出计划，并在这个 `--yolo` 会话中写入文件。观察终端输出中的变更，然后在编辑器中查看结果。
4. 在编辑器中打开生成的 `src/lib/publishers.ts`。
5. 注意，这个 helper 是一个带类型的函数，第一参数接收 `db` 客户端，并返回一个带类型的 publishers 数组——这来自 `.github/instructions/drizzle.instructions.md` 中的数据层约定（该文件适用于 `src/lib/*.ts`）。
6. 注意，生成的代码**缺少** TSDoc 文档注释和文件级注释头。

> [!CAUTION]
> Copilot 是概率性的——即使没有明确要求，它也有可能会添加文档注释。如果出现这种情况也没关系；更新说明后的*一致性*提升仍然是这里要观察的重点。

## 添加新的全库标准

如前所述，`.github/copilot-instructions.md` 旨在向 Copilot 提供项目级信息。现在为它补充存储库编码标准，以改善代码建议质量。

1. 重新打开 `.github/copilot-instructions.md`。
2. 找到 **Code formatting requirements** 部分，应该在第 27 行附近。注意它已经记录了项目的编码标准——但尚未加入代码内文档规则，这就是生成的 helper 没有文档注释的原因。
3. 在现有标准的正下方添加以下 markdown 行，指示 Copilot 添加文件注释头和 TSDoc 文档注释：

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. 保存 `copilot-instructions.md`。

> [!TIP]
> 正如上一课所示，说明文件既可以在存储库级别创建（`.github/copilot-instructions.md`）用于全局指导，也可以创建为 `*.instructions.md` 文件，用于特定语言、文件类型或任务。像刚刚添加的文档注释规则这类项目级标准，就应该放在存储库级文件中。

## 重新运行提示并观察变化

既然说明中已经加入文档注释规则，就请 Copilot CLI 更新刚刚生成的 publishers 文件。同一条标准指令会引导这次重写。

1. 在 Copilot CLI 会话中发送 `/clear`，以全新的对话开始。
2. 发送以下提示：

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. 等待编辑完成，然后重新打开 `src/lib/publishers.ts`。
4. 注意，文件现在会以类似下面的注释块开头：

   ```typescript
   /**
    * Tailspin Toys Crowd Funding platform 的 publisher 数据访问辅助函数。
    * 提供从数据库检索 publisher 信息的函数。
    */
   ```

5. 注意，生成的函数现在会包含类似下面的 TSDoc 注释：

   ```typescript
   /**
    * 返回所有 publisher 的列表，包含其 id 和 name。
    *
    * @param db - Drizzle 数据库客户端。
    * @returns 一个 Promise，解析为 publisher 对象数组。
    */
   ```

6. 保留这个更新后的文件。它是下一节练习将继续扩展的第一块数据切片。

## 提交并推送这第一块过滤功能

1. 在终端中确认已变更的文件：

   ```bash
   git status
   ```

2. 暂存说明更新和 helper：

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. 提交变更：

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. 推送分支：

   ```bash
   git push -u origin update-custom-instructions
   ```

## 总结和后续步骤

已经了解了 Copilot 如何从本项目中的说明文件获取上下文，然后使用 Copilot CLI 完成了以下事项：

- 在*现有*说明的基础上，生成了用于过滤功能的 publishers 数据访问 helper 基础；
- 向 `.github/copilot-instructions.md` 添加了一项新的全库标准；
- 运行后续提示，并观察重新生成的代码如何采用这项新标准；
- 提交并推送说明更新和 helper 基础。

下一步，将在[生成代码练习][next-lesson]中应用这些说明，实现积压工作中的功能。

## 资源

- [GitHub Copilot 自定义的说明文件][instruction-files]
- [创建自定义说明的最佳实践][instructions-best-practices]
- [为 Copilot 编写更好自定义说明的 5 个技巧][copilot-instructions-five-tips]
- [Awesome Copilot——说明文件及其他资源集合][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
