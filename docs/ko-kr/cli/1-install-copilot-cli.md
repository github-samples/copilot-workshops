---
title: "연습 1 - GitHub Copilot CLI 설치"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[GitHub Copilot CLI][about-copilot-cli]는 터미널에서 실행되는 강력한 에이전트형 코딩 도우미입니다. 코드베이스를 탐색하고, 코드를 생성하고, 명령을 실행하고, 외부 도구와 상호 작용하는 작업을 모두 명령줄에서 수행할 수 있습니다. 작업을 위임하고, 변경을 요청하고, 흐름을 유지할 수 있습니다. 예상할 수 있듯 첫 단계는 도구를 설치하는 일입니다. 다행히 이미 익숙한 도구로 설치할 수 있습니다.

이 연습에서는 다음을 학습합니다.

- npm을 사용해 GitHub Copilot CLI를 설치합니다.
- GitHub 계정으로 인증합니다.
- 설치를 확인합니다.

## 시나리오

팀에서는 늘어나는 백로그를 처리하기 위해 AI agent를 사용하기 시작했습니다. Copilot CLI는 많은 개발자가 주로 작업하는 터미널 안으로 그 기능을 가져옵니다. 이 연습을 마치면 설치와 인증이 완료되어, 워크숍의 나머지 단계를 진행할 준비가 됩니다.

## 코드스페이스에서 터미널 열기

Copilot CLI를 설치하기 전에 코드스페이스에서 터미널 창을 열어야 합니다.

