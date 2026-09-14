---
title: "Lesson 2 - 별점 추가로 작은 성과 얻기"
description: "GitHub Copilot app에서 첫 번째 에이전트 세션을 시작하고 게임 카드를 조금 변경한 다음 첫 번째 끌어오기 요청으로 병합합니다."
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

이전 레슨에서는 워크스페이스를 살펴보고 빠른 채팅을 사용했습니다. 이제 **에이전트 세션**을 시작하고 프로젝트를 처음으로 변경합니다. 변경 범위는 작게 유지합니다. 게임 데이터에는 이미 별점이 있지만 홈페이지의 게임 카드에는 아직 표시되지 않습니다. 에이전트에게 별점을 표시하도록 요청하고, 변경 내용을 검토하고, 첫 번째 끌어오기 요청으로 병합합니다.

이 레슨에서는 다음 작업을 수행합니다.

- 에이전트 세션을 시작하고 세션의 구조를 알아봅니다.
- 에이전트에게 프로젝트를 작고 구체적으로 변경하도록 요청합니다.
- 워크스페이스의 diff 보기에서 변경 내용을 검토합니다.
- 앱을 로컬에서 실행하여 브라우저에서 변경 내용을 확인합니다.
- 첫 번째 끌어오기 요청을 열고 병합합니다.

## 시나리오

Tailspin Toys의 각 게임에는 별점이 있을 수 있으며, 별점은 이미 게임 세부 정보 페이지에 표시됩니다. 하지만 홈페이지의 게임 카드에는 제목, 카테고리, 퍼블리셔, 설명만 표시됩니다. 첫 세션 연습으로 에이전트에게 각 카드에 기존 별점을 표시하도록 요청합니다. 첫 번째 세션에 적합한 작고 독립적인 변경입니다.

## 세션 구조

**세션**은 에이전트와의 대화입니다. 이 워크숍에서는 **new working tree**를 선택하여 세션 전용 체크아웃과 브랜치를 사용합니다. 이렇게 하면 레슨마다 별도 브랜치를 만들지 않고 각 PR 마일스톤을 격리할 수 있습니다. 세션은 사이드바에서 리포지토리별로 그룹화되며, 원하는 세션을 선택하여 전환할 수 있습니다.

세션 안에는 에이전트와의 **대화**, 에이전트가 파일을 탐색하고 편집할 때의 **도구 활동**, diff와 함께 표시되는 **변경된 파일** 목록이 있습니다.

## 세션을 시작하고 변경 요청하기

새 세션을 시작하여 프로젝트를 탐색하고 기능을 구현합니다. [이전 레슨][prior-lesson]에서 GitHub 리포지토리의 프로젝트를 추가했습니다. 해당 리포지토리에 새 세션을 만들고 변경을 요청합니다.

1. GitHub Copilot app으로 돌아가거나 앱을 엽니다.
2. **Home screen**을 선택합니다.
3. 리포지토리로 `tailspin-toys`가 선택되어 있는지 확인합니다.

   ![리포지토리 선택기가 tailspin-toys로 설정되고 프롬프트 아래에 모델 선택기가 표시된 GitHub Copilot app 프롬프트 상자](../../_images/app-2-start-session.png)

4. 프롬프트 상자 아래에서 **new working tree**와 **Interactive** 모드를 선택합니다. 다음 프롬프트로 변경을 요청합니다.

   ```plaintext
   편집하기 전에 이 체크아웃과 브랜치를 식별하고, 커밋하지 않은 변경이 없는 새 워크트리인지 확인한 다음 origin을 가져오고 이 세션 브랜치를 origin/main으로 fast-forward해 주십시오. HEAD가 origin/main과 일치하는지 확인해 주십시오. 미커밋 변경이나 분기가 있거나 업데이트할 수 없으면 중단하고 설명해 주십시오. 재설정하거나 작업을 버리지 마십시오.

   게임 카드에 각 게임의 별점을 표시해 주십시오. Game 타입에는 이미 starRating 필드가 있으며 5점 만점의 숫자이거나 아직 평가되지 않은 경우 null입니다. src/components/GameCard.astro의 각 카드에 표시하고, starRating이 null이면 대신 "No rating yet"을 표시해 주십시오. 변경을 작게 유지하고 카드 레이아웃을 재구성하거나 데이터 모델을 변경하지 마십시오.

   리포지토리 지침을 따르고 적절한 테스트를 추가하거나 업데이트한 다음 관련된 기존 npm 검사를 실행해 주십시오. 필수 조건을 살펴보고 설치 전에 질문해 주십시오. 변경된 파일과 검사 결과를 보고한 다음 제가 검토할 수 있도록 중단해 주십시오. 커밋, 푸시, 끌어오기 요청 생성, 다른 기능 구현은 하지 마십시오.
   ```

