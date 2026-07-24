---
slug: ko-kr/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[**GitHub Copilot CLI**](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)는 터미널에서 GitHub Copilot을 에이전트형 코딩 도우미로 사용할 수 있게 해줍니다. 코드베이스를 탐색하고, 코드를 생성하고, 명령을 실행하고, 외부 도구에 연결하는 작업을 모두 명령줄에서 처리하므로 그래픽 편집기로 전환하지 않고도 작업 흐름을 유지할 수 있습니다.

이 연습 전체에서 Copilot CLI를 설치하고 인증한 다음, 커스텀 지침으로 프로젝트 컨텍스트를 제공한 뒤 plan mode를 사용해 의도적으로 기능을 생성합니다. 이어서 Playwright MCP server를 연결해 실제 브라우저에서 해당 기능을 테스트하고, 재사용 가능한 agent skills와 custom agents로 Copilot을 확장합니다. 마지막으로 slash commands로 컨텍스트, 모델, 공유를 관리하는 방법을 살펴보고, 완성한 내용을 검토합니다.

## 연습

| 연습 | 주제 | 설명 |
|----------|-------|-------------|
| [0. 사전 준비][ex0] | 설정 | 리포지토리(Repository)와 코드스페이스(Codespace)를 만듭니다 |
| [1. Copilot CLI 설치][ex1] | 설치 | Copilot CLI를 설치하고 인증합니다 |
| [2. 커스텀 지침][ex2] | 컨텍스트 | 지침을 추가하고 Copilot CLI가 이를 따르는 모습을 확인합니다 |
| [3. 코드 생성][ex3] | 코드 생성 | plan mode를 사용해 기능을 생성합니다 |
| [4. Playwright MCP로 테스트][ex4] | 외부 도구 | Playwright MCP server를 추가하고 브라우저에서 기능을 테스트합니다 |
| [5. 에이전트 스킬][ex5] | 스킬 | 특화된 스킬로 Copilot을 강화합니다 |
| [6. 커스텀 에이전트][ex6] | 에이전트 | 커스텀 에이전트를 검토하고 사용합니다 |
| [7. 슬래시 명령][ex7] | CLI 기능 | 컨텍스트, 모델, 공유, 그리고 선택적으로 cloud agent 위임을 살펴봅니다 |
| [8. 검토][ex8] | 요약 | 핵심 개념과 다음 단계를 검토합니다 |

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
[ex2]: 2-custom-instructions/
[ex3]: 3-generating-code/
[ex4]: 4-mcp/
[ex5]: 5-agent-skills/
[ex6]: 6-custom-agents/
[ex7]: 7-slash-commands/
[ex8]: 8-review/
