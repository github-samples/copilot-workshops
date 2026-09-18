---
title: "モジュール 1 - プロジェクトとモデルを準備する"
description: "Azure ツールをセットアップし、Tailspin のカタログをエクスポートして、GitHub Copilot CLI で Foundry モデルを選択してテストします。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

これは、[オプション: Foundry を組み込む][overview]の最初のモジュールです。ツールとカタログを準備してから、Copilot で Foundry プロジェクトを作成し、エージェントを構築する前にデプロイ済みのモデルをテストします。

このモジュールでは、次の内容に取り組みます。

- Azure のコマンド ライン ツールと Azure Skills Plugin をインストールする。
- カタログをエクスポートし、Foundry での作業を計画する。
- モデルを選択してデプロイし、カタログの情報の範囲を守れるかテストする。

## シナリオ

Tailspin Toys には、カタログにある事実と、会社が提供していない情報とを区別できるコンシェルジュが必要です。評価の高いパズル ゲームを紹介するのは役立つおすすめですが、そのゲームの資金調達総額を作り上げてはいけません。チームは、本格的なアシスタントの開発に取り組む前に、選んだモデルがその境界を守れることを確かめたいと考えています。

## 前提条件とセットアップ

Azure で Backer Concierge をホストし、Copilot CLI の支援を受けながら作業を進めます。まず、Copilot が Azure リソースを操作するためのコマンド ライン ツールとプラグインを準備します。

> [!IMPORTANT]
> [クリーンアップの手順][cleanup]は、シリーズを完了する場合だけでなく、このモジュールで終了する場合にも適用されます。

1. Azure サブスクリプションがあることを確認します。必要な場合は、[$200 分のクレジット付きの無料 Azure サブスクリプション][azure-free]や、[$100 分のクレジット付きの Azure for Students][azure-students]などの選択肢があります。
2. Tailspin Toys の codespace に戻り、ターミナルを開きます。
3. 開発コンテナーに Azure CLI をインストールします。

    ```bash
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    az version
    ```

4. `az login` で Azure CLI にサインインし、`az account show` で正しいサブスクリプションを使っていることを確認します。
5. [Azure Developer CLI][install-azd] バージョン 1.27.1 以降をインストールします。Microsoft Foundry では、ホスト型エージェントのテストとデプロイに `azd` を使います。

    ```bash
    curl -sL https://aka.ms/install-azd.sh | bash
    azd version
    ```

6. `azd auth login` で Azure Developer CLI にサインインし、`azd config show` で正しいサブスクリプションを使っていることを確認します。
7. Azure Developer CLI (azd) の Foundry 拡張機能をインストールします。

    ```bash
    azd ext install microsoft.foundry
    ```

8. コマンド パレットから、新しい Copilot CLI セッションを横に開きます。<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Mac) または <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows/Linux) を押し、**Chat: New Copilot CLI session to the side** を選択します。
9. Azure Skills マーケットプレースを追加します。この操作が必要なのは、プラグインを初めてインストールするときだけです。

    ```text
    /plugin marketplace add microsoft/azure-skills
    ```

10. [Azure Skills Plugin][azure-skills] をインストールします。このプラグインは、Azure スキル、Azure MCP Server、Foundry MCP Server を GitHub Copilot CLI に追加します。

    ```text
    /plugin install azure@azure-skills
    ```

11. プラグインによって Azure MCP サーバーが構成されたことを確認します。

    ```text
    /mcp list
    ```

12. スキルや MCP サーバーが表示されない場合は、`/skills reload` または `/restart` を試し、再度確認します。

スキルは Copilot にワークフローを教え、MCP サーバーは Azure リソースの確認や操作を可能にします。

## 作業用ブランチを準備する

前の演習で、ほかの機能ブランチを作成してプッシュしている場合があります。エージェントの作業を分離するため、このオプション シリーズは最新の `main` ブランチから始めます。

1. シェルのターミナルで `main` に切り替え、最新の変更をプルし、Backer Concierge 用のブランチを作成します。

    ```bash
    git checkout main
    git pull
    git checkout -b foundry-agent-cli
    ```

