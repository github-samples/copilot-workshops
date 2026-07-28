---
title: "연습 7 - GitHub Copilot CLI의 슬래시 명령"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

좋은 CLI 도구라면 그렇듯 GitHub Copilot CLI에도 다양한 slash commands가 포함되어 있습니다. 이 명령은 고급 기능, "내부 동작" 정보, 추가 구성 옵션을 제공합니다. 이미 `/clear`로 컨텍스트를 지우고 `/mcp`로 MCP server를 검사하는 방법을 살펴보았습니다. 이제 `/context`, `/model`, `/share`, `/delegate`를 포함한 몇 가지 강력한 명령을 더 살펴보겠습니다.

## 시나리오

이제 핵심 CLI 흐름은 모두 살펴보았습니다. 이번에는 세션 공유, 모델 전환, [Copilot cloud agent][about-cloud-agent]에 작업 위임 같은 추가 기능을 알아보겠습니다.

이 연습에서는 다음을 사용합니다.

- `/share`로 세션을 팀과 공유할 수 있도록 GitHub gist를 만듭니다.
- `/context`로 Copilot CLI가 현재 사용 중인 컨텍스트를 확인합니다.
- `/model`로 사용 가능한 모델 목록을 확인하고 원한다면 다른 모델을 선택합니다.
- `/delegate`로 선택적으로 작업을 cloud agent에 넘깁니다. 이 기능을 사용하려면 cloud agent가 필요하며, Copilot Student, Pro, Pro+, Business, Enterprise에서 사용할 수 있습니다. 즉 Copilot Free를 제외한 모든 플랜에서 사용할 수 있습니다.

## 세션 공유하기

AI 도구를 포함해 어떤 도구든 잘 활용하는 것은 하나의 기술입니다. 팀으로 함께 작업하면서 서로의 학습 내용을 공유하는 것은 모두의 경험을 개선하고 더 높은 품질의 코드를 생성하는 가장 좋은 방법입니다. 이를 지원하기 위해 Copilot CLI는 `/share` 명령을 제공합니다. `/share` 명령은 세션에서 사용한 프롬프트와 Copilot이 따랐던 로직을 포함해 세션 세부 정보를 담은 markdown 파일이나 GitHub gist를 생성할 수 있습니다.

이제 팀과 공유할 수 있는 GitHub gist를 만들어 보겠습니다.

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
1. Copilot CLI 프롬프트 창에서 다음 명령을 보냅니다.

    ```
    /share gist
    ```

2. 잠시 후 Copilot이 gist를 만들고 링크를 표시합니다.
3. 링크 텍스트를 복사합니다.
4. 새 브라우저 탭에 링크를 붙여 넣어 gist를 살펴봅니다. gist에 전송된 프롬프트, 사용한 스킬과 agent, Copilot의 사고 과정, 로컬에서 실행한 명령의 코드와 결과까지 강조되어 있는 점을 확인합니다.

`/share`가 생성하는 gist와 markdown 파일은 코드가 어떻게 생성되었는지 문서화하거나, 원하는 결과를 얻기 위해 Copilot으로 어떤 작업을 수행했는지 팀과 공유하는 용도로 사용할 수 있습니다.

## Copilot CLI의 컨텍스트 살펴보기

더 크거나 복잡한 작업을 수행할 때는 모델의 최대 context window에 도달할 수 있습니다. 창의 정확한 크기는 사용 중인 모델과 Copilot CLI 버전에 따라 달라집니다. Context window가 가득 차면 Copilot CLI는 이를 자동으로 compact하여 정보를 요약하고 현재 작업과 관련이 없다고 판단한 항목을 제거합니다. Slash commands를 사용하면 현재 컨텍스트 상태를 확인할 수도 있고 수동으로 compact할 수도 있습니다. 이제 context window를 살펴보겠습니다.

1. Copilot CLI 프롬프트 창에서 다음 명령을 보냅니다.

    ```
    /context
    ```

2. 잠시 후 Copilot CLI가 현재 컨텍스트를 시각적으로 표현한 결과를 생성합니다.

    ![Copilot CLI의 context window 화면](../../_images/cli-7-context-window.png)

3. 표시된 모델(이미지와 다를 수 있음)과 현재 사용된 token 비율을 확인합니다. 나머지 정보는 다음을 보여 줍니다.

    | 제목 | 설명 |
    | ------------ | ------------------------------------------------------ |
    | System/Tools | 지침 파일, 파일 내용, 도구 정의 |
    | Messages | 사용자와 Copilot 간의 대화 기록 |
    | Buffer | 응답 생성을 위해 Copilot CLI가 예약한 공간 |
    | Free space | 남아 있는 여유 공간 |

4. 다음 slash command를 Copilot CLI에 보내 대화 기록을 compact합니다.

    ```
    /compact
    ```

5. 완료되면 다음 명령을 보내 현재 컨텍스트 통계를 다시 표시합니다.

    ```
    /context
    ```

6. 컨텍스트 변화에 주목합니다. 현재 context window가 상대적으로 작을 가능성이 높으므로 큰 차이가 없을 수도 있습니다.

