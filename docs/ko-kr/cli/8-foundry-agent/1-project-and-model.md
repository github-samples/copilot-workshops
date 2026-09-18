---
title: "모듈 1 - 프로젝트와 모델 준비하기"
description: "Azure 도구를 설정하고, Tailspin 카탈로그를 내보낸 뒤 GitHub Copilot CLI로 Foundry 모델을 선택하고 테스트합니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

이 모듈은 [선택 사항: Foundry 통합하기][overview]의 첫 번째 모듈입니다. 도구와 카탈로그를 준비한 뒤, 에이전트를 빌드하기 전에 Copilot을 사용해 Foundry 프로젝트를 만들고 배포된 모델을 테스트합니다.

이 모듈에서는 다음을 수행합니다.

- Azure 명령줄 도구와 Azure Skills Plugin을 설치합니다.
- 카탈로그를 내보내고 Foundry 작업을 계획합니다.
- 모델을 선택하고 배포한 뒤 카탈로그가 제공하는 정보의 범위를 지키는지 테스트합니다.

## 시나리오

Tailspin Toys에는 카탈로그의 사실과 회사가 제공하지 않는 정보를 구분할 수 있는 컨시어지(Concierge)가 필요합니다. 유용한 추천이라면 평점이 높은 퍼즐 게임을 소개할 수 있지만, 그 게임의 총 모금액을 지어내서는 안 됩니다. 완전한 도우미를 만드는 데 투자하기 전에, 팀은 선택한 모델이 이러한 경계를 지킬 수 있는지 확인하고자 합니다.

## 사전 준비 및 설정

Azure를 사용해 Backer Concierge를 호스팅하고 Copilot CLI로 작업을 진행합니다. 먼저 Copilot이 Azure 리소스를 다룰 수 있도록 명령줄 도구와 플러그인을 준비합니다.

> [!IMPORTANT]
> [정리 지침][cleanup]은 시리즈를 모두 마친 경우뿐 아니라 이 모듈을 마친 뒤 중단하는 경우에도 적용됩니다.

1. Azure 구독이 있는지 확인합니다. 구독이 필요하다면 [$200 크레딧이 포함된 무료 Azure 구독][azure-free] 또는 [$100 크레딧이 포함된 Azure for Students][azure-students] 등의 옵션을 사용할 수 있습니다.
2. Tailspin Toys 코드스페이스로 돌아가 터미널을 엽니다.
3. 개발 컨테이너에 Azure CLI를 설치합니다.

    ```bash
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    az version
    ```

4. `az login`으로 Azure CLI에 로그인하고 `az account show`로 올바른 구독을 사용 중인지 확인합니다.
5. [Azure Developer CLI][install-azd] 버전 1.27.1 이상을 설치합니다. Microsoft Foundry는 `azd`를 사용해 호스트된 에이전트를 테스트하고 배포합니다.

    ```bash
    curl -sL https://aka.ms/install-azd.sh | bash
    azd version
    ```

6. `azd auth login`으로 Azure Developer CLI에 로그인하고 `azd config show`로 올바른 구독을 사용 중인지 확인합니다.
7. Azure Developer CLI(azd) Foundry 확장을 설치합니다.

    ```bash
    azd ext install microsoft.foundry
    ```

8. 명령 팔레트에서 새 Copilot CLI 세션을 옆에 엽니다. <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>(Mac) 또는 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>(Windows/Linux)를 누른 뒤 **Chat: New Copilot CLI session to the side**를 선택합니다.
9. Azure Skills 마켓플레이스를 추가합니다. 플러그인을 처음 설치할 때만 이 작업이 필요합니다.

    ```text
    /plugin marketplace add microsoft/azure-skills
    ```

10. [Azure Skills Plugin][azure-skills]을 설치합니다. 이 플러그인은 Azure 스킬, Azure MCP Server, Foundry MCP Server를 GitHub Copilot CLI에 추가합니다.

    ```text
    /plugin install azure@azure-skills
    ```

11. 플러그인이 Azure MCP 서버를 구성했는지 확인합니다.

    ```text
    /mcp list
    ```

12. 스킬이나 MCP 서버가 표시되지 않으면 `/skills reload` 또는 `/restart`를 실행한 뒤 다시 확인합니다.

스킬은 Copilot에 작업 흐름을 알려 주고, MCP 서버는 Copilot이 Azure 리소스를 살펴보고 다룰 수 있도록 합니다.

## 작업 브랜치 준비하기

