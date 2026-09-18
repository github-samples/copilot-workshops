---
title: "연습 6 - GitHub Copilot CLI로 커스텀 에이전트 사용하기"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## 커스텀 에이전트란 무엇인가요?

GitHub Copilot의 [커스텀 에이전트][custom-agents-concept]를 사용하면 개발 워크플로 안의 특정 작업이나 도메인에 맞춘 전문 AI 도우미를 만들 수 있습니다. 리포지토리의 `.github/agents` 폴더 안에 있는 markdown 파일로 agent를 정의하면, 특정 종류의 작업을 더 효과적으로 수행하도록 Copilot을 이끄는 집중된 지침, 모범 사례, 코딩 패턴, 도메인별 지식을 제공할 수 있습니다. 팀은 전문성을 재사용 가능한 agent로 체계화할 수 있습니다. 예를 들어 [WCAG][wcag] 준수를 강제하는 접근성 agent, 보안 코딩 관행을 따르는 보안 agent, 일관된 테스트 패턴을 유지하는 테스트 agent 등을 만들 수 있습니다.

커스텀 에이전트는 프로젝트의 `.github/agents` 폴더 또는 전역 `~/.copilot/agents`의 markdown 파일로 정의합니다. 각 파일에는 최소한 `name`과 `description`이 포함된 YAML frontmatter가 있고, 그 뒤에 agent의 동작, 전문성, 지침을 정의하는 markdown 프롬프트가 이어집니다.

### 커스텀 에이전트와 에이전트 스킬 비교하기

커스텀 에이전트와 [에이전트 스킬][agent-skills-concept] 사이에는 개념적으로 겹치는 부분이 있습니다. 둘 다 주로 markdown 파일로 정의되며 AI에게 작업 수행 방법을 알려 줍니다. 가장 깔끔하게 구분하면 **커스텀 에이전트**는 작업자이고, **스킬**은 도구입니다.

커스텀 에이전트는 자체 컨텍스트 창을 가지며, 작업을 수행하는 과정에서 스킬(심지어 다른 agent까지도)을 오케스트레이션하도록 설계됩니다. 이 실습에서 접근성 커스텀 에이전트는 접근성 가이드라인을 기준으로 사이트를 검토하고 업데이트합니다. 이 과정에서 pull request 워크플로 스킬이나 테스트 실행 및 관리를 담당하는 스킬 같은 도구를 호출할 수도 있습니다.

> [!NOTE]
> 커스텀 에이전트를 작성하는 유일한 "정답"은 없습니다. AI의 다른 작업과 마찬가지로, 환경과 시나리오에 가장 잘 맞는 방식을 찾기 위해 테스트하고 반복해 보아야 합니다.

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/
## 시나리오

많은 웹 애플리케이션이 모든 사용자에게 접근 가능하지 못하며, 지금 작업 중인 웹 사이트도 예외는 아닙니다. 커스텀 에이전트를 사용해 접근성 문제를 식별하고 해결해 보겠습니다.

Tailspin Toys는 시각 능력이나 선호도와 관계없이 모든 사용자가 crowdfunding platform을 이용할 수 있도록 보장하는 데 전념하고 있습니다. 최근 사용자 피드백에 따르면 현재 dark theme는 텍스트와 배경색 사이의 대비가 충분하지 않아 일부 사용자가 읽기 어렵다고 느끼고 있습니다. 이 접근성 문제를 해결하기 위해 디자인 팀은 사용자가 켜고 끌 수 있는 high-contrast mode 구현을 요청했습니다.

접근성은 매우 중요하므로 가능한 한 빠르게 구현하고 싶습니다. 커스텀 에이전트를 활용해 이 기능을 생성합니다.
이 연습에서는 다음을 수행합니다.

- 커스텀 에이전트를 살펴봅니다.
- 커스텀 에이전트를 활성화하고 Copilot CLI를 사용해 작업을 할당합니다.

## 접근성 커스텀 에이전트 검토하기

접근성을 위해 이미 커스텀 에이전트가 준비되어 있습니다. Copilot을 어떻게 안내하는지 이해하기 위해 내용을 검토해 보겠습니다.

1. `.github/agents/accessibility.md`를 엽니다.
2. `name`과 `description` 필드가 포함된 YAML frontmatter를 확인합니다.

> [!CAUTION]
> `name`과 `description`이 포함된 frontmatter는 커스텀 에이전트에 필수입니다.

3. 이어지는 섹션을 훑어보며 다음 내용을 확인합니다.
   - 접근 가능한 웹 사이트를 위한 코드를 생성할 때의 핵심 책임
   - 접근성 모범 사례
   - HTML, CSS, JavaScript용 코드 예시
   - 흔한 함정과 실수 목록

## Copilot CLI에서 커스텀 에이전트 사용하기

Copilot CLI에서는 `/agent` 명령으로 커스텀 에이전트를 시작할 수 있습니다. 이제 웹 사이트에 접근성 점검을 수행해 보겠습니다.

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
1. Copilot CLI의 프롬프트 창에 `/agent`를 입력하고 <kbd>Enter</kbd>를 눌러 agent 목록을 엽니다.
2. 사용 가능한 agent 목록에서 **Accessibility agent**를 선택합니다.
3. 다음 프롬프트를 사용해 접근성 agent에게 접근성 백로그 항목을 검토하고 수정 사항을 생성해 달라고 요청합니다.

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. Copilot이 작업을 시작합니다. 먼저 issue를 가져오고, 검토를 수행하고, 업데이트를 생성하고, 마지막으로 PR을 만듭니다. PR을 만들 때 프로젝트의 PR 전용 스킬을 사용하는 점도 확인할 수 있습니다.

> [!NOTE]
> 이 과정은 몇 분 정도 걸릴 수 있습니다. 지금까지 학습한 내용을 되돌아보거나, 음료를 즐기거나, Copilot CLI에서 사용할 수 있는 추가 명령을 다루는 다음 모듈을 미리 살펴보기에 좋은 시간입니다.

## 요약 및 다음 단계

이 연습에서는 GitHub Copilot의 [커스텀 에이전트][custom-agents]를 살펴보았습니다. 커스텀 에이전트는 특정 작업과 도메인에 맞춘 전문 AI 도우미입니다. 커스텀 에이전트를 사용하면 팀의 전문성과 표준을 재사용 가능한 agent로 체계화해 Copilot이 특정 유형의 작업을 더 효과적으로 수행하도록 안내할 수 있습니다.

다음 개념을 살펴보았습니다.

- 커스텀 에이전트가 어떻게 정의되는지
- Copilot CLI에서 커스텀 에이전트를 사용하는 방법

다음으로는 [몇 가지 slash commands][next-lesson]를 살펴보며 Copilot CLI의 추가 팁을 알아보겠습니다.

## 리소스

- [커스텀 에이전트][custom-agents]
- [리포지토리용 커스텀 에이전트 만들기][creating-custom-agents]
- [Awesome-copilot의 커스텀 에이전트][awesome-copilot-agents]
- [조직에서 커스텀 에이전트를 사용하기 위한 준비][org-custom-agents]
- [엔터프라이즈에서 커스텀 에이전트를 사용하기 위한 준비][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
