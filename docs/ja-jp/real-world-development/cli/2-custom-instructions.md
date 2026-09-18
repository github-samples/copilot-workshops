---
title: "演習 2 - カスタム命令 (Copilot CLI)"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[← 前のレッスン: Copilot CLI のインストール][previous-lesson] · [次のレッスン: CLI でコードを生成する →][next-lesson]

生成 AI を使って作業するときは、コンテキストが重要です。特定のやり方で進める必要があるタスクや、Copilot に知っておいてほしい背景情報がある場合は、そのコンテキストを確実に渡すことが大切です。Copilot を補助するためのツールはいくつかあり、このワークショップ全体で確認していきます。最初に取り上げるのは [instruction file][instruction-files] です。instruction file は通常、コードそのものをどのように構成すべきかに重点を置きます。これにより、どのようなコードが必要かだけでなく、どのように構成すべきかも Copilot に理解させられます。

この演習では、次のことを行います。

- リポジトリの custom instruction と、パス単位で適用される instruction file を通じて、プロジェクト固有のコンテキスト、コーディング ガイドライン、ドキュメント標準がどのように Copilot に渡るかを確認する。
- *現在の* instruction のまま、フィルタリングの最初のデータ スライス（publishers helper）を生成する。
- `.github/copilot-instructions.md` に、リポジトリ全体に適用される新しい標準を追加する。
- フォローアップのプロンプトを実行し、再生成されたコードが新しい標準を取り入れる様子を確認する。
- instruction の更新と helper を commit し、次の演習でその続きに取り組めるようにする。

> [!CAUTION]
> 生成されたコードは、設定した標準から外れることがあります。Copilot は非決定的です。目的は、instruction を更新したあとに振る舞いの傾向がどう変わるかを確認することであり、出力を 1 文字単位で一致させることではありません。

## Instruction files

### シナリオ

優れた開発チームと同様に、Tailspin Toys にも開発プラクティスに関するガイドラインと要件があります。たとえば次のような内容です。

- データ レイヤーには常に unit test が必要です。
- UI はダーク モードで、モダンな印象にする必要があります。
- ドキュメントは TSDoc の doc comment としてコード内に追加する必要があります。
- 各ファイルの先頭には、そのファイルの役割を説明するコメント ブロックを追加する必要があります。

Instruction file を使うことで、これらのプラクティスに沿ってタスクを実行するために必要な情報を Copilot に確実に渡せます。

### Custom instructions

Custom instruction を使うと、コンテキストや設定を Copilot に渡せるため、コーディング スタイルや要件をより正確に理解させられます。これは非常に強力な機能であり、より関連性の高い提案やコード スニペットを Copilot から引き出すのに役立ちます。好みのコーディング規約、使用するライブラリ、含めたいコメントの種類まで指定できます。instruction はリポジトリ全体に対して作成することも、タスク レベルのコンテキストとして特定のファイル種別向けに作成することもできます。

instruction file には 2 種類あります。

- `.github/copilot-instructions.md` は、リポジトリへの**すべて**のリクエストで Copilot に送られる単一の instruction file です。このファイルにはプロジェクト レベルの情報、つまり Copilot に送るほとんどの chat や CLI リクエストに関連するコンテキストを含める必要があります。たとえば、使用している技術スタック、作成中のものの概要、ベスト プラクティス、その他のグローバル ガイダンスなどです。
- `.github/instructions/*.instructions.md` ファイルは、特定のタスクやファイル種別向けに作成できます。TypeScript や Astro のような特定の言語向けガイドラインや、UI component 作成、unit test 追加などのタスク向けガイドラインを提供するために使えます。

> [!NOTE]
> IDE で作業している場合、instruction file は Copilot Chat でのコード生成にのみ使用されます。コード補完や next-edit suggestion には使われません。
>
> Copilot Chat、Copilot CLI、Copilot cloud agent は、コード生成時にリポジトリ レベルの instruction file と `*.instructions.md` ファイル（`applyTo` front matter 付き）の両方を使用します。
>
> さらに、Copilot は [ほかの標準を使った instruction file][custom-instructions-support] もサポートしており、AGENTS.md や CLAUDE.md ファイルも利用できます。

### Instruction file を管理するためのベスト プラクティス

instruction file の作成に関する詳しい説明は、このワークショップの範囲外です。ただし、サンプル プロジェクトに含まれている例は、代表的なアプローチを示しています。大まかには次のとおりです。

- `copilot-instructions.md` の instruction は、何を作っているかの説明、プロジェクト構造、グローバルなコーディング標準など、プロジェクト レベルのガイダンスに集中させます。
- `*.instructions.md` ファイルは、ファイル種別（unit test、Astro component、データ レイヤー）や特定のタスク向けに、具体的な instruction を提供するために使います。
- 自然言語を使います。ガイダンスは明確に保ちます。コードの望ましい形と望ましくない形の両方の例を示します。

