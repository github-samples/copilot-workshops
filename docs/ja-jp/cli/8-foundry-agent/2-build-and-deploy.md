---
title: "モジュール 2 - エージェントを構築してデプロイする"
description: "GitHub Copilot CLI と Microsoft Foundry Skill を使って Backer Concierge のひな形を作成し、テストしてデプロイします。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

[モジュール 1][previous-lesson]では、カタログを準備し、デプロイ済みのモデルをテストしました。[コンシェルジュを作るオプション シリーズ][overview]の 2 番目のモジュールでは、その土台をホスト型エージェントに発展させます。

このモジュールでは、次の内容に取り組みます。

- デプロイ可能な専用のカタログ コピーを含むエージェントのひな形を作成する。
- グラウンディングと会話の継続性をローカルでテストする。
- エージェントをデプロイし、リモートで呼び出す。

## シナリオ

Tailspin Toys が必要としているのは、モデルからの 1 回限りの回答だけではありません。支援者は、コンシェルジュが直前に勧めたゲームを覚えていて、それらに関する追加の質問に答えることを期待しています。また、コンシェルジュを開発者のマシンからホスト型サービスに移しても、回答の信頼性を維持する必要があります。

## 既存のプロジェクトで続ける

このモジュールは、モジュール 1 で動作を確認したモデルを引き継ぎます。別の Azure リソース一式を作成するのではなく、同じプロジェクトとデプロイを使い続けます。

1. `foundry-agent-cli` ブランチの Tailspin Toys リポジトリと、モジュール 1 の Copilot CLI セッションに戻ります。
2. `db/catalog.json` が利用でき、モデルのテストで使った Foundry プロジェクト、選択したモデルのデプロイ、Azure のサインインが引き続き利用できることを確認します。セットアップが未完了の場合は、先に[プロジェクトとモデルを準備する][previous-lesson]を完了してください。

> [!IMPORTANT]
> ホスト型エージェントはパブリック プレビューであり、課金対象の Azure リソースを作成します。このモジュールで終了する場合も、[クリーンアップの手順][cleanup]に従ってください。

## Backer Concierge エージェントのひな形を作成する

Microsoft Foundry Skill に、既存の Tailspin Toys リポジトリ内でホスト型エージェントのひな形を作成するよう依頼し、実行する前にパッケージ化と構成を確認します。

1. Copilot CLI に次のプロンプトを入力します。

    ```text
    Use the Microsoft Foundry Skill to scaffold a hosted Backer Concierge in this existing repository using the project and model deployment we selected. Start from the Python 3.13 Basic hosted-agent sample, use Microsoft Agent Framework with the Responses API and code deployment, and keep the agent in agent/backer-concierge. Keep one azure.yaml at the repository root with a service using host: azure.ai.agent.

    Ground every answer in db/catalog.json. Never invent games, publishers, ratings, funding totals, backer counts, pledge tiers, prices, player counts, play times, or release dates. Ask one short clarifying question when a request is vague and preserve conversation context. Ensure the catalog is copied into the deployable service during preparation so the deployed agent never depends on a file outside its service directory. Add focused tests for catalog loading and grounding behavior.

    Scaffold and test locally, but do not deploy the hosted agent yet. Stop and ask me to authenticate if needed.
    ```

2. セッションを確認し、Foundry プロジェクト、モデルのデプロイ、エージェント名、環境に関する質問に答えます。
3. Copilot の作業が終わったら、変更を確認します。

    ```text
    /diff
    ```

    次の点を確認します。

    - `azure.yaml` に `host: azure.ai.agent` のサービスが含まれている。
    - サービスが `agent/backer-concierge` を参照している。
    - デプロイするサービス パッケージに、自動生成された専用のカタログ コピーが含まれている。
    - 手作業で編集する 2 つのカタログを管理するのではなく、1 つのスクリプトまたはビルド手順で `db/catalog.json` からコピーを更新している。
    - エージェントが、選択したモデルのデプロイと Responses API を使っている。
    - 指示の中で、カタログに存在しない事実を明示的に拒否している。
    - 資格情報、アクセス トークン、`.env` ファイル、`.azure` 環境ファイルがコミット対象としてステージングされていない。

    ひな形作成後のチェックポイントとして、次の構成を確認します。

    ```text
    tailspin-toys/
    ├── azure.yaml
    ├── agent/
    │   └── backer-concierge/
    │       ├── catalog.json
    │       └── requirements.txt
    ├── db/
    │   └── catalog.json
    └── src/
    ```

> [!IMPORTANT]
> `azd deploy` は、ホスト型エージェントのサービス ディレクトリをパッケージ化します。実行時に `agent/backer-concierge` からリポジトリ レベルの `db/catalog.json` を参照すると、ローカルでは動いてもデプロイ後に失敗する可能性があります。生成されたコピーは、デプロイ前に `agent/backer-concierge/` ディレクトリ内で利用できる必要があります。

4. サービスを起動する前に、対象を絞ったテストを実行し、生成された構成を確認するよう Copilot に依頼します。

    ```text
    Run the focused Backer Concierge tests. Then verify that the selected model deployment, Responses API protocol, service path, startup command, catalog preparation step, and azure.ai.agent host configuration are consistent. Fix only problems in this hosted-agent project and rerun the failed checks.
    ```

    対象を絞ったテストがすべて成功するまでは、先に進まないでください。

    ![生成されたエージェントのひな形を検証する](../../../_images/cli-8-verify-generated-agent.png)

