---
title: "실습 6 - GitHub Copilot의 작업 반복 개선"
authors:
  - geektrainer
lastUpdated: 2026-06-30
next: false
---

| [← 이전 실습: 에이전트 모니터링 및 관리][previous-lesson] |
| :-- |

## 작업 검토

지금까지 이 실습에서 GitHub Copilot과 함께 사용자 경험을 개선하는 여러 작업을 수행했습니다. 에이전트 모드(Agent mode)로 클라이언트와 서버 전반에 필터링을 추가하고, Playwright MCP 서버로 브라우저에서 해당 작업을 수동 테스트했습니다. 그런 다음 사용자 지정 에이전트로 고대비 및 밝은 모드 전환 기능을 구현하고, 진행 중인 세션의 방향을 조정하여 작업을 확장했습니다. 이제 로컬 작업을 게시하고 팀에서 검토하는 방식으로 살펴볼 차례입니다.

### 시나리오

생성형 AI가 도입되어도 소프트웨어 설계와 DevOps의 기본은 변하지 않습니다. Copilot이 만든 결과물도 정식 검토 과정을 거쳐야 합니다. 이를 염두에 두고 codespace의 접근성 변경 사항을 푸시한 뒤 풀 리퀘스트(Pull request)를 열고, 팀의 나머지 구성원이 참여하기 전에 변경 내용을 살펴봅니다.
## 접근성 기능 게시

[실습 4][exercise-4]와 [실습 5][exercise-5]에서 접근성 사용자 지정 에이전트로 구현한 고대비 및 밝은 모드 전환 기능은 codespace에 커밋된 변경 사항으로 남아 있습니다. 팀의 나머지 구성원이 검토할 수 있도록 브랜치에 푸시하고 풀 리퀘스트를 엽니다.

1. codespace로 돌아갑니다.
2. VS Code에서 **Source Control** 보기를 엽니다.
3. 접근성 변경 사항을 커밋했는지 확인합니다. 실습 5의 변경 사항 중 커밋하지 않은 것이 있다면 스테이징한 뒤 `Add high-contrast and light-mode toggles`와 같이 내용을 알 수 있는 메시지로 커밋합니다.
4. **Publish Branch**를 선택하여 브랜치를 게시합니다. 또는 **...** 메뉴 → **Push**를 사용합니다.
5. VS Code에서 github.com의 새 브랜치를 열지 묻습니다. 안내를 수락하거나 직접 리포지토리로 이동하여 브랜치 배너의 **Compare & pull request**를 선택합니다.
6. 명확한 제목(예: `Add high-contrast and light-mode toggles`)을 지정하고 수행한 작업과 이유를 요약하는 짧은 설명을 작성합니다.
7. **Create pull request**를 선택합니다.
8. PR을 열면 **Files changed** 탭을 선택하여 작업 전체를 검토합니다. 특히 다음 항목에 주의합니다.
   - 모드를 전환하는 토글 UI 컴포넌트.
   - 사용자 기본 설정을 유지하기 위한 로컬 스토리지 사용.
   - 고대비 및 밝은 모드의 CSS 또는 스타일 변경 사항.
   - 접근성 속성(ARIA 레이블, 키보드 탐색 등).
   - 모드 전환을 관리하는 JavaScript/TypeScript 코드.

9. **Conversation** 탭으로 돌아갑니다.
10. 승인을 기다리는 워크플로가 있다면 **Approve and run workflows**를 선택합니다.

    ![워크플로 승인 및 실행](../../_images/shared-approve-workflows.png)
11. 워크플로가 완료될 때까지 기다립니다. 문제가 없다면 통과한 결과가 표시됩니다.

> [!TIP]
> 접근성 작업에 대한 다른 의견이 필요하다면 PR 댓글에 `@copilot`을 태그하고 "이 PR에 추가적인 WCAG 문제가 있는지 검토해 줘" 또는 "키보드 탐색 개선 사항을 제안해 줘"와 같이 요청합니다. Copilot이 새 세션을 시작하여 댓글의 요청을 처리합니다.

## 선택 실습 - 로컬에서 계속 탐색

