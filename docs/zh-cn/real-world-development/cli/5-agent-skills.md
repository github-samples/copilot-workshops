---
title: "练习 5 - 使用智能体技能"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

应用开发经常包含一些可重复的任务，例如生成构建、运行测试或创建 pull request。**智能体技能 (Agent skills)** 让你可以为 Copilot——以及其他 AI 智能体——提供执行这些任务的指导。一个技能是一个文件夹，其中包含说明、脚本和资源，智能体可以按需加载。[Agent Skills 是一项开放标准][agent-skills-repo]，被多种智能体采用，因此同一个技能可以同时在 agent mode 的 Copilot Chat、Copilot cloud agent、Copilot CLI 和 GitHub Copilot app 中使用。

技能存放在项目的 `.github/skills` 文件夹中，也可以全局存放在 `~/.copilot/skills`。每个技能都是一个文件夹，其中包含一个 `SKILL.md` 文件。该文件具有 YAML frontmatter（至少包含 `name` 和 `description`），后面跟着 markdown 说明：

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

技能还可以包含脚本、资源和参考资料等子文件夹。完整结构请参见[智能体技能规范][agent-skills-spec]。

> [!TIP]
> 技能是动态加载的。智能体会根据 `description` 字段判断应使用哪个技能——清晰、针对场景的描述，是一个技能会被使用还是被忽略的关键区别。

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification

接下来看看，一个技能如何确保 pull request 符合团队制定的规范。

## 场景

团队对 pull request（PR）有一组要求：

- 提交消息要清晰，文件分组要合理。
- 创建 PR 之前，所有测试都必须通过。
- 每个 PR 都必须包含以下部分：
    - 说明为什么要进行这些更改。
    - 概述已更改的文件。
    - 重要代码块的片段。
    - 按组整理的更改详情。

由于团队正在使用 Copilot 生成代码和 PR，因此希望确保 AI 工具也能遵循这些要求。

在本练习中，将：

- 探索一个现有的用于创建 pull request 的技能。
- 了解 AI 智能体如何使用技能。
- 在技能的帮助下，创建一个符合准则的 PR。

## 执行技能

当智能体判断某个技能有必要时，会动态加载它。决定使用哪些技能的依据，就是 `SKILL.md` 文件中的描述。因此，使用场景清晰的描述非常重要。

## 探索 PR 技能

由于 Tailspin Toys 对创建 PR 有一套要求，因此他们创建了一个技能，帮助 AI 工具生成符合这些准则的 PR。现在来看看这个技能，了解它会执行什么。

1. 打开 `.github/skills/make-contribution/SKILL.md`。
2. 注意其中的名称和描述。可以看到，描述中强调了它适用的场景，也就是当请求创建 pull request 或提交代码时。
3. 通读这个技能。注意其中定义了分支应如何创建、提交应如何生成，以及 pull request 的内容应包含什么。

## 使用技能

如前所述，技能会由 Copilot CLI 自动调用。因此，只需请求 Copilot 创建一个 PR。

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

1. 使用以下提示，请 Copilot 创建一个 PR：

    ```
    Can you please create a pull request for me!
    ```

2. Copilot 会确认这个请求。稍等片刻后，会看到 Copilot 显示它正在使用 **make-contribution** 技能。

3. 然后 Copilot 会遵循该技能中的说明。它会先运行测试，然后创建分支、提交，最后创建 PR。
4. 创建 PR 后，返回存储库并打开该 PR。注意其中各个部分遵循了技能中设定的准则，与团队提出的要求一致。
5. 在进入下一节练习前，将本地工作区重置到从 `main` 创建的新分支，以便后续无障碍工作与这个过滤功能 PR 保持分离：

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## 总结和后续步骤

在智能体技能的帮助下，已经创建了一个符合文档要求的新 PR。完成了以下事项：

- 探索了一个现有的 pull request 创建技能。
- 了解了 AI 智能体如何使用技能。
- 在技能的帮助下，创建了一个符合准则的 PR。

技能非常适合处理任务，但如果需要更强大的操作能力，就应该利用[自定义智能体][next-lesson]，下一节就会探索这一点。

## 资源

- [关于 Agent Skills][about-agent-skills]
- [Agent Skills 规范][agent-skills-spec]
- [Agent Skills 存储库][agent-skills-repo]
- [awesome-copilot 上的 Agent Skills][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
