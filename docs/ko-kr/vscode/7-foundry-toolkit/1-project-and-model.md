---
title: "프로젝트 및 모델 준비"
description: "Tailspin 카탈로그를 내보내고 Backer Concierge의 수락 기준에 따라 배포한 모델을 테스트합니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 선택 사항: Foundry 통합][overview] |
|:--|

첫 번째 모듈에서는 VS Code와 Microsoft Foundry Toolkit을 사용하여 Backer Concierge에 필요한 데이터와 모델을 준비합니다. 필수 워크숍에서 사용한 본인의 Tailspin Toys 리포지토리에서 작업합니다.

## 학습 목표

- 카탈로그를 내보내고 제공하는 정보의 범위를 파악합니다.
- Foundry 프로젝트를 준비하고 수락 기준과 할당량에 따라 모델을 선택합니다.
- 에이전트 코드를 작성하기 전에 Model Playground에서 그라운딩(Grounding) 동작을 검증합니다.

## 시나리오

Tailspin 후원자는 신뢰할 수 있는 추천을 원합니다. 퍼즐 게임 팬은 지어낸 모금액이 아니라 실제 게임과 정확한 평점을 기대합니다. 안내 도우미는 카탈로그의 정보 범위를 명확히 지키고, 후원자가 원하는 것을 추측하기보다 도움이 되는 질문 하나를 하는 습관을 갖추어야 합니다.

## 작업 영역 준비

툴킷은 모델 탐색, 배포, 프롬프트 엔지니어링(Prompt engineering), 평가, 에이전트 배포를 VS Code에서 지원합니다. Azure 접근 권한을 확보하고 변경 사항을 정리한 기능 브랜치를 마련하여 이후 작업을 준비합니다.

> [!IMPORTANT]
> Foundry Toolkit과 호스팅 에이전트(Hosted agent)는 공개 미리 보기로 제공됩니다. 이 모듈에서는 유료 Azure 리소스를 만듭니다. 생성을 승인하기 전에 구독 권한, 지역, 할당량, 예상 비용을 확인합니다. 에이전트를 만들기 전에 중단하더라도 [리소스 정리][cleanup]를 수행할 수 있습니다.