## カタログをエクスポートする

エージェントには、読み取り可能なファイル形式のカタログが必要です。Tailspin Toys のサンプルには、このためのテスト済みエクスポート スクリプトが含まれています。

1. Copilot CLI に戻り、次を入力します。

    ```text
    Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
    ```

    Copilot は、次と同等のコマンドを実行するはずです。

    ```bash
    npm install
    npm run db:setup
    npm run db:export
    ```

    ![カタログのエクスポート結果の概要](../../../_images/cli-8-export-db-catalog.png)

2. `db/catalog.json` を開きます。21 個のゲームが含まれ、それぞれにタイトル、説明、カテゴリ、パブリッシャー、星評価があることを確認します。`note` フィールドには、カタログに資金調達総額、支援者数、支援プラン、発売日が含まれないと記載されています。価格、プレイ人数、プレイ時間のフィールドもありません。こうした情報の欠如が、エージェントが守るべき境界を定めます。

## Foundry での作業を計画する

Copilot が Azure リソースを作成したり、エージェントのコードを追加したりする前に、プラン モードで予定するワークフローを明確にします。

1. 次のプロンプトを入力します。

    ```text
    /plan Use the Microsoft Foundry Skill to plan a Backer Concierge hosted agent for this existing Tailspin Toys repository. Use a public Foundry project, Python 3.13, Microsoft Agent Framework, the Responses API, the Basic sample, and code deployment. Keep the agent in agent/backer-concierge and keep one azure.yaml at the repository root. Ground every answer in db/catalog.json, preserve conversation context, and add focused tests. Include project setup, model selection, local testing, deployment, remote invocation, estimated cost-bearing resources and cleanup.
    ```

2. 提案された計画を確認します。Copilot が `microsoft-foundry` スキルを使う予定であり、ホスト型エージェントを既存の Astro アプリケーションから分離していることを確認します。懸念事項や予想外の内容があれば、進める前に修正を依頼してください。
3. 方針に納得できたら、プラン モードを終了します。

## Foundry プロジェクトとモデルをセットアップする

エージェントには Foundry プロジェクトとデプロイ済みのモデルが必要です。Microsoft Foundry Skill を使い、サブスクリプション内の現在の提供状況とクォータに基づいて選択します。

1. Copilot にプロジェクトの作成を依頼します。リソースの作成を承認する前に、選択したサブスクリプション、リージョン、クォータ、推定コストを確認します。

    ```text
    Use the Microsoft Foundry Skill to create a public Foundry project for this project. Use the resource group rg-tailspin-toys and project name tailspin-toys.
    ```

    ![パブリックな Foundry プロジェクトを作成する](../../../_images/cli-8-create-foundry-project.png)

2. プロジェクトの準備ができたら、Copilot にモデルの提案を依頼します。

    ```text
    Use the Microsoft Foundry Skill to recommend two or three current chat models available in the tailspin-toys project for the Backer Concierge acceptance criteria in the issue titled "Add a Backer Concierge assistant for catalog questions". Prioritize low latency, instruction following, grounding fidelity, available quota, and models that aren't approaching retirement. There is no complex math or multi-step planning. Explain the tradeoffs and wait for me to choose a model from the recommended options.
    ```

    Copilot から、推奨された選択肢の中からモデルを選ぶよう求められる場合があります。

    ![推奨された選択肢の中からモデルを選択する](../../../_images/cli-8-select-foundry-model.png)

    以降の手順では `gpt-5.4-mini` を使いますが、提供状況とクォータはリージョンによって異なります。

3. 推奨された選択肢からモデルを選び、Copilot に選択したモデルのデプロイを依頼します。デプロイを承認する前に、容量とコストを確認します。

    ```text
    Deploy the model we selected to the tailspin-toys Foundry project and use the model name as the deployment name. Choose an SKU with available quota, ask me to confirm the capacity before deployment. After deployment, show me the deployment status.
    ```

    ![選択したモデルをデプロイする](../../../_images/cli-8-deploy-foundry-model.png)

