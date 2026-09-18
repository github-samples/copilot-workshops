---
title: "연습 3 - GitHub Copilot CLI로 프로젝트 기능 추가하기"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

예상할 수 있듯이 GitHub Copilot CLI로 수행하는 핵심 작업은 프로젝트에 기능, 동작, 코드를 추가하는 일입니다. 이제 백로그의 issue 중 하나를 가져와 Copilot이 구현을 도와주도록 해보겠습니다.

## 시나리오

이제 프로젝트의 필터링 작업을 마무리할 차례입니다. 백로그에는 이미 필터링 issue가 있고, 이전 연습에서 foundation helper도 만들었습니다. Copilot이 issue 세부 정보를 가져오고, 기존 작업을 고려한 뒤, 남은 기능을 구현하도록 해보겠습니다.

이 연습에서는 다음을 수행합니다.

- Plan mode를 사용해 필터링 기능 구현 계획을 생성합니다.
- Copilot으로 웹 사이트에 필터링을 추가하는 데 필요한 코드를 생성합니다.

이 연습이 끝나면 프로젝트에 새로운 기능이 추가됩니다.

## Plan mode 활용하기

AI의 가장 뛰어난 활용 방식 중 하나는 계획 수립입니다. 무엇을 만들고 싶은지 대략적인 개념은 있지만 아이디어를 정리할 대상이 필요할 때가 많습니다. AI 도구는 후속 질문을 하고, 빠진 구성 요소나 잠재적인 함정을 함께 검토하면서 생각을 구체화하도록 도와줍니다. Copilot CLI는 이 과정을 지원하기 위해 plan mode를 제공합니다. 또한 계획 수립에 들인 시간은 Copilot이 요구 사항에 더 잘 맞는 코드를 생성하는 데 도움이 됩니다.

Copilot CLI의 plan mode를 사용해 새 기능 생성 과정을 시작합니다.

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
1. Copilot CLI에 다음 프롬프트를 입력해 필터링 issue를 바탕으로 계획을 생성합니다.

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

2. Copilot이 계획을 세우는 동안 후속 질문을 할 수 있습니다. 질문이 나오면 원하는 구현 방식에 맞게 답변합니다.
3. 계획이 생성되면 설계 청사진을 검토합니다. 데이터 계층과 UI 전반의 남은 변경 사항, 그리고 테스트 생성이 권장되는 것을 확인할 수 있습니다.
4. Copilot CLI는 계획에 대한 추가 피드백을 제공할 수 있는 기능도 제공합니다. 안내된 영역으로 커서를 이동한 뒤 제안을 입력하면 Copilot이 이를 반영한 새 버전의 계획을 제시합니다.
5. 계획이 만족스럽다면 Copilot이 제공하는 옵션을 선택해 새 기능 구현을 시작합니다.

> [!NOTE]
> Copilot은 확률적으로 동작하므로, 정확한 텍스트와 제공되는 옵션은 달라질 수 있습니다. 하지만 구현을 시작하는 옵션이 표시되며 대체로 다음과 비슷한 문구를 보게 됩니다.
>
> `Yes, and switch to autopilot mode`.
>
> Copilot은 위 예시처럼 [autopilot mode](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)를 활성화하는 옵션을 제안할 수 있습니다. Autopilot mode를 사용하면 Copilot CLI가 각 단계마다 입력을 기다리지 않고 작업을 진행합니다. 처음 지시를 주면 Copilot CLI가 작업이 완료되었다고 판단할 때까지 각 단계를 자율적으로 처리합니다. 현재는 격리된 환경에서 작업하므로 autopilot을 실행하고 모든 도구를 허용해도 괜찮습니다.

6. Copilot이 파일 생성을 시작합니다.

> [!NOTE]
> 이 작업은 몇 분 정도 걸릴 수 있습니다. Copilot이 파일을 수정하고 생성하며, 테스트를 업데이트 및 생성하고, 모든 테스트를 실행해 성공 여부를 확인하는 모습을 보게 됩니다. 지금까지 살펴본 내용을 되돌아보거나 잠시 음료를 즐기기 좋은 시간입니다.

## 코드 검토하기

AI가 생성한 코드는 운영 환경에 병합하기 전에 반드시 검토해야 합니다. 이제 Copilot이 기능 구현 과정에서 생성하거나 수정한 파일을 살펴보겠습니다.

1. Copilot CLI에서 다음 명령을 사용해 "diff" 또는 코드 변경 사항을 표시합니다.

    ```
    /diff
    ```

2. 변경된 파일을 확인합니다. 화살표 키로 좌우 이동하면서 서로 다른 파일을 볼 수 있습니다. 새 필터 컨트롤과 클라이언트 측 필터링이 들어간 게임 목록 페이지, `src/lib/games.ts`, `games.test.ts` 같은 테스트 파일이 업데이트된 것을 확인할 수 있습니다. Copilot이 전체 구현에 맞춰 기존 helper를 조정했다면 `publishers.ts`가 수정된 경우도 있을 수 있습니다.

## 요약 및 다음 단계

이제 Copilot CLI의 도움으로 웹 사이트에 필터링 기능을 추가했습니다. 구체적으로 다음을 수행했습니다.

- Plan mode를 사용해 필터링 기능 구현 계획을 생성했습니다.
- Copilot을 사용해 웹 사이트에 필터링을 추가하는 데 필요한 코드를 생성했습니다.

물론 다음 단계는 실제로 동작하는지 확인하는 것입니다. Pull request를 열기 전에 [Playwright MCP server로 기능 테스트하기][next-lesson]로 이동해 검증해 보겠습니다.

## 리소스

- [Copilot CLI 사용하기][using-copilot-cli]
- [Copilot CLI 소개][about-copilot-cli]
- [Copilot CLI의 컨텍스트 관리][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
