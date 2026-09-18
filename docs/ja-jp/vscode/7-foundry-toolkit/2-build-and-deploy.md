---
title: "エージェントを構築してデプロイする"
description: "VS Code で Backer Concierge のひな形を作成してデバッグし、Foundry ホスト型エージェントとしてデプロイしてテストします。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 前のモジュール: プロジェクトとモデルを準備する][previous-lesson] |
|:--|

このモジュールでは、[プロジェクトとモデルを準備する][previous-lesson]で用意したカタログとテスト済みモデルを使います。Microsoft Foundry Toolkit とそのカスタムエージェント **AIAgentExpert** が、VS Code でのローカル構築とホスト環境へのデプロイを案内します。

## 目標

- 既存の Tailspin Toys ワークスペースに、カタログを根拠として回答するエージェントのひな形を作成します。
- Agent Inspector でローカルの動作をデバッグします。
- 既存の Foundry プロジェクトにデプロイし、ホスト型エージェントを検証します。

## シナリオ

信頼できるおすすめを提供するには、1 回の会話でうまくいくだけでは不十分です。Tailspin Toys のコンシェルジュには、支援者が曖昧な質問をしたり、手元にない資金調達の詳細をしつこく求めたりしても、カタログの情報範囲を守ることが求められます。ホスト環境のコンシェルジュにも、非公開でテストしたときと同じ信頼性が必要です。

## ワークスペースで作業を再開する

エージェントは既存のモデルデプロイを使います。新しい Foundry プロジェクトを作成する必要はありません。

1. VS Code で同じ Tailspin Toys リポジトリを開き、`foundry-agent-vscode` ブランチを使います。`db/catalog.json` が存在し、**Foundry Toolkit** > **My Resources** に `tailspin-toys` プロジェクトとテスト済みモデルのデプロイが表示されることを確認します。
2. [前のチェックポイント][previous-lesson]が完了していることを確認します。リソースをクリーンアップした場合は、先に進む前にプロジェクトとモデルの準備をもう一度完了します。
3. Azure Developer CLI (`azd`) がまだ利用できない場合はインストールします。ホスト型エージェントのデプロイに使います。自分の OS に対応するコマンドだけを選びます。

   ```bash
   # macOS / Linux
   curl -fsSL https://aka.ms/install-azd.sh | bash

   # Windows (PowerShell)
   winget install microsoft.azd
   ```

4. 既存のプロジェクトで使っているサブスクリプションにサインインします。

   ```bash
   azd auth login
   ```

> [!IMPORTANT]
> ホスト型エージェントと Foundry Toolkit はパブリックプレビューです。デプロイすると課金対象のリソースが作成されます。コマンドを承認する前に、サブスクリプション、権限、リージョン、クォータ、見積もり費用を確認します。

## エージェントを作成してデバッグする

ツールキットは現在のリポジトリにコードのひな形を作成し、専用の Copilot Chat を開きます。Agent Inspector では、デプロイ前にローカルのリクエスト、イベント、ツール呼び出しを確認できます。

1. **Foundry Toolkit** を選択し、**Developer Tools**、**+ Build** の順に展開して **+ Create Agent** を選択します。**Create Agent** で **Code an agent with Copilot** を選択します。

   ![エージェント作成ページを示すスクリーンショット。](../../../_images/vscode-create-agent.png)

2. 新しいチャットで **AIAgentExpert** に切り替わっていることを確認します。生成されたプロンプトを次のカスタマイズ済みプロンプトに置き換え、送信します。

   ```text
   /foundrytk-quick-start Create a backer concierge AI agent called 'Backer Concierge'. The agent should use the model I deployed to answer catalog questions and recommend games grounded strictly in db/catalog.json. Review the acceptance criteria in the issue titled 'Add a Backer Concierge assistant for catalog questions' and ensure the agent meets them. Generate the code into agent/backer-concierge in the current workspace and ask me if anything is unclear.
   ```

