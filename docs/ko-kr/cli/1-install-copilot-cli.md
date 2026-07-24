---
title: "연습 1 - GitHub Copilot CLI 설치"
authors:
  - geektrainer
lastUpdated: 2026-06-30
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

1. 아직 열지 않았다면 코드스페이스로 돌아갑니다.
2. <kbd>Ctrl</kbd>+<kbd>`</kbd>를 눌러 터미널 창을 엽니다.
3. VS Code 창 하단에 터미널 패널이 나타나는지 확인합니다.

## Copilot CLI 설치

Copilot CLI는 [npm][install-npm], [WinGet][install-winget], [Homebrew][install-homebrew]로 설치할 수 있습니다. GitHub Codespaces에는 Node.js가 이미 설치되어 있으므로 npm을 사용해 Copilot CLI를 설치합니다.

1. 터미널에서 Node.js가 설치되어 있고 버전 요구 사항을 충족하는지 확인합니다.

   ```bash
   node --version
   ```

   버전 22 이상(예: `v22.x.x`)이 표시되어야 합니다.

2. npm을 사용해 코드스페이스에 Copilot CLI를 전역 설치합니다.

   ```bash
   npm install -g @github/copilot
   ```

3. 버전을 확인해 설치를 검증합니다.

   ```bash
   copilot --version
   ```

   버전 번호(예: `v1.0.XX`)가 표시되어야 합니다.

> [!TIP]
> 권한 오류가 발생하면 일부 시스템에서는 `sudo npm install -g @github/copilot`를 사용해야 할 수 있습니다. 하지만 GitHub Codespaces에서는 일반적으로 필요하지 않습니다.

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

   ```
   What files are in this project?
   ```

4. Copilot이 리포지토리를 탐색하고 프로젝트 구조 요약을 제공해야 합니다.
5. `/help` 명령으로 사용 가능한 slash commands를 확인합니다.

   ```
   /help
   ```

6. 터미널에서 다음 명령을 입력해 Copilot CLI를 종료합니다. 이후 연습에서 다시 Copilot CLI로 돌아옵니다.

   ```
   exit
   ```

## 요약 및 다음 단계

축하합니다! GitHub Copilot CLI를 성공적으로 설치하고 인증했습니다. 다음을 학습했습니다.

- npm을 사용해 Copilot CLI를 설치합니다.
- GitHub 계정으로 인증합니다.
- Copilot CLI가 작업할 디렉터리를 신뢰하도록 설정합니다.
- 설치가 올바르게 작동하는지 확인합니다.

이제 Copilot CLI가 설치되었으니, Copilot에 프로젝트 컨텍스트를 제공해 보겠습니다. [연습 2 - CLI로 커스텀 지침 사용하기][next-lesson]로 계속 진행합니다.

## 리소스

- [GitHub Copilot CLI 설치][install-copilot-cli]
- [Copilot CLI 소개][about-copilot-cli]
- [Copilot CLI 사용하기][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-custom-instructions/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
