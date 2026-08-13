---
title: "연습 2 - 커스텀 지침(Copilot CLI)"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[← 이전 연습: Copilot CLI 설치][previous-lesson] · [다음 연습: CLI로 코드 생성하기 →][next-lesson]

생성형 AI로 작업할 때는 컨텍스트가 핵심입니다. 작업을 특정 방식으로 수행해야 하거나 Copilot이 알아야 할 배경 정보가 있다면, 그 컨텍스트를 사용할 수 있게 해야 합니다. Copilot을 돕는 여러 도구가 있으며, 이 워크숍 전반에서 이를 살펴봅니다. 먼저 [instruction files][instruction-files]부터 시작합니다. Instruction files는 일반적으로 코드 자체를 어떻게 구성해야 하는지에 초점을 맞춥니다. 이를 통해 Copilot은 원하는 코드가 *무엇인지*뿐 아니라 *어떻게* 구조화되어야 하는지도 이해할 수 있습니다.

이 연습에서는 다음을 수행합니다.

- 리포지토리 커스텀 지침과 경로 범위 지침 파일을 통해 프로젝트별 컨텍스트, 코딩 가이드라인, 문서화 표준이 Copilot에 전달되는 방식을 살펴봅니다.
- 현재 지침이 적용된 상태에서 필터링을 위한 첫 번째 데이터 조각인 publishers helper를 생성합니다.
- `.github/copilot-instructions.md`에 새로운 리포지토리 전체 표준을 추가합니다.
- 후속 프롬프트를 실행하고 재생성된 코드가 새 표준을 따르는 모습을 확인합니다.
- 다음 연습에서 이어서 사용할 수 있도록 지침 업데이트와 helper를 커밋합니다.

> [!CAUTION]
> 생성된 코드는 설정한 표준 일부와 다를 수 있습니다. Copilot은 비결정적입니다. 목표는 출력이 문자 단위로 완전히 일치하는 것이 아니라, 지침을 업데이트한 뒤 동작 경향이 어떻게 바뀌는지 확인하는 것입니다.

## 지침 파일

### 시나리오

훌륭한 개발 조직답게 Tailspin Toys에는 개발 관행에 대한 가이드라인과 요구 사항이 있습니다. 여기에는 다음이 포함됩니다.

- 데이터 계층에는 항상 단위 테스트가 필요합니다.
- UI는 dark mode여야 하며 현대적인 느낌을 제공해야 합니다.
- 코드 문서는 TSDoc doc comments 형태로 추가해야 합니다.
- 각 파일의 맨 앞에는 파일의 역할을 설명하는 주석 블록을 추가해야 합니다.

Instruction files를 사용하면 Copilot이 이러한 관행에 맞춰 작업을 수행하는 데 필요한 정보를 갖추도록 할 수 있습니다.

### 커스텀 지침

커스텀 지침을 사용하면 Copilot에 컨텍스트와 선호 사항을 제공하여 코딩 스타일과 요구 사항을 더 잘 이해하도록 도울 수 있습니다. 이 기능은 더 관련성 높은 제안과 코드 스니펫을 얻도록 Copilot의 방향을 조정하는 강력한 방법입니다. 선호하는 코딩 규칙, 라이브러리, 코드에 포함하고 싶은 주석 유형까지 지정할 수 있습니다. 전체 리포지토리에 대한 지침을 만들 수도 있고, 작업 수준 컨텍스트를 위해 특정 파일 형식에 대한 지침을 만들 수도 있습니다.

지침 파일에는 두 가지 유형이 있습니다.

- `.github/copilot-instructions.md`는 리포지토리에 대한 **모든** 요청에서 Copilot으로 전송되는 단일 지침 파일입니다. 이 파일에는 프로젝트 수준 정보, 즉 Copilot에 보내는 대부분의 채팅 또는 CLI 요청에 공통으로 관련된 컨텍스트를 담아야 합니다. 사용 중인 기술 스택, 빌드 중인 내용의 개요, 모범 사례, 기타 전역 가이드라인이 여기에 포함될 수 있습니다.
- `.github/instructions/*.instructions.md` 파일은 특정 작업이나 파일 형식을 위해 만들 수 있습니다. TypeScript나 Astro 같은 특정 언어에 대한 지침을 제공하거나, UI 컴포넌트 또는 새로운 단위 테스트 세트 생성 같은 작업에 대한 지침을 제공할 수 있습니다.

