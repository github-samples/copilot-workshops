---
title: "Lesson 3 - 사용자 지정 지침으로 Copilot 안내"
description: "문서화 표준을 추가하고 작은 기존 도우미나 구성 요소에서 시연한 다음 둘을 두 번째 끌어오기 요청으로 병합합니다."
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

생성형 AI를 사용할 때는 컨텍스트가 중요합니다. 작업을 특정 방식으로 수행해야 하거나 Copilot이 알아야 할 배경 정보가 있다면 해당 컨텍스트를 제공해야 합니다. 가장 강력한 도구 중 하나는 원하는 코드의 *내용*뿐 아니라 코드의 *구조*도 설명하는 [지침 파일][instruction-files]입니다. 이 레슨에서는 리포지토리에 문서화 표준을 추가합니다. 이후 대부분의 작업과 마찬가지로 백로그의 이슈에서 시작하여 에이전트가 변경하도록 합니다.

이 레슨에서는 다음 작업을 수행합니다.

- 리포지토리 지침과 경로 범위 지침 파일이 에이전트에 전달되는 방식을 살펴봅니다.
- 백로그의 지침 이슈에서 세션을 시작합니다.
- 에이전트에게 적절한 리포지토리 지침 파일에 범위를 좁힌 문서화 표준을 추가하도록 요청합니다.
- 작은 실제 코드 변경으로 표준을 시연하고 검증한 다음 PR 2를 병합합니다.

## 시나리오

모범적인 개발 조직인 Tailspin Toys에는 개발 방식에 관한 지침과 요구 사항이 있습니다. 여기에는 다음 항목이 포함됩니다.

- 주석은 코드를 다시 설명하기보다 의도와 명확하지 않은 결정을 설명해야 합니다.
- `db/`와 `src/lib/`에서 내보내는 함수는 TSDoc/JSDoc으로 목적, 매개 변수, 반환값을 문서화하고, 주입 가능한 `db` 인수가 있다면 함께 설명해야 합니다.
- 재사용 가능한 Astro 구성 요소는 `Props` 계약을 문서화하고, 관련 코드가 바뀌면 주석도 최신 상태로 유지해야 합니다.
- 기존 서식과 린트 지침을 보존해야 합니다.

지침 파일을 사용하면 Copilot이 이러한 방식에 맞게 작업을 수행하는 데 필요한 정보를 제공할 수 있습니다.

## 지침 파일

사용자 지정 지침은 Copilot에 컨텍스트와 기본 설정을 제공하여 코딩 스타일과 요구 사항을 더 잘 이해하게 합니다. 이 기능을 사용하면 Copilot이 더 관련성 높은 제안과 코드 조각을 생성하도록 안내할 수 있습니다. 선호하는 코딩 규칙과 라이브러리는 물론 코드에 포함할 주석 유형까지 지정할 수 있습니다. 리포지토리 전체에 적용되는 지침이나 작업 수준의 컨텍스트를 제공하는 특정 파일 유형용 지침을 만들 수 있습니다.

이 프로젝트는 두 종류의 지침 파일을 사용합니다.

- `.github/copilot-instructions.md`는 리포지토리의 **모든** 요청에서 Copilot에 전달되는 단일 지침 파일입니다. 이 파일에는 Copilot에 보내는 대부분의 채팅 또는 CLI 요청과 관련된 프로젝트 수준 정보를 포함해야 합니다. 사용 중인 기술 스택, 구축 중인 항목의 개요, 모범 사례, 기타 전역 지침을 포함할 수 있습니다.
- 특정 작업이나 파일 유형에 맞게 `.github/instructions/*.instructions.md` 파일을 만들 수 있습니다. TypeScript 또는 Astro 같은 특정 언어나 UI 구성 요소 또는 새 단위 테스트 집합 만들기와 같은 작업에 관한 지침을 제공할 수 있습니다.

> [!NOTE]
> 다른 지침 형식과 지원 여부는 하네스에 따라 다릅니다. 특정 형식에 의존하기 전에 [사용자 지정 지침 지원 참조][custom-instructions-support]를 확인합니다.

### 지침 파일 관리 모범 사례

지침 파일 만들기를 모두 다루는 것은 이 워크숍의 범위를 벗어납니다. 하지만 샘플 프로젝트의 예제는 대표적인 접근 방식을 보여 줍니다. 개괄적인 지침은 다음과 같습니다.

