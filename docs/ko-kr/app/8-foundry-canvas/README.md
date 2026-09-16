---
title: "선택 사항: Foundry 통합"
slug: ko-kr/app/8-foundry-canvas
description: "Microsoft Foundry Canvas로 카탈로그에 근거한 Backer Concierge를 구축하고, 각 단계에서 안전하게 작업을 마치는 방법을 알아봅니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/ko-kr/app/9-review/
  label: 검토 및 다음 단계
next:
  link: /copilot-workshops/ko-kr/app/8-foundry-canvas/1-project-and-model/
  label: 프로젝트와 모델 준비
---

이 선택 실습 과정에서는 GitHub Copilot app의 Microsoft Foundry Canvas를 사용하여 Tailspin Toys에 **Backer Concierge**를 추가합니다. 카탈로그에 근거한 모델 실험으로 시작하여 호스팅 에이전트를 구축한 다음 로컬 웹사이트에 통합합니다.

## 실습 과정

각 모듈은 체크포인트와 안전하게 작업을 마칠 수 있는 지점으로 끝납니다. 전체 과정에서 동일한 Tailspin Toys 리포지토리, 워크트리(Worktree) 브랜치, 이슈에 연결된 세션, Foundry 프로젝트, 모델 배포를 계속 사용합니다.

- [프로젝트와 모델 준비][module-1]에서는 카탈로그 정보의 범위를 정하고, 프로젝트와 모델 배포를 만든 다음 Canvas에서 확인합니다.
- [에이전트 빌드 및 배포][module-2]에서는 Backer Concierge의 기본 구조를 생성하고 로컬에서 테스트한 다음, 호스팅 에이전트를 배포하고 다시 테스트합니다.
- [에이전트를 사이트에 연결][module-3]에서는 자격 증명을 안전하게 보호하는 로컬 프록시, 접근성을 갖춘 채팅 위젯, 엔드투엔드(End-to-end) 테스트, Agent merge를 추가합니다.

> [!IMPORTANT]
> Microsoft Foundry Canvas와 호스팅 에이전트는 공개 미리 보기 상태입니다.
>
> 이 과정에서는 모델 배포와 모듈 2부터 사용하는 호스팅 에이전트 등 요금이 발생하는 Azure 리소스를 만듭니다. 리소스를 만들기 전에 구독, 지역, 할당량, 예상 비용을 승인해야 합니다. 프로젝트와 모델까지만 준비하고 중단하더라도 리소스를 정리해야 합니다.

1. [프로젝트와 모델 준비][module-1]부터 시작합니다. 이 워크숍 콘텐츠 리포지토리가 아니라 Tailspin Toys 리포지토리에서 작업합니다.
2. 프로젝트와 모델, 호스팅 배포, 전체 통합 중 원하는 지점에서 작업을 마칠 때 해당 모듈의 체크포인트를 기록하고, 실험을 마치면 아래의 공통 정리 절차를 따릅니다. 정리 후 나중에 계속하려면 삭제한 리소스를 복원하고 구성을 다시 확인해야 합니다.

## 리소스 정리

진행한 단계에 따라 정리 방법이 달라집니다. 프로젝트와 모델까지만 준비한 경우에는 `azure.yaml`, `azd` 환경, 호스팅 에이전트가 필요하지 않습니다.

> [!WARNING]
> 리소스를 삭제하면 복구할 수 없습니다. 여기서는 이 워크숍 전용 리소스만 삭제할 수 있습니다. 공유 리소스 그룹은 절대 삭제하면 안 됩니다. 대신 리소스 소유자와 협의하여 워크숍 리소스를 개별적으로 제거하는 것이 안전합니다.

1. 시작해 둔 로컬 Agent Inspector, Azure Function, Astro 개발 서버 프로세스를 각각의 터미널에서 중지합니다. Azure 리소스를 삭제하기 전에 필요한 체크포인트 세부 정보를 기록합니다.
2. Azure Portal에서 활성 구독 ID, 정확한 워크숍 리소스 그룹 이름, 그룹에 포함된 모든 리소스를 확인합니다. Foundry 프로젝트와 모델 배포가 이번 실습에 속하는지 확인합니다. 구독, 소유권, 리소스 구성이 불명확하면 이를 해결할 때까지 정리를 중단합니다.
3. 작업을 마친 지점에 맞는 정리 경로를 선택합니다. 모듈 1만 완료했다면 다음 단계를 건너뛰고 5단계를 따릅니다. 정리만을 위해 `azure.yaml`을 만들거나 `azd`를 초기화하지 않습니다. 모듈 2 또는 3에서 Canvas로 배포했다면 4단계로 진행합니다.
4. 호스팅 배포를 정리하려면 루트에 `azure.yaml`이 있는 동일한 Tailspin Toys 워크트리에서 터미널을 엽니다. 선택한 `azd` 환경이 이번 실습의 구독과 리소스를 대상으로 하는지 확인하고, 삭제할 리소스를 검토한 다음, 모든 대상이 워크숍 전용인 경우에만 다음 명령을 실행합니다.

   ```bash
   azd down --purge
   ```

5. 프로젝트와 모델까지만 준비한 경우 또는 `azd down` 실행 후에도 워크숍 전용 리소스 그룹이 남아 있는 경우에는 포털에서 구독, 그룹 이름, 전체 리소스 목록을 다시 확인합니다. 그룹 전체가 이번 실습 전용이고 이름이 정확히 `rg-tailspin-toys`이면 다음 명령을 실행합니다. 이름이 다르면 확인한 전용 그룹 이름으로 바꿉니다. 공유 그룹이라면 이 명령을 실행하지 말고 소유자와 협의하여 리소스를 개별적으로 정리합니다.

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. Azure Portal에서 삭제가 완료되었는지 확인합니다. `--no-wait`를 사용하면 삭제가 완료되기 전에 명령이 반환됩니다. 워크숍 모델 배포와 호스팅 에이전트 리소스가 모두 제거되었는지 확인하고, 공유 리소스를 삭제하지 않으면서 요금이 발생하는 나머지 워크숍 리소스를 정리합니다.
7. 선택한 체크포인트 기록과 리소스 정리를 마치면 [검토 및 다음 단계][core-review]로 돌아갑니다.

## 리소스

Microsoft 문서에서는 Canvas, 호스팅 배포, 관련 권한을 설명합니다.

- [Microsoft Foundry Canvas란?][foundry-canvas]
- [Foundry Canvas로 첫 번째 호스팅 에이전트 배포][hosted-agent-quickstart]
- [호스팅 에이전트 권한][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
