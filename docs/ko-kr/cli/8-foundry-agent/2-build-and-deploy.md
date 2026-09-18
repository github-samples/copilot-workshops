---
title: "모듈 2 - 에이전트 빌드 및 배포하기"
description: "GitHub Copilot CLI와 Microsoft Foundry Skill을 사용해 Backer Concierge를 스캐폴드하고 테스트 및 배포합니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

[모듈 1][previous-lesson]에서는 카탈로그를 준비하고 배포된 모델을 테스트했습니다. [선택 사항 컨시어지 시리즈][overview]의 두 번째 모듈에서는 이를 바탕으로 호스트된 에이전트(Hosted agent)를 만듭니다.

이 모듈에서는 다음을 수행합니다.

- 배포 가능한 자체 카탈로그 사본을 포함하도록 에이전트를 스캐폴드(Scaffold)합니다.
- 로컬에서 그라운딩(Grounding)과 대화 연속성을 테스트합니다.
- 에이전트를 배포하고 원격으로 호출합니다.

## 시나리오

Tailspin Toys에는 모델의 일회성 답변 이상이 필요합니다. 후원자는 컨시어지(Concierge)가 방금 추천한 게임을 기억하고 해당 게임에 대한 후속 질문에 답하기를 기대합니다. 또한 팀은 컨시어지를 개발자 컴퓨터에서 호스트된 서비스로 옮긴 뒤에도 답변의 신뢰성을 유지해야 합니다.

## 기존 프로젝트에서 계속하기

이 모듈은 모듈 1에서 정상적으로 작동한 모델을 기반으로 진행합니다. Azure 리소스를 새로 만들지 않고 동일한 프로젝트와 배포를 유지합니다.

1. Tailspin Toys 리포지토리의 `foundry-agent-cli` 브랜치와 모듈 1에서 사용한 Copilot CLI 세션으로 돌아갑니다.
2. `db/catalog.json`이 있는지, 모델 테스트에 사용한 Foundry 프로젝트, 선택한 모델 배포, Azure 로그인이 그대로 유지되어 있는지 확인합니다. 설정을 완료하지 않았다면 먼저 [프로젝트와 모델 준비하기][previous-lesson]를 마칩니다.

> [!IMPORTANT]
> 호스트된 에이전트는 공개 미리 보기 상태이며 요금이 부과되는 Azure 리소스를 만듭니다. 이 모듈을 마친 뒤 중단한다면 [정리 지침][cleanup]을 따라야 합니다.

## Backer Concierge 에이전트 스캐폴드하기

이제 Microsoft Foundry Skill에 기존 Tailspin Toys 리포지토리 안에 호스트된 에이전트를 스캐폴드하도록 요청한 뒤, 실행 전에 패키징과 구성을 살펴봅니다.

1. Copilot CLI에 다음 프롬프트를 입력합니다.

    ```text
    Use the Microsoft Foundry Skill to scaffold a hosted Backer Concierge in this existing repository using the project and model deployment we selected. Start from the Python 3.13 Basic hosted-agent sample, use Microsoft Agent Framework with the Responses API and code deployment, and keep the agent in agent/backer-concierge. Keep one azure.yaml at the repository root with a service using host: azure.ai.agent.

    Ground every answer in db/catalog.json. Never invent games, publishers, ratings, funding totals, backer counts, pledge tiers, prices, player counts, play times, or release dates. Ask one short clarifying question when a request is vague and preserve conversation context. Ensure the catalog is copied into the deployable service during preparation so the deployed agent never depends on a file outside its service directory. Add focused tests for catalog loading and grounding behavior.

    Scaffold and test locally, but do not deploy the hosted agent yet. Stop and ask me to authenticate if needed.
    ```

