---
slug: ko-kr/cli/8-foundry-agent
title: "선택 사항: Foundry 통합하기"
description: "모델을 준비하고, 카탈로그에 근거한 에이전트를 빌드 및 배포한 뒤 Tailspin Toys에 연결하는 3개 모듈 시리즈입니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

이 선택 사항 시리즈에서는 GitHub Copilot CLI와 Microsoft Foundry Skill을 사용해 Tailspin Toys 카탈로그를 대화형 도우미로 만듭니다. 3개 모듈을 통해 프로젝트와 모델 설정부터 호스트된 에이전트(Hosted agent)와 실제로 작동하는 웹사이트 통합까지 진행합니다.

이 시리즈에서는 다음을 수행합니다.

- Azure 환경을 준비하고 카탈로그를 기준으로 모델을 테스트합니다.
- 호스트된 Backer Concierge 에이전트를 스캐폴드(Scaffold)하고 테스트 및 배포합니다.
- 로컬 서버 측 프록시(Proxy)와 채팅 위젯을 통해 에이전트를 웹사이트에 연결합니다.

## 시나리오

Tailspin Toys의 후원자는 카테고리와 퍼블리셔별로 게임을 탐색할 수 있지만, 이러한 필터만으로는 모든 후원자가 다음에 즐길 게임을 찾기 어렵습니다. *Git 말장난을 좋아하는 사람에게는 어떤 게임이 어울릴까요?* 같은 질문을 하는 후원자도 있습니다. 이런 질문에는 드롭다운으로 답할 수 없습니다.

Tailspin Toys는 후원자가 대화를 통해 게임을 찾도록 돕는 **Backer Concierge**를 만들려고 합니다. Tailspin 카탈로그에 있는 게임을 추천하고, 취향이 모호할 때는 이를 구체화하는 짧은 질문을 하며, 후속 질문을 받으면 앞서 추천한 내용을 기억해야 합니다.

후원자에게는 믿을 수 있는 답변이 필요합니다. 컨시어지(Concierge)는 카탈로그에 있는 정보만 사용하고, 확인할 수 없는 세부 정보는 없다고 명확히 알려야 합니다. 게임, 퍼블리셔, 평점, 총 모금액, 후원자 수, 가격, 플레이어 수, 플레이 시간, 출시일을 지어내서는 안 됩니다.

## 다음 단계 선택하기

각 모듈은 동일한 Tailspin Toys 리포지토리, 브랜치, Foundry 프로젝트에서 이전 모듈의 결과를 이어서 사용합니다. 각 모듈은 작동하는 결과물을 확인하는 단계로 끝납니다.

| 모듈 | 수행할 작업 | 완료 시점의 결과물 |
| --- | --- | --- |
| [1. 프로젝트와 모델 준비하기][project-model] | 도구를 설정하고, 카탈로그를 내보내고, 모델을 선택하고 테스트합니다 | 카탈로그 질문에 올바르게 답하는 배포된 모델 |
| [2. 에이전트 빌드 및 배포하기][build-deploy] | 에이전트를 스캐폴드하고, 동작을 테스트한 뒤 Foundry에 배포합니다 | 정상적으로 작동하는 호스트된 Backer Concierge |
| [3. 에이전트를 웹사이트에 연결하기][connect-site] | 로컬 프록시와 채팅 위젯을 빌드한 뒤 전체 흐름을 테스트합니다 | 로컬 웹사이트에서 사용할 수 있는 컨시어지 |

> [!IMPORTANT]
> Microsoft Foundry 호스트된 에이전트는 공개 미리 보기 상태입니다.
>
> 이 시리즈에서는 모델 배포와 호스트된 에이전트를 비롯해 요금이 부과되는 Azure 리소스를 만듭니다. 리소스를 만들기 전에 선택한 구독, 지역, 할당량, 예상 비용을 검토해야 합니다. 첫 번째 또는 두 번째 모듈을 마친 뒤 중단하더라도 [정리 지침][cleanup]을 따라야 합니다.

1. 선택 사항 시리즈를 시작하려면 [프로젝트와 모델 준비하기][project-model]로 이동합니다. 설정 지침도 해당 모듈에 포함되어 있습니다.
2. 핵심 워크숍을 마무리하고 싶다면 [검토 및 다음 단계][review]로 이동합니다.

## 리소스 정리하기

어느 모듈에서든 실험을 마쳤다면 원치 않는 비용이 발생하지 않도록 Azure 리소스를 제거합니다. 정리하면 이후 모듈에 필요한 리소스도 제거되므로, 나중에 계속하려면 다시 만들어야 합니다.

> [!CAUTION]
> `rg-tailspin-toys`가 이 연습 전용이고 유지해야 할 리소스가 없는 경우에만 삭제합니다. 공유 리소스 그룹을 삭제하면 관련 없는 리소스도 함께 제거됩니다.

1. 실행한 로컬 에이전트, Function 또는 Astro 개발 서버가 있다면 해당 터미널에서 <kbd>Ctrl</kbd>+<kbd>C</kbd>를 눌러 중지합니다.
2. Copilot CLI를 종료합니다. 모듈 2에서 에이전트를 스캐폴드했다면 동일한 `azd` 환경을 사용해 Tailspin Toys 리포지토리 루트에서 다음을 실행합니다.

    ```bash
    azd down --purge
    ```

3. `az account show`로 선택한 구독을 확인합니다. 해당 구독의 `rg-tailspin-toys`를 살펴보고 남아 있는 모든 리소스가 이 연습에 속하는지 확인합니다. 모듈 1을 마친 뒤 중단했다면 `azd` 서비스를 스캐폴드하지 않았더라도 Foundry 프로젝트와 모델을 정리해야 합니다.
4. 워크숍 전용 리소스 그룹이 아직 존재하고 제거하려는 리소스만 포함되어 있다면 다음을 실행합니다.

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. Azure Portal에서 리소스 그룹 삭제가 완료되었는지 확인합니다. `--no-wait` 명령은 삭제가 완료되기 전에 반환됩니다.

## 리소스

- [Azure Skills Plugin][azure-skills]
- [코딩 에이전트에서 Microsoft Foundry Skill 사용하기][foundry-skill]
- [Microsoft Foundry Skill로 첫 호스트된 에이전트 배포하기][hosted-agent-quickstart]
- [호스트된 에이전트 권한][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #리소스-정리하기
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
