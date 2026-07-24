---
title: "练习 0：先决条件"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

开始 Copilot CLI 练习前，需要先完成环境准备。将先创建 Tailspin Toys 存储库的个人副本，再启动一个 [codespace][codespaces]。下一节练习会使用其中集成的终端来安装并运行 Copilot CLI。

## 设置实验存储库

为了给即将编写的代码创建一份存储库副本，需要基于 [模板][template-repository] 创建一个实例。这个新实例会包含实验所需的全部文件，后续练习都会在其中完成。

1. 在新的浏览器窗口中，访问本实验的 GitHub 存储库：`https://github.com/github-samples/tailspin-toys`。
2. 在实验存储库页面上，选择 **Use this template** 按钮创建自己的存储库副本。然后选择 **Create a new repository**。

    ![“Use this template”按钮](../../_images/ex0-use-template.png)

3. 如果参加的是由 GitHub 或 Microsoft 主办的活动，请按照导师提供的说明操作。否则，可以在已启用 GitHub Copilot 访问权限的组织中创建这个新存储库。

    ![输入存储库模板设置](../../_images/ex0-repository-settings.png)

4. 记下创建的存储库路径（**organization-or-user-name/repository-name**），后续实验会用到它。

> [!NOTE]
> **积压工作已准备就绪**
>
> 通过模板创建存储库时，系统会自动创建一组 GitHub issue 作为积压工作。整个工作坊都会围绕这些 issue 展开，无需手动新建。

## 创建 codespace

接下来，将使用 codespace 完成实验练习。

[GitHub Codespaces][codespaces] 是一个基于云的开发环境，可以直接在浏览器中编写、运行和调试代码。它提供功能完整的 IDE，并支持多种编程语言、扩展和工具。

1. 打开刚创建的存储库。
2. 选择绿色的 **Code** 按钮。

    ![选择 Code 按钮](../../_images/ex0-code-button.png)

3. 选择 **Codespaces** 选项卡，再选择 **+** 按钮创建新的 Codespace。

    ![创建新的 codespace](../../_images/ex0-create-codespace.png)

codespace 的创建需要几分钟，但仍然比手动安装所有服务快得多。等待期间，可以先了解 GitHub Copilot 的其他功能，接下来就会用到。

> [!CAUTION]
> 后续练习还会回到这个 codespace。现在先将它保留在浏览器标签页中，不要关闭。

> [!NOTE]
> 本工作坊设计为在 codespace 或本地 [dev container][dev-containers] 中运行。这两种方式都能确保环境已安装顺畅体验所需的全部先决条件。如果更希望在本地运行，请在 VS Code 中打开克隆后的存储库，并在出现提示时选择 **Reopen in Container**——VS Code 会构建与 codespace 相同的 dev container。

[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers

## 总结

恭喜，已经创建了实验存储库的副本，也开始了 codespace 的创建流程。后续开始使用 Copilot CLI 时，会在其中完成操作。

## 下一步

接下来安装 Copilot CLI，并使用 GitHub 账户完成验证。继续前往[练习 1 - 安装 GitHub Copilot CLI][next-lesson]。

## 资源

- [GitHub Codespaces 概览][codespaces]
- [从模板创建存储库][template-repository]
- [Codespaces 快速入门][codespaces-quickstart]

[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