- `copilot-instructions.md`의 지침은 구축 중인 항목의 설명, 프로젝트 구조, 전역 코딩 표준 등 프로젝트 수준의 안내에 집중합니다.
- `*.instructions.md` 파일을 사용하여 파일 유형(단위 테스트, Astro 구성 요소, 데이터 계층) 또는 특정 작업에 관한 구체적인 지침을 제공합니다.
- 자연어를 사용하고 지침을 명확하게 유지합니다. 코드가 따라야 하는 예와 피해야 하는 예를 제공합니다.

AI를 사용하는 방식이 하나로 정해져 있지 않듯 지침 파일을 만드는 방식도 하나로 정해져 있지 않습니다. 실험을 통해 프로젝트에 가장 적합한 방법을 찾을 수 있습니다.

> [!TIP]
> GitHub Copilot을 사용하는 모든 프로젝트에는 충실한 지침 파일 모음이 있어야 합니다. 이 프로젝트의 파일을 살펴보면 여러 코드 파일 유형을 위한 지침 파일이 있다는 것을 알 수 있습니다.
>
> 템플릿이나 시작점을 찾고 있습니까? 지침 파일, 사용자 지정 에이전트, 기타 리소스가 가득한 리포지토리인 [awesome-copilot][awesome-copilot]을 살펴봅니다.

## 프로젝트의 사용자 지정 지침 파일 살펴보기

이 리포지토리와 함께 제공되는 지침 파일을 읽어 봅니다. 핵심 `copilot-instructions.md` 하나와 여러 작업을 위한 `*.instructions.md` 파일 모음이 있습니다. 편집기 또는 GitHub 웹 UI에서 파일을 엽니다.

1. 검토 패널이 표시되지 않으면 오른쪽 위의 **Toggle review panel**을 선택하여 엽니다.

   ![Create PR 오른쪽의 Toggle review panel 버튼을 화살표로 가리키는 GitHub Copilot app 위쪽 도구 모음](../../_images/app-2-review-panel.png)

2. 검토 패널에 새 항목을 추가하려면 **+**를 선택합니다.
3. **File**을 선택합니다.
4. `copilot-instructions.md`를 검색합니다.
5. 파일 목록에서 `copilot-instructions.md`를 선택하여 엽니다.
6. 파일을 살펴봅니다. 프로젝트에 관한 간단한 설명과 **Agent notes**, **Code standards**, **Scripts**, **Repository Structure** 같은 섹션을 확인합니다. **Code standards** 아래에서 중첩된 **GitHub Actions Workflows** 지침을 확인합니다. 이 내용은 Copilot과의 모든 상호 작용에 적용됩니다.
7. 폴더 탐색기를 열려면 **Show folder view**를 선택합니다.

   ![GitHub Copilot app에서 파일이 열린 검토 패널의 Show folder view 버튼](../../_images/app-show-folder-view.png)

8. `.github/instructions` 폴더로 이동하여 파일을 살펴봅니다. Astro 파일, Drizzle 데이터 계층, 테스트 등에 관한 지침이 있습니다.
9. `.github/instructions/unit-tests.instructions.md`를 엽니다. 위쪽의 `applyTo` 필드는 지침이 적용되는 파일을 결정하는 glob을 리포지토리 루트 기준으로 설정합니다. 여기서는 TypeScript 테스트 파일(예: `**/*.test.ts`와 일치하는 파일)이 모두 일치합니다.
10. 이 프로젝트의 단위 테스트 작성에 관한 구체적인 지침을 확인합니다.
11. 마지막으로 `.github/instructions/drizzle.instructions.md`를 열고 아래쪽으로 스크롤합니다. 다른 지침 파일(예: `unit-tests.instructions.md`)과 프로젝트의 기존 파일로 연결되는 링크를 확인합니다. 이를 통해 큰 지침 집합을 더 작고 재사용 가능한 파일로 나누고 Copilot이 코드를 생성할 때 따를 예제를 지정할 수 있습니다. 이 경로는 리포지토리 루트가 아니라 지침 파일을 기준으로 합니다.

> [!NOTE]
> 규칙을 추가하기 전에 기존 지침과 실제 코딩 표준 이슈를 비교합니다. 이 레슨은 일률적인 파일 헤더나 코드를 다시 설명하는 주석이 아니라 의도 중심 주석, 내보내는 데이터 계층 함수 문서화, Astro `Props` 계약에 집중합니다.

## 지침 이슈에서 시작

이 세션을 만들기 전에 PR 1이 병합되었는지 확인합니다. PR 2용 새 워크트리에서 시작하고 별점 브랜치에서 계속하지 않습니다. 대부분의 작업은 이슈에서 시작하므로 코딩 표준 이슈를 요구 사항으로 사용합니다.