instruction file の作り方に唯一の正解があるわけではなく、AI の使い方にも唯一の正解はありません。試行錯誤しながら、自分のプロジェクトに最適な方法を見つけてください。

> [!TIP]
> GitHub Copilot を使うすべてのプロジェクトには、充実した instruction file のセットがあるべきです。このプロジェクトの instruction file を見ていくと、[UI 更新][ui-instructions] や [Astro][astro-instructions] など、多くの種類のタスク向けのファイルがあることに気づくかもしれません。
>
> Copilot は instruction file の生成も支援できます。各 surface で公開方法は異なります（たとえば VS Code の **Configure Chat → Generate Agent Instructions** や、Copilot CLI の `/init` など）。現在使用している surface のレッスンで、関係がある場面に案内があります。
>
> テンプレートや出発点を探していますか。instruction file、custom agent、そのほかのリソースが集まったリポジトリ [awesome-copilot][awesome-copilot] を確認してください。

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
## このプロジェクトの custom instruction file を確認する

このリポジトリに含まれている instruction file をひととおり読んでみましょう。中核となる `copilot-instructions.md` が 1 つあり、さまざまなタスク向けの `*.instructions.md` ファイル群があります。エディターまたは GitHub の Web UI で開いて確認します。

1. `.github/copilot-instructions.md` を開きます。
2. ファイルを確認し、プロジェクトの簡潔な説明に加えて、**Agent notes**、**Code standards**、**Scripts**、**Repository Structure** などのセクションに注目します。**Code standards** の中にある **GitHub Actions Workflows** に関するガイダンスにも注目してください。これらは Copilot とのあらゆるやり取りに適用されます。
3. `.github/instructions` フォルダーを開いて中を見てみます。Astro ファイル、Drizzle データ レイヤー、test などに関する instruction があることを確認してください。
4. `.github/instructions/unit-tests.instructions.md` を開きます。先頭にある `applyTo` フィールドに注目してください。ここには、どのファイルに instruction を適用するかを決める glob パターン（repo root からの相対パス）が設定されています。この例では、任意の TypeScript test ファイル（たとえば `**/*.test.ts` に一致するもの）が対象になります。
5. このプロジェクトの unit test 作成に特化した instruction を確認します。
6. 最後に `.github/instructions/drizzle.instructions.md` を開き、一番下までスクロールします。ほかの instruction file（`unit-tests.instructions.md` など）や、プロジェクト内の既存ファイルへのリンクがあることに注目してください。これにより、大きな instruction セットを小さく再利用しやすい単位に分割し、コード生成時に Copilot が従うべき例を示せます。（そこに書かれているパスは repo root ではなく instruction file からの相対パスです。）

> [!NOTE]
> `copilot-instructions.md` の **Code formatting requirements** セクションには、このプロジェクトのコーディング標準が記載されていますが、コード内ドキュメントはまだ必須ではありません。次の手順で、TSDoc の doc comment とファイル コメント ヘッダーのルールを追加します。
## ブランチを作成する

コード変更を行うため、作業用ブランチを作成します。

1. codespace のターミナルで、新しいブランチを作成して切り替えます。

   ```bash
   git checkout -b update-custom-instructions
   ```

2. Copilot CLI がインストール済みで、認証されていることを確認します。

   ```bash
   copilot --version
   ```

   コマンドが見つからない場合や、まだログインしていない場合は、[演習 1 - GitHub Copilot CLI のインストール](../1-install-copilot-cli/) に戻ってください。

## instruction を更新する*前に* Copilot CLI を使う

custom instruction の効果を見るため、まずは現在の instruction を使ってコードを生成します。その後でファイルを更新し、フォローアップのプロンプトを実行します。