> [!TIP]
> モデルの提供状況は変わります。適切なのは、例に固定で指定されたモデルではなく、プロジェクトで利用可能だと Copilot が確認したモデルです。

## デプロイ済みのモデルをテストする

ホスト型エージェントを構築する前に、モデルが Backer Concierge のグラウンディング（根拠となる情報に基づいて回答すること）のルールを守るかテストします。エージェントのコードや構成は使わず、予定している指示とカタログのコンテキストでテストします。

まず、サインイン中のアカウントに、モジュール 2 でのホスト型エージェント開発用の **Foundry Project Manager** ロールと、モデルを直接呼び出して推論するための **Cognitive Services OpenAI User** ロールを付与します。その後、カタログに含まれない情報も要求する、カタログに関する質問をします。

1. 新しいターミナルを開き、アカウント、プロジェクト、ユーザーの値を設定します。`<foundry-account-name>` は、プロジェクト作成時に表示された Foundry アカウント名に置き換えます。

    ```bash
    SUBSCRIPTION_ID=$(az account show --query id --output tsv)
    USER_OBJECT_ID=$(az ad signed-in-user show --query id --output tsv)
    FOUNDRY_ACCOUNT="<foundry-account-name>"
    ACCOUNT_SCOPE=$(az cognitiveservices account show --name "$FOUNDRY_ACCOUNT" --resource-group rg-tailspin-toys --query id --output tsv)
    PROJECT_SCOPE="$ACCOUNT_SCOPE/projects/tailspin-toys"
    ```

2. **Foundry Project Manager** ロールを割り当てます。

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Foundry Project Manager" \
       --scope "$PROJECT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

3. **Cognitive Services OpenAI User** ロールを割り当てます。

    ```bash
    az role assignment create \
       --assignee-object-id "$USER_OBJECT_ID" \
       --assignee-principal-type User \
       --role "Cognitive Services OpenAI User" \
       --scope "$ACCOUNT_SCOPE" \
       --subscription "$SUBSCRIPTION_ID"
    ```

4. Copilot CLI に戻り、次を入力します。

    ```text
    Use the Microsoft Foundry Skill to test my deployed model directly in the tailspin-toys project without creating an agent. Ground it with content from @db/catalog.json and ask: "I love puzzle games about tracking down bugs. What should I back, and how much funding has it raised?" Show me the response and useful metadata like tokens used and response time (only if you can obtain it). Do not change files or create resources.
    ```

    ![カタログに実在するゲームを勧め、資金調達データがないことを伝える Foundry モデルの回答](../../../_images/cli-8-foundry-agent-response.png)

5. 回答を確認します。カタログに実在するゲームだけを勧め、カタログの正しい詳細を使い、資金調達に関する情報がないことを説明している必要があります。モデルがタイトル、ゲームの詳細、資金調達総額を作り上げた場合は、続行する前に別の推奨モデルと比較してください。

> [!NOTE]
> このテストは、一時的な指示とカタログのコンテキストを使って、デプロイ済みのモデルだけをテストするものです。エージェントのテストではありません。モジュール 2 では、ひな形を作成した後にテストを繰り返し、ホスト型エージェントのコード、パッケージ化、会話の動作を検証します。

## まとめと次のステップ

Azure ツールを準備し、カタログをエクスポートして、デプロイ済みのモデルが Backer Concierge のグラウンディング ルールに従うかテストしました。このモジュールのチェックポイントは、不足している情報を作り上げずに、カタログに実在するゲームを勧めるモデルです。

次は、同じリポジトリ、`foundry-agent-cli` ブランチ、Copilot CLI セッション、Foundry プロジェクト、選択したモデルのデプロイを使って、[エージェントを構築してデプロイします][next-lesson]。ここで終了する場合は、継続的なコストを避けるために [Azure リソースをクリーンアップしてください][cleanup]。

[overview]: ../
[next-lesson]: ../2-build-and-deploy/
[cleanup]: ../#リソースをクリーンアップする
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azd]: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
