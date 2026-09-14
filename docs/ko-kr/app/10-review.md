---
title: "Lesson 10 - 마무리 및 다음 단계"
description: "App의 아홉 핵심 모듈, 네 PR 마일스톤, 재사용 가능한 품질 워크플로를 돌아보고 추가 리소스를 살펴봅니다."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

지난 여러 레슨에서 GitHub Copilot app으로 아이디어를 기능으로 만들고 병합하기까지 다음 작업을 수행했습니다.

- 리포지토리를 연결하고 앱의 워크스페이스와 미리 생성된 백로그를 살펴봤습니다.
- 직접 작업과 이슈에서 세션을 시작하고 Plan 및 Autopilot 모드로 에이전트의 작업 방식을 제어했습니다.
- 사용자 지정 지침으로 에이전트를 안내한 다음, 셸 스크립트가 포함된 재사용 가능한 스킬을 만들도록 요청하고, 스크립트를 검토한 후 린트, 단위 테스트, 엔드투엔드 테스트, 타입 검사를 실행했습니다.
- Playwright MCP 서버를 사용하여 실제 브라우저에서 작업을 테스트했습니다.
- 요구 사항, 커버리지, 스킬 스크립트 결과, 브라우저 근거를 평가할 QA 사용자 지정 에이전트를 만들고 선택했습니다.
- 공유 캔버스에서 에이전트와 협업했습니다.
- 초기 PR을 직접 명시적으로 병합한 다음 기능과 캔버스 PR 워크플로에서 **Agent Merge**를 승인했습니다.

설정 레슨 0~1에 이어 아홉 개의 핵심 모듈인 레슨 2~10을 진행했습니다. 산출물과 다음 단계를 돌아봅니다. 이 마무리에서는 다른 실습 작업을 시작하지 않습니다.

## 제공한 결과

워크숍에는 네 번의 PR 마일스톤이 있으며, 각각 업데이트된 `main`에서 시작한 자체 브랜치를 사용합니다.

1. **별점:** 게임 카드에 기존 `starRating`과 명시적인 미평가 상태를 표시합니다.
2. **지침과 시연:** 문서화 규칙을 추가하고 작은 실제 코드 변경에 미친 영향을 검증합니다.
3. **필터링과 품질 워크플로:** 이슈를 구현하고 셸 스크립트를 포함하는 `quality-checks` 스킬과 QA 프로필을 만들며 관련 테스트를 포함합니다.
4. **리포지토리에 저장한 이슈 분류 캔버스:** 다른 기능을 자동으로 구현하지 않고 이슈 컨텍스트를 추가하는 보드를 공유합니다.

레슨 4~8은 동일한 필터링 세션, 워크트리, 브랜치를 사용했습니다. 체크포인트 커밋으로 PR 3 안에서 진행 상황을 보존했으며 스킬, MCP 구성, QA에 별도의 기능 브랜치가 필요하지 않았습니다. 이후 각 마일스톤은 앞선 PR이 병합되고 새 세션 브랜치가 `origin/main`에서 업데이트된 후에만 시작했습니다.

## 서로 다른 검증 방식

초기 기능은 기존 npm 검사를 사용했습니다. 필터링에는 직접 수행하는 브라우저 검토를 추가했습니다. 스킬은 함께 제공되는 스크립트로 네 가지 검사를 반복 가능하게 만들었고, MCP는 에이전트의 직접 브라우저 관찰을 추가했으며, QA는 요구 사항과 커버리지를 최종 검증과 결합했습니다. PR에서는 제출한 리비전에 적용될 때만 QA 근거를 재사용했습니다.

추가한 테스트는 실제 커버리지 부족을 해결해야 합니다. 새 테스트가 필요 없는 QA 실행도 올바를 수 있습니다. 누락된 도구, 건너뛴 검사, 실패는 드러내야 할 차단 요인이지 통과가 아닙니다. 병합 승인 전에 코드와 근거를 검토하고 변경 후 관련 근거를 갱신합니다.

