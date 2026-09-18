---
title: "演習 6 - GitHub Copilot CLI のカスタム エージェント"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## custom agent とは

GitHub Copilot の [カスタム エージェント][custom-agents-concept] を使うと、開発ワークフロー内の特定のタスクや領域に合わせた専門的な AI アシスタントを作成できます。リポジトリの `.github/agents` フォルダー内にある markdown ファイルで agent を定義することで、focused instruction、best practice、コーディング パターン、ドメイン固有の知識を Copilot に与え、特定の種類の作業をより効果的に進められるようにできます。チームは自分たちの専門知識を再利用可能な agent として定義できます。たとえば、[WCAG][wcag] への準拠を徹底するアクセシビリティ agent、secure coding practice に従うセキュリティ agent、一定の test pattern を保つ testing agent などです。

custom agent は、プロジェクトの `.github/agents` フォルダー、またはグローバルな `~/.copilot/agents` にある markdown ファイルで定義します。各ファイルには、少なくとも `name` と `description` を含む YAML frontmatter があり、その後に agent の振る舞い、専門性、instruction を定義する markdown プロンプトが続きます。

### custom agent と agent skill の比較

custom agent と [agent skill][agent-skills-concept] には、概念的に重なる部分があります。どちらも主に markdown ファイルで定義され、AI にどのように作業すべきかを伝えます。最も分かりやすい区別は、**custom agent** は作業者で、**skill** はツールだということです。

custom agent には独自の context window があり、作業を進める中で skill（さらにはほかの agent）をオーケストレーションすることを前提に設計されています。このラボでは、アクセシビリティ custom agent がガイドラインに照らしてサイトをレビューし、更新します。その過程で、pull request ワークフロー用の skill や、test の実行と管理を行う skill などを呼び出すことがあります。

> [!NOTE]
> custom agent の書き方に、唯一の「正しい」方法はありません。AI 全般に言えることですが、自分の環境やシナリオに合う形を見つけるために、テストと反復を行ってください。

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/
## シナリオ

多くの Web アプリケーションは、すべてのユーザーにとって十分にアクセシブルとは言えず、現在作業している Web サイトも例外ではありません。アクセシビリティ上の不足を特定して解消するために、custom agent を使用します。

Tailspin Toys は、自社のクラウドファンディング プラットフォームを、視覚能力や好みにかかわらずすべてのユーザーが利用しやすいものにしたいと考えています。最近のユーザー フィードバックでは、現在の dark theme はテキストと背景色のコントラストが不十分で読みにくいという指摘がありました。このアクセシビリティ上の懸念に対応するため、デザイン チームは、ユーザーがオン / オフを切り替えられる high-contrast mode の実装を求めています。

アクセシビリティは重要であるため、できるだけ早く実装したいと考えています。そこで、機能生成のために custom agent を活用します。
この演習では、次のことを行います。

- custom agent を確認する。
- custom agent を有効にし、Copilot CLI を使ってタスクを割り当てる。

## アクセシビリティ custom agent を確認する

アクセシビリティ用の custom agent は、すでに用意されています。Copilot をどのように導くのか理解するために、その内容を確認しましょう。

1. `.github/agents/accessibility.md` を開きます。
2. `name` フィールドと `description` フィールドを持つ YAML frontmatter を確認します。

> [!CAUTION]
> `name` と `description` を含む frontmatter は、custom agent に必須です。

3. 続いて、次の内容が示されている各セクションを読みます。
   - アクセシブルな Web サイトのコードを生成するときの中核的な責務。
   - アクセシビリティのベスト プラクティス。
   - HTML、CSS、JavaScript のコード例。
   - よくある落とし穴やミスの一覧。
## Copilot CLI で custom agent を使う

Copilot CLI では、`/agent` コマンドを使って custom agent を開始できます。では、Web サイトに対してアクセシビリティの確認を実行しましょう。

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
1. Copilot CLI のプロンプト ウィンドウで `/agent` と入力し、<kbd>Enter</kbd> を押して agent の一覧を表示します。
2. 利用可能な agent の一覧から **Accessibility agent** を選択します。
3. 次のプロンプトを使い、アクセシビリティ agent に対してアクセシビリティ関連のバックログ項目をレビューし、修正を生成するよう依頼します。

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

4. Copilot がタスクの実行を開始します。まず issue を取得し、その後レビュー、更新の生成、最後に PR の作成へと進みます。PR を作成するときに、このプロジェクトの PR 用 skill を利用していることにも気づくはずです。

> [!NOTE]
> この処理には数分かかることがあります。ここまでに学んだ内容を振り返ったり、飲み物を楽しんだり、Copilot CLI で利用できる追加コマンドを扱う次のモジュールを先に読んだりするのによい時間です。

## まとめと次のステップ

このレッスンでは、GitHub Copilot の [カスタム エージェント][custom-agents] を確認しました。custom agent は、特定のタスクや領域に合わせた専門的な AI アシスタントです。custom agent を使うと、チームの専門知識や標準を再利用可能な agent に落とし込み、Copilot が特定の種類の作業をより効果的に行えるよう導けます。

このレッスンで確認した内容は次のとおりです。

- custom agent がどのように定義されるか。
- Copilot CLI で custom agent を使う方法。

次は、[いくつかの slash command][next-lesson] を確認し、Copilot CLI の追加テクニックを学びましょう。

## リソース

- [カスタム エージェント][custom-agents]
- [リポジトリ用カスタム エージェントの作成][creating-custom-agents]
- [awesome-copilot のカスタム エージェント][awesome-copilot-agents]
- [organization で custom agent を使う準備][org-custom-agents]
- [enterprise で custom agent を使う準備][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
