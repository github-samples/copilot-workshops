---
title: "エージェントをサイトに接続する"
description: "ホスト環境の Backer Concierge をローカルプロキシ経由で接続し、アクセシビリティに対応したチャットウィジェットをテストします。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
next: false
---

| [← 前のモジュール: エージェントを構築してデプロイする][previous-lesson] |
|:--|

このモジュールでは、[エージェントを構築してデプロイする][previous-lesson]で用意したホスト型エージェントを Tailspin Toys に接続します。VS Code の Copilot Chat で作成するのはローカルの統合であり、公開された本番エンドポイントではありません。

## 目標

- 資格情報と Foundry の会話識別子を、ローカルのサーバー側プロキシの背後に保持します。
- 会話の継続性を備え、アクセシビリティに対応したチャットウィジェットを追加します。
- リソースをクリーンアップする前に、バックエンドと体験全体を検証します。

## シナリオ

支援者は、カタログを離れずにコンシェルジュに相談できることを期待しています。会話では文脈を保持し、キーボードで操作でき、非公開の接続情報を保護する必要があります。信頼を得るには、誠実なおすすめだけでなく、安全でアクセシビリティに対応した体験も欠かせません。

## ワークスペースで作業を再開する

統合の接続先は既存のホスト型エージェントです。Tailspin Toys は完全に事前レンダリングされた静的 Web サイトなので、ブラウザーのコードにエージェントの資格情報を安全に保持することはできません。

1. VS Code で同じ Tailspin Toys リポジトリを開き、`foundry-agent-vscode` ブランチを使います。前のチェックポイントで用意したホスト型エージェントが、既存の `tailspin-toys` プロジェクトで引き続き **Running** であることと、ローカルの Azure サインインがそのサブスクリプションを対象としていることを確認します。
2. **AIAgentExpert** ではなく、通常の **Agent** モードで Copilot Chat を開きます。**+**、**GitHub Issues** の順に選択し、Issue **Add a Backer Concierge assistant for catalog questions** を選んで添付します。

## ローカルプロキシを構築して検証する

`/api` 内のローカル Azure Functions プロキシが接続情報を保持し、サイトをローカルで実行している間のリクエストを転送します。Copilot は **Azure skills** を使って準備と検証を進められます。

> [!IMPORTANT]
> このワークショップのプロキシはローカル開発専用です。匿名でアクセスできる公開エンドポイントとしてデプロイしないでください。本番環境では、アプリケーション固有の認証と不正利用対策が必要です。これには、レート制限やクォータ、CORS 制限、監視、コスト管理が含まれます。

1. Copilot にプロキシの作成を依頼します。

   ```text
   Add a local Azure Functions proxy in api for the static Astro site to call my deployed Backer Concierge securely during development. Use my existing local Azure sign-in to call the hosted agent, keep all credentials out of the browser, protect conversation state with opaque handles, validate requests, sanitize errors, add focused tests, and configure the Astro dev server so /api requests reach the local Function. Don't create public deployment infrastructure.
   ```

2. 受け入れる前に変更をレビューします。資格情報と Foundry の会話識別子がサーバーにとどまり、ローカル設定がバージョン管理から除外され、リクエストに制限が設けられ、対象を絞ったテストに合格していることを確認します。
3. UI を構築する前に、バックエンドが動作することを確かめます。

   ```text
   Start the local Functions host and test /api/concierge by asking "Which games are under $30?" Show me the sanitized response and confirm that no credentials or internal conversation identifiers are returned.
   ```

4. ターミナルの応答を確認します。回答を含む `response` プロパティを持つ有効な JSON であり、価格情報のでっち上げがなく、資格情報や内部の会話識別子を含まないことが期待されます。確認に失敗した場合は、Copilot に修正を依頼し、バックエンドのテストを繰り返します。
5. **Keep** で変更を保持し、**/clear** を使って、同じリポジトリとブランチでウィジェット用の新しいチャットを始めます。ローカルプロキシの設定と既存のホスト型エージェントへの接続は維持します。

## ウィジェットを構築してテストする

これで UI の接続先となるバックエンドの検証が済みました。エンドツーエンドテストでは、使いやすさとカタログの情報範囲の両方を確認します。

1. Copilot にウィジェットの追加を依頼します。

   ```text
   Add an accessible Backer Concierge chat widget to the Astro site. Connect it to /api/concierge, preserve the conversation using the returned opaque handle, follow the existing design guidance, support keyboard use, and make it testable.
   ```

   ![Backer Concierge のチャットウィジェットの動作を示すスクリーンショット](../../../_images/tailspin-toys-backer-concierge-agent.png)

2. Function とサイトを実行したまま、体験全体を検証します。

   ```text
   Use Playwright MCP to test the Backer Concierge widget end to end. Verify the core chat flow, conversation continuity, keyboard and accessibility behavior, grounding boundaries, and safe use of the local proxy. Report the results and fix any failures.
   ```

3. テスト結果と変更を Issue の受け入れ基準に照らしてレビューします。基準は、根拠に基づく回答、資金調達額をでっち上げないこと、確認の質問を 1 つすること、アクセシビリティに対応した UI、エンドツーエンドのテストカバレッジです。問題が修正され、影響する確認が再実行されたことを確認します。

## 完了時のチェックポイント

資格情報を安全に扱うローカルプロキシを構築し、アクセシビリティに対応したチャットウィジェットを接続して、ホスト型 Backer Concierge との会話フロー全体を検証しました。このモジュールのチェックポイントは、カタログの範囲を守り、資格情報と Foundry の内部識別子をブラウザーに渡さない、ローカルでテスト済みのサイト統合です。プロキシやサイトの本番環境へのデプロイではありません。

試すのを終えたら、ローカルのサービスを停止し、継続的な費用が発生しないように [Azure リソースをクリーンアップします][cleanup]。その後、メインのワークショップの [VS Code の概要][vscode-overview]に戻ります。

[previous-lesson]: ../2-build-and-deploy/
[cleanup]: ../#リソースをクリーンアップする
[vscode-overview]: ../../
