---
title: "练习 5 - 创建并使用 quality-checks 技能"
description: "让 Copilot 创建带有配套 shell 脚本的可复用质量检查技能，检查技能内容，并在筛选功能分支上执行。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

筛选功能已经实现，并已使用现有 npm 命令完成检查。现在，将这些检查封装为可复用的**智能体技能**。练习 4–8 始终使用同一个筛选功能会话和分支；本练习不创建 pull request。

在本练习中，将：

- 在创建自定义配置前返回 **Interactive** 模式。
- 让 Copilot 创建 `quality-checks`，然后停下来供你检查。
- 通过配套脚本执行全部四项检查，并证明单文件测试参数只会选中指定文件。
- 在筛选功能分支上为技能创建检查点。

## 指令、脚本和资源

技能将可复用的任务指令、可执行脚本和辅助资源打包，供智能体按需加载。自定义智能体定义专业角色、指令和可用工具。两者相辅相成：自定义智能体可以执行脚本，包括技能附带的脚本。

存储库技能位于 `.github/skills/<skill-name>/SKILL.md`，包含带有 `name` 和 `description` 的 frontmatter 以及 Markdown 指令。脚本和其他资源存放在旁边。这里将让 Copilot 生成 `.github/skills/quality-checks/SKILL.md` 及其配套脚本，而不是复制现成答案。[Agent Skills 规范][skill-spec]介绍了这种格式。

Copilot 根据已发现技能的描述，决定何时加载它。不要假定新技能会立即被已打开的会话发现；运行部分提供了明确读取技能的备用方式。格式可移植并不意味着无需满足 shell 或项目的前提条件。

## 创建技能

发送提示前返回 **Interactive** 模式。保持当前检出目录和分支。如果使用的旧版模板已经包含此技能，应先检查并扩展它，而不是覆盖已有的自定义内容。

```plaintext
创建 .github/skills/quality-checks/SKILL.md 和四个封装脚本，分别调用 npm run lint、npm run test:unit、npm run test:e2e 和 npm run typecheck:all。先阅读 package.json、README、测试配置和存储库指令。

识别当前环境。macOS/Linux/WSL 只创建 Bash .sh 脚本，原生 Windows 只创建 PowerShell .ps1 脚本；如果无法确定，先询问。不要同时创建两种实现。封装脚本仅负责根据自身位置解析存储库根目录，验证该目录包含本项目的 package.json，然后调用 npm。根目录无效时，应明确报错并失败退出。支持任意工作目录和包含空格的路径。保留输出和失败退出代码，包括 PowerShell 原生命令的失败。npm 的 -- 分隔符只插入一次；调用方直接提供工具参数，不再添加 --。不要管理端口或进程。

在 SKILL.md 中提供 name 和 description frontmatter、运行全部四个封装脚本的指令、前提条件、故障排查方法，以及包含一个现有单元测试文件的可移植调用示例。所有 Bash 示例都必须显式调用 bash；绝不绕过 PowerShell 执行策略。解释 Playwright 的服务器复用：只停止确实由自己启动的服务器，否则先询问。

只创建技能和必需的脚本。不要运行检查或探测，不要安装任何内容、修改应用代码、提交或创建 PR。然后停止，等待检查。
```

## 检查技能

1. 在编辑器中打开 `.github/skills/quality-checks/SKILL.md` 及其配套脚本，并检查差异。
2. 检查 `name` 和 `description` 是否说明了技能及其适用场景。阅读指令，不要只看元数据。
3. 确认执行顺序确实调用 `.github/skills/quality-checks/` 下的配套脚本，执行 lint、单元测试、E2E 和类型检查。
4. 检查每个封装脚本是否根据自身位置解析根目录，并明确检查推导出的目录是否包含此检出目录中预期的 `package.json`。命令因 npm 搜索祖先目录而成功，并不能证明根目录正确。检查路径是否加引号、参数是否转发、输出是否可见，以及失败时是否正确退出；PowerShell 必须传递原生 npm 命令的失败状态。
5. 检查文档中只运行一个单元测试文件的示例。封装脚本负责插入 npm 的 `--` 分隔符，因此调用方应直接传递目标工具的参数，不再添加分隔符。可复用指令中不应包含特定机器的检出目录绝对路径。在运行任何内容之前，让 Copilot 修正遗漏或问题。
6. 脚本应仅负责根目录和清单文件验证，以及运行现有 npm 检查。端口和进程相关决策应放在 SKILL.md 中，而不是通过 shell 进程管理代码实现。确认只有智能体实际启动的服务器才可以停止；工作目录或进程名称匹配不能证明归属。交付的文件应仅包含技能、必需的封装脚本和必要的共享辅助文件，不含临时探测或调试文件。