IDE에서 에이전트와 반복적으로 작업하는 것도 하나의 기술이며, 이를 익히려면 반복해야 합니다. VS Code에서 진행할 수 있는 후속 세션의 예시는 다음과 같습니다.

- 게임 상세 페이지에 후원자 관심 등록 양식을 추가합니다.
- 게임 목록 페이지에 페이지 매김을 구현합니다.
- `src/lib/`의 데이터 접근 도우미에 입력 유효성 검사와 오류 처리를 추가합니다.
- 접근성 에이전트의 범위를 확장합니다. 예를 들어 사이트 전체의 키보드 포커스 순서를 점검합니다.

## 요약

축하합니다. VS Code 과정을 완료했습니다! 이 실습에서 수행한 작업은 다음과 같습니다.

- **Playwright MCP로 기능을 수동 테스트했습니다.** Playwright MCP 서버를 추가하고 Copilot이 브라우저를 조작하여 필터링 기능을 검증하도록 한 뒤 풀 리퀘스트를 열었습니다.
- **에이전트 모드로 스택 전반의 변경 사항을 함께 처리했습니다.** 한 세션에서 클라이언트, 서버, 테스트에 걸친 필터 기능을 추가했습니다.
- **사용자 지정 에이전트를 사용했습니다.** 에이전트 선택기에서 접근성 중심의 사용자 지정 에이전트를 선택하고 리포지토리에 고대비 모드를 구현하는 과정을 살펴보았습니다.
- **에이전트 세션을 관리하고 방향을 조정했습니다.** 제안된 변경 사항을 인라인으로 검토하고 원하는 내용을 수락했으며, 밝은 모드 후속 작업으로 세션을 확장했습니다.
- **풀 리퀘스트로 작업을 마무리했습니다.** 로컬 작업을 게시하고 팀에서 검토하는 방식으로 처음부터 끝까지 살펴보았습니다.

## 검토 및 다음 단계

이것으로 필수 VS Code 과정을 마칩니다. 워크숍을 완료했으므로 여기서 마무리해도 됩니다.

Copilot의 에이전트 기능을 더 폭넓게 이해하고 싶다면, 다른 과정에서 서로 다른 환경을 통해 관련 시나리오를 살펴볼 수 있습니다.

- 💻 [**CLI 과정**](../../cli/) — 터미널에서 Copilot CLI로 비슷한 흐름을 진행합니다. 계획 모드, 에이전트 스킬, 사용자 지정 에이전트, `/share`, `/context`, `/delegate`와 같은 슬래시 명령을 다룹니다.
- ☁️ [**클라우드 에이전트 과정**](../../cloud/) — 클라우드 에이전트에 이슈를 할당하고, 에이전트 페이지에서 세션을 모니터링하며, 풀 리퀘스트를 비동기적으로 반복 개선하는 데 초점을 맞춥니다.

여기서 시작한 작업을 계속 확장할 수도 있습니다. [awesome-copilot][awesome-copilot]에서 본인의 프로젝트에 맞게 활용할 수 있는 더 많은 지침 파일, 사용자 지정 에이전트, 스킬을 찾아볼 수 있습니다.

선택 확장 과정인 [선택 사항: Foundry 통합][exercise-7]에서는 VS Code와 Microsoft Foundry Toolkit을 사용하여 모델을 준비하고 Backer Concierge를 배포한 뒤 사이트에 연결합니다.

## 참고 자료

- [GitHub Copilot][github-copilot]
- [VS Code의 Copilot Chat][copilot-chat-vscode]
- [에이전트 모드 사용][agent-mode]

---

| [← 이전 실습: 에이전트 관리][previous-lesson] |
|:--|

[previous-lesson]: ../5-managing-agents/
[exercise-4]: ../4-custom-agents/
[exercise-5]: ../5-managing-agents/
[exercise-7]: ../7-foundry-toolkit/
[github-copilot]: https://github.com/features/copilot
[copilot-chat-vscode]: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
[agent-mode]: https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
[awesome-copilot]: https://github.com/github/awesome-copilot
