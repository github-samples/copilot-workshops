---
slug: ko-kr/vscode/7-foundry-toolkit
title: "선택 사항: Foundry 통합"
description: "VS Code와 Microsoft Foundry Toolkit으로 세 가지 집중 모듈에 걸쳐 카탈로그에 근거한 Backer Concierge를 만듭니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 이전 실습: GitHub Copilot의 작업 반복 개선][previous-lesson] |
|:--|

필수 VS Code 과정은 실습 6에서 완료됩니다. 이 선택 확장 과정에서는 VS Code의 GitHub Copilot Chat과 Microsoft Foundry Toolkit을 사용하여 Tailspin 카탈로그를 기반으로 Backer Concierge를 만들고, 호스팅 에이전트(Hosted agent)로 배포한 뒤 로컬 프록시(Proxy)를 통해 사이트에 연결합니다.

## 시나리오

후원자는 필터만으로는 답할 수 없는 질문을 합니다. git 말장난을 좋아하는 사람에게 어떤 게임이 어울리는지, 특정 퍼즐 게임이 다른 게임보다 더 잘 맞는 이유는 무엇인지 궁금해합니다. Tailspin Toys에는 실제 카탈로그의 게임을 추천하고, 필요할 때 명확히 하기 위한 질문을 하며, 모금액이나 기타 정보를 알 수 없을 때 이를 솔직히 인정하여 신뢰를 얻는 안내 도우미가 필요합니다.

## 모듈

각 모듈은 작동하는 결과물을 확인하는 것으로 마무리합니다. 세 모듈 모두 동일한 학습자 리포지토리, 기능 브랜치, Foundry 프로젝트를 사용하며, 모듈 사이에 프로젝트를 다시 만들지 않습니다.

| 모듈 | 완료 점검 항목 |
|--------|-----------------------|
| [1. 프로젝트 및 모델 준비][module-1] | 카탈로그를 내보내고 그라운딩(Grounding) 규칙에 따라 배포한 모델 테스트 |
| [2. 에이전트 빌드 및 배포][module-2] | 로컬 에이전트 디버깅 및 호스팅 에이전트 테스트 |
| [3. 사이트에 에이전트 연결][module-3] | 로컬 프록시 및 접근성을 갖춘 위젯의 엔드투엔드 테스트 |

> [!IMPORTANT]
> Microsoft Foundry Toolkit과 호스팅 에이전트는 공개 미리 보기로 제공됩니다. 이 모듈에서는 모델 배포와 호스팅 에이전트를 비롯한 유료 Azure 리소스를 만듭니다. 구독 권한, 지역별 가용성, 할당량, 비용에 따라 참여가 제한될 수 있습니다.

## 시작하기 전에

이 확장 과정은 워크숍 문서 리포지토리가 아니라 본인의 Tailspin Toys 리포지토리에서 진행합니다.

1. 선택 기능을 시작하기 전에 필수 워크숍 작업을 저장하고 커밋하여 푸시했는지 확인합니다.
2. [프로젝트 및 모델 준비][module-1]부터 시작합니다. 이어서 진행하는 경우 Tailspin Toys 리포지토리를 `foundry-agent-vscode` 브랜치에서 다시 열고 **Foundry Toolkit** > **My Resources**에 `tailspin-toys` 프로젝트와 모델 배포가 남아 있는지 확인합니다.
3. 어느 모듈에서든 중단할 때는 다음 모듈을 위해 의도적으로 리소스를 유지하고 지속적인 비용을 부담하는 경우가 아니라면 [리소스 정리][cleanup]를 따릅니다.

## 리소스 정리

어느 체크포인트에서든 실습을 마쳤다면 불필요한 비용이 발생하지 않도록 Azure 리소스를 삭제합니다. 정리하면 이후 모듈에 필요한 리소스도 함께 삭제되므로, 나중에 이어서 진행하려면 다시 만들어야 합니다.

> [!WARNING]
> `rg-tailspin-toys`는 이 실습 전용이고 보관할 리소스가 없는 경우에만 삭제합니다. 공유 리소스 그룹을 삭제하면 관련 없는 리소스까지 제거됩니다.
>
> 모듈 1에서 다른 리소스 그룹 이름을 승인했다면 아래의 모든 명령에서 `rg-tailspin-toys`를 해당 이름으로 바꿉니다.

1. 시작한 Agent Inspector 디버그 세션, Azure Functions 호스트, Astro 개발 서버를 각 터미널에서 중지합니다.
2. 모듈 2에서 호스팅 에이전트를 배포했다면 `azure.yaml`이 있는 생성된 에이전트 디렉터리에서 터미널을 열고 동일한 `azd` 환경을 선택한 뒤 다음을 실행합니다.

   ```bash
   azd down --purge
   ```

3. 선택한 구독과 워크숍 리소스 그룹이 아직 남아 있는지 확인합니다.

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   명령이 `false`를 반환하면 정리가 완료된 것입니다. `true`를 반환하면 그룹의 리소스를 검토합니다.

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   남아 있는 리소스가 모두 이 실습에 속하는지 확인합니다. 모듈 1에서 중단했다면 `azd` 서비스를 배포하지 않았더라도 Foundry 프로젝트와 모델은 정리해야 합니다.

4. 워크숍 전용 리소스 그룹이 아직 존재하고 삭제하려는 리소스만 포함되어 있다면 다음을 실행합니다.

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. `--no-wait`는 삭제가 완료되기 전에 반환되므로, 다음 명령이 `false`를 반환할 때까지 다시 실행합니다.

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## 참고 자료

- [Visual Studio Code용 Foundry Toolkit][foundry-toolkit]
- [Microsoft Foundry 에이전트 확장 개요][foundry-extension]

| [다음 모듈: 프로젝트 및 모델 준비 →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #리소스-정리
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
