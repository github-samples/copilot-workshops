---
title: "에이전트 빌드 및 배포"
description: "VS Code에서 Backer Concierge의 스캐폴드를 생성하고 디버깅한 뒤 Foundry 호스팅 에이전트로 배포하고 테스트합니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 이전 모듈: 프로젝트 및 모델 준비][previous-lesson] |
|:--|

이 모듈에서는 [프로젝트 및 모델 준비][previous-lesson]에서 만든 카탈로그와 테스트한 모델을 사용합니다. Microsoft Foundry Toolkit과 **AIAgentExpert** 사용자 지정 에이전트가 VS Code에서 로컬 빌드와 호스팅 배포를 안내합니다.

## 학습 목표

- 기존 Tailspin Toys 작업 영역에서 카탈로그에 근거한 에이전트의 스캐폴드(Scaffold)를 생성합니다.
- Agent Inspector로 로컬 동작을 디버깅합니다.
- 기존 Foundry 프로젝트에 배포하고 호스팅 에이전트(Hosted agent)를 검증합니다.

## 시나리오

신뢰할 수 있는 추천은 단 한 번의 대화에서만 성립해서는 안 됩니다. Tailspin Toys의 안내 도우미는 후원자가 모호한 질문을 하거나 알 수 없는 모금 정보를 집요하게 요구하더라도 카탈로그의 정보 범위를 지켜야 합니다. 호스팅된 안내 도우미도 비공개로 테스트했을 때와 똑같이 안정적으로 동작해야 합니다.

## 작업 영역에서 이어서 진행

에이전트는 기존 모델 배포를 사용하므로 새 Foundry 프로젝트를 만들 필요가 없습니다.

1. VS Code에서 동일한 Tailspin Toys 리포지토리의 `foundry-agent-vscode`를 엽니다. `db/catalog.json`이 존재하고 **Foundry Toolkit** > **My Resources**에 `tailspin-toys` 프로젝트와 테스트한 모델 배포가 표시되는지 확인합니다.
2. [이전 완료 점검][previous-lesson]을 마쳤는지 확인합니다. 리소스를 정리했다면 프로젝트와 모델 준비를 다시 완료한 뒤 계속합니다.
3. Azure Developer CLI(`azd`)가 아직 없다면 설치합니다. 호스팅 에이전트 배포에 필요합니다. 운영 체제에 맞는 명령만 선택합니다.

   ```bash
   # macOS / Linux
   curl -fsSL https://aka.ms/install-azd.sh | bash

   # Windows (PowerShell)
   winget install microsoft.azd
   ```

4. 기존 프로젝트에 사용하는 구독으로 로그인합니다.

   ```bash
   azd auth login
   ```

> [!IMPORTANT]
> 호스팅 에이전트와 Foundry Toolkit은 공개 미리 보기로 제공됩니다. 배포 시 유료 리소스를 만듭니다. 명령을 승인하기 전에 구독, 권한, 지역, 할당량, 예상 비용을 확인합니다.

## 에이전트 생성 및 디버깅

툴킷은 현재 리포지토리에 코드 스캐폴드를 생성하고 특화된 Copilot Chat을 엽니다. Agent Inspector를 사용하면 배포 전에 로컬 요청, 이벤트, 도구 호출을 확인할 수 있습니다.

1. **Foundry Toolkit**을 선택하고 **Developer Tools**, **+ Build**를 차례로 펼친 뒤 **+ Create Agent**를 선택합니다. **Create Agent**에서 **Code an agent with Copilot**을 선택합니다.

   ![에이전트 생성 페이지를 보여 주는 스크린샷.](../../../_images/vscode-create-agent.png)

2. 새 채팅이 **AIAgentExpert**로 전환되는지 확인합니다. 생성된 프롬프트를 다음의 사용자 지정 프롬프트로 바꾸고 전송합니다.

   ```text
   /foundrytk-quick-start Create a backer concierge AI agent called 'Backer Concierge'. The agent should use the model I deployed to answer catalog questions and recommend games grounded strictly in db/catalog.json. Review the acceptance criteria in the issue titled 'Add a Backer Concierge assistant for catalog questions' and ensure the agent meets them. Generate the code into agent/backer-concierge in the current workspace and ask me if anything is unclear.
   ```