1. 코드스페이스로 돌아가 설정이 완료될 때까지 기다립니다.
2. <kbd>Ctrl</kbd>+<kbd>`</kbd>를 눌러 터미널 창을 엽니다.
3. VS Code 창 하단에 터미널 패널이 나타나는지 확인합니다.

## 학습 환경 확인

코드스페이스 터미널에서 워크숍 콘텐츠 리포지토리가 아니라 자신의 Tailspin Toys 리포지토리에 있는지 확인합니다. `README.md`와 `package.json`에서 설정 및 검사 명령을 읽습니다. 현재 Tailspin Toys에는 Node.js 22.13 이상, 프로젝트 의존성, E2E 테스트용 Playwright Chromium이 필요합니다.

```bash
pwd
git remote -v
node --version
gh auth status
```

GitHub CLI(`gh`)는 PR과 CI를 확인하는 데 유용합니다. 인증되지 않았다면 `gh auth login`을 실행하고 브라우저 안내를 따릅니다. 계정이 이 리포지토리에 브랜치를 푸시하고 PR을 생성하고 병합할 수 있는지 확인합니다. 조직 정책에 따라 다른 검토자가 필요할 수 있습니다. 코드 변경을 시작하기 전에 리포지토리 설정 안내에 따라 누락된 필수 조건을 해결하고, 설치 내용을 검토한 후 승인합니다.

CLI는 시작한 체크아웃에서 실행됩니다. 대화를 시작해도 격리된 워크트리(Worktree)가 자동으로 생성되지는 않습니다. 이 워크숍에서는 PR 마일스톤마다 하나의 브랜치를 사용합니다. 먼저 별점과 지침 실증을 병합한 후 연습 4~8에서 동일한 필터링 브랜치를 유지합니다.

## Copilot CLI 설치

Copilot CLI는 [npm][install-npm], [WinGet][install-winget], [Homebrew][install-homebrew]로 설치할 수 있습니다. GitHub Codespaces에는 Node.js가 이미 설치되어 있으므로 npm을 사용해 Copilot CLI를 설치합니다.

1. 터미널에서 Node.js가 설치되어 있고 버전 요구 사항을 충족하는지 확인합니다.

   ```bash
   node --version
   ```

   CLI 자체의 요구 사항이 다르더라도 Tailspin Toys에는 버전 22.13 이상이 필요합니다. 버전이 너무 낮다면 학습용 리포지토리의 설정 안내를 따릅니다.

2. npm을 사용해 코드스페이스에 Copilot CLI를 전역 설치합니다.

   ```bash
   npm install -g @github/copilot
   ```

3. 버전을 확인해 설치를 검증합니다.

   ```bash
   copilot --version
   ```

   버전 번호(예: `v1.0.XX`)가 표시되어야 합니다.

> [!NOTE]
> 권한 오류로 설치가 실패하면 익숙하지 않은 명령을 관리자 권한으로 다시 실행하지 말고 npm 설정을 확인하거나 워크숍 진행자에게 도움을 요청합니다.

## GitHub로 인증하기

Copilot CLI를 처음 실행하면 GitHub 계정으로 인증하라는 메시지가 표시됩니다.

1. Copilot CLI를 시작합니다.

   ```bash
   copilot
   ```

2. 현재 로그인되어 있지 않다면 인증 프롬프트가 표시됩니다. Copilot CLI는 device code를 보여 주고 URL로 이동하라고 안내합니다.
3. 화면의 안내를 따릅니다.
   - 제공된 URL을 브라우저에서 엽니다.
   - 메시지가 표시되면 device code를 입력합니다.
   - Copilot CLI가 GitHub 계정에 액세스하도록 승인합니다.
4. 인증이 완료되면 질문과 명령을 받을 준비가 된 Copilot CLI 프롬프트가 표시됩니다.

> [!NOTE]
> 코드스페이스에서는 GitHub 세션을 통해 이미 인증되어 있을 수 있습니다. Copilot CLI가 인증 메시지 없이 시작되면 바로 진행하면 됩니다.

## 디렉터리를 신뢰하고 모든 것이 작동하는지 확인하기

이제 처음으로 Copilot CLI 프롬프트가 열렸으니, 이 워크숍 리포지토리를 신뢰하도록 설정하고 Copilot CLI가 제대로 설치되어 연결되었는지 확인해 보겠습니다.

1. Copilot CLI가 이 폴더의 파일을 신뢰하는지 확인해 달라고 요청하면 세 가지 옵션이 표시됩니다.
   - **Yes, proceed**: 이번 세션에만 신뢰
   - **Yes, and remember this folder for future sessions**: 영구적으로 신뢰
   - **No, exit (Esc)**: 파일 액세스 허용 안 함
2. 이 워크숍에서는 계속 이 리포지토리에서 작업하므로 **Yes, and remember this folder for future sessions**를 선택합니다.
3. 간단한 질문을 해 Copilot이 작동하는지 확인합니다.

   ```plaintext
   이 프로젝트에는 어떤 파일이 있습니까?
   ```

4. Copilot이 리포지토리를 탐색하고 프로젝트 구조 요약을 제공해야 합니다.
5. `/help` 명령으로 사용 가능한 slash commands를 확인합니다.

   ```text
   /help
   ```

6. Copilot 프롬프트에서 다음 명령을 입력해 이 세션을 종료합니다. 첫 변경은 새 세션에서 시작합니다.

   ```text
   /exit
   ```

## 모드와 권한 이해

Copilot CLI는 시작한 디렉터리와 Git 브랜치에서 작업합니다. 디렉터리를 신뢰하면 리포지토리 컨텍스트를 사용할 수 있지만, 모든 도구 작업을 승인하는 것과는 다릅니다. 파일 변경, 셸 명령, GitHub 작업에 대한 권한 요청을 검토합니다.

학습용 리포지토리 루트에서 다음 명령으로 코드 연습을 시작합니다.

```bash
copilot --enable-all-github-mcp-tools
```

GitHub MCP 서버는 기본 제공됩니다. 이 플래그는 이슈와 PR 작업에 필요한 전체 도구를 노출하지만, 인증과 리포지토리 권한 및 도구 승인은 계속 적용됩니다. 플래그 자체가 커밋이나 PR을 승인하지는 않습니다.

<kbd>Shift</kbd>+<kbd>Tab</kbd>으로 일반 **Interactive**, **Plan**, **Autopilot** 모드를 순환합니다. 요청 전에 모드 표시를 확인합니다. 초기 변경에서는 Interactive를 유지하고, 필터링은 구축 전에 계획하며, 사용자 지정을 만들고 검토하기 전에는 명시적으로 Interactive로 돌아옵니다.

> [!CAUTION]
> 모드와 권한 설정은 다릅니다. Autopilot은 자율적으로 작업을 계속하며, `--allow-all`과 별칭 `--yolo`는 모든 도구, 경로, URL 권한을 부여합니다. 이 워크숍은 매번 무제한 권한으로 세션을 시작할 것을 요구하지 않습니다. 코드스페이스에서도 액세스를 허용하기 전에 범위를 검토합니다.

## 요약 및 다음 단계

축하합니다! GitHub Copilot CLI를 성공적으로 설치하고 인증했습니다. 다음을 학습했습니다.

- npm을 사용해 Copilot CLI를 설치합니다.
- GitHub 계정으로 인증합니다.
- Copilot CLI가 작업할 디렉터리를 신뢰하도록 설정합니다.
- 설치가 올바르게 작동하는지 확인합니다.

Copilot CLI를 설치했으므로 [연습 2 - 별점 추가로 작은 성과 얻기][next-lesson]에서 검토하기 쉬운 작은 변경을 수행합니다.

## 리소스

- [GitHub Copilot CLI 설치][install-copilot-cli]
- [Copilot CLI 소개][about-copilot-cli]
- [Copilot CLI 사용하기][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