> [!NOTE]
> 지침 파일은 Copilot이 생성하는 코드에 큰 영향을 주므로 Copilot을 명확하게 안내하는지 주의 깊게 확인해야 합니다. 이 레슨처럼 Copilot으로 초안을 만든 다음 요구 사항을 충족하는지 직접 검토하는 방법이 좋습니다.

1. 사이드바에서 **My work**를 선택합니다.
2. **Update our repository coding standards** 이슈를 선택하여 엽니다.
3. 오른쪽 위의 **New session**을 선택하고 **new working tree**와 **Interactive** 모드를 선택합니다.

   ![오른쪽 위의 New session 버튼을 화살표로 가리키는 GitHub Copilot app 이슈 보기](../../_images/app-new-session-from-issue.png)

4. 다음 프롬프트를 사용합니다. 편집 전에 새 세션 브랜치를 업데이트하면 앱의 로컬 체크아웃이 오래되었더라도 최근 병합된 `main`에서 실제로 시작할 수 있습니다.

   ```plaintext
   편집하기 전에 이 체크아웃과 브랜치를 식별하고 미커밋 변경이 없는 새 워크트리인지 확인한 다음 origin을 가져오고 이 세션 브랜치를 origin/main으로 fast-forward해 주십시오. HEAD가 origin/main과 일치하며 병합된 별점 PR을 포함하는지 확인해 주십시오. 미커밋 변경이나 분기가 있거나 해당 병합이 누락되었으면 중단해 주십시오. 재설정하거나 작업을 버리거나 다른 브랜치를 만들지 마십시오.

   "Update our repository coding standards" 이슈와 기존 리포지토리 지침을 읽어 주십시오. 범위를 좁힌 문서화 규칙을 추가해 주십시오. 작동 방식보다 의도를 설명하고, db/와 src/lib/에서 내보내는 함수를 TSDoc/JSDoc으로 문서화하여 목적, 매개 변수, 반환값, 존재하는 경우 주입 가능한 db 인수를 다뤄 주십시오. 재사용 가능한 Astro 구성 요소의 Props 계약을 문서화하고 관련 코드 변경 시 주석도 최신 상태로 유지하도록 해 주십시오.

   중복이나 모순 없이 각 규칙을 적절한 기존 지침 파일에 배치하고 README에서 업데이트된 표준을 링크하거나 요약해 주십시오. 기존 서식과 린트 지침을 보존해 주십시오. 일률적인 파일 헤더를 요구하거나 서식 도구를 이전하거나 애플리케이션 전체의 문서를 다시 작성하거나 필터링을 구현하지 마십시오. 지침 diff를 보여 준 다음 검토를 위해 중단해 주십시오. 스킬이나 에이전트를 만들거나 커밋, 푸시, PR 생성을 하지 마십시오.
   ```

Copilot이 업데이트를 적용합니다.

## 변경 내용 검토

업데이트된 지침을 읽고 실제 파일에서 효과를 시연합니다. 코드 조각을 제안하는 것만으로는 리포지토리 지침이 코드 변경에 영향을 미쳤음을 보여 줄 수 없습니다.

1. 오른쪽 위의 **Changes**를 선택하여 코드 변경 내용을 엽니다.

   ![Changes 탭을 화살표로 가리키는 GitHub Copilot app 세션 패널 탭](../../_images/app-select-changes.png)

2. 업데이트된 지침 파일과 README 참조를 검토합니다. 일률적인 파일 헤더 요구 사항을 만들지 않고 이슈의 주석 철학, 내보내는 함수 문서화, 구성 요소 계약에 규칙이 맞는지 확인합니다.

> [!NOTE]
> AI는 결정론적이 아니라 확률적으로 작동하므로 정확한 텍스트는 달라질 수 있습니다.

3. 지침을 검토한 후 동일한 세션에서 범위를 제한한 시연을 요청합니다.

   ```plaintext
   db/ 또는 src/lib/에서 내보내는 작은 기존 TypeScript 도우미 하나나 재사용 가능한 Astro 구성 요소 하나에서 업데이트된 문서화 규칙을 시연해 주십시오. 리포지토리를 살펴보고 적절한 기존 파일을 선택해 주십시오. publishers 도우미가 있다고 가정하지 마십시오. 동작을 보존하는 작은 가독성 개선을 적용하고 관련 함수 문서화 또는 Props 계약 지침을 적용해 주십시오. 코드를 다시 설명하기만 하는 주석을 추가하지 말고 명확하지 않은 의도를 설명해 주십시오.

   변경 범위를 해당 시연과 직접 관련된 테스트로 제한해 주십시오. 필터링을 구현하거나 새 기능을 만들지 마십시오. 관련된 기존 npm 검사를 실행하고, 변경 내용과 지침이 코드에 미친 영향을 보고한 다음 검토를 위해 중단해 주십시오. 설치 전에 질문해 주십시오. 커밋, 푸시, PR 생성은 하지 마십시오.
   ```