## 모범 사례

AI 도구를 사용할 때는 도구를 둘러싼 인프라가 결과의 품질을 좌우합니다. 이 워크숍에서는 지침, 스킬, QA 프로필을 만들었습니다. 이를 검토하고 세션 간에 재사용합니다. 사용자 지정 에이전트는 전문가 역할과 지침을 정의하며 사용 가능한 도구는 구성과 하네스 권한에 따라 결정됩니다. 스킬은 필요할 때 불러오는 재사용 가능한 작업 지침, 실행 가능한 스크립트, 보조 리소스를 묶어 제공합니다. 사용자 지정 에이전트도 스킬과 함께 제공되는 스크립트를 비롯한 스크립트를 실행할 수 있습니다. 설득력 있는 설명에 의존하지 말고 실제 스크립트 실행과 사용자 지정 에이전트 선택을 확인합니다.

작업에 맞는 **모드와 모델**을 선택합니다. 구축 전에 접근 방식을 검토하려면 **Plan**을 사용하고, 범위가 명확한 변경에서 계속 참여하려면 **Interactive**를 사용하며, 범위가 명확하고 격리된 작업에만 **Autopilot**을 사용합니다. 일상적인 편집에는 빠른 모델을 선택하고 복잡한 작업에는 추론 능력이 더 높은 모델을 선택합니다.

컨텍스트는 인프라만큼 중요합니다. 만들려는 *항목*, 그 *이유*, 원하는 *방식*을 명확하게 설명하면 출력이 크게 달라집니다. 빠른 채팅은 아이디어를 전체 세션에 적용하기 전에 범위를 정하기에 적합합니다.

## 더 살펴볼 내용

핵심 워크플로를 모두 살펴봤습니다. 다음 기능도 확인해 볼 만합니다.

- 전체 세션이 필요 없는 빠른 일회성 질문을 위한 **Quick chats**
- 최근 작업 요약 같은 반복 또는 요청 시 작업을 위한 [**Automations**][using-automations]. 도입 전에 일정, 권한, 범위를 검토합니다. 자동화 만들기는 다음 단계이며 이 워크숍에 포함되지 않습니다.
- 구축 전에 문제를 함께 검토하고 유용한 피드백을 받기 위한 **Rubber duck**
- 반복 가능한 전문 작업을 위해 역할, 도구, 지침을 패키지하는 [**Custom agents**][custom-agents]
- 세션에서 일어난 일을 서술형으로 생성하는 [`/chronicle`][chronicle]
- Ollama, Foundry Local, LM Studio를 통한 로컬 모델을 포함하여 자체 공급자의 모델을 사용하는 [Bring your own key (BYOK)][byok]
- GitHub에서 호스팅하는 격리된 환경에서 세션을 실행하는 [Cloud sandboxes][sandboxes]
- 리포지토리, 세션, 프롬프트에서 바로 앱을 여는 [Deep links][deep-links]

## 다음 단계

어떤 도구든 더 능숙하게 사용하려면 계속 사용해야 합니다. 프로덕션 코드, 취미 프로젝트, 오랫동안 생각만 하고 만들지 못했던 작은 앱에 사용해 봅니다. 배운 내용을 팀과 공유하고 팀의 경험에서도 배웁니다. 언제나 그렇듯 문서를 살펴봅니다.

GitHub Copilot 생태계를 더 살펴보려면 [VS Code 실습 과정][vscode-harness], [Copilot CLI 실습 과정][cli-harness], [Cloud agent 실습 과정][cloud-harness]을 확인합니다.

## 리소스

- [GitHub Copilot app 정보][about-copilot-app]
- [GitHub Copilot app 시작하기][getting-started]
- [GitHub Copilot app 사용자 지정][customize]
- [자동화 사용][using-automations]
- [캔버스 확장 사용][canvas-docs]
- [클라우드 및 로컬 샌드박스 정보][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links