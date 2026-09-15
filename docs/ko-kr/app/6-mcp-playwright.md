---
title: "Lesson 6 - Playwright MCP로 기능 검증"
description: "Customize에서 Playwright MCP를 구성하고 기존 기능 워크트리의 필터링을 브라우저에서 관찰합니다."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

이전 레슨에서는 프로젝트의 검사를 quality-checks 스킬로 묶어 실행했습니다. 이제 에이전트가 필터링 UI를 직접 관찰하도록 브라우저 접근 권한을 제공합니다. 동일한 필터링 세션, 워크트리, 브랜치를 유지합니다. 이 레슨은 브라우저 검증 근거를 추가하는 단계이며 다른 기능, 전체 테스트 스위트 실행, PR을 추가하지 않습니다.

이 레슨에서는 다음 작업을 수행합니다.

- Model Context Protocol (MCP)의 개념과 GitHub Copilot app에서 사용하는 방식을 이해합니다.
- **Customize**에서 Playwright MCP 서버를 추가합니다.
- 에이전트에게 브라우저를 조작하여 필터링 기능을 살펴보도록 요청합니다.

## 시나리오

단위 테스트와 엔드투엔드 테스트도 중요하지만 UI 업데이트를 검증하려면 실제로 UI와 상호 작용해야 합니다. Copilot이 사용자처럼 작업 중인 웹사이트를 사용하도록 하여 변경 작업을 더 자동화하고, 업데이트가 예상대로 작동한다는 확신을 높이려고 합니다.

## Model Context Protocol (MCP)이란?

[Model Context Protocol (MCP)][mcp-blog-post]은 AI 에이전트가 외부 도구 및 서비스와 통신하는 방법을 제공합니다. MCP를 사용하면 AI 에이전트가 외부 도구 및 서비스와 실시간으로 통신할 수 있습니다. 따라서 리소스를 사용하여 최신 정보에 접근하고 도구를 사용하여 사용자를 대신해 작업을 수행할 수 있습니다.

이러한 도구와 리소스에는 AI 에이전트와 외부 도구 및 서비스를 연결하는 MCP 서버를 통해 접근합니다. MCP 서버는 AI 에이전트와 외부 도구(예: 기존 API 또는 NPM 패키지 같은 로컬 도구) 간의 통신을 관리합니다. 각 MCP 서버는 AI 에이전트가 접근할 수 있는 서로 다른 도구 및 리소스 집합을 나타냅니다.

널리 사용되는 기존 MCP 서버의 예는 다음과 같습니다.

