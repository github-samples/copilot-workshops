---
slug: ko-kr/app
title: "GitHub Copilot app"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[**GitHub Copilot app**](https://docs.github.com/copilot/concepts/agents/github-copilot-app)은 Copilot CLI를 기반으로 구축된 데스크톱 애플리케이션으로, 에이전트 기반 개발을 하나의 집중된 워크스페이스에서 수행할 수 있게 해 줍니다. 병렬 에이전트 세션, 전환 가능한 세션 모드, 공유 캔버스, GitHub 이슈 및 끌어오기 요청 기본 관리 기능을 제공합니다. 여기에는 끌어오기 요청의 리베이스, 검토 피드백, CI 수정, 병합 과정을 관리하는 **Agent Merge**도 포함됩니다.

설정 레슨 0~1에서 프로젝트와 App 워크스페이스를 준비합니다. 아홉 개의 핵심 모듈인 레슨 2~10은 별점을 추가하는 작은 변경과 실제 코드로 효과를 확인하는 문서화 규칙으로 시작합니다. 그런 다음 필터링을 계획하고 구축하며, 셸 스크립트를 포함하는 quality-checks 스킬을 만들고 실행하고, Playwright MCP로 기능을 관찰하며, 요구 사항과 커버리지를 평가할 QA 사용자 지정 에이전트를 만듭니다. 전체 기능 PR을 검토하고 Agent Merge를 승인한 다음 공유 이슈 분류 캔버스를 만들고 병합합니다.

워크숍에는 네 번의 PR 마일스톤이 있습니다. 별점, 지침과 시연, 필터링과 스킬·QA 프로필·테스트, 마지막으로 캔버스입니다. 각 마일스톤은 업데이트된 `main`에서 시작하며, 모듈별이 아니라 PR별로 하나의 브랜치를 사용합니다. 레슨 4~8은 동일한 필터링 세션, 워크트리, 브랜치를 유지합니다. 캔버스를 다시 열 때는 이슈 컨텍스트만 추가하고 다른 기능이나 다섯 번째 PR을 시작하지 않습니다. 자동화는 추가 실습이 아니라 다음 단계의 링크로 소개합니다.

## 레슨

| 레슨 | 주제 | 설명 |
|--------|-------|-------------|
| [0. 필수 조건][ex0] | 설정 | Node.js를 설치하고 Tailspin Toys 프로젝트의 복사본 만들기 |
| [1. Copilot app 설치][ex1] | 설정 | 앱을 설치하고 프로젝트를 연결한 다음 워크스페이스 살펴보기 |
| [2. 별점 추가로 작은 성과 얻기][ex2] | 첫 번째 변경 | 기존 별점과 null 대체 표시를 추가하고 PR 1 병합하기 |
| [3. 사용자 지정 지침으로 Copilot 안내][ex3] | 컨텍스트 | 문서화 표준과 실제 시연을 추가하고 PR 2 병합하기 |
| [4. Plan과 Autopilot으로 필터링 구축][ex4] | 구현 | 계획을 승인하고 필터링을 구현·검사한 다음 체크포인트 저장하기 |
| [5. quality-checks 스킬 만들기 및 사용][ex5] | 반복 가능한 검사 | 함께 제공할 셸 스크립트를 만들고 검토하고 실행하기 |
| [6. Playwright MCP로 기능 검증][ex6] | 브라우저 관찰 | Customize에서 MCP를 구성하고 필터링 동작 살펴보기 |
| [7. QA 에이전트 만들기 및 사용][ex7] | 요구 사항과 커버리지 | 전문가 프로필을 선택하고 최종 검증 근거 수집하기 |
| [8. 기능 PR 만들기 및 병합][ex8] | 검토와 병합 | 필터링, 스킬, QA 프로필, 테스트를 검토한 다음 PR 3의 Agent Merge 승인하기 |
| [9. 이슈 분류 캔버스 만들기][ex9] | 협업 | 리포지토리에 저장하는 캔버스를 PR 4로 공유하고 이슈 컨텍스트 추가하기 |
| [10. 마무리 및 다음 단계][ex10] | 요약 | 워크플로, 산출물, 추가 리소스 돌아보기 |

## 필수 조건

워크숍에 참여하기 전에 다음 항목을 준비했는지 확인합니다.

- [ ] 활성 **Copilot Student, Pro, Pro+, Business, or Enterprise** 플랜이 있는 GitHub 계정
- [ ] **macOS, Linux, or Windows**를 실행하는 컴퓨터
- [ ] 컴퓨터에 [Git 설치][install-git]

> [!TIP]
> 유료 플랜이 없습니까? 인증된 학생은 [GitHub Education][callout-student-plan-education]을 통해 GitHub Copilot을 무료로 사용할 수 있습니다. **Copilot Student** 플랜에는 이 워크숍에서 사용하는 에이전트, MCP, 코드 검토, Copilot CLI 기능이 포함되어 있으므로 모든 실습 과정을 완료할 수 있습니다.

> [!NOTE]
> Copilot app은 codespace가 아니라 사용자의 컴퓨터에서 실행되므로, [레슨 0][ex0]에서는 앱을 설치하기 전에 Node.js를 설치하고 프로젝트 복사본을 만드는 방법을 안내합니다.

> [!NOTE]
> Copilot Business 또는 Copilot Enterprise를 사용하는 경우 앱을 사용하려면 관리자가 **Copilot CLI** 정책을 활성화해야 합니다.

## 시작하기

[**레슨 0: 필수 조건부터 시작 →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students