이전 연습에서 다른 기능 브랜치를 만들고 푸시했을 수 있습니다. 에이전트 작업을 별도로 유지하도록 최신 `main` 브랜치에서 이 선택 사항 시리즈를 시작합니다.

1. 셸 터미널에서 `main`으로 전환하고 최신 변경 사항을 가져온 뒤 Backer Concierge용 브랜치를 만듭니다.

    ```bash
    git checkout main
    git pull
    git checkout -b foundry-agent-cli
    ```

## 카탈로그 내보내기 파일 생성하기

에이전트가 읽을 수 있도록 카탈로그를 파일로 제공해야 합니다. Tailspin Toys 샘플에는 이를 위한 검증된 내보내기 스크립트가 포함되어 있습니다.

1. Copilot CLI로 돌아가 다음을 입력합니다.

    ```text
    Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
    ```

    Copilot은 다음에 해당하는 명령을 실행해야 합니다.

    ```bash
    npm install
    npm run db:setup
    npm run db:export
    ```

    ![카탈로그 내보내기 요약](../../../_images/cli-8-export-db-catalog.png)

2. `db/catalog.json`을 엽니다. 제목, 설명, 카테고리, 퍼블리셔, 별점이 있는 게임 21개가 포함되어 있는지 확인합니다. `note` 필드에는 카탈로그에 총 모금액, 후원자 수, 후원 등급, 출시일이 없다고 명시되어 있습니다. 가격, 플레이어 수, 플레이 시간 필드도 없습니다. 이러한 누락 항목이 에이전트가 지켜야 할 정보의 경계를 정의합니다.

## Foundry 작업 계획하기

Copilot이 Azure 리소스를 만들거나 에이전트 코드를 추가하기 전에, 계획 모드(Plan mode)를 사용해 예정된 작업 흐름을 확인합니다.

1. 다음 프롬프트를 입력합니다.

    ```text
    /plan Use the Microsoft Foundry Skill to plan a Backer Concierge hosted agent for this existing Tailspin Toys repository. Use a public Foundry project, Python 3.13, Microsoft Agent Framework, the Responses API, the Basic sample, and code deployment. Keep the agent in agent/backer-concierge and keep one azure.yaml at the repository root. Ground every answer in db/catalog.json, preserve conversation context, and add focused tests. Include project setup, model selection, local testing, deployment, remote invocation, estimated cost-bearing resources and cleanup.
    ```

2. 제안된 계획을 검토합니다. Copilot이 `microsoft-foundry` 스킬을 사용하려는지, 호스트된 에이전트를 기존 Astro 애플리케이션과 분리하는지 확인합니다. 우려되거나 예상과 다른 부분이 있으면 진행하기 전에 수정을 요청합니다.
3. 접근 방식이 만족스러우면 계획 모드를 종료합니다.

## Foundry 프로젝트와 모델 설정하기

에이전트에는 Foundry 프로젝트와 배포된 모델이 필요합니다. Microsoft Foundry Skill을 사용해 구독 내 현재 가용성과 할당량을 기준으로 선택합니다.

1. Copilot에 프로젝트 생성을 요청합니다. 리소스 생성을 승인하기 전에 선택한 구독, 지역, 할당량, 예상 비용을 확인합니다.

    ```text
    Use the Microsoft Foundry Skill to create a public Foundry project for this project. Use the resource group rg-tailspin-toys and project name tailspin-toys.
    ```

    ![공개 Foundry 프로젝트 생성하기](../../../_images/cli-8-create-foundry-project.png)

2. 프로젝트가 준비되면 Copilot에 모델 추천을 요청합니다.

    ```text
    Use the Microsoft Foundry Skill to recommend two or three current chat models available in the tailspin-toys project for the Backer Concierge acceptance criteria in the issue titled "Add a Backer Concierge assistant for catalog questions". Prioritize low latency, instruction following, grounding fidelity, available quota, and models that aren't approaching retirement. There is no complex math or multi-step planning. Explain the tradeoffs and wait for me to choose a model from the recommended options.
    ```

    Copilot이 추천 옵션 중에서 모델을 선택하도록 요청할 수 있습니다.

    ![추천 옵션 중에서 모델 선택하기](../../../_images/cli-8-select-foundry-model.png)

    나머지 단계에서는 `gpt-5.4-mini`를 사용하지만, 가용성과 할당량은 지역에 따라 다릅니다.