> [!NOTE]
> 当前 Tailspin Toys 需要 Node.js 22.13 或更高版本、项目依赖项，以及用于 E2E 检查的 Playwright Chromium。在检出目录的 README 和 `package.json` 中确认前提条件。缺少前提条件或 PowerShell 执行策略阻止运行时，需要经批准的解决方案，而不是自动安装、绕过策略或悄悄改为直接运行 npm。

## 运行技能

确认上一练习的开发服务器已停止。Playwright 会为 E2E 构建并提供预览服务，但其本地配置可以复用端口 `4321` 上的服务器。其他检出目录的服务器不能为当前功能提供有效证据。

如果 Copilot CLI 提供 `/quality-checks`，选择它来显式调用已发现的技能，并附上以下请求。如果未发现技能，直接在此会话中发送相同请求；本练习支持通过读取技能的方式运行它。

```plaintext
读取 .github/skills/quality-checks/SKILL.md，并按照其中的指令验证此检出目录中的筛选功能。先检查每个封装脚本的代码，确认其推导出的目录包含此检出目录中预期的 package.json，且根目录无效时会明确报错并失败退出，而不是依赖 npm 在祖先目录中查找包。不要为模拟失败而移动、重命名、删除或修改存储库文件。实际运行其配套脚本，执行 lint、单元测试、端到端测试和类型检查。同时运行文档中只运行一个单元测试文件的示例，直接传递目标工具的参数，因为 npm 的 -- 分隔符由封装脚本负责。根据测试运行器的结果，确认仅运行了指定文件，并报告该文件名及实际执行的测试文件数量。仅回显参数或返回退出代码 0，不能证明文件选择正确。

报告每次脚本调用及其结果，包括失败、跳过的检查或缺失的前提条件。不要在技能脚本无法使用时悄悄改为直接运行 npm 命令。确认待测试的检出目录和服务器，只停止你启动的服务器，并在安装任何内容或停止其他进程前询问。不要修改应用代码、切换分支、提交、推送或创建 pull request。
```

检查工具调用和输出。四个脚本都必须实际执行；描述检查内容或跳过检查都不算通过。对于单文件示例，将请求的文件名与运行器实际输出的文件结果及报告的数量进行比较：应只运行该文件。如果还运行了其他文件，回显参数或退出代码 0 都不足以证明正确。失败是有用的证据：修正技能，或在获批后解决环境配置阻碍，再重新运行受影响的检查。不要停止无关进程，也不要强行消除端口冲突。

## 保存检查点

检查技能及其运行结果后，授权创建本地检查点：

```plaintext
检查当前差异，仅为 quality-checks 技能文件创建检查点提交。保留现有筛选功能分支。不要推送或创建 pull request。
```

技能文件将与筛选功能、QA 配置和相关测试一起纳入练习 8 的功能 PR。继续在同一检出目录中完成[练习 6 - 使用 Playwright MCP 验证功能][next-lesson]。

## 更多技能示例

以下社区示例仅供参考，不是额外任务。采用前先检查其前提条件和行为：

- [贡献工作流：`make-repo-contribution`][contribution-example]。
- [需求文档：`prd`][prd-example]。
- [图表及配套导出脚本：`drawio`][drawio-example]。
- [浏览器测试：`webapp-testing`][browser-example]。

上游贡献示例名为 `make-repo-contribution`；旧版 Tailspin 模板使用另一个名称 `make-contribution`。本工作坊不依赖其中任何一个贡献技能。

[previous-lesson]: ../4-build-filtering/
[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