3. `agent/backer-concierge`에 생성된 코드를 검토합니다. 배포 가능한 에이전트에 카탈로그가 포함되어 있고, 관련 테스트를 통과했으며, 자격 증명이나 로컬 환경 파일이 커밋되지 않을지 확인합니다.
4. 작업 표시줄에서 **Run and Debug**를 선택하고 <kbd>F5</kbd>로 디버거를 시작합니다. **Agent Inspector**가 열리고 에이전트 서버에 연결되는지 확인합니다.
5. [배포한 모델 테스트][model-tests]의 프롬프트 여섯 개를 모두 재사용합니다. 게임 9개로 구성된 하위 집합의 순위가 전체 카탈로그 순위와 같다고 가정하지 말고 전체 `db/catalog.json`을 기준으로 답변을 점검합니다.
6. **Input & Output**, **Events**, **Tools** 사이를 전환하여 페이로드(Payload), 세션 이벤트, 도구 호출을 살펴봅니다. 수락 기준을 위반하는 동작이 있다면 Copilot에 수정을 요청하고 배포하기 전에 관련 테스트와 Inspector 점검을 다시 실행합니다.

   ![로컬 에이전트 디버깅 워크플로를 보여 주는 스크린샷.](../../../_images/vscode-agent-debug.png)

## 호스팅 에이전트 배포 및 테스트

**Go production** 핸드오프(Handoff)는 기존 에이전트를 Foundry용으로 패키징합니다. 이후에 만드는 사이트 프록시(Proxy)를 프로덕션용 공개 서비스로 만들어 주는 것은 아닙니다.

1. 에이전트를 생성한 Copilot Chat에서 **Go production**을 선택하고 기본 프롬프트를 다음 내용으로 바꾼 뒤 전송합니다.

   ```text
   /foundrytk-quick-start Review this agent for deployment readiness, run its tests, then deploy it to my existing tailspin-toys Foundry project. Show me the deployment status and test the deployed agent.
   ```

   ![AIAgentExpert 에이전트의 핸드오프 옵션을 보여 주는 스크린샷.](../../../_images/vscode-go-production-handoff.png)

2. 채팅과 터미널에서 매개 변수와 명령 승인 요청을 검토합니다. 배포 대상이 기존 `tailspin-toys` 프로젝트인지 확인하고 승인하기 전에 유료 리소스를 검토합니다.
3. Copilot이 평가 테스트 모음을 제안하면 추가 점검으로 수락하여 진행할 수 있습니다.
4. **Foundry Toolkit**을 선택하고 **My Resources**를 펼친 뒤 **Agents**를 선택합니다. **Agents** 탭에서 **Hosted Agent**로 전환합니다.

   ![배포한 호스팅 에이전트를 보여 주는 스크린샷.](../../../_images/vscode-agent-deployed.png)

5. 에이전트 이름을 선택하고 배포 상태가 **Running**인지 확인합니다. **Playground**로 전환하고 배포된 카탈로그를 기준으로 그라운딩(Grounding), 누락된 정보, 카탈로그 외부 항목, 모호한 요청, 순위 점검을 반복합니다.

   ![배포한 호스팅 에이전트의 답변을 보여 주는 스크린샷.](../../../_images/vscode-agent-response.png)

6. 배포나 답변에 문제가 있다면 Copilot과 함께 보고된 상태 및 로그를 살펴보고, 기존 프로젝트에서 문제를 수정한 뒤 점검을 반복합니다. 배포를 검증하지 않은 채로 계속하지 않습니다.

## 완료 점검

Backer Concierge를 스캐폴드하고 Agent Inspector에서 카탈로그 근거 기반 응답을 디버깅했으며, **Go production** 핸드오프로 Foundry에 배포한 뒤 Playground에서 호스팅 버전을 다시 테스트했습니다. 이 모듈의 완료 점검 항목은 없는 정보를 지어내지 않고 카탈로그 범위를 지키며 실행 중인 호스팅 에이전트입니다.

다음에는 동일한 `tailspin-toys` 프로젝트, 모델 배포, 호스팅 에이전트를 사용하여 사이트에 에이전트를 연결합니다. 여기서 중단한다면 지속적인 비용이 발생하지 않도록 [Azure 리소스를 정리합니다][cleanup].

| [다음 모듈: 사이트에 에이전트 연결 →][next-lesson] |
|--:|

[previous-lesson]: ../1-project-and-model/
[model-tests]: ../1-project-and-model/#배포한-모델-테스트
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#리소스-정리