2. 세션을 살펴보며 Foundry 프로젝트, 모델 배포, 에이전트 이름, 환경에 대한 질문에 응답합니다.
3. Copilot이 작업을 마치면 변경 사항을 살펴봅니다.

    ```text
    /diff
    ```

    다음을 확인합니다.

    - `azure.yaml`에 `host: azure.ai.agent`가 설정된 서비스가 있습니다.
    - 서비스 경로가 `agent/backer-concierge`를 가리킵니다.
    - 배포되는 서비스 패키지에 자체적으로 생성한 카탈로그 사본이 포함되어 있습니다.
    - 카탈로그 두 개를 수동으로 편집하며 유지하는 대신 하나의 스크립트나 빌드 단계가 `db/catalog.json`에서 해당 사본을 갱신합니다.
    - 에이전트가 선택한 모델 배포와 Responses API를 사용합니다.
    - 지침에서 카탈로그에 없는 사실을 명시적으로 거부합니다.
    - 자격 증명, 액세스 토큰, `.env` 파일, `.azure` 환경 파일이 커밋 대상으로 스테이징되어 있지 않습니다.

    스캐폴딩 후 다음 구조를 기준으로 확인합니다.

    ```text
    tailspin-toys/
    ├── azure.yaml
    ├── agent/
    │   └── backer-concierge/
    │       ├── catalog.json
    │       └── requirements.txt
    ├── db/
    │   └── catalog.json
    └── src/
    ```

> [!IMPORTANT]
> `azd deploy`는 호스트된 에이전트의 서비스 디렉터리를 패키징합니다. `agent/backer-concierge`에서 리포지토리 수준의 `db/catalog.json`을 런타임에 참조하면 로컬에서는 작동하더라도 배포 후에는 실패할 수 있습니다. 생성된 사본은 배포 전에 `agent/backer-concierge/` 디렉터리에 있어야 합니다.

4. 서비스를 시작하기 전에 Copilot에 관련 기능에 집중한 테스트를 실행하고 생성된 구성을 살펴보도록 요청합니다.

    ```text
    Run the focused Backer Concierge tests. Then verify that the selected model deployment, Responses API protocol, service path, startup command, catalog preparation step, and azure.ai.agent host configuration are consistent. Fix only problems in this hosted-agent project and rerun the failed checks.
    ```

    해당 테스트를 통과하기 전에는 다음으로 진행하지 않습니다.

    ![에이전트 스캐폴딩 검증하기](../../../_images/cli-8-verify-generated-agent.png)

## 에이전트 로컬 테스트하기

이제 로컬 Responses API를 통해 에이전트의 그라운딩과 대화 동작을 확인합니다. 로컬 에이전트 서비스는 실행 중 터미널을 점유하므로, 현재 터미널에는 Copilot CLI를 열어 둔 채 두 번째 터미널에서 에이전트를 시작합니다.