3. 추천 옵션 중에서 모델을 선택한 뒤 Copilot에 선택한 모델의 배포를 요청합니다. 배포를 승인하기 전에 용량과 비용을 검토합니다.

    ```text
    Deploy the model we selected to the tailspin-toys Foundry project and use the model name as the deployment name. Choose an SKU with available quota, ask me to confirm the capacity before deployment. After deployment, show me the deployment status.
    ```

    ![선택한 모델 배포하기](../../../_images/cli-8-deploy-foundry-model.png)

> [!TIP]
> 모델 가용성은 시간이 지남에 따라 달라집니다. 예제에 하드코딩된 모델이 아니라, Copilot이 프로젝트에서 사용할 수 있다고 확인한 모델을 선택하는 것이 올바른 방법입니다.

## 배포된 모델 테스트하기

호스트된 에이전트를 빌드하기 전에 모델이 Backer Concierge의 그라운딩(Grounding) 규칙을 따르는지 테스트합니다. 에이전트 코드나 구성 없이, 사용할 지침과 카탈로그 컨텍스트로 테스트합니다.

먼저 로그인한 계정에 모듈 2의 호스트된 에이전트 개발을 위한 **Foundry Project Manager** 역할과 직접 모델 추론을 위한 **Cognitive Services OpenAI User** 역할을 부여합니다. 그런 다음 카탈로그에 없는 정보도 함께 요청하는 카탈로그 질문을 합니다.

1. 새 터미널을 열고 계정, 프로젝트, 사용자 값을 설정합니다. `<foundry-account-name>`을 프로젝트 생성 시 안내받은 Foundry 계정 이름으로 바꿉니다.

    ```bash
    SUBSCRIPTION_ID=$(az account show --query id --output tsv)
    USER_OBJECT_ID=$(az ad signed-in-user show --query id --output tsv)
    FOUNDRY_ACCOUNT="<foundry-account-name>"
    ACCOUNT_SCOPE=$(az cognitiveservices account show --name "$FOUNDRY_ACCOUNT" --resource-group rg-tailspin-toys --query id --output tsv)
    PROJECT_SCOPE="$ACCOUNT_SCOPE/projects/tailspin-toys"
    ```

2. **Foundry Project Manager** 역할을 할당합니다.

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Foundry Project Manager" \
       --scope "$PROJECT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

3. **Cognitive Services OpenAI User** 역할을 할당합니다.

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Cognitive Services OpenAI User" \
       --scope "$ACCOUNT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

4. Copilot CLI로 돌아가 다음을 입력합니다.

    ```text
    Use the Microsoft Foundry Skill to test my deployed model directly in the tailspin-toys project without creating an agent. Ground it with content from @db/catalog.json and ask: "I love puzzle games about tracking down bugs. What should I back, and how much funding has it raised?" Show me the response and useful metadata like tokens used and response time (only if you can obtain it). Do not change files or create resources.
    ```

    ![실제 카탈로그 게임을 추천하고 모금 데이터가 없다고 안내하는 Foundry 모델 응답](../../../_images/cli-8-foundry-agent-response.png)

5. 응답을 검토합니다. 카탈로그에 실제로 있는 게임만 추천하고, 올바른 카탈로그 정보를 사용하며, 모금 정보를 확인할 수 없다고 설명해야 합니다. 모델이 제목, 게임 정보, 총 모금액을 지어낸다면 계속 진행하기 전에 다른 추천 모델과 비교합니다.

> [!NOTE]
> 이 테스트는 임시 지침과 카탈로그 컨텍스트로 배포된 모델만 테스트합니다. 에이전트를 테스트하는 것은 아닙니다. 모듈 2에서는 스캐폴딩(Scaffolding) 후 이 테스트를 반복해 호스트된 에이전트의 코드, 패키징, 대화 동작을 검증합니다.

## 요약 및 다음 단계

Azure 도구를 준비하고, 카탈로그를 내보내고, 배포된 모델이 Backer Concierge의 그라운딩 규칙을 따르는지 테스트했습니다. 이 모듈의 완료 기준은 누락된 정보를 지어내지 않고 실제 카탈로그 게임을 추천하는 모델입니다.

다음으로 동일한 리포지토리, `foundry-agent-cli` 브랜치, Copilot CLI 세션, Foundry 프로젝트, 선택한 모델 배포를 사용해 [에이전트를 빌드하고 배포합니다][next-lesson]. 여기서 중단한다면 비용이 계속 발생하지 않도록 [Azure 리소스를 정리합니다][cleanup].

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#리소스-정리하기
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azd]: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
