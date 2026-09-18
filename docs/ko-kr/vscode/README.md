---
slug: ko-kr/vscode
title: "VS Code"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

VS Code의 [**GitHub Copilot Chat**](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)은 이미 사용 중인 코드 편집기에 GitHub Copilot을 통합합니다. Visual Studio Code와 GitHub Codespaces에서 Copilot Chat의 에이전트 모드(Agent mode)를 사용하고, MCP를 통해 외부 도구를 연결하며, 사용자 지정 에이전트를 활용합니다. IDE를 벗어나지 않고 이 모든 작업을 수행하며, Copilot은 파일, 터미널, 문제를 모두 확인할 수 있습니다.

먼저 사용자 지정 지침을 추가하고 Copilot이 이를 따르는지 살펴봅니다. 그런 다음 에이전트 모드로 UI, 데이터 계층, 테스트에 걸쳐 필터링 기능을 만듭니다. 이어서 Playwright MCP 서버를 연결하고 Copilot이 브라우저를 조작하여 기능을 테스트하도록 한 뒤 풀 리퀘스트(Pull request)를 엽니다. 마지막으로 접근성 작업을 위한 사용자 지정 에이전트를 검토하고 사용한 다음, Copilot의 변경 사항을 모니터링하고 방향을 조정하며 반복해서 개선합니다. 모든 작업은 편집기 안에서 진행합니다.

## 실습

| 실습 | 주제 | 설명 |
|----------|-------|-------------|
| [0. 사전 요구 사항][ex0] | 설정 | 리포지토리와 codespace 만들기 |
| [1. 사용자 지정 지침][ex1] | 컨텍스트 | VS Code에서 사용자 지정 지침 추가 및 검증 |
| [2. 에이전트 모드][ex2] | 코드 생성 | 에이전트 모드로 필터링 기능 만들기 |
| [3. Playwright와 MCP][ex3] | 외부 도구 | Playwright MCP 서버로 브라우저에서 기능 테스트 |
| [4. 사용자 지정 에이전트][ex4] | 특화된 에이전트 | 사용자 지정 에이전트 검토 및 사용 |
| [5. 에이전트 관리][ex5] | 모니터링 | 에이전트 세션 모니터링 및 방향 조정 |
| [6. 반복 개선][ex6] | 검토 | 로컬에서 Copilot의 작업을 검토하고 다음 단계 선택 |
| [선택 사항: Foundry 통합][foundry-toolkit] | AI 에이전트 | VS Code와 Foundry Toolkit으로 세 모듈에 걸쳐 모델을 준비하고 에이전트를 배포한 뒤 사이트에 연결 |

## 사전 요구 사항

워크숍에 참여하기 전에 다음을 준비합니다.

- [ ] **Copilot Student, Pro, Pro+, Business 또는 Enterprise** 요금제를 사용 중인 GitHub 계정
- [ ] GitHub Codespaces 접근 권한

> [!TIP]
> 유료 요금제가 없어도 괜찮습니다. 인증된 학생은 [GitHub Education][callout-student-plan-education]을 통해 GitHub Copilot을 무료로 사용할 수 있습니다. **Copilot Student** 요금제에는 이 워크숍에서 사용하는 에이전트, MCP, 코드 리뷰, Copilot CLI 기능이 포함되어 있으므로 모든 과정을 완료할 수 있습니다.

[callout-student-plan-education]: https://github.com/education/students
## 시작하기

[**실습 0: 사전 요구 사항부터 시작 →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-custom-instructions/
[ex2]: 2-agent-mode/
[ex3]: 3-mcp/
[ex4]: 4-custom-agents/
[ex5]: 5-managing-agents/
[ex6]: 6-iterating/
[foundry-toolkit]: 7-foundry-toolkit/
