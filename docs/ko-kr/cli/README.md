---
slug: ko-kr/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[**GitHub Copilot CLI**](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)는 터미널에서 GitHub Copilot을 에이전트형 코딩 도우미로 사용할 수 있게 해줍니다. 코드베이스를 탐색하고, 코드를 생성하고, 명령을 실행하고, 외부 도구에 연결하는 작업을 모두 명령줄에서 처리하므로 그래픽 편집기로 전환하지 않고도 작업 흐름을 유지할 수 있습니다.

연습 0~1에서 설정한 후 연습 2~10의 아홉 개 핵심 모듈을 완료합니다. 별점 추가로 작은 성과를 얻고, 문서화 지침을 정립한 다음, **Plan**과 **Autopilot** 모드로 필터링을 구축합니다. 이어서 재사용 가능한 quality-checks 스킬을 만들고 Playwright MCP로 동작을 검증하며 QA 에이전트를 만들어 기능을 제공합니다. 마지막으로 CLI 조작 방법과 완성한 내용을 살펴봅니다.

## 연습

| 연습 | 주제 | 설명 |
|----------|-------|-------------|
| [0. 사전 준비][ex0] | 설정 | 리포지토리(Repository)와 코드스페이스(Codespace)를 만듭니다 |
| [1. Copilot CLI 설치][ex1] | 설치 | Copilot CLI를 설치하고 인증합니다 |
| [2. 별점 추가로 작은 성과 얻기][ex2] | 첫 변경 | 기존 별점을 표시하고 검증한 후 PR 1을 병합합니다 |
| [3. 사용자 지정 지침으로 Copilot 안내][ex3] | 컨텍스트 | 문서화 규칙을 추가하고 실증한 후 PR 2를 병합합니다 |
| [4. Plan과 Autopilot으로 필터링 구축][ex4] | 구현 | 계획을 검토하고 Autopilot을 승인한 후 테스트하고 체크포인트를 저장합니다 |
| [5. quality-checks 스킬 만들기 및 사용][ex5] | 스킬 | 셸 스크립트를 포함한 검사를 생성하고 검토하고 실행합니다 |
| [6. Playwright MCP로 기능 검증][ex6] | 브라우저 도구 | 실제 브라우저에서 필터링 동작을 관찰합니다 |
| [7. QA 에이전트 만들기 및 사용][ex7] | 에이전트 | 요구 사항과 커버리지를 평가하고 최종 근거를 수집합니다 |
| [8. 기능 PR 생성 및 병합][ex8] | 제공 | 필터링과 재사용 가능한 사용자 지정을 PR 3에서 함께 검토합니다 |
| [9. 슬래시 명령과 CLI 옵션 살펴보기][ex9] | CLI 조작 | 컨텍스트, 모델, 세션, 공유 대상을 확인합니다 |
| [10. 마무리 및 다음 단계][ex10] | 요약 | 공통 자산과 세 번의 PR 마일스톤을 검토합니다 |

## 브랜치와 끌어오기 요청

별점, 지침과 작은 실증, 필터링과 quality-checks 스킬·QA 프로필·관련 테스트를 담은 세 개의 끌어오기 요청을 병합합니다. 처음 두 PR은 각각 병합한 후 업데이트된 `main`에서 다음 마일스톤을 시작합니다.

연습 4~8은 하나의 기능 브랜치와 체크아웃을 공유합니다. 진행 중 체크포인트 커밋을 저장합니다. 스킬 생성, MCP 설정, QA 선택 시 새 기능 브랜치를 만들지 않습니다. 연습 9에서는 다른 기능이나 PR을 시작하지 않고 조작 방법을 살펴봅니다.

## 사전 준비

이 워크숍에 참여하기 전에 다음 사항을 준비합니다.

- [ ] **Copilot Student, Pro, Pro+, Business 또는 Enterprise** 플랜이 활성화된 GitHub 계정
- [ ] 터미널/명령줄 사용에 대한 기본 이해
- [ ] 설치 및 구성된 Git

> [!TIP]
> 유료 플랜이 없나요? 인증된 학생은 [GitHub Education][callout-student-plan-education]을 통해 GitHub Copilot을 무료로 사용할 수 있습니다. **Copilot Student** 플랜에는 이 워크숍에서 사용하는 agent, MCP, code review, Copilot CLI 기능이 모두 포함되어 있으므로 모든 harness를 완료할 수 있습니다.

[callout-student-plan-education]: https://github.com/education/students

> [!NOTE]
> Copilot Business 또는 Copilot Enterprise를 사용하는 경우, 관리자가 Copilot CLI 사용을 활성화했는지 확인합니다.

## 시작하기

[**연습 0: 사전 준비부터 시작하기 →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