4. 채팅 응답뿐 아니라 실제 파일 diff를 검토합니다. 문서가 실제 동작을 설명하는지, 가독성 변경이 동작을 보존하는지 확인합니다. 관련 테스트, 린트, 타입 검사 결과를 검토하고 실패를 해결한 후 계속합니다.

이제 프로젝트의 지침 파일을 업데이트하고 그 영향을 확인했습니다.

## 끌어오기 요청 열기 및 병합

지침 파일은 리포지토리 자산이므로 팀의 다른 구성원과 공유됩니다. 다른 자산과 마찬가지로 작업 내용이 포함된 PR을 만듭니다.

먼저 검토한 지침과 시연을 함께 승인합니다.

```plaintext
관련 테스트를 포함하여 코딩 표준 지침, README 참조, 범위를 제한한 코드 시연의 전체 diff를 검토해 주십시오. 검증 결과를 요약하고 검토한 변경을 이 세션 브랜치에 커밋해 주십시오. 브랜치를 푸시하고 리포지토리의 PR 템플릿을 사용하며 코딩 표준 이슈를 연결하여 main을 대상으로 끌어오기 요청 하나를 만들어 주십시오. 이슈의 모든 수락 기준을 충족하지 않았다면 부분 기여로 설명하고, 미완료 작업에는 이슈를 닫는 키워드를 사용하지 마십시오. 병합하지 마십시오.
```

1. 세션의 PR 링크를 엽니다. 앱에 **Create PR** 확인이 표시되면 중복 PR을 만들지 않고 이를 선택합니다.
2. 메시지가 표시되면 **Sign in with your browser**를 선택하고 안내에 따라 인증합니다.
3. Copilot이 PR을 만들기 시작합니다.

**My work**에서 지침과 코드 변경을 모두 포함한 전체 PR diff를 살펴봅니다. 학습용 리포지토리의 CI 결과와 필수 검토를 확인합니다. 실패를 해결한 후 **Ready to merge**를 선택합니다. CI는 시연이나 직접 검토를 대체하지 않습니다.

4. **Ready to merge**를 선택합니다.
5. 새 대화 상자에서 **Merge pull request**를 선택하여 끌어오기 요청을 병합합니다.

> [!NOTE]
> 필터링을 시작하기 전에 PR 2가 `main`에 병합되었는지 확인합니다. 새 워크트리만으로 최신 코드를 보장할 수는 없습니다. 레슨 4에서 원격 내용을 가져오고 새 세션 브랜치를 `origin/main`으로 fast-forward한 다음 앞선 두 병합이 모두 포함되었는지 확인한 후 계획합니다.

## 요약 및 다음 단계

앱이 지침 파일에서 컨텍스트를 가져오는 방식을 살펴본 다음 세션을 사용하여 리포지토리 전체에 적용되는 표준을 추가하고 병합했습니다. 구체적으로 다음 작업을 수행했습니다.

- 리포지토리의 `copilot-instructions.md`와 경로 범위 `*.instructions.md` 파일을 살펴봤습니다.
- 백로그의 지침 이슈에서 세션을 시작했습니다.
- 에이전트에게 적절한 지침 파일에 범위를 좁힌 문서화 규칙을 추가하고 README에서 참조하도록 요청했습니다.
- 실제 코드 변경에 표준이 미친 영향을 살펴보고 결과를 검증한 다음 둘을 PR 2로 병합했습니다.

다음으로 새 세션에서 필터링 기능을 구축하고 방금 병합한 표준을 따르는지 확인합니다. [레슨 4 - Plan과 Autopilot으로 필터링 구축][next-lesson]을 계속 진행합니다.

## 리소스

- [GitHub Copilot 사용자 지정을 위한 지침 파일][instruction-files]
- [GitHub Copilot app 사용자 지정][customize-app]
- [사용자 지정 지침 만들기 모범 사례][instructions-best-practices]
- [Awesome Copilot — 지침 파일 및 기타 리소스 모음][awesome-copilot]

[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-build-filtering/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests