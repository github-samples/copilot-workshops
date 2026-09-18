---
title: "사이트에 에이전트 연결"
description: "로컬 프록시를 통해 호스팅된 Backer Concierge를 연결하고 접근성을 갖춘 채팅 위젯을 테스트합니다."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
next: false
---

| [← 이전 모듈: 에이전트 빌드 및 배포][previous-lesson] |
|:--|

이 모듈에서는 [에이전트 빌드 및 배포][previous-lesson]의 호스팅 에이전트(Hosted agent)를 Tailspin Toys에 연결합니다. VS Code의 Copilot Chat은 공개 프로덕션 엔드포인트가 아니라 로컬 통합을 만듭니다.

## 학습 목표

- 자격 증명과 Foundry 대화 식별자를 로컬 서버 측 프록시(Proxy) 내부에 유지합니다.
- 대화의 연속성을 유지하는 접근성 있는 채팅 위젯을 추가합니다.
- 리소스를 정리하기 전에 백엔드와 전체 사용자 경험을 검증합니다.

## 시나리오

후원자는 카탈로그를 벗어나지 않고도 안내 도우미에게 조언을 구할 수 있어야 합니다. 대화는 맥락을 유지하고, 키보드로 이용할 수 있으며, 비공개 연결 정보를 보호해야 합니다. 신뢰를 얻으려면 정직한 추천뿐만 아니라 안전하고 접근성을 갖춘 경험도 필요합니다.

## 작업 영역에서 이어서 진행

통합 대상은 기존 호스팅 에이전트입니다. Tailspin Toys는 모든 페이지를 미리 렌더링한 정적 웹사이트이므로 브라우저 코드에 에이전트의 자격 증명을 안전하게 보관할 수 없습니다.

1. VS Code에서 동일한 Tailspin Toys 리포지토리의 `foundry-agent-vscode`를 엽니다. 이전 완료 점검의 호스팅 에이전트가 기존 `tailspin-toys` 프로젝트에서 여전히 **Running** 상태이고 로컬 Azure 로그인이 해당 구독을 대상으로 하는지 확인합니다.
2. **AIAgentExpert** 대신 일반 **Agent** 모드로 Copilot Chat을 엽니다. **+**, **GitHub Issues**를 차례로 선택한 뒤 해당 이슈를 선택하여 **Add a Backer Concierge assistant for catalog questions**를 첨부합니다.

## 로컬 프록시 빌드 및 검증

`/api`의 로컬 Azure Functions 프록시는 사이트가 로컬에서 실행되는 동안 연결 정보를 보관하고 요청을 전달합니다. Copilot은 **Azure skills**를 사용하여 프록시를 준비하고 검증할 수 있습니다.

> [!IMPORTANT]
> 이 워크숍 프록시는 로컬 개발 전용입니다. 익명으로 접근할 수 있는 공개 엔드포인트로 배포하지 않습니다. 프로덕션에는 애플리케이션에 맞는 인증과 악용 방지 제어가 필요하며, 여기에는 요청 속도 제한이나 할당량, CORS 제한, 모니터링, 비용 제어가 포함됩니다.

1. Copilot에 프록시 생성을 요청합니다.

   ```text
   Add a local Azure Functions proxy in api for the static Astro site to call my deployed Backer Concierge securely during development. Use my existing local Azure sign-in to call the hosted agent, keep all credentials out of the browser, protect conversation state with opaque handles, validate requests, sanitize errors, add focused tests, and configure the Astro dev server so /api requests reach the local Function. Don't create public deployment infrastructure.
   ```

2. 변경 사항을 수락하기 전에 검토합니다. 자격 증명과 Foundry 대화 식별자를 서버에 유지하고, 로컬 설정을 버전 관리에서 제외하며, 요청에 제한을 적용하고, 관련 테스트를 통과했는지 확인합니다.
3. UI를 만들기 전에 백엔드가 작동함을 입증합니다.

   ```text
   Start the local Functions host and test /api/concierge by asking "Which games are under $30?" Show me the sanitized response and confirm that no credentials or internal conversation identifiers are returned.
   ```

4. 터미널의 응답을 확인합니다. 답변을 담은 `response` 속성이 있는 유효한 JSON이어야 하며, 지어낸 가격 정보나 자격 증명, 내부 대화 식별자가 없어야 합니다. 점검에 실패하면 Copilot에 수정을 요청하고 백엔드 테스트를 반복합니다.
5. **Keep**으로 변경 사항을 유지하고 **/clear**를 사용하여 동일한 리포지토리와 브랜치에서 위젯 작업을 새로 시작합니다. 로컬 프록시 구성과 기존 호스팅 에이전트 연결을 유지합니다.

## 위젯 빌드 및 테스트

이제 UI에서 사용할 백엔드를 검증했습니다. 엔드투엔드 테스트(End-to-end test)로 사용성과 카탈로그의 정보 범위를 모두 점검합니다.

1. Copilot에 위젯 추가를 요청합니다.

   ```text
   Add an accessible Backer Concierge chat widget to the Astro site. Connect it to /api/concierge, preserve the conversation using the returned opaque handle, follow the existing design guidance, support keyboard use, and make it testable.
   ```

   ![Backer Concierge 채팅 위젯이 동작하는 모습을 보여 주는 스크린샷](../../../_images/tailspin-toys-backer-concierge-agent.png)

2. Function과 사이트를 계속 실행한 상태에서 전체 사용자 경험을 검증합니다.

   ```text
   Use Playwright MCP to test the Backer Concierge widget end to end. Verify the core chat flow, conversation continuity, keyboard and accessibility behavior, grounding boundaries, and safe use of the local proxy. Report the results and fix any failures.
   ```

3. 이슈의 수락 기준에 따라 테스트 결과와 변경 사항을 검토합니다. 근거에 기반한 답변, 모금액을 지어내지 않는 동작, 명확히 하기 위한 질문 하나, 접근성 있는 UI, 엔드투엔드 테스트가 기준입니다. 실패한 부분을 수정하고 관련 점검을 다시 실행했는지 확인합니다.

## 완료 점검

자격 증명을 안전하게 보호하는 로컬 프록시를 만들고 접근성 있는 채팅 위젯을 연결했으며, 호스팅 Backer Concierge를 대상으로 전체 대화 흐름을 검증했습니다. 이 모듈의 완료 점검 항목은 카탈로그 범위를 지키고 자격 증명과 Foundry 내부 식별자를 브라우저에 노출하지 않는, 로컬에서 테스트한 사이트 통합입니다. 프록시나 사이트의 프로덕션 배포가 아닙니다.

실습을 마치면 로컬 서비스를 중지하고 지속적인 비용이 발생하지 않도록 [Azure 리소스를 정리합니다][cleanup]. 그런 다음 핵심 워크숍의 [VS Code 개요][vscode-overview]로 돌아갑니다.

[previous-lesson]: ../2-build-and-deploy/
[cleanup]: ../#리소스-정리
[vscode-overview]: ../../
