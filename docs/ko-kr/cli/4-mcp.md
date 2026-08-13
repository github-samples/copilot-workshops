---
title: "연습 4 - Playwright MCP server로 기능 테스트하기"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

방금 Copilot CLI로 필터링 기능을 생성했습니다. Pull request를 열기 전에 브라우저에서 실제로 동작하는지 확인해야 합니다. 직접 앱을 눌러 보며 확인하는 대신 **Playwright MCP server**를 연결해 Copilot이 실제 브라우저를 제어하면서 기능을 테스트하도록 해보겠습니다.

이 연습에서는 다음을 수행합니다.

- Model Context Protocol(MCP)이 무엇인지 이해하고, MCP server가 Copilot CLI를 어떻게 확장하는지 살펴봅니다.
- Playwright MCP server를 Copilot CLI에 추가합니다.
- 브라우저에서 필터링 기능을 수동 테스트하도록 Copilot에 요청합니다.

## Model Context Protocol(MCP)이란 무엇인가요?

[Model Context Protocol(MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/)은 AI agent가 외부 도구 및 서비스와 통신할 수 있는 방법을 제공합니다. MCP를 사용하면 AI agent는 외부 도구와 서비스를 실시간으로 사용할 수 있습니다. 이를 통해 최신 정보에 접근하고(resources 사용), 작업을 대신 수행하도록(tools 사용) 할 수 있습니다.

이러한 도구와 리소스는 MCP server를 통해 접근합니다. MCP server는 AI agent와 외부 도구 및 서비스 사이의 브리지 역할을 합니다. MCP server는 AI agent와 외부 도구(기존 API 또는 NPM package 같은 로컬 도구 등) 간의 통신을 관리합니다. 각 MCP server는 AI agent가 접근할 수 있는 서로 다른 도구와 리소스 집합을 나타냅니다.

널리 사용되는 MCP server 예시는 다음과 같습니다.

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: GitHub 리포지토리를 관리하기 위한 API 집합에 접근할 수 있게 해줍니다. 새 리포지토리 생성, 기존 리포지토리 업데이트, issue 및 pull request 관리 같은 작업을 AI agent가 수행할 수 있습니다.
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**: Playwright를 사용한 브라우저 자동화 기능을 제공합니다. 웹 페이지 탐색, 양식 입력, 버튼 선택 같은 작업을 AI agent가 수행할 수 있습니다.

서로 다른 도구와 리소스에 접근할 수 있게 해주는 다른 MCP server도 많이 있습니다. GitHub는 검색성과 생태계 기여를 높이기 위해 [MCP registry](https://github.com/mcp)를 제공합니다.

> [!CAUTION]
> 보안 측면에서 MCP server는 프로젝트의 다른 dependency와 동일하게 취급해야 합니다. MCP server를 사용하기 전에 소스 코드를 신중히 검토하고, 게시자를 확인하며, 보안 영향을 고려합니다. 신뢰할 수 있는 MCP server만 사용하고, 민감한 리소스나 작업에 대한 액세스를 부여할 때는 특히 주의합니다.

> [!NOTE]
> [GitHub MCP server][github-mcp-server]는 Copilot CLI에 **기본 내장**되어 있습니다. 별도 설정 없이 바로 사용할 수 있으며, 워크숍 전반에서 Copilot이 리포지토리를 읽고 쓰고 있었던 것도 이 서버 덕분입니다. 이 연습에서는 Copilot에 브라우저를 제공하기 위해 두 번째 서버인 Playwright를 추가합니다.

## Playwright MCP server 추가하기

서버를 추가하는 가장 빠른 방법은 대화형 `/mcp add` 명령입니다. Copilot이 제어할 수 있는 브라우저를 제공하는 [Playwright MCP server][playwright-mcp-server]를 등록합니다.

> [!TIP]
> **Copilot CLI 세션 시작하기**
>
> 아래 연습을 시작하기 전에 코드스페이스로 돌아가 터미널을 엽니다(이미 열려 있지 않다면 <kbd>Ctrl</kbd>+<kbd>`</kbd>). 그런 다음 `--yolo`와 `--enable-all-github-mcp-tools`를 사용해 Copilot CLI를 시작합니다.
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 이 프로젝트의 가장 최근 세션을 새로 시작하지 않고 이어서 사용하려면 `copilot --yolo --enable-all-github-mcp-tools --continue`를 실행합니다. 이전 연습에서 Copilot CLI가 이미 실행 중이라면 `/clear`를 보내 새 대화를 시작합니다.
>
> `--enable-all-github-mcp-tools`는 현재 세션에서 읽기/쓰기 GitHub MCP 도구를 활성화하므로, 워크숍 흐름 중 Copilot이 백로그를 읽고 pull request를 열 수 있습니다.

> [!CAUTION]
> `--yolo`는 전체 자동 권한(`--allow-all-tools`, `--allow-all-paths`, `--allow-all-urls`)을 활성화합니다. Codespace나 VM 같은 격리된 환경에서만 사용하고, 일상적인 개발을 위한 기본 별칭으로는 절대 설정하지 않습니다. 자세한 내용은 [Allowing and denying tool use][allow-all-warning]를 참고합니다.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
1. Copilot CLI 세션에서 다음을 입력합니다.

    ```text
    /mcp add
    ```

2. 구성 양식이 나타나면 <kbd>Tab</kbd>으로 필드 사이를 이동하면서 다음과 같이 입력합니다.

    - **Server Name**: `playwright`
    - **Server Type**: **Local**(또는 **STDIO**로 표시됨)을 선택합니다.
    - **Command**: `npx @playwright/mcp@latest --headless`
    - **Tools**: 서버의 모든 도구를 허용하기 위해 `*` 그대로 둡니다.

3. <kbd>Ctrl</kbd>+<kbd>S</kbd>를 눌러 저장합니다. 서버가 추가되고 즉시 사용할 수 있습니다. 재시작은 필요하지 않습니다.

`--headless` 플래그는 Playwright가 표시 창 없이 브라우저를 실행하도록 지정합니다. 데스크톱을 표시할 수 없는 코드스페이스 안에서는 이 설정이 필요합니다. 내부적으로는 다음 내용이 `~/.copilot/mcp-config.json` 파일에 기록됩니다.

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. MCP server 목록을 확인해 서버가 등록되어 활성 상태인지 검증합니다.

    ```text
    /mcp show
    ```

5. 기본 제공 `github` server와 함께 `playwright`가 표시되어야 합니다.

> [!NOTE]
> Tailspin Toys 프로젝트는 이미 end-to-end 테스트에 Playwright를 사용하므로, Playwright에 필요한 브라우저가 대체로 이미 설치되어 있습니다. 나중에 Copilot이 브라우저가 없다고 보고하면 `npx playwright install chromium`를 실행하도록 요청한 뒤 다시 시도합니다.

## 웹 사이트 시작하기

Playwright MCP server가 테스트를 수행하려면 실행 중인 앱이 필요합니다. Copilot CLI에서 작업하는 동안 계속 실행되도록 **별도의** 터미널에서 Astro dev server를 시작합니다.

1. <kbd>Ctrl</kbd>+<kbd>`</kbd>를 선택해 코드스페이스에서 새 터미널을 엽니다.
2. 웹 사이트를 시작합니다.

    ```bash
    npm run dev
    ```

3. 이 터미널은 계속 실행된 상태로 둡니다. `Astro server: http://localhost:4321` 배너가 표시되면 앱이 준비된 것입니다.

## 필터링 기능 테스트하기

Copilot CLI 세션으로 돌아가 Copilot에 기능 테스트를 요청합니다.

[Playwright MCP server][playwright-mcp-server]는 Copilot이 실제 브라우저를 제어할 수 있게 해줍니다. 직접 앱을 눌러 보며 작업을 확인하는 대신, agent가 페이지를 열고, 탐색하고, 필터를 적용하고, 결과를 다시 읽어 준 다음, 본 내용을 요약할 수 있습니다. 대화를 벗어나지 않고 기능이 기대대로 동작하는지 확인하는 가장 빠른 방법입니다.

내부적으로 Playwright MCP server는 스크린샷이 아니라 페이지의 [accessibility tree][playwright-mcp-server]를 기반으로 동작합니다. 즉, agent는 보조 기술이 처리하는 방식과 유사하게 구조화되고 레이블이 지정된 요소(버튼, 링크, 목록 항목)를 기준으로 추론합니다. 따라서 빠른 기능 점검이 가벼운 접근성 sanity check 역할도 함께 합니다.

서버가 연결되고 앱이 실행 중인 상태에서 Copilot에게 방금 만든 필터링 기능을 검증해 달라고 요청합니다.

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

Copilot은 Playwright MCP server를 통해 브라우저를 실행하고, 각 단계를 수행한 뒤, 확인한 내용을 보고합니다. 요약 내용을 issue의 acceptance criteria와 비교해 보고, 어긋나는 부분이 있으면 후속 질문을 하거나 pull request를 열기 전에 코드를 수정하도록 다시 요청합니다.

> [!NOTE]
> 이 테스트를 수행하려면 앱이 `http://localhost:4321`에서 실행 중이어야 합니다. Dev server를 중지했다면 프롬프트를 보내기 전에 다시 시작합니다. Copilot이 처음으로 Playwright MCP server를 사용할 때 브라우저를 다운로드해야 할 수도 있습니다. 브라우저가 없다고 보고하면 `npx playwright install chromium`를 실행하도록 요청한 뒤 다시 시도합니다.

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
## 요약 및 다음 단계

축하합니다. Copilot CLI에서 Playwright MCP server를 사용해 기능을 수동으로 테스트했습니다. 정리하면 다음을 수행했습니다.

- Model Context Protocol(MCP)이 무엇인지 학습하고, MCP server가 Copilot CLI를 어떻게 확장하는지 살펴보았습니다.
- `/mcp add`로 Playwright MCP server를 추가했습니다.
- 기능을 배포하기 전에 Copilot에게 브라우저를 제어해 필터링 기능을 검증하도록 요청했습니다.

이제 기능이 동작함을 확인했으니, 다음 연습으로 이동해 [에이전트 스킬의 도움을 받아 pull request를 열 수 있습니다][next-lesson].

## 리소스

- [MCP가 대체 무엇이고 왜 모두가 이야기할까요?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Copilot CLI용 MCP server 추가하기][cli-add-mcp]
- [GitHub MCP Server][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