> [!NOTE]
> IDE에서 작업할 때 지침 파일은 Copilot Chat의 코드 생성에만 사용되며, code completions나 next-edit suggestions에는 사용되지 않습니다.
>
> Copilot Chat, Copilot CLI, Copilot cloud agent는 코드를 생성할 때 리포지토리 수준 지침과 `applyTo` front matter가 있는 `*.instructions.md` 파일을 모두 사용합니다.
>
> 또한 Copilot은 AGENTS.md와 CLAUDE.md를 포함한 [다른 표준의 지침 파일도 지원합니다][custom-instructions-support].

### 지침 파일 관리 모범 사례

지침 파일을 만드는 방법 전체를 이 워크숍에서 모두 다루지는 않습니다. 하지만 샘플 프로젝트에 포함된 예시는 대표적인 접근 방식을 보여 줍니다. 높은 수준에서 보면 다음과 같습니다.

- `copilot-instructions.md`의 지침은 빌드 중인 내용의 설명, 프로젝트 구조, 전역 코딩 표준처럼 프로젝트 수준 가이드에 집중합니다.
- `*.instructions.md` 파일은 파일 형식(단위 테스트, Astro 컴포넌트, 데이터 계층)이나 특정 작업에 대한 구체적인 지침을 제공하는 데 사용합니다.
- 자연어를 사용합니다. 가이드는 명확하게 유지합니다. 코드가 어떻게 보여야 하는지와 어떻게 보이면 안 되는지에 대한 예시를 제공합니다.

AI를 사용하는 방법이 하나로 정해져 있지 않듯, 지침 파일을 만드는 방법도 하나로 정해져 있지 않습니다. 실험을 통해 프로젝트에 가장 잘 맞는 방식을 찾게 됩니다.

> [!TIP]
> GitHub Copilot을 사용하는 모든 프로젝트에는 탄탄한 instruction files 모음이 있어야 합니다. 이 프로젝트의 instruction files를 살펴보면 [UI 업데이트][ui-instructions]와 [Astro][astro-instructions]를 포함해 다양한 작업 유형에 대한 파일이 있다는 점을 확인할 수 있습니다.
>
> Copilot은 instruction files 생성도 도와줄 수 있습니다. 각 표면마다 노출 방식은 다르지만(예: VS Code의 **Configure Chat → Generate Agent Instructions**, Copilot CLI의 `/init`) 관련이 있는 경우 현재 사용 중인 표면의 연습에서 이를 안내합니다.
>
> 템플릿이나 시작점을 찾고 있나요? Instruction files, custom agents, 기타 리소스를 모아 둔 리포지토리인 [awesome-copilot][awesome-copilot]을 살펴봅니다.

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
## 이 프로젝트의 커스텀 지침 파일 살펴보기

잠시 시간을 내어 이 리포지토리에 포함된 지침 파일을 읽어 봅니다. 핵심 `copilot-instructions.md` 하나와 다양한 작업을 위한 `*.instructions.md` 파일 모음이 있습니다. 편집기 또는 GitHub 웹 UI에서 열어 봅니다.

1. `.github/copilot-instructions.md`를 엽니다.
2. 파일을 살펴보면서 프로젝트의 간단한 설명과 **Agent notes**, **Code standards**, **Scripts**, **Repository Structure** 같은 섹션을 확인합니다. **Code standards** 아래에 중첩된 **GitHub Actions Workflows** 가이드가 있다는 점에 주목합니다. 이 내용은 Copilot과 상호 작용할 때 전반적으로 적용됩니다.
3. `.github/instructions` 폴더를 열어 둘러봅니다. Astro 파일, Drizzle 데이터 계층, 테스트 등 다양한 지침이 있는지 확인합니다.
4. `.github/instructions/unit-tests.instructions.md`를 엽니다. 상단의 `applyTo` 필드를 확인합니다. 이 필드는 지침이 적용될 파일을 결정하는 glob(리포지토리 루트 기준)을 설정합니다. 여기서는 모든 TypeScript test 파일(예: `**/*.test.ts`와 일치하는 파일)에 적용됩니다.
5. 이 프로젝트에서 단위 테스트를 만들 때 적용되는 구체적인 지침을 확인합니다.
6. 마지막으로 `.github/instructions/drizzle.instructions.md`를 열고 맨 아래로 스크롤합니다. 다른 지침 파일(`unit-tests.instructions.md` 등)과 프로젝트의 기존 파일에 대한 링크가 있는지 확인합니다. 이렇게 하면 더 큰 지침 세트를 더 작고 재사용 가능한 파일로 나눌 수 있고, 코드 생성 시 Copilot이 따를 예시를 가리킬 수 있습니다. (해당 경로는 리포지토리 루트가 아니라 지침 파일 기준 상대 경로입니다.)