1. Azure 구독에 접근할 수 있는지 확인합니다. 자격 요건과 서비스 제한에 따라 [$200 크레딧을 제공하는 무료 Azure 계정][azure-free]이나 [$100 크레딧을 제공하는 Azure for Students][azure-students]를 사용할 수 있습니다.
2. VS Code의 작업 표시줄에서 **Extensions**를 선택하고 **Foundry Toolkit**을 검색한 뒤 **Install**을 선택합니다. 작업 표시줄에 툴킷 아이콘이 나타납니다.
3. **Azure** 아이콘을 선택하고 **Sign in to Azure…**를 선택한 뒤 Foundry 프로젝트에 사용할 구독을 선택합니다. 툴킷 인증을 완료하면 Copilot이 [Microsoft Foundry Skill][foundry-skill]을 사용하여 대화 방식으로 리소스를 준비할 수 있습니다.
4. Tailspin Toys 작업 영역에서 **Terminal** > **New Terminal**을 열거나 <kbd>Control</kbd>+<kbd>\`</kbd>(Mac) 또는 <kbd>Ctrl</kbd>+<kbd>\`</kbd>(Windows/Linux)를 누릅니다. 이전 작업을 커밋하고 푸시했는지 확인한 뒤 기능 브랜치를 만듭니다.

   ```bash
   git checkout main
   git pull
   git checkout -b foundry-agent-vscode
   ```

5. **Agent** 모드로 새 Copilot Chat을 열고 다음과 같이 요청합니다.

   ```text
   Show me the open issue about a Backer Concierge assistant and summarize its acceptance criteria.
   ```

6. Copilot이 **Add a Backer Concierge assistant for catalog questions** 이슈를 표시하는지 확인합니다. 수락 기준은 근거에 기반한 답변, 모금액을 지어내지 않는 동작, 명확히 하기 위한 질문 하나, 엔드투엔드 테스트를 갖춘 접근성 있는 UI를 요구합니다.

## 카탈로그 내보내기

카탈로그 내보내기 스크립트는 에이전트가 답변의 근거로 사용할 데이터 원본을 제공합니다.

1. Tailspin Toys 리포지토리 터미널에서 마이그레이션과 시드 데이터 입력을 수행한 뒤 `db/catalog.json`을 작성합니다.

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

2. `db/catalog.json`을 열고 게임 21개가 들어 있는지 확인합니다. 각 게임에는 제목, 설명, 카테고리, 배급사, 별점과 함께 누락된 정보를 설명하는 `note` 필드가 있어야 합니다. 총모금액, 후원자 수, 후원 등급, 출시일은 포함하지 않으므로 에이전트는 이 정보 범위를 지켜야 합니다.

## Foundry 프로젝트 설정

프로젝트에는 모델을 두고 나중에는 호스팅 에이전트도 추가합니다. 이 모듈을 이어서 진행할 때는 다른 프로젝트를 만들지 않고 동일한 프로젝트를 사용합니다.

1. 작업 표시줄에서 **Foundry Toolkit**을 선택하고 **Help and Feedback**을 펼친 뒤 **Ask Copilot**을 선택합니다. 드롭다운에서 원하는 모델을 확인하고 생성된 `/foundrytk-quick-start` 프롬프트를 보냅니다.

   ![Foundry Toolkit 빠른 시작 순서를 보여 주는 스크린샷.](../../../_images/vscode-foundry-setup.png)

2. 대화형 워크플로에서 **Where are you starting from?**에 **Set up Foundry**로 답한 뒤 **What do you have already?**에 **I have an Azure subscription or Foundry resources**로 답합니다.
3. 도구 승인 요청을 검토합니다. 제안한 명령과 범위가 적절하다면 이 세션에 대해 **Allow azmcp …**를 선택하여 반복되는 승인 요청을 줄입니다.
4. **Microsoft Foundry: Create Project**의 **Choose a resource group**에서 **Create new resource group**을 선택하고 `rg-tailspin-toys`를 입력합니다. 사용할 모델을 제공하는 지역을 선택하고 **Enter project name**에 `tailspin-toys`를 입력합니다. `East US 2`와 `Sweden Central`은 다양한 모델을 제공하는 초기 후보 지역입니다. 실제 선택은 현재 가용성과 할당량에 따라 결정합니다. 이어서 진행하는 경우에는 기존 프로젝트를 선택합니다.
5. 배포 성공 알림이 나타날 때까지 기다립니다. 툴킷에서 **My Resources**를 펼치고 이 프로젝트가 기본 프로젝트인지 확인합니다.

## 모델 탐색 및 배포

여기서는 가장 크거나 가장 새로운 모델을 선택하는 것보다 규칙 준수와 그라운딩이 더 중요합니다. 이슈는 속도, 충실도, 지역별 가용성, 할당량을 비교할 수 있는 구체적인 기준을 제공합니다.

1. Copilot Chat에서 **+**, **GitHub Issues**를 차례로 선택하고 **Add a Backer Concierge assistant for catalog questions**를 첨부합니다. 다음 프롬프트를 보냅니다.

   ```text
   /microsoft-foundry recommend a model for the agent described in this issue. There's no math or multi-step planning here, so reasoning depth isn't a priority. Prioritize speed instead. Recommend 2-3 candidates available in my Azure region with the trade-offs between them, tell me which you'd pick and why, and check my quota. Avoid deprecated & older models according to the model retirement schedule
   ```

2. 추천 내용을 읽고 요구 사항과 사용 가능한 할당량에 가장 적합한 모델을 선택합니다. Copilot에 배포를 요청합니다.

   ```text
   /microsoft-foundry Deploy the model I selected to the tailspin-toys project and use the model name as the deployment name. Confirm the available quota and capacity with me before creating it.
   ```

3. 승인하기 전에 프로젝트, 배포, 용량, 비용을 확인합니다. 범위를 검토한 결과 적절하다면 이 세션에 대해 **Allow az …**를 선택하여 반복되는 요청을 줄입니다.
4. **Foundry Toolkit**을 선택하고 **My Resources**를 펼친 뒤 **Models**를 선택합니다. 배포한 모델이 Foundry 아래에 나타나는지 확인합니다. 스크린샷은 예시이며 지역에 따라 다른 모델을 제공할 수 있습니다.

   ![Foundry Toolkit의 모델 배포 예시를 보여 주는 스크린샷.](../../../_images/vscode-model-deployed.png)

## 배포한 모델 테스트

Model Playground에는 카탈로그 파일이 없습니다. 시스템 프롬프트(System prompt)에 게임 9개로 줄인 하위 집합을 넣으면 모델이 그라운딩 규칙을 따르는지 테스트하기에 충분합니다.

1. **Models**에서 배포한 모델 이름을 선택하여 해당 모델이 미리 지정된 **Model Playground**를 엽니다. 다음 시스템 프롬프트를 붙여 넣습니다.

   ```text
   You're the Backer Concierge for Tailspin Toys. Only recommend games from this catalog — never invent games, publishers, ratings, or any funding/price/date info. If a request is vague, ask one short question first.

   CATALOG

   | Title | Category | Publisher | Rating |
   | --- | --- | --- | --- |
   | Bug Buster Brainteaser | Puzzle | GitHub Games | 3.0 |
   | Merge Conflict Mystery | Puzzle | DevMasters Inc. | 3.8 |
   | Stack Trace Secrets | Puzzle | Ops Interactive | 3.6 |
   | Deployment Dynasty | Simulation | Ops Interactive | 5.0 |
   | Script Strike | Action | CodeForge Studios | 5.0 |
   | Pipeline Conquest | Strategy | DevMasters Inc. | 3.9 |
   | Repo Rulers | Strategy | Ops Interactive | 4.1 |
   | Server Siege | Strategy | GitHub Games | 3.3 |
   | Code Quest Odyssey | Adventure | CodeForge Studios | 4.8 |
   ```

2. `I love puzzle games about tracking down bugs. What should I back?`로 그라운딩을 테스트합니다. 목록에 있는 실제 게임을 정확한 정보와 함께 제시해야 합니다.
3. `How much has Pipeline Conquest raised so far, and how many backers does it have?`로 누락된 정보를 테스트합니다. 카탈로그에서 모금액이나 후원자를 추적하지 않으므로 명확히 답변을 거절한 다음 알고 있는 정보를 제공해야 합니다.
4. `I need something for four players, about an hour long.`으로 다른 정보 범위를 테스트합니다. 플레이어 수와 플레이 시간을 알 수 없다고 설명한 뒤 다음 추천에 도움이 되는 후속 질문 하나를 해야 합니다.
5. `Do you have Wingspan? If not, what's the closest thing you've got?`로 카탈로그에 없는 게임을 요구하는 상황을 테스트합니다. Wingspan이 카탈로그에 있다고 주장하거나 외부 지식으로 설명하지 않고 실제 Tailspin 게임으로 대화를 전환해야 합니다.
6. `Recommend me something good.`으로 모호한 요청을 테스트합니다. 짧은 확인 질문 하나를 하고, 카테고리나 테마를 알기 전에는 추천하지 않아야 합니다.
7. `What are your three highest rated games?`로 순위를 테스트합니다. Deployment Dynasty와 Script Strike가 5.0점, 그다음 Code Quest Odyssey가 4.8점으로 올바른 순서와 정확한 점수를 제시해야 합니다.
8. 점검에 실패하면 Copilot과 실패한 답변 및 규칙을 논의하고, 구성이나 모델 선택을 조정한 뒤 점검을 반복하여 통과한 후 계속합니다.

## 완료 점검

VS Code 작업 영역을 준비하고 카탈로그를 내보냈으며, Foundry 프로젝트를 만들고 배포한 모델이 Backer Concierge의 근거 기반 응답 규칙을 지키는지 테스트했습니다. 이 모듈의 완료 점검 항목은 없는 정보를 지어내지 않고 카탈로그에 실제로 있는 게임을 추천하는 모델이며, 아직 배포한 에이전트는 아닙니다.

다음에는 동일한 `tailspin-toys` 프로젝트와 선택한 모델 배포를 사용하여 에이전트를 빌드하고 배포합니다. 여기서 중단한다면 지속적인 비용이 발생하지 않도록 [Azure 리소스를 정리합니다][cleanup].

| [다음 모듈: 에이전트 빌드 및 배포 →][next-lesson] |
|--:|

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#리소스-정리
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[foundry-skill]: https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/SKILL.md
