---
title: "연습 0: 사전 준비"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Copilot CLI 연습을 시작하기 전에 모든 것을 준비해야 합니다. Tailspin Toys 리포지토리(Repository)의 복사본을 만들고 [코드스페이스][codespaces]를 시작합니다. 다음 연습에서는 해당 코드스페이스의 통합 터미널을 사용해 Copilot CLI를 설치하고 실행합니다.

## 실습용 리포지토리 설정

앞으로 작성할 코드를 위한 리포지토리 복사본을 만들기 위해 [template][template-repository]에서 새 인스턴스(Instance)를 만듭니다. 새 인스턴스에는 실습에 필요한 파일이 모두 포함되며, 연습을 진행하는 동안 이 리포지토리를 사용합니다.

1. 새 브라우저 창에서 이 실습의 GitHub 리포지토리로 이동합니다: `https://github.com/github-samples/tailspin-toys`.
2. 실습용 리포지토리 페이지에서 **Use this template** 버튼을 선택해 리포지토리 복사본을 만듭니다. 그런 다음 **Create a new repository**를 선택합니다.

    ![Use this template 버튼](../../_images/ex0-use-template.png)

3. GitHub 또는 Microsoft가 진행하는 행사에서 이 워크숍을 수행하는 경우에는 멘토가 제공하는 안내를 따릅니다. 그렇지 않다면 GitHub Copilot에 액세스할 수 있는 조직에 새 리포지토리를 만들어도 됩니다.

    ![리포지토리 템플릿 설정 입력 화면](../../_images/ex0-repository-settings.png)

4. 이후 실습에서 참조할 수 있도록 생성한 리포지토리 경로(**organization-or-user-name/repository-name**)를 기록해 둡니다.

> [!NOTE]
> **백로그가 준비되었습니다**
>
> template에서 리포지토리를 만들면 GitHub issue 백로그가 자동으로 생성됩니다. 워크숍 내내 이 issue를 바탕으로 작업하므로 직접 등록할 내용은 없습니다.

## 코드스페이스 만들기

이제 코드스페이스를 사용해 실습을 진행합니다.

[GitHub Codespaces][codespaces]는 브라우저에서 직접 코드를 작성하고, 실행하고, 디버그할 수 있는 클라우드 기반 개발 환경입니다. 여러 프로그래밍 언어, 확장, 도구를 지원하는 완전한 기능의 IDE를 제공합니다.

1. 방금 만든 리포지토리로 이동합니다.
2. 초록색 **Code** 버튼을 선택합니다.

    ![Code 버튼 선택 화면](../../_images/ex0-code-button.png)

3. **Codespaces** 탭을 선택한 다음 **+** 버튼을 선택해 새 Codespace를 만듭니다.

    ![새 codespace 만들기](../../_images/ex0-create-codespace.png)

코드스페이스를 만드는 데는 몇 분 정도 걸리지만, 모든 서비스를 수동으로 설치하는 것보다 훨씬 빠릅니다. 기다리는 동안에는 GitHub Copilot의 다른 기능을 살펴볼 수 있으며, 다음 단계에서 그 부분을 이어서 알아봅니다.

> [!CAUTION]
> 이후 연습에서 다시 코드스페이스로 돌아옵니다. 지금은 브라우저 탭에서 그대로 열어 둡니다.

> [!NOTE]
> 이 워크숍은 코드스페이스 또는 로컬 [dev container][dev-containers] 안에서 실행하도록 설계되었습니다. 두 환경 모두 원활한 진행에 필요한 사전 요구 사항이 모두 설치된 상태를 보장합니다. 로컬에서 실행하고 싶다면 복제한 리포지토리를 VS Code에서 열고, 메시지가 표시되면 **Reopen in Container**를 선택합니다. 그러면 코드스페이스에서 사용하는 것과 동일한 dev container를 VS Code가 빌드합니다.

[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
## 요약

축하합니다! 실습용 리포지토리 복사본을 만들었습니다. 또한 Copilot CLI 작업을 시작할 때 사용할 코드스페이스 생성도 시작했습니다.

## 다음 단계

Copilot CLI를 설치하고 GitHub 계정으로 인증해 보겠습니다. [연습 1 - GitHub Copilot CLI 설치][next-lesson]로 계속 진행합니다.

## 리소스

- [GitHub Codespaces 개요][codespaces]
- [템플릿에서 리포지토리 만들기][template-repository]
- [Codespaces 빠른 시작][codespaces-quickstart]

[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