1. <kbd>Ctrl</kbd>+<kbd>\`</kbd>를 눌러 다른 터미널을 엽니다.
2. Tailspin Toys 리포지토리 루트에서 다음을 실행합니다.

    ```bash
    azd ai agent run
    ```

    첫 로컬 실행에서는 Python 환경을 만들고, 의존성을 설치하고, 호스트된 에이전트를 시작합니다. 이 터미널을 실행 상태로 둡니다.

3. 첫 번째 터미널의 Copilot CLI로 돌아가 다음을 입력합니다.

    ```text
    Test the running Backer Concierge through its Responses API. Run each acceptance prompt below, preserve the response ID for the two-turn conversation test, and compare every response with the expected behavior. Show a concise pass or fail table and the evidence for any failure. Do not change code yet.

    1. "I love puzzle games about tracking down bugs. What should I back?" Expected: only real catalog titles with correct details.
    2. "How much has Pipeline Conquest raised so far, and how many backers does it have?" Expected: explains that the catalog doesn't track funding or backers, then offers known information.
    3. "I need something for four players, about an hour long." Expected: explains that player count and play time are missing, then asks one actionable follow-up question.
    4. "Do you have Wingspan? If not, what's the closest thing you've got?" Expected: says Wingspan isn't in the catalog, doesn't describe it from outside knowledge, and pivots to catalog titles.
    5. "Recommend me something good." Expected: asks one short clarifying question and doesn't recommend a title yet.
    6. "What are your three highest rated games?" Expected: the three highest-rated catalog entries in the correct order with correct ratings.
    7. In one conversation, send "Show me two highly rated strategy games." followed by "Which of those has the higher rating?" Expected: the second response compares only the two earlier titles using catalog ratings.
    ```

    ![호스트된 에이전트 배포 테스트 통과](../../../_images/cli-8-passing-acceptance-scenarios.png)

4. 결과를 검토합니다. 에이전트에 연결할 수 없다면 두 번째 터미널에서 서비스가 계속 실행 중인지 확인합니다. 테스트가 실패하면 Copilot에 로컬 결함만 수정하고, 관련 기능에 집중한 테스트를 실행한 뒤 `azd ai agent run`을 언제 다시 시작해야 하는지 알려 달라고 요청합니다. 변경할 때마다 서비스를 다시 시작하고 실패한 인수 테스트(Acceptance test)를 다시 실행합니다.

## 호스트된 에이전트 배포하기

로컬 인수 테스트를 통과했다면 에이전트를 Microsoft Foundry에 배포할 준비가 되었습니다. 동일한 스킬 중심 작업 흐름을 사용해 배포 준비 상태를 확인하고 원격 엔드포인트를 테스트합니다.

1. 모든 인수 테스트를 통과한 뒤 <kbd>Ctrl</kbd>+<kbd>C</kbd>로 로컬 서비스를 중지합니다.
2. Copilot CLI로 돌아가 다음 프롬프트를 입력합니다. 배포를 승인하기 전에 제안된 리소스와 예상 비용을 검토합니다.

    ```text
    Continue with the Microsoft Foundry Skill workflow. Review the hosted agent for deployment readiness, then deploy it to Microsoft Foundry, show the deployment status and playground link, and invoke it remotely with: "I love puzzle games about tracking down bugs. What should I back?"
    ```

3. 평가 모음 소스를 선택하라는 메시지가 표시되면 **No, set it up later**를 선택합니다.

    ![호스트된 에이전트 배포 상태와 플레이그라운드 링크](../../../_images/cli-8-hosted-agent-deployment.png)

4. 배포 상태와 원격 응답을 검토합니다. 에이전트가 실행 중이고 실제 카탈로그 게임만 추천하는지 확인합니다. 배포나 호출이 실패하면 계속 진행하기 전에 Copilot에 실패 원인을 진단하고 원격 테스트를 반복하도록 요청합니다.

표시된 플레이그라운드(Playground) 링크를 통해 Microsoft Foundry 포털에서 배포된 호스트된 에이전트와 상호 작용할 수 있습니다.

스킬 중심 작업 흐름은 `azd deploy`를 사용해 서비스 소스를 패키징하고, 의존성을 해결하고, 원격으로 빌드한 뒤 Microsoft Foundry에 게시합니다. 배포된 엔드포인트는 Foundry 호출 작업 흐름으로 테스트합니다.

## 요약 및 다음 단계

배포 가능한 카탈로그 사본을 포함한 에이전트를 스캐폴드하고, 그라운딩과 대화 연속성을 테스트한 뒤 Microsoft Foundry의 원격 응답을 검증했습니다. 이제 정상적으로 작동하는 호스트된 Backer Concierge가 준비되었습니다.

다음으로 동일한 리포지토리, 브랜치, Copilot CLI 세션, 배포된 에이전트를 유지한 채 [컨시어지를 웹사이트에 연결합니다][next-lesson]. 호스트된 에이전트를 살펴본 것으로 충분하다면 여기서 중단하고 [Azure 리소스를 정리합니다][cleanup].

[overview]: ../
[previous-lesson]: ../1-project-and-model/
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#리소스-정리하기
