---
title: "연습 8 - 검토 및 다음 단계"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

지난 여러 연습에서 다음을 포함해 GitHub Copilot CLI의 가장 일반적인 사용 사례를 살펴보았습니다.

- GitHub 및 다른 MCP server와 상호 작용하기
- 지침 파일을 사용해 코드 생성을 안내하기
- 스킬을 구현해 Copilot CLI 도구 상자에 새 도구를 추가하기
- 고급 작업과 더 복잡한 작업을 위해 커스텀 agent 호출하기
- Slash commands를 사용해 세션을 관리하고, 선택적으로 `/delegate`를 통해 cloud agent로 다시 연결하기

이제 몇 가지 slash commands, 모범 사례, 다음 단계를 정리해 보겠습니다.

## 슬래시 명령

Copilot CLI에는 이를 제어하거나 내부에서 무슨 일이 일어나고 있는지 확인할 수 있는 다양한 slash commands가 있습니다. 이미 현재 컨텍스트를 지우고 새 채팅을 시작하는 `/clear`, MCP server를 검사하고 관리하는 `/mcp`를 사용해 보았습니다. 추가로 유용할 수 있는 명령은 다음과 같습니다.

| 명령 | 설명 |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir`         | Copilot의 신뢰 목록에 디렉터리를 추가합니다 |
| `/clear`, `/new`   | 대화 기록을 지우고 새로 시작합니다 |
| `/compact`         | 컨텍스트 창 사용량을 줄이기 위해 대화 기록을 요약합니다 |
| `/context`         | 컨텍스트 창 token 사용량과 시각화를 보여 줍니다 |
| `/diff`            | 현재 디렉터리에서 이루어진 변경 사항을 검토합니다 |
| `/model`           | 사용할 AI 모델을 선택합니다(Claude Sonnet, GPT-5 등) |
| `/plan <prompt>`   | 코딩 전에 구현 계획을 만듭니다 |
| `/review <prompt>` | 변경 사항을 분석하도록 코드 리뷰 agent를 실행합니다 |
| `/delegate`        | 비동기 처리를 위해 작업을 Copilot cloud agent에 위임합니다 |
| `/session`         | 세션 정보와 작업 공간 요약을 보여 줍니다 |
| `/share`           | 세션을 markdown 파일 또는 GitHub gist로 공유합니다 |
| `/skills`          | 향상된 기능을 위한 스킬을 관리합니다 |
| `/usage`           | 세션 사용량 지표와 통계를 표시합니다 |

> [!TIP]
> `/help`를 사용하면 전체 명령 목록과 keyboard shortcuts를 확인할 수 있습니다.

## 모범 사례

어떤 AI 도구를 사용하든, 그 결과물의 품질은 기반 인프라에 크게 좌우됩니다. 강력한 지침 파일, 커스텀 에이전트, 에이전트 스킬은 모두 중요한 역할을 하며, 이 워크숍에서 각각을 살펴보았습니다. [Awesome-copilot][awesome-copilot]은 템플릿을 찾기에 좋은 자료이며, Copilot 자체도 시작점을 마련할 수 있도록 이러한 요소를 스캐폴드해 줄 수 있습니다.

인프라만큼이나 컨텍스트도 중요합니다. *무엇을* 만들고 싶은지, *왜* 필요한지, *어떻게* 만들고 싶은지를 명확하게 설명하면 결과가 크게 달라집니다. Copilot에 도움이 될 만한 정보라면 반드시 전달합니다.

## 다음 단계

도구 사용 능력을 향상하는 가장 좋은 방법은 계속 사용하는 것입니다. 운영 코드에도, 취미 프로젝트에도, 오랫동안 마음속에 있었지만 아직 만들지 못한 작은 앱에도 사용해 봅니다. 학습한 내용을 팀과 공유하고, 팀으로부터도 배웁니다. 그리고 늘 그렇듯 문서를 계속 탐색합니다.

GitHub Copilot 생태계를 더 살펴보고 싶다면 [VS Code harness](../../vscode/) 또는 [Cloud agent harness](../../cloud/)를 확인합니다.

## 리소스

- [Copilot CLI 소개][about-copilot-cli]
- [Copilot CLI 사용하기][using-copilot-cli]
- [Awesome Copilot 리포지토리][awesome-copilot]
- [커스텀 지침 가이드][repo-instructions]
- [에이전트 스킬 문서][agent-skills]
- [커스텀 에이전트 문서][custom-agents]
- [MCP 사양][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