> [!TIP]
> **Copilot CLI セッションを開始する**
>
> 以下の演習を始める前に、codespace に戻ってターミナルを開きます（まだ開いていない場合は <kbd>Ctrl</kbd>+<kbd>\`</kbd>）。次に、`--yolo` と `--enable-all-github-mcp-tools` を付けて Copilot CLI を起動します。
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 新しく開始する代わりに、このプロジェクトの直近のセッションを引き継ぐには `copilot --yolo --enable-all-github-mcp-tools --continue` を実行します。前の演習から Copilot CLI がすでに実行中であれば、`/clear` を送ってクリーンな会話を開始してください。
>
> `--enable-all-github-mcp-tools` を付けると、現在のセッションで GitHub MCP の読み取り / 書き込みツールが有効になります。これにより、ワークショップの流れの中で Copilot がバックログを読み取り、pull request を開けるようになります。

> [!CAUTION]
> `--yolo` は完全な自動権限（`--allow-all-tools`、`--allow-all-paths`、`--allow-all-urls`）を有効にします。Codespace や VM のような分離された環境でのみ使用し、日常的な開発の既定値として alias しないでください。詳しくは [Allowing and denying tool use][allow-all-warning] を参照してください。

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
1. `.github/copilot-instructions.md` を自動的に読み取れるよう、Copilot CLI セッションが**repository root** から実行されていることを確認します。
2. Copilot CLI のプロンプトで、フィルタリング UI が利用する publishers helper を生成するよう依頼します。

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

3. Copilot CLI はプロジェクトを探索し、計画を提案し、この `--yolo` セッションでファイルを書き込みます。ターミナル出力の変化を確認し、その後エディターでレビューします。
4. 生成された `src/lib/publishers.ts` をエディターで開きます。
5. helper が型付き関数として生成され、第一引数に `db` client を受け取り、publishers の型付き配列を返していることを確認してください。これは `.github/instructions/drizzle.instructions.md` にあるデータ レイヤーの規約（`src/lib/*.ts` に適用される）によるものです。
6. 生成されたコードに、TSDoc の doc comment とファイル レベルのコメント ヘッダーが**含まれていない**ことを確認します。

> [!CAUTION]
> Copilot は確率的に動作するため、指示しなくても doc comment を追加する可能性があります。その場合でも問題ありません。instruction 更新後に一貫性が向上することが、この演習での重要なポイントです。

## 新しいリポジトリ標準を追加する

先ほど説明したように、`.github/copilot-instructions.md` は Copilot にプロジェクト レベルの情報を提供するためのファイルです。リポジトリのコーディング標準を文書化し、コード提案の質を高めましょう。

1. `.github/copilot-instructions.md` をもう一度開きます。
2. **Code formatting requirements** セクションを探します。27 行目付近にあるはずです。ここにプロジェクトのコーディング標準が記載されている一方で、コード内ドキュメントに関するルールがまだないことに注目してください。そのため、生成された helper には doc comment がありませんでした。
3. 既存の標準のすぐ下に、次の markdown 行を追加して、ファイル コメント ヘッダーと TSDoc の doc comment を追加するよう Copilot に指示します。

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. `copilot-instructions.md` を保存します。

> [!TIP]
> 前のレッスンで見たとおり、instruction file はグローバル ガイダンス向けのリポジトリ レベル（`.github/copilot-instructions.md`）にも、特定の言語、ファイル種別、タスク向けの `*.instructions.md` としても作成できます。いま追加した doc comment ルールのような、プロジェクト全体に適用する標準を置く場所としては、リポジトリ レベルのファイルが適切です。
## プロンプトを再実行して変化を確認する

instruction に doc comment ルールを追加したので、先ほど生成した publishers ファイルを更新するよう Copilot CLI に依頼します。同じ標準ディレクティブが、書き換えの方向性を導きます。

1. Copilot CLI セッションで `/clear` を送信し、新しい会話を始めます。
2. 次のプロンプトを送信します。

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. 編集が完了したら、`src/lib/publishers.ts` をもう一度開きます。
4. ファイルの先頭に、次のようなコメント ブロックが追加されていることを確認します。

   ```typescript
   /**
    * Publisher data-access helpers for the Tailspin Toys Crowd Funding platform.
    * Provides functions to retrieve publisher information from the database.
    */
   ```

5. 生成された関数に、次のような TSDoc の doc comment が含まれていることを確認します。

   ```typescript
   /**
    * Returns a list of all publishers with their id and name.
    *
    * @param db - The Drizzle database client.
    * @returns A promise that resolves to an array of publisher objects.
    */
   ```

6. この更新済みファイルはそのまま残してください。次の演習で、この最初のデータ スライスを土台として使います。

## フィルタリングの最初のスライスを commit して push する

1. ターミナルで、変更されたファイルを確認します。

   ```bash
   git status
   ```

2. instruction の更新と helper を stage します。

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. 変更を commit します。

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. ブランチを push します。

   ```bash
   git push -u origin update-custom-instructions
   ```

## まとめと次のステップ

このプロジェクトの instruction file から Copilot がどのようにコンテキストを取得するかを確認し、そのうえで Copilot CLI を使って次のことを行いました。

- *既存の* instruction を使って、フィルタリング用の publishers data-access helper の土台を生成する。
- `.github/copilot-instructions.md` に、リポジトリ全体の新しい標準を追加する。
- フォローアップのプロンプトを実行し、再生成されたコードが新しい標準を取り入れる様子を確認する。
- instruction の更新と helper の土台の両方を commit して push する。

次は、[コード生成の演習][next-lesson] で、これらの instruction を適用しながらバックログの作業を実装します。

## リソース

- [GitHub Copilot のカスタマイズ用 instruction file][instruction-files]
- [custom instruction 作成のベスト プラクティス][instructions-best-practices]
- [Copilot 向けの custom instruction をより良く書くための 5 つのヒント][copilot-instructions-five-tips]
- [Awesome Copilot — instruction file などのリソース集][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