> [!NOTE]
> `copilot-instructions.md`의 **Code formatting requirements** 섹션에는 프로젝트 코딩 표준이 문서화되어 있지만, 아직 코드 내부 문서화는 요구하지 않습니다. 다음 단계에서 TSDoc doc comments와 파일 주석 헤더에 대한 규칙을 추가합니다.

## 브랜치 만들기

코드를 변경할 예정이므로 작업용 브랜치를 만듭니다.

1. 코드스페이스 터미널에서 새 브랜치를 만들고 전환합니다.

   ```bash
   git checkout -b update-custom-instructions
   ```

2. Copilot CLI가 설치 및 인증되었는지 확인합니다.

   ```bash
   copilot --version
   ```

   명령을 찾을 수 없거나 아직 로그인하지 않았다면 [연습 1 - GitHub Copilot CLI 설치](../1-install-copilot-cli/)로 돌아갑니다.

## 지침을 업데이트하기 *전*에 Copilot CLI 사용하기

커스텀 지침의 영향을 확인하려면 먼저 현재 지침이 적용된 상태에서 코드를 생성합니다. 이후 파일을 업데이트하고 후속 프롬프트를 실행합니다.

> [!TIP]
> **Copilot CLI 세션 시작하기**
>
> 아래 연습을 시작하기 전에 코드스페이스로 돌아가 터미널을 엽니다(이미 열려 있지 않다면 <kbd>Ctrl</kbd>+<kbd>`</kbd>). 그런 다음 `--yolo`와 `--enable-all-github-mcp-tools`를 사용해 Copilot CLI를 시작합니다.
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 이 프로젝트의 가장 최근 세션을 새로 시작하지 않고 이어서 사용하려면 `copilot --yolo --enable-all-github-mcp-tools --continue`를 실행합니다. 이전 연습에서 Copilot CLI가 이미 실행 중이라면 `/clear`를 보내 새 대화를 시작합니다.
>
> `--enable-all-github-mcp-tools`는 현재 세션에서 읽기/쓰기 GitHub MCP 도구를 활성화하므로, 워크숍 흐름 중 Copilot이 백로그를 읽고 pull request를 열 수 있습니다.

> [!CAUTION]
> `--yolo`는 전체 자동 권한(`--allow-all-tools`, `--allow-all-paths`, `--allow-all-urls`)을 활성화합니다. Codespace나 VM 같은 격리된 환경에서만 사용하고, 일상적인 개발을 위한 기본 별칭으로는 절대 설정하지 않습니다. 자세한 내용은 [Allowing and denying tool use][allow-all-warning]를 참고합니다.

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
1. Copilot CLI 세션이 **repository root**에서 실행 중인지 확인합니다. 그래야 `.github/copilot-instructions.md`를 자동으로 불러옵니다.
2. Copilot CLI 프롬프트에서 필터링 UI가 사용할 publishers helper를 생성해 달라고 요청합니다.

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

3. Copilot CLI는 프로젝트를 탐색하고, 계획을 제안하고, 이 `--yolo` 세션에서 파일을 작성합니다. 터미널 출력의 변경 내용을 확인한 뒤 편집기에서 검토합니다.
4. 편집기에서 생성된 `src/lib/publishers.ts`를 엽니다.
5. helper가 첫 번째 인수로 `db` client를 받고, publisher의 typed array를 반환하는 typed function이라는 점을 확인합니다. 이는 `src/lib/*.ts`에 적용되는 `.github/instructions/drizzle.instructions.md`의 데이터 계층 규칙에서 비롯됩니다.
6. 생성된 코드에 TSDoc doc comments와 파일 수준 주석 헤더가 **없다**는 점을 확인합니다.

> [!CAUTION]
> Copilot은 확률적으로 동작하므로, 지시하지 않았더라도 doc comments를 추가할 가능성이 있습니다. 그런 경우에도 괜찮습니다. 지침 업데이트 후 *일관성*이 향상되는 점이 핵심입니다.

## 새로운 리포지토리 표준 추가하기

앞서 설명했듯이 `.github/copilot-instructions.md`는 Copilot에 프로젝트 수준 정보를 제공하도록 설계되었습니다. 이제 리포지토리 코딩 표준을 문서화해 코드 제안을 개선해 보겠습니다.

1. `.github/copilot-instructions.md`를 다시 엽니다.
2. **Code formatting requirements** 섹션을 찾습니다. 대략 27번째 줄 근처에 있을 것입니다. 이 섹션이 프로젝트의 코딩 표준을 문서화하고 있지만, 아직 코드 내부 문서화 규칙이 없기 때문에 생성된 helper에 doc comments가 없었다는 점을 확인합니다.
3. 기존 표준 바로 아래에 다음 markdown 줄을 추가해 Copilot이 파일 주석 헤더와 TSDoc doc comments를 넣도록 지시합니다.

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. `copilot-instructions.md`를 저장합니다.

> [!TIP]
> 이전 연습에서 본 것처럼 지침 파일은 전역 가이드를 위한 리포지토리 수준(`.github/copilot-instructions.md`)으로 만들 수도 있고, 특정 언어, 파일 형식, 작업을 위한 `*.instructions.md` 파일로 만들 수도 있습니다. 방금 추가한 doc comment 규칙처럼 프로젝트 전반에 적용되는 표준은 리포지토리 수준 파일에 두는 것이 적절합니다.

## 프롬프트를 다시 실행하고 변화를 관찰하기

이제 지침에 doc comment 규칙이 추가되었으므로 방금 생성한 publishers 파일을 Copilot CLI로 업데이트해 보겠습니다. 동일한 표준 지시가 다시 작성된 코드에도 적용됩니다.

1. Copilot CLI 세션에서 `/clear`를 보내 새 대화를 시작합니다.
2. 다음 프롬프트를 보냅니다.

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. 편집이 완료되면 `src/lib/publishers.ts`를 다시 엽니다.
4. 이제 파일 맨 앞에 다음과 비슷한 주석 블록이 추가된 점을 확인합니다.

   ```typescript
   /**
    * Publisher data-access helpers for the Tailspin Toys Crowd Funding platform.
    * Provides functions to retrieve publisher information from the database.
    */
   ```

5. 생성된 함수에 이제 다음과 비슷한 TSDoc doc comment가 포함된 점을 확인합니다.

   ```typescript
   /**
    * Returns a list of all publishers with their id and name.
    *
    * @param db - The Drizzle database client.
    * @returns A promise that resolves to an array of publisher objects.
    */
   ```

6. 업데이트된 파일은 그대로 유지합니다. 다음 연습에서 이 파일을 기반으로 첫 번째 데이터 조각을 확장합니다.

## 첫 번째 필터링 조각 커밋 및 푸시하기

1. 터미널에서 변경된 파일을 확인합니다.

   ```bash
   git status
   ```

2. 지침 업데이트와 helper를 stage합니다.

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. 변경 사항을 커밋합니다.

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. 브랜치를 푸시합니다.

   ```bash
   git push -u origin update-custom-instructions
   ```

## 요약 및 다음 단계

이 프로젝트의 지침 파일을 통해 Copilot이 어떻게 컨텍스트를 받아들이는지 살펴본 다음, Copilot CLI를 사용해 다음을 수행했습니다.

- 기존 지침을 바탕으로 필터링용 publishers data-access helper 기반을 생성했습니다.
- `.github/copilot-instructions.md`에 새로운 리포지토리 전체 표준을 추가했습니다.
- 후속 프롬프트를 실행하고 재생성된 코드가 새 표준을 따르는 모습을 확인했습니다.
- 지침 업데이트와 helper 기반을 모두 커밋하고 푸시했습니다.

다음으로는 [코드 생성 연습][next-lesson]에서 백로그 작업을 구현하면서 이 지침을 적용합니다.

## 리소스

- [GitHub Copilot 사용자 지정을 위한 instruction files][instruction-files]
- [커스텀 지침 작성 모범 사례][instructions-best-practices]
- [Copilot용 더 나은 커스텀 지침을 작성하는 5가지 팁][copilot-instructions-five-tips]
- [Instruction files와 기타 리소스를 모아 둔 Awesome Copilot][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
