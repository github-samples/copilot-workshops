---
title: "モジュール 3 - エージェントを Web サイトに接続する"
description: "ローカルの Azure Functions プロキシとアクセシブルなチャット ウィジェットを通じて、ホスト型の Backer Concierge を Tailspin Toys に接続します。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
next: false
---

[モジュール 2][previous-lesson]では、Backer Concierge をデプロイしてテストしました。[コンシェルジュを作るオプション シリーズ][overview]の最後のモジュールでは、そのエージェントをローカルの Tailspin Toys Web サイトから利用できるようにします。

このモジュールでは、次の内容に取り組みます。

- Foundry の資格情報をサーバー内に保持する、ローカルの Azure Functions プロキシを構築する。
- アクセシブルなチャット ウィジェットをサイトに追加する。
- 会話の一連の流れを検証し、リソースをクリーンアップする。

## シナリオ

支援者がゲームを見つけるのは、開発者のターミナルや Azure ポータルではなく、Tailspin Toys の Web サイトです。チームは、カタログと並べてコンシェルジュを提供したいと考えています。チャットは追加の質問に対応し、サービスの資格情報を保護する必要があります。

## ホスト型エージェントを引き続き使う

Web サイトとの統合には、モジュール 2 でデプロイしたエージェントが必要です。エージェントは Foundry で実行したままにし、プロキシと Web サイトをローカルで実行します。

1. `foundry-agent-cli` ブランチの Tailspin Toys リポジトリと、既存の Copilot CLI セッションに戻ります。
2. Backer Concierge がデプロイされており、[エージェントを構築してデプロイする][previous-lesson]でのリモート呼び出しが成功したことを確認します。Azure リソースをすでに削除した場合は、前のモジュールの手順で再作成してから続行してください。

> [!IMPORTANT]
> このモジュールのプロキシと Web サイトはローカルで実行します。本番 Web サイトのデプロイではありません。[クリーンアップ][cleanup]を完了するまで、モデルとホスト型エージェントは課金対象の Azure リソースのままです。

## サーバー側プロキシを構築する

Tailspin Toys は、すべて事前レンダリングされています。ブラウザーのコードからホスト型エージェントを直接呼び出したり、ブラウザーで Foundry の資格情報を受け取ったりしてはいけません。ローカルの Azure Functions を追加し、**サーバー側で資格情報を隔離する境界**にします。これにより、Foundry への認証を行い、エージェントの回答だけをブラウザーに返します。

`microsoft-foundry` スキルはホスト型エージェントのワークフローを担当し、同じプラグインに含まれる、より広範な Azure スキルはローカルの Function プロジェクトを準備できます。それらのスキルでプロキシを構築し、資格情報を公開せずにエージェントに接続できることを確認します。

1. Copilot CLI で、次を入力します。

    ```text
    Use the Azure skills to add an Azure Functions v4 Node.js and TypeScript project in api with one POST /api/concierge endpoint that invokes my deployed Backer Concierge hosted agent. This Function will run locally only; don't add it to azure.yaml or create Azure deployment infrastructure. Use DefaultAzureCredential with my local Azure sign-in. Keep the HTTP trigger thin, isolate the Foundry client in a unit-testable module, validate and limit request bodies, set explicit timeouts, and return sanitized errors. Store the Foundry project endpoint and agent name in local server-side settings that are excluded from version control. Never return credentials or access tokens to the browser. The Astro site is `output: 'static'` with no dev proxy, so also add a local-only Vite dev-server proxy for /api to the Function's port in astro.config.mjs, so relative /api/concierge requests reach it during `astro dev`.

    For conversation state, generate a high-entropy handle on the server, map it to the Foundry conversation server-side with an expiration, and never expose a raw Foundry conversation or thread identifier. Reject malformed, expired, and unknown handles. Add focused unit tests.
    ```

    ![Azure Functions ローカル プロキシのセットアップ](../../../_images/cli-8-azure-functions-proxy.png)

2. 別のターミナルを開き、Copilot が提示したコマンドでローカルの Function を起動します。Function は実行したままにします。
3. Copilot CLI に戻り、ローカル プロキシをテストするよう Copilot に依頼します。

    ```text
    Send a request to the local /api/concierge endpoint asking "Which games are under $30?" and show me the sanitized JSON response. Confirm that the request reaches the deployed Backer Concierge through DefaultAzureCredential.
    ```

4. 回答を確認します。カタログには価格が含まれないことを説明している必要があります。Foundry のトークン、資格情報、プロジェクトのエンドポイント、Foundry の会話識別子そのもの、スタック トレースが含まれていてはいけません。

    ![ローカルのコンシェルジュ エンドポイントから返された、機密情報を除去済みの JSON レスポンス](../../../_images/cli-8-sanitized-json-response.png)

## チャット ウィジェットを構築する

プロキシにより、ブラウザーからコンシェルジュに安全に接続できます。次に、サイトにチャット ウィジェットを追加し、Playwright で会話の一連の流れを確認します。

1. Copilot にサイトとの統合を依頼します。

    ```text
    Add an accessible Backer Concierge chat widget as an Astro component and render it site-wide from Layout.astro. It should POST to /api/concierge and thread the conversation using the returned opaque conversation handle, follow the dark theme in style.instructions.md, support Escape to close, and include data-testid attributes.
    ```

2. ローカルの Function は実行したままにして、別のターミナルで Copilot が提示したコマンドを使い、Astro サイトを起動します。
3. Copilot CLI に戻ります。[演習 4][playwright-lesson]で追加した Playwright MCP サーバーは、すでに利用できます。Copilot にウィジェットのテストを依頼します。

    ```text
    Use the Playwright MCP server to test the Backer Concierge widget end to end in the running Tailspin Toys site. Verify its core chat flow, conversation continuity, accessibility, error handling, grounding boundaries, and secure use of the local proxy. Report the results and include evidence for any failures.
    ```

    ![Tailspin Toys サイト内の Backer Concierge ウィジェットのスクリーンショット](../../../_images/cli-8-backer-concierge-widget.png)

4. 報告された根拠と照らし合わせて結果を確認します。失敗したチェックがある場合は、関連するプロキシやウィジェットの動作を修正するよう Copilot に依頼し、失敗したチェックを再実行してから終了してください。

## リソースをクリーンアップする

最終チェックポイントに到達しました。ローカルの Web サイトでコンシェルジュが動作しています。共通のクリーンアップ手順は、シリーズ全体で作成したローカル サービスと Azure リソースの両方を対象としています。

1. [リソースをクリーンアップする][cleanup]の手順を完了します。ローカル サービスを停止し、Azure リソースの削除が完了したことの確認も含めて実施してください。

## まとめと次のステップ

ローカルのサーバー側プロキシとアクセシブルなチャット ウィジェットを通じて、ホスト型の Backer Concierge を Tailspin Toys に接続しました。シリーズ全体を通じて、GitHub Copilot CLI と Foundry を使い、モデルの準備、エージェントの構築とデプロイ、Web サイトとの統合全体の検証に取り組みました。

CLI ワークショップを締めくくるために、[振り返りと次のステップ][review]に進みます。

[overview]: ../
[previous-lesson]: ../2-build-and-deploy/
[review]: ../../9-review/
[playwright-lesson]: ../../4-mcp/
[cleanup]: ../#リソースをクリーンアップする