> [!NOTE]
> 프롬프트에 Copilot이 업데이트할 파일 이름을 포함했습니다. Copilot이 작업에 포함할 파일을 반드시 지정할 필요는 없지만, 방향을 제시하면 Copilot이 코드를 더 빠르게 생성하고 토큰 사용량을 줄이는 데 도움이 됩니다.

5. <kbd>Enter</kbd>를 눌러 Copilot에 프롬프트를 보냅니다.

Copilot app은 먼저 프로젝트의 격리된 복사본인 새 작업 트리를 만들고 작업을 시작합니다. 그런 다음 프로젝트를 탐색하고 새 기능을 추가하기 위해 업데이트해야 할 파일을 찾은 후 필요한 코드를 만듭니다. 이제 Copilot app으로 새 기능을 추가했습니다.

## diff 검토

AI가 생성한 모든 변경 내용은 작더라도 병합하기 전에 검토해야 합니다. Copilot app에서 바로 변경 내용을 살펴봅니다.

1. 앱 오른쪽 위에서 **Toggle review panel**을 선택합니다. Copilot이 적용한 보류 중인 모든 변경 내용을 보여 주는 diff 화면이 열립니다.

   ![Create PR 오른쪽의 Toggle review panel 버튼을 화살표로 가리키는 GitHub Copilot app 위쪽 도구 모음](../../_images/app-2-review-panel.png)

2. 게임 세부 정보를 표시하는 핵심 파일인 `GameCard.astro`에 코드가 추가된 것을 확인합니다. 다음 코드와 비슷해야 합니다. 별점이 있으면 표시하고 `starRating`이 `null`이면 "No rating yet"으로 대체하는 작은 블록입니다.

   ```astro
   {game.starRating !== null ? (
       <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-900/60 text-amber-300" data-testid="game-rating">
           ★ {game.starRating} / 5
       </span>
   ) : (
       <span class="text-xs font-medium text-slate-500" data-testid="game-rating-empty">
           No rating yet
       </span>
   )}
   ```

> [!NOTE]
> 모든 생성형 AI 도구와 마찬가지로 Copilot은 결정론적이 아니라 확률적으로 작동하므로 정확한 코드는 위 예제와 다를 수 있지만 대체로 비슷해야 합니다.

## 변경 내용 확인

브라우저를 열기 전에 에이전트의 자동 검사 결과를 검토합니다. 아직 존재하지 않는 스킬 대신 프로젝트의 기존 npm 스크립트를 사용하여 숫자 `starRating`과 `null` 대체 표시를 테스트하는지 확인합니다. 누락된 필수 조건이나 건너뛴 검사는 통과가 아닙니다.

그런 다음 세션의 내장 터미널로 앱을 수동 확인합니다. 서버를 시작하기 전에 워크트리를 식별하고 다른 체크아웃의 서버를 재사용하지 않습니다.

1. Copilot app 오른쪽의 검토 패널에서 **Terminal**을 선택합니다. **Terminal** 버튼이 없으면 **+**(**Open in panel** 레이블)를 선택한 다음 **Terminal**을 선택합니다.

   ![GitHub Copilot app 검토 패널의 Terminal 버튼](../../_images/app-terminal-screenshot.png)

2. 터미널 창에 다음 명령을 입력하여 웹앱의 개발 서버를 시작합니다.

   ```shell
   npm run dev
   ```