3. `agent/backer-concierge` に生成されたコードをレビューします。デプロイ可能なエージェントにカタログが含まれ、対象を絞ったテストに合格し、資格情報やローカル環境ファイルがコミットされないことを確認します。
4. アクティビティバーで **Run and Debug** を選択し、<kbd>F5</kbd> でデバッガーを起動します。**Agent Inspector** が読み込まれ、エージェントサーバーに接続することを確認します。
5. [デプロイ済みモデルをテストする][model-tests]の 6 つのプロンプトをすべて再利用します。9 個のゲームの抜粋での順位がカタログ全体の順位だと思い込まず、`db/catalog.json` 全体に照らして回答を確認します。
6. **Input & Output**、**Events**、**Tools** を切り替え、ペイロード、セッションイベント、ツール呼び出しを調べます。動作が受け入れ基準に反する場合は、Copilot に修正を依頼し、デプロイ前に対象を絞ったテストと Inspector での確認を再実行します。

   ![ローカルでのエージェントのデバッグ手順を示すスクリーンショット。](../../../_images/vscode-agent-debug.png)

## ホスト型エージェントをデプロイしてテストする

**Go production** のハンドオフでは、既存のエージェントを Foundry 用にパッケージ化します。これによって、後で作成するサイトのプロキシが本番対応の公開サービスになるわけではありません。

1. エージェント作成用の Copilot Chat で **Go production** を選択し、既定のプロンプトを次の内容に置き換えて送信します。

   ```text
   /foundrytk-quick-start Review this agent for deployment readiness, run its tests, then deploy it to my existing tailspin-toys Foundry project. Show me the deployment status and test the deployed agent.
   ```

   ![AIAgentExpert エージェントのハンドオフの選択肢を示すスクリーンショット。](../../../_images/vscode-go-production-handoff.png)

2. チャットとターミナルでパラメーターとコマンドの承認内容を確認します。デプロイ先が既存の `tailspin-toys` プロジェクトであることを確認し、承認する前に課金対象のリソースを確認します。
3. Copilot が評価スイートを提案した場合は、必要に応じて受け入れ、追加の確認として実行します。
4. **Foundry Toolkit** を選択し、**My Resources** を展開して **Agents** を選択します。**Agents** タブで **Hosted Agent** に切り替えます。

   ![デプロイ済みのホスト型エージェントを示すスクリーンショット。](../../../_images/vscode-agent-deployed.png)

5. エージェント名を選択し、デプロイ状態が **Running** であることを確認します。**Playground** に切り替え、デプロイしたカタログに照らして、根拠に基づく回答、不足しているデータ、カタログ外の情報、曖昧な依頼、順位付けの確認を繰り返します。

   ![デプロイ済みのホスト型エージェントからの回答を示すスクリーンショット。](../../../_images/vscode-agent-response.png)

6. デプロイや回答に問題がある場合は、Copilot とともに報告された状態とログを調べ、既存のプロジェクト内で問題を修正して、確認を繰り返します。デプロイの検証が済むまで先に進まないでください。

## 完了時のチェックポイント

Backer Concierge のひな形を生成し、Agent Inspector でカタログに基づく回答をデバッグし、**Go production** の受け渡しで Foundry にデプロイして、ホスト型バージョンを Playground で再テストしました。このモジュールのチェックポイントは、情報がない場合に作り話をせず、カタログの範囲を守って稼働するホスト型エージェントです。

次は、同じ `tailspin-toys` プロジェクト、モデルのデプロイ、ホスト型エージェントを使って、エージェントをサイトに接続します。ここで終了する場合は、継続的な費用が発生しないように [Azure リソースをクリーンアップします][cleanup]。

| [次のモジュール: エージェントをサイトに接続する →][next-lesson] |
|--:|

[previous-lesson]: ../1-project-and-model/
[model-tests]: ../1-project-and-model/#デプロイ済みモデルをテストする
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#リソースをクリーンアップする
