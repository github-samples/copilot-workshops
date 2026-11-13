---
title: "레슨 1 - GitHub Copilot app 설치"
description: "GitHub Copilot app을 설치하고, 템플릿에서 만든 리포지토리를 연결하고, 워크스페이스를 살펴보고, 빠른 채팅을 사용해 봅니다."
authors:
  - geektrainer
lastUpdated: 2026-10-05
---

[**GitHub Copilot app**][about-copilot-app]은 에이전트 기반 개발을 위한 데스크톱 애플리케이션입니다. GitHub Copilot CLI를 기반으로 하며 GitHub와 기본적으로 통합되어 리포지토리, 브랜치, CI 파이프라인을 바로 사용할 수 있습니다. 모든 작업을 직접 수행하고 반복 작업을 자동화하는 방식 대신, 각자 격리된 워크스페이스에서 여러 에이전트를 병렬로 지시하는 워크플로를 위해 설계되었습니다. Node.js를 설치하고 프로젝트 복사본을 준비했으므로 이제 앱을 설치하고 해당 리포지토리를 연결합니다.

이 레슨에서는 다음 작업을 수행합니다.

- GitHub Copilot app을 설치하고 로그인합니다.
- GitHub 리포지토리에서 프로젝트를 앱에 추가합니다.
- 템플릿에서 미리 생성한 백로그를 포함하여 워크스페이스를 살펴봅니다.
- 빠른 채팅을 사용하여 앱 자체에 관해 알아봅니다.

## 시나리오

팀에서 늘어나는 백로그를 처리하기 위해 AI 에이전트를 도입하고 있습니다. Copilot app에서는 이슈 선택, 에이전트 실행, 변경 내용 검토, 끌어오기 요청 병합을 한곳에서 지시할 수 있습니다. 이 레슨에서는 앱을 설치하고 연결한 다음 프로젝트에 관한 대화를 시작하는 방법을 익힙니다.

> [!NOTE]
> 적격 Copilot 플랜인 Copilot Free, Copilot Student 또는 유료 플랜(Pro, Pro+, Business, Enterprise)이 필요합니다. Copilot Business 또는 Copilot Enterprise를 사용하는 경우 관리자가 **GitHub Copilot app** 정책을 활성화한 상태로 유지해야 합니다.

## GitHub Copilot app 설치 및 구성

GitHub Copilot app을 사용하려면 먼저 앱을 설치해야 합니다. Windows, macOS, Linux용 버전이 제공됩니다. 앱을 설치하고 인증한 다음 Tailspin Toys 리포지토리를 앱에 추가합니다.

1. 브라우저에서 [GitHub Copilot app 랜딩 페이지][download-app]를 엽니다.
2. 플랫폼에 맞는 앱을 다운로드하고 랜딩 페이지의 지침에 따라 설치합니다.
3. 설치가 끝나면 앱을 엽니다.
4. **Sign in to GitHub**을 선택하고 안내에 따라 GitHub.com 또는 GHE.com 계정으로 로그인합니다. 데이터 상주를 지원하는 GitHub Enterprise Cloud를 사용하는 경우 **GitHub Enterprise Cloud**를 선택하고 메시지가 표시되면 `*.ghe.com` 호스트 이름을 입력합니다.

   GitHub Enterprise Server를 사용하는 경우 먼저 클라우드 계정으로 온보딩을 완료합니다. 그런 다음 **Settings**를 열고 **Accounts**, **Add account**, **GitHub Enterprise Server**를 차례로 선택합니다. [Enterprise Server 로그인 가이드][ghes-sign-in]에 설명된 대로 안내에 따라 브라우저에서 앱을 승인합니다.

5. 온보딩에서 리포지토리 선택 화면이 표시되면 템플릿에서 만든 Tailspin Toys 리포지토리를 선택합니다. 리포지토리 선택을 건너뛰고 온보딩을 마친 후 프로젝트를 추가할 수도 있습니다.
6. 메시지가 표시되면 테마를 선택한 다음 온보딩을 마칩니다.
7. 사이드바의 **Sessions**에서 리포지토리를 찾습니다. 이미 목록에 있으면 다시 추가할 필요가 없습니다.
8. 리포지토리가 아직 연결되지 않았다면 **Sessions** 옆의 **+**를 선택하여 새 세션을 만든 다음 **Add GitHub repository**를 선택합니다. 사전 준비 레슨에서 기록해 둔 소유자와 리포지토리 이름을 사용합니다.
9. 리포지토리가 사이드바에 나타나는지 확인합니다. 여기서 사용하는 레이아웃에서는 `tailspin-toys` 같은 리포지토리 폴더가 **Sessions** 아래에 그룹화되고, 각 리포지토리 아래에 개별 세션이 표시됩니다.

## 워크스페이스 살펴보기

프로젝트를 연결했으므로 잠시 워크스페이스의 구성을 살펴봅니다. 앱의 사이드바는 몇 가지 영역으로 구성됩니다.