3. 서버가 시작되면 브라우저 창을 엽니다. 잠시만 기다리면 됩니다.
4. 서버가 출력한 로컬 URL을 엽니다. 일반적으로 `http://localhost:4321`입니다. 포트가 사용 중이면 관련 없는 프로세스를 중지하지 말고 소유자를 확인합니다.
5. 평가된 게임 카드에 5점 만점의 값이 표시되는지 확인합니다. 미평가 데이터가 있으면 **No rating yet**이 표시되는지 확인합니다. 없다면 관찰했다고 주장하지 말고 자동 테스트로 null 사례를 검증합니다.
6. 터미널 창으로 돌아갑니다.
7. <kbd>Control</kbd>+<kbd>C</kbd>(Mac) 또는 <kbd>Ctrl</kbd>+<kbd>C</kbd>(Windows/Linux)를 눌러 직접 시작한 개발 서버를 중지합니다.

## 첫 번째 끌어오기 요청 열기 및 병합

변경 내용이 올바르므로 이제 PR 1을 만들 차례입니다. 먼저 구현과 별도로 커밋과 PR 생성을 승인합니다.

```plaintext
별점 변경과 테스트의 전체 diff를 검토하고, 검증 결과를 요약하고, 검토된 변경을 이 세션 브랜치에 커밋해 주십시오. 브랜치를 푸시하고 리포지토리의 PR 템플릿을 사용하여 main을 대상으로 끌어오기 요청을 만들어 주십시오. 병합하지 마십시오.
```

1. 세션에서 생성된 PR 링크를 엽니다. 앱에 **Create PR** 확인이 표시되면 이를 선택하여 요청을 승인하고 두 번째 PR을 만들지 않습니다.
2. 메시지가 표시되면 **Sign in with your browser**를 선택하고 안내에 따라 인증합니다.
3. Copilot이 PR을 만들기 시작합니다.

PR이 만들어지면 **My work**에서 전체 PR diff와 검사를 살펴봅니다. 학습용 리포지토리의 워크플로 결과를 읽고, 필수 검사와 검토가 완료되기를 기다리며, 실패를 해결한 후 병합합니다. **Ready to merge**는 변경 내용 검토나 로컬 검증 근거를 대체하지 않습니다.

4. 채팅 바로 위의 **PR** 버블을 선택하여 검토 창에서 PR을 열고 끌어오기 요청을 확인합니다. 필요에 따라 여기에서 PR을 검토할 수 있습니다.
5. 준비가 되면 **Ready to merge**를 선택합니다.
6. 새 대화 상자에서 **Merge pull request**를 선택하여 끌어오기 요청을 병합합니다.

계속하기 전에 PR 1이 `main`에 병합되었는지 확인합니다. 학습용 리포지토리를 병합하는 것만으로 웹사이트가 배포되지는 않습니다. 다음 레슨은 새 워크트리에서 시작하고 `origin/main`으로 업데이트하여 이 PR을 포함합니다.

## 요약 및 다음 단계

첫 번째 에이전트 세션을 시작하고 첫 번째 변경을 제공했습니다. 구체적으로 다음 작업을 수행했습니다.

- 에이전트 세션을 시작하고 세션의 구조를 알아봤습니다.
- 에이전트에게 게임 카드를 작고 구체적으로 변경하도록 지시했습니다.
- 워크스페이스의 diff 보기에서 변경 내용을 검토했습니다.
- 앱을 로컬에서 실행하여 브라우저에서 별점을 확인했습니다.
- PR 1을 만들고 검사를 검토한 다음 명시적으로 병합했습니다.

다음으로 백로그의 이슈 중 하나에서 시작하여 앱으로 리포지토리에 사용자 지정 지침 표준을 추가합니다. [레슨 3 - 사용자 지정 지침으로 Copilot 안내][next-lesson]를 계속 진행합니다.

## 리소스

- [GitHub Copilot app에서 에이전트 세션 사용][agent-sessions]
- [GitHub Copilot app 정보][about-copilot-app]
- [GitHub Copilot app으로 이슈 및 끌어오기 요청 관리][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#github-copilot-app-설치-및-구성
[previous-lesson]: ../1-install-copilot-app/
[next-lesson]: ../3-custom-instructions/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests