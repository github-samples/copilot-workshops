---
title: "연습 5 - 에이전트 스킬 사용하기"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

앱 개발에는 빌드 생성, 테스트 실행, pull request 작성처럼 반복 가능한 작업이 자주 포함됩니다. **에이전트 스킬(Agent Skills)**을 사용하면 Copilot과 다른 AI agent에 이러한 작업을 수행하는 방법에 대한 가이드를 제공할 수 있습니다. 스킬은 agent가 필요할 때 불러올 수 있는 지침, 스크립트, 리소스 폴더입니다. [Agent Skills는 오픈 표준][agent-skills-repo]이며, 여러 agent에서 사용됩니다. 따라서 동일한 스킬을 Copilot Chat in agent mode, Copilot cloud agent, Copilot CLI, GitHub Copilot app 전반에서 사용할 수 있습니다.

스킬은 프로젝트의 `.github/skills` 폴더 또는 전역 `~/.copilot/skills`에 저장됩니다. 각 스킬은 YAML frontmatter(`name`과 `description`)가 포함된 `SKILL.md` 파일과 그 뒤에 이어지는 markdown 지침으로 구성된 폴더입니다.

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

스킬에는 스크립트, asset, 참고 자료를 담은 하위 폴더도 포함될 수 있습니다. 전체 구조는 [agent skills specification][agent-skills-spec]에서 다룹니다.

> [!TIP]
> 스킬은 동적으로 로드됩니다. 어떤 스킬이 적용되는지는 agent가 `description` 필드를 기준으로 판단합니다. 시나리오별로 명확한 설명이 있어야 실제로 사용되는 스킬이 되고, 그렇지 않으면 무시될 수 있습니다.

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
이제 스킬이 팀의 사양에 맞는 pull request를 보장하는 방법을 살펴보겠습니다.

## 시나리오

팀에는 pull request(PR)에 대한 다음 요구 사항이 있습니다.

- 명확한 커밋 메시지를 사용하고, 파일은 논리적으로 그룹화해야 합니다.
- PR을 만들기 전에 모든 테스트가 통과해야 합니다.
- 각 PR에는 다음 섹션이 포함되어야 합니다.
    - 변경이 필요한 이유에 대한 설명
    - 변경된 파일 개요
    - 중요한 코드 블록 스니펫
    - 수행한 변경 사항을 묶어 설명하는 세부 내용

팀은 Copilot으로 코드와 PR을 생성하고 있으므로, AI 도구가 이러한 요구 사항을 따르도록 보장하고 싶어 합니다.

이 연습에서는 다음을 수행합니다.

- Pull request 생성을 위한 기존 스킬을 살펴봅니다.
- AI agent가 스킬을 활용하는 방식을 학습합니다.
- 스킬의 도움으로 가이드라인에 맞는 PR을 만듭니다.

## 스킬 실행하기

스킬은 agent가 필요하다고 판단할 때 동적으로 로드됩니다. 어떤 스킬을 사용할지는 `SKILL.md` 파일의 설명에 따라 결정됩니다. 따라서 스킬의 사용 사례를 정의하는 명확한 설명을 작성하는 것이 중요합니다.

## PR 스킬 살펴보기

Tailspin Toys에는 PR 생성에 대한 요구 사항이 있으므로, AI 도구가 이러한 가이드라인을 따르는 PR을 생성할 수 있도록 도와주는 스킬을 만들었습니다. 이 스킬이 무엇을 하는지 이해하기 위해 내용을 살펴보겠습니다.

1. `.github/skills/make-contribution/SKILL.md`를 엽니다.
2. 이름과 설명을 확인합니다. 설명이 pull request 생성 또는 코드 커밋 요청이 있을 때 사용해야 하는 시나리오를 어떻게 강조하는지 확인합니다.
3. 스킬 내용을 읽어 봅니다. 브랜치 생성 방식, 커밋 생성 방식, pull request 내용에 관한 규칙이 정의되어 있음을 확인합니다.

## 스킬 사용하기

앞서 강조했듯이 스킬은 Copilot CLI가 자동으로 호출합니다. 따라서 Copilot에게 PR 생성을 요청하기만 하면 됩니다.

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
1. 다음 프롬프트를 사용해 Copilot에게 PR 생성을 요청합니다.

    ```
    Can you please create a pull request for me!
    ```

2. Copilot이 요청을 확인합니다. 잠시 후 Copilot이 **make-contribution** 스킬을 사용 중이라고 표시하는 것을 확인할 수 있습니다.

3. Copilot은 이어서 스킬의 지침을 따릅니다. 먼저 테스트를 실행한 뒤 브랜치, 커밋, 그리고 최종적으로 PR을 생성합니다.
4. PR이 생성되면 리포지토리로 돌아가 PR을 엽니다. 섹션이 스킬에 정의된 가이드라인을 따르고 있으며, 팀이 제시한 요구 사항과 일치하는지 확인합니다.
5. 다음 연습으로 넘어가기 전에 이 필터링 PR과 접근성 작업을 분리하기 위해 로컬 작업 공간을 `main`에서 새 브랜치로 초기화합니다.

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## 요약 및 다음 단계

에이전트 스킬의 도움으로 문서화된 요구 사항을 충족하는 새로운 PR을 만들었습니다. 다음을 수행했습니다.

- Pull request 생성을 위한 기존 스킬을 살펴보았습니다.
- AI agent가 스킬을 활용하는 방식을 학습했습니다.
- 스킬의 도움으로 가이드라인에 맞는 PR을 만들었습니다.

스킬은 특정 작업에 적합하지만, 더 강력한 작업을 수행하려면 [custom agents][next-lesson]를 활용해야 합니다. 다음으로 이를 살펴보겠습니다.

## 리소스

- [에이전트 스킬 소개][about-agent-skills]
- [Agent Skills Specification][agent-skills-spec]
- [Agent Skills Repository][agent-skills-repo]
- [Awesome-copilot의 Agent Skills][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