- **New** - 이름에서 알 수 있듯이 여기서 Copilot과 새 채팅 세션을 시작할 수 있습니다.
- **Pull requests** - 앱의 GitHub 기본 통합을 통해 끌어오기 요청을 표시합니다. 앱을 벗어나지 않고 끌어오기 요청을 찾아 필터링하고, CI 상태를 확인하고, 끌어오기 요청을 검토할 수 있습니다.
- **Issues** - 같은 방식으로 이슈를 표시합니다. 이슈를 찾아 필터링하고 이슈에서 세션을 시작할 수 있습니다.
- **Automations** — 일정에 따라 또는 요청 시 실행되는 저장된 에이전트 작업입니다. 할 일 목록 관리, 정기적인 프로젝트 유지 관리, 기타 반복 작업을 맡기는 데 유용합니다. 마무리에서 다음 단계로 링크를 제공하며 추가 워크숍 실습으로 다루지는 않습니다.
- **Customize** - MCP 서버, 플러그인, 스킬, 기타 구성 요소 형태로 Copilot app에 기능을 추가합니다. Playwright MCP를 구성할 때 사용합니다.
- **Chats** — 별도의 브랜치나 워크스페이스가 필요하지 않은 질문과 브레인스토밍을 위한 가벼운 대화입니다. 이 섹션은 첫 채팅을 시작한 후에 나타납니다. 보이지 않으면 **Sessions** 옆의 **+**를 선택하여 첫 채팅을 시작합니다.
- **Sessions** — 리포지토리 폴더와 해당 에이전트 세션을 그룹화합니다. `tailspin-toys` 같은 리포지토리 이름을 선택하면 해당 리포지토리 보기가 열리고, 그 아래의 세션을 선택하면 해당 대화로 돌아갑니다. 각 세션은 격리된 워크스페이스에서 실행되므로 변경 내용이 충돌하지 않게 여러 세션을 동시에 실행할 수 있습니다. 별점을 추가할 때 첫 번째 세션을 시작합니다.

워크숍을 진행하면서 워크스페이스를 살펴봅니다.

> [!TIP]
> 확실하지 않으면 Copilot에 질문합니다. 방법을 모르거나 가능한지 궁금한 작업이 있다면 Copilot에 질문하여 안내를 받을 수 있습니다.

### 미리 생성된 백로그 찾기

백로그가 없는 프로젝트는 거의 없으며 Tailspin Toys도 마찬가지입니다. 템플릿에서 리포지토리를 만들 때 생성된 백로그를 살펴봅니다.

1. 사이드바의 **Sessions**에서 (하위 개별 세션이 아닌) Tailspin Toys 리포지토리 폴더를 선택합니다. 그런 다음 리포지토리 상단 탐색에서 **Issues**를 선택합니다.
2. 이슈 번호를 가정하지 말고 다음 제목으로 이슈를 찾습니다.

   - Allow users to filter games by category and publisher
   - Update our repository coding standards

3. 이슈를 선택하여 세부 정보를 읽습니다. 각 이슈는 에이전트 세션을 시작하는 지점이기도 합니다. 먼저 빠른 변경을 완료한 후 필터링 이슈에서 시작합니다.

> [!NOTE]
> **Issues**와 **Pull requests**의 항목 목록은 Copilot app에 추가한 리포지토리의 항목만 표시하도록 자동으로 필터링됩니다. 다른 리포지토리의 작업 항목을 보려면 해당 리포지토리를 앱에 추가합니다.

## 빠른 채팅 사용해 보기

앱에 익숙해지는 좋은 방법은 앱을 사용하여 *앱 자체*에 관해 알아보는 것입니다. 이때 **빠른 채팅**이 적합합니다. 빠른 채팅에서는 브랜치나 작업 트리를 만들지 않고 질문하거나 브레인스토밍할 수 있으므로, 세션이 필요 없는 일회성 질문에 알맞습니다.

1. 사이드바에서 **Chats** 옆의 **+**를 선택하여 새 채팅을 엽니다. **Chats**가 아직 보이지 않으면 **Sessions** 옆의 **+**를 선택하여 첫 채팅을 시작합니다. 그러면 이후에 **Chats**가 나타납니다.
2. 앱의 세션이 어떻게 작동하는지 질문합니다.

   ```plaintext
   How does the GitHub Copilot app use worktrees?
   ```

3. 대화 보기에서 응답을 읽습니다. 각 세션이 격리된 git 작업 트리에서 실행되므로 변경 내용이 충돌하지 않게 여러 에이전트를 병렬로 실행할 수 있다는 점을 확인할 수 있습니다. 언제든지 대화를 계속하거나 새 채팅을 시작할 수 있습니다.

## 요약 및 다음 단계

GitHub Copilot app을 설치하고 프로젝트를 연결하고 워크스페이스를 살펴봤습니다. 다음 방법을 배웠습니다.

- 앱을 설치하고 GitHub에 로그인합니다.
- GitHub 리포지토리에서 프로젝트를 추가합니다.
- 워크스페이스를 살펴보고 **Issues**에서 미리 생성된 백로그를 찾습니다.
- 빠른 채팅을 사용하여 일회성 질문을 합니다.

다음으로 첫 번째 에이전트 세션을 시작하고 프로젝트를 처음으로 변경하여 게임 카드에 별점을 표시합니다. [레슨 2 - 별점 추가로 작은 성과 얻기][next-lesson]를 계속 진행합니다.

## 리소스

- [GitHub Copilot app 정보][about-copilot-app]
- [GitHub Copilot app 시작하기][getting-started]
- [GitHub Copilot app에서 에이전트 세션 사용][agent-sessions]

[next-lesson]: ../2-add-star-rating/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[download-app]: https://gh.io/app
[ghes-sign-in]: https://docs.github.com/enterprise-server@3.22/copilot/copilot-on-ghes/sign-in-on-copilot-app