## エージェントをローカルでテストする

ローカルの Responses API を通じて、エージェントのグラウンディングと会話の動作を確認します。ローカルのエージェント サービスは実行中にターミナルを占有するため、現在のターミナルでは Copilot CLI を開いたままにし、2 つ目のターミナルからエージェントを起動します。

1. <kbd>Ctrl</kbd>+<kbd>\`</kbd> を使って、別のターミナルを開きます。
2. Tailspin Toys リポジトリのルートから、次を実行します。

    ```bash
    azd ai agent run
    ```

    ローカルでの初回実行では、Python 環境を作成し、依存関係をインストールして、ホスト型エージェントを起動します。このターミナルは実行したままにします。

3. 最初のターミナルの Copilot CLI に戻り、次を入力します。

    ```text
    Test the running Backer Concierge through its Responses API. Run each acceptance prompt below, preserve the response ID for the two-turn conversation test, and compare every response with the expected behavior. Show a concise pass or fail table and the evidence for any failure. Do not change code yet.

    1. "I love puzzle games about tracking down bugs. What should I back?" Expected: only real catalog titles with correct details.
    2. "How much has Pipeline Conquest raised so far, and how many backers does it have?" Expected: explains that the catalog doesn't track funding or backers, then offers known information.
    3. "I need something for four players, about an hour long." Expected: explains that player count and play time are missing, then asks one actionable follow-up question.
    4. "Do you have Wingspan? If not, what's the closest thing you've got?" Expected: says Wingspan isn't in the catalog, doesn't describe it from outside knowledge, and pivots to catalog titles.
    5. "Recommend me something good." Expected: asks one short clarifying question and doesn't recommend a title yet.
    6. "What are your three highest rated games?" Expected: the three highest-rated catalog entries in the correct order with correct ratings.
    7. In one conversation, send "Show me two highly rated strategy games." followed by "Which of those has the higher rating?" Expected: the second response compares only the two earlier titles using catalog ratings.
    ```

    ![ホスト型エージェントのデプロイに向けたテストの成功結果](../../../_images/cli-8-passing-acceptance-scenarios.png)

4. 結果を確認します。エージェントに接続できない場合は、2 つ目のターミナルでサービスがまだ実行中であることを確認します。テストが失敗した場合は、ローカルの不具合だけを修正し、対象を絞ったテストを実行して、`azd ai agent run` の再起動が必要なタイミングを知らせるよう Copilot に依頼します。変更するたびにサービスを再起動し、失敗した受け入れテストを再実行します。

## ホスト型エージェントをデプロイする

ローカルの受け入れテストが成功したら、エージェントを Microsoft Foundry にデプロイする準備が整います。同じスキル主導のワークフローで、デプロイの準備状況を確認し、リモート エンドポイントをテストします。

1. すべての受け入れテストが成功したら、<kbd>Ctrl</kbd>+<kbd>C</kbd> でローカル サービスを停止します。
2. Copilot CLI に戻り、次のプロンプトを入力します。デプロイを承認する前に、提案されたリソースと推定コストを確認してください。

    ```text
    Continue with the Microsoft Foundry Skill workflow. Review the hosted agent for deployment readiness, then deploy it to Microsoft Foundry, show the deployment status and playground link, and invoke it remotely with: "I love puzzle games about tracking down bugs. What should I back?"
    ```

3. 評価スイートのソースを選ぶよう求められた場合は、**No, set it up later** を選択します。

    ![ホスト型エージェントのデプロイ状況とプレイグラウンドへのリンク](../../../_images/cli-8-hosted-agent-deployment.png)

4. デプロイ状況とリモートからの回答を確認します。エージェントが実行中であり、カタログに実在するゲームだけを勧めていることを確認します。デプロイまたは呼び出しが失敗した場合は、続行する前に、Copilot に原因の診断を依頼してリモート テストを繰り返します。

表示されたプレイグラウンドのリンクから、Microsoft Foundry ポータルでデプロイ済みのホスト型エージェントと対話できます。

スキル主導のワークフローは、`azd deploy` でサービスのソースをパッケージ化し、依存関係を解決してリモートでビルドし、Microsoft Foundry に公開します。デプロイ済みのエンドポイントのテストには、Foundry の呼び出しワークフローを使います。

## まとめと次のステップ

デプロイ可能なカタログ コピーを含むエージェントのひな形を作成し、グラウンディングと会話の継続性をテストして、Microsoft Foundry からのリモートの回答を検証しました。これで、正常に動作するホスト型の Backer Concierge が完成しました。

次は、同じリポジトリ、ブランチ、Copilot CLI セッション、デプロイ済みのエージェントを使って、[コンシェルジュを Web サイトに接続します][next-lesson]。ホスト型エージェントを試すだけで十分な場合は、ここで終了して [Azure リソースをクリーンアップできます][cleanup]。

[overview]: ../
[previous-lesson]: ../1-project-and-model/
[next-lesson]: ../3-connect-to-site/
[cleanup]: ../#リソースをクリーンアップする