> [!NOTE]
> Copilot CLI는 컨텍스트가 가득 차면 자동으로 compact를 수행합니다. 용량이 100%에 가까워지면 프롬프트 창 바로 위에 비율을 표시합니다. 일반적으로는 비동기적으로 compact를 수행하므로, 작업 중에도 계속 Copilot과 상호 작용할 수 있습니다. 다만 작업을 수행하는 동안 몇 초간 실행 중인 작업을 차단할 수도 있습니다.

### 컨텍스트 사용 모범 사례

대부분의 세션에서는 Copilot이 별도 지시 없이도 컨텍스트를 효율적으로 관리합니다. 하지만 다음과 같이 히스토리를 직접 지우거나 compact하도록 지시하고 싶어지는 상황도 있을 수 있습니다.

- 애플리케이션의 다른 부분이나 관련 없는 작업으로 전환하는 경우, 오래되고 관련 없는 컨텍스트가 Copilot을 혼란스럽게 하지 않도록 `/clear`를 사용해 새로 시작할 수 있습니다.
- 최대 context window에 가까워지고 있다면 `/compact`로 수동으로 컨텍스트를 정리해 시점을 직접 제어할 수 있습니다.

> [!CAUTION]
> 다시 말해 대부분의 시간에는 Copilot이 직접 컨텍스트를 관리합니다. 오래된 정보 때문에 Copilot이 약간 혼란스러워 보이거나 관련 없는 작업으로 전환하려는 경우에만 수동 명령 사용을 고려합니다.

## 모델 선택하기

모델마다 강점이 다르고, 개발자마다 선호도도 다릅니다. Copilot CLI는 사용 가능한 모델을 나열하고 원하는 모델을 선택할 수 있게 해줍니다.

1. Copilot CLI에 다음 slash command를 보내 모델 목록을 표시합니다.

    ```
    /model
    ```

2. 모델 목록을 확인합니다. 각 모델 옆에는 이름과 요청당 비용 modifier가 함께 표시됩니다.
3. 원한다면 새 모델을 선택합니다. 아니면 <kbd>Esc</kbd>를 선택해 모델 목록을 종료합니다.

> [!CAUTION]
> Copilot CLI의 모델 선택은 유지됩니다.

## Cloud agent에 위임하기(선택 사항)

터미널에서 계속 작업하고 싶지만 더 오래 걸리는 작업은 Copilot cloud agent에 넘기고 싶을 때가 있습니다. `/delegate` 명령은 현재 Copilot CLI 세션을 GitHub.com으로 보내고, cloud agent가 이를 받아 비동기적으로 작업한 뒤 완료되면 pull request를 엽니다.

> [!NOTE]
> `/delegate`에는 cloud agent가 필요합니다. Copilot Student, Pro, Pro+, Business, Enterprise에서 사용할 수 있으며, Copilot Free에서는 사용할 수 없습니다. 액세스 권한이 없다면 이 섹션을 읽고 실습 단계는 건너뜁니다.

1. 워크숍에서 누적된 컨텍스트가 함께 위임되지 않도록 먼저 현재 세션을 지웁니다.

    ```
    /clear
    ```

2. 범위가 작고 명확한 프롬프트를 보냅니다. 예를 들어 백로그에 있는 pagination stretch goal을 위임할 수 있습니다.

    ```
    Implement pagination on the game list page so it shows a fixed number of games per page with Previous and Next controls, and add tests.
    ```

3. 다음 slash command를 보내 세션을 cloud agent에 넘기고, 위임할 프롬프트를 확인합니다.

    ```
    /delegate
    ```

4. 브라우저에서 [Copilot agents](https://github.com/copilot/agents)를 열어 진행 상황을 모니터링합니다.
5. 이 harness에서는 pull request가 완료될 때까지 기다릴 필요는 없습니다. 나중에 다시 돌아와도 됩니다. 비동기 agent 작업 관리 방법을 더 깊이 알아보고 싶다면 [Cloud agent harness](../../cloud/)를 계속 진행합니다.

## 요약 및 다음 단계

Copilot CLI의 slash commands를 사용하면 구성을 변경하고, 세션을 공유하고, Copilot이 내부적으로 어떻게 동작하는지에 대한 정보를 얻을 수 있습니다. 이 연습에서는 다음을 사용하거나 살펴보았습니다.

- `/share`로 세션을 팀과 공유할 GitHub gist를 만들었습니다.
- `/context`로 Copilot CLI가 현재 사용 중인 컨텍스트를 확인했습니다.
- `/model`로 사용 가능한 모델 목록을 살펴보고 원한다면 새 모델을 선택할 수 있음을 확인했습니다.
- `/delegate`를 cloud agent로 연결하는 선택적 브리지로 학습했습니다.

물론 더 많은 slash commands가 있으며, Copilot CLI로 탐색할 내용도 더 많습니다. 마지막으로 [학습한 내용을 검토하고][next-lesson] 학습을 계속하기 위한 다음 단계를 살펴보며 여정을 마무리하겠습니다.

## 리소스

- [Copilot CLI 사용하기][using-copilot-cli]
- [Copilot CLI 소개][about-copilot-cli]
- [Copilot CLI의 컨텍스트 관리][context-management]
- [Copilot CLI로 세션 공유하기][share-sessions]
- [Copilot CLI에서 모델 선택하기][selecting-models]

[previous-lesson]: ../6-custom-agents/
[next-lesson]: ../8-review/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
[share-sessions]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#share-sessions
[selecting-models]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#select-an-llm
