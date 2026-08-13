---
title: "演習 4 - Playwright MCP サーバーで機能をテストする"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Copilot CLI でフィルタリング機能を生成したので、pull request を開く前に、ブラウザーで正しく動作することを確認する必要があります。自分でアプリを操作して確認する代わりに、**Playwright MCP server** を接続し、Copilot に実際のブラウザーを操作させて機能をテストしてもらいます。

この演習では、次のことを行います。

- Model Context Protocol（MCP）とは何か、そして MCP server がどのように Copilot CLI を拡張するかを理解する。
- Playwright MCP server を Copilot CLI に追加する。
- ブラウザーでフィルタリング機能を手動テストするよう Copilot に依頼する。

## Model Context Protocol (MCP) とは

[Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) は、AI agent が外部ツールやサービスと通信するための方法を提供します。MCP を使用すると、AI agent は外部ツールやサービスとリアルタイムでやり取りできます。これにより、最新情報にアクセスし（resources を利用）、代わりに操作を実行できます（tools を利用）。

これらの tool や resource には、MCP server を通じてアクセスします。MCP server は AI agent と外部ツールやサービスの間をつなぐブリッジとして機能します。MCP server は、AI agent と外部ツール（既存の API や NPM package のようなローカル ツールなど）の通信を管理します。各 MCP server は、AI agent がアクセスできる別々の tool と resource のセットを表します。

すでに広く使われている MCP server として、次のようなものがあります。

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: GitHub リポジトリを管理するための API セットにアクセスできます。新しいリポジトリの作成、既存リポジトリの更新、issue や pull request の管理などを AI agent が実行できます。
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**: Playwright を使ったブラウザー自動化機能を提供します。Web ページへの移動、フォーム入力、ボタン選択などを AI agent が実行できます。

ほかにも、さまざまな tool や resource へのアクセスを提供する MCP server が多数あります。GitHub は、エコシステムの発見性とコントリビューションを高めるために [MCP registry](https://github.com/mcp) を公開しています。

> [!CAUTION]
> セキュリティの観点では、MCP server はプロジェクト内のほかの依存関係と同じように扱ってください。MCP server を使用する前に、ソース コードを慎重に確認し、公開元を検証し、セキュリティ上の影響を検討してください。信頼できる MCP server のみを使用し、機密性の高い resource や操作へのアクセスを与える際は慎重に判断してください。

> [!NOTE]
> [GitHub MCP server][github-mcp-server] は Copilot CLI に**組み込まれています**。そのため、追加設定なしで利用でき、ワークショップ全体を通して Copilot がリポジトリを読み書きできていたのはこの server によるものです。この演習では、Copilot にブラウザーを与えるために 2 つ目の server として Playwright を追加します。

## Playwright MCP server を追加する

server を追加する最も手早い方法は、対話式の `/mcp add` コマンドです。ここでは、Copilot が制御できるブラウザーを提供する [Playwright MCP server][playwright-mcp-server] を登録します。

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
1. Copilot CLI セッションで、次を入力します。

    ```text
    /mcp add
    ```

2. 設定フォームが表示されます。<kbd>Tab</kbd> でフィールド間を移動し、次のように入力します。

    - **Server Name**: `playwright`
    - **Server Type**: **Local**（**STDIO** とも表示されます）を選択する
    - **Command**: `npx @playwright/mcp@latest --headless`
    - **Tools**: server のすべての tool を許可するため、`*` のままにする

3. <kbd>Ctrl</kbd>+<kbd>S</kbd> を押して保存します。server は追加され、再起動なしですぐに利用できます。

`--headless` フラグを付けると、Playwright は表示ウィンドウなしでブラウザーを実行します。デスクトップ表示のない codespace 内ではこれが必要です。内部的には、server が `~/.copilot/mcp-config.json` に書き込まれます。

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. MCP server の一覧を表示して、server が登録済みでアクティブであることを確認します。

    ```text
    /mcp show
    ```

5. 組み込みの `github` server と並んで `playwright` が表示されるはずです。

> [!NOTE]
> Tailspin Toys プロジェクトでは、エンドツーエンド test にすでに Playwright を使用しています。そのため、Playwright が必要とするブラウザーは通常すでにインストールされています。後で Copilot からブラウザーが見つからないと報告された場合は、`npx playwright install chromium` を実行してから再試行してください。

## Web サイトを起動する

Playwright MCP server がテストを実行するには、対象となるアプリが起動している必要があります。Copilot CLI で作業している間も実行し続けられるよう、**別の**ターミナルで Astro の dev server を起動します。

1. <kbd>Ctrl</kbd>+<kbd>\`</kbd> を選択して、codespace で新しいターミナルを開きます。
2. Web サイトを起動します。

    ```bash
    npm run dev
    ```

3. このターミナルはそのまま動かしておきます。`Astro server: http://localhost:4321` の表示が出たら、アプリの準備は完了です。

## フィルタリング機能をテストする

Copilot CLI セッションに戻り、Copilot に機能をテストするよう依頼します。

[Playwright MCP server][playwright-mcp-server] は、Copilot に実際のブラウザーを操作させます。自分でアプリを操作して確認する代わりに、agent がページを開き、移動し、filter を適用し、その結果を読み取って要約できます。会話を離れずに、機能が期待どおりに動作することを確認する最も速い方法です。

内部的には、Playwright MCP server はスクリーンショットではなく、ページの [accessibility tree][playwright-mcp-server] を基に動作します。つまり、agent はボタン、リンク、リスト項目などの構造化されラベル付けされた要素を、支援技術と同じように扱います。そのため、簡単な機能確認が、軽いアクセシビリティの健全性チェックも兼ねることになります。

server を接続し、アプリを起動したら、次のように Copilot に依頼して、先ほど実装したフィルタリング機能を試してもらいます。

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

Copilot は Playwright MCP server 経由でブラウザーを起動し、各ステップを実行して、確認結果を報告します。その要約を issue の受け入れ条件と照らし合わせて読み、違和感があれば、追跡質問をしたり、pull request を開く前にコード修正を依頼したりしてください。

> [!NOTE]
> このテストでは、アプリが `http://localhost:4321` で動作している必要があります。dev server を停止していた場合は、プロンプトを送る前に再起動してください。Copilot が初めて Playwright MCP server を使う際には、ブラウザーのダウンロードが必要になることがあります。ブラウザーが見つからないと報告された場合は、`npx playwright install chromium` を実行して再試行してください。

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
## まとめと次のステップ

おめでとうございます。Playwright MCP server を使って、Copilot CLI で機能を手動テストできました。要点を振り返ると、次のことを行いました。

- Model Context Protocol（MCP）とは何か、そして MCP server がどのように Copilot CLI を拡張するかを学ぶ。
- `/mcp add` で Playwright MCP server を追加する。
- Copilot にブラウザー操作を任せ、出荷前にフィルタリング機能を検証する。

機能が正しく動作することを確認できたので、次の演習に進み、[agent skill の助けを借りて pull request を開く][next-lesson] ことができます。

## リソース

- [MCP とは何か、なぜいま注目されているのか][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Copilot CLI に MCP server を追加する][cli-add-mcp]
- [GitHub MCP Server][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