- [**GitHub MCP Server**](https://github.com/github/github-mcp-server): GitHub 리포지토리 관리를 위한 API 집합에 접근할 수 있게 합니다. AI 에이전트가 새 리포지토리 만들기, 기존 리포지토리 업데이트, 이슈 및 끌어오기 요청 관리 같은 작업을 수행할 수 있습니다.
- [**Playwright MCP Server**][playwright-mcp-server]: Playwright를 사용하는 브라우저 자동화 기능을 제공합니다. AI 에이전트가 웹페이지 이동, 양식 작성, 버튼 선택 같은 작업을 수행할 수 있습니다.

다양한 도구와 리소스에 접근할 수 있는 다른 MCP 서버도 많습니다. GitHub는 MCP 서버를 쉽게 찾고 생태계에 기여할 수 있도록 [MCP registry](https://github.com/mcp)를 호스팅합니다.

> [!CAUTION]
> MCP 서버를 프로젝트의 다른 종속성과 동일하게 취급합니다. MCP 서버를 사용하기 전에 소스 코드를 주의 깊게 검토하고, 게시자를 확인하고, 보안 영향을 고려합니다. 신뢰하는 MCP 서버만 사용하고 중요한 리소스나 작업에 대한 접근 권한을 부여할 때 주의합니다.

## Playwright MCP 서버 추가

현재 [App 사용자 지정 문서][customize-app]는 MCP 검색 및 관리에 사이드바의 **Customize**를 사용합니다. 리포지토리나 Copilot CLI에 구성한 MCP 서버를 App에서 이미 사용할 수도 있으므로 중복 추가 전에 설치된 서버를 확인합니다.

1. 사이드바에서 **Customize**를 선택합니다.
2. **MCP**를 선택한 다음 **Installed**에서 기존 Playwright 서버를 확인합니다.
3. 필요하면 사용 가능한 서버에서 **Playwright**를 찾거나 게시자가 문서화한 사용자 지정 서버 추가 절차를 사용합니다.
4. 게시자, 구성, 설치 요청을 검토한 후 승인합니다. 안내에 따라 서버를 추가합니다. 조직 정책이나 누락된 필수 조건으로 설정이 차단될 수 있습니다.
5. **Interactive** 모드를 유지한 채 기존 필터링 세션으로 돌아갑니다. 검증 요청 전에 Playwright MCP 브라우저 도구를 사용할 수 있는지 확인합니다. 설정 문제를 우회하려고 새 기능 워크트리를 만들지 않습니다.

설정이 실패하면 도구 없이 브라우저를 사용했다는 주장을 수락하지 말고 구성이나 권한 문제를 해결합니다. 브라우저 창의 표시 여부는 서버 구성에 따라 달라집니다. 실제 도구 활동과 관찰 결과가 검증 근거입니다.

## Copilot에 Playwright로 기능 탐색 요청

레슨 4에서 저장한 실제 이슈 URL과 승인한 추가 합의 사항을 사용합니다. 에이전트가 자체 서버를 시작하기 전에 이전 레슨에서 수동으로 시작한 개발 서버를 중지합니다. 에이전트는 테스트할 체크아웃과 서버를 식별해야 합니다.

1. 다음 프롬프트를 사용하여 새 기능을 검증하도록 Copilot에 요청합니다.

   ```plaintext
   구성된 Playwright MCP 서버를 사용하여 이 이슈를 기준으로 필터링 기능을 관찰해 주십시오: <filtering-issue-URL>. 계획에서 승인한 추가 합의 사항은 다음과 같습니다: <합의한 추가 사항을 붙여 넣거나 none 작성>. 이 필터링 워크트리와 브랜치를 유지해 주십시오.

   체크아웃을 식별하고 해당 개발 서버를 시작한 다음 실제 브라우저 도구로 필수 여러 카테고리 선택, 퍼블리셔 필터링, 조합 필터링, 접근성 있는 컨트롤, 합의한 초기화나 빈 결과 동작을 확인해 주십시오. 실패하거나 차단된 검사를 포함하여 기준에 따른 관찰 결과를 보고해 주십시오. 관찰하지 않은 동작을 확인했다고 주장하지 마십시오.

   이 단계는 브라우저 관찰이며 전체 자동 테스트를 다시 실행하는 단계가 아닙니다. 애플리케이션 코드, 테스트, 스킬, 에이전트 프로필을 변경하거나 커밋, 푸시, PR 생성을 하지 마십시오. 누락된 MCP 도구나 필수 조건은 차단으로 보고하고 설치 전에 질문해 주십시오. 다른 체크아웃의 서버를 재사용하거나 관련 없는 프로세스를 중지하지 마십시오. 완료하면 직접 시작한 서버만 중지해 주십시오.
   ```

Playwright MCP 도구 호출, 테스트한 URL, 보고한 브라우저 관찰 결과를 살펴봅니다. 소스 코드나 이전 E2E 결과만으로 작성한 설명은 MCP 사용을 입증하지 못합니다.

2. 이슈와 승인한 추가 합의 사항을 기준으로 요약을 읽습니다. 결함이 있으면 범위를 좁힌 수정을 별도로 승인하고 변경된 diff를 검토한 다음 관련 자동 검사와 브라우저 관찰을 반복합니다. 수정 전 근거는 수정된 리비전을 입증하지 못합니다.
3. 에이전트가 직접 시작한 서버를 중지했는지 확인합니다. 레슨 7에서 QA 프로필을 만들기 전까지 이 필터링 세션을 열어 두고 **Interactive** 모드를 유지합니다.

이 단계는 직접 관찰을 확보하며 자동 테스트 커버리지를 대체하지 않습니다. 실패하거나 차단된 관찰 결과를 QA에서 확인할 수 있도록 남겨 둡니다.

## 요약 및 다음 단계

GitHub Copilot app에서 Playwright MCP 서버를 사용하여 실제 브라우저로 기능을 살펴봤습니다. 요약하면 다음 작업을 수행했습니다.

- Model Context Protocol (MCP)의 개념과 앱에서 MCP 도구를 제공하는 방식을 배웠습니다.
- **Customize**에서 Playwright MCP 서버를 구성했습니다.
- 에이전트에게 브라우저를 조작하여 필터링 기능을 살펴보도록 요청했습니다.

다음으로 전문가 프로필을 통해 요구 사항, 브라우저 관찰, 커버리지, 스킬을 결합합니다. 동일한 세션에서 [레슨 7 - QA 에이전트 만들기 및 사용][next-lesson]을 계속 진행합니다. 아직 기능 PR을 만들지 않습니다.

## 리소스

- [MCP란 무엇이며 왜 모두가 이야기할까요?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [GitHub Copilot app에서 MCP 서버 구성][customize-app]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app