---
title: "プロジェクトとモデルを準備する"
description: "Tailspin のカタログをエクスポートし、Foundry プロジェクトとモデルデプロイを作成して、Canvas で検証します。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/ja-jp/app/8-foundry-canvas/
  label: "オプション: Foundry を組み込む"
next:
  link: /copilot-workshops/ja-jp/app/8-foundry-canvas/2-build-and-deploy/
  label: エージェントを構築してデプロイする
---

最初のモジュールでは、Backer Concierge に必要なデータと Azure リソースを準備します。この段階では、エージェントのコードやホステッド エージェントのデプロイは必要ありません。

このモジュールを終えると、次のものが揃います。

- グラウンディングの制約を明示したカタログのエクスポート。
- 機能要件に合わせて選んだ Foundry プロジェクトとモデルデプロイ。
- Canvas で検証済みのデプロイと、カタログの範囲に限定したモデルの簡単なスモークチェックの結果。

## シナリオ

Tailspin Toys の支援者は、カテゴリやパブリッシャーでゲームを絞り込めます。しかし、*Git の言葉遊びが好きな人には、どのゲームが合いますか?* といった質問には、ドロップダウンでは答えられません。Backer Concierge は Tailspin のカタログにあるゲームだけを勧め、ゲーム、パブリッシャー、評価、資金調達総額、支援者数、価格、プレイヤー数、プレイ時間、発売日を捏造してはいけません。信頼できるカタログと適切なモデルが、こうした回答の基盤になります。

## ツールと Issue セッションを準備する

このセットアップでは、GitHub Copilot app を Azure に接続し、機能に関するすべての作業をまとめて進められるようにします。

> [!IMPORTANT]
> Microsoft Foundry Canvas とホステッド エージェントはパブリックプレビュー段階です。このモジュールでは課金対象の Azure リソースを作成します。リソースを作成する前に、サブスクリプション、リージョン、クォータ、推定コストを確認する必要があります。

1. [200 ドルのクレジット付き無料 Azure サブスクリプション][azure-free]や [100 ドルのクレジット付き Azure for Students][azure-students]などの Azure サブスクリプションと、ワークショップのリソースを作成する権限があることを確認します。
2. 使用する OS に対応した [Azure CLI][install-azure-cli] をインストールし、`az version` でインストールを確認します。Azure Developer CLI のセットアップは、ホステッド エージェントのモジュールで行います。
3. GitHub Copilot app を開き、**Customize** を開いてから **Plugins** を選択します。`microsoft-foundry` を検索し、Canvas と Foundry スキルを含む Microsoft Foundry プラグインの **Install** を選択します。

   ![Microsoft Foundry プラグインのインストール](../../../_images/app-8-install-foundry-plugin.png)

4. **Customize** で **Plugins** を選択し、`azure` を検索するか、**Featured** 一覧から選択します。次に、Azure プラグインの **Install** を選択します。
5. **My work** タブで、Tailspin Toys リポジトリの **Add a Backer Concierge assistant for catalog questions** というタイトルの Issue を探して開きます。**New session** を選択し、新しい worktree で Issue にリンクされたセッションを開始します。3 つのモジュールすべてで、このリポジトリ、worktree ブランチ、Issue セッションを使い続けてください。
6. `/microsoft-foundry`、続いて `/azure` と入力し、両方のスキルがインストールされ、利用可能であることを確認します。まだプロンプトは送信しないでください。プラグインがすぐに表示されない場合は、アプリを再起動し、同じ Issue セッションに戻って再確認します。

## カタログをエクスポートする

サンプルリポジトリには、エージェントが読み込めるファイルを生成するエクスポートスクリプトが含まれています。

7. この Issue にリンクされた worktree セッションで、プロンプトボックスの既定の `/fix-issue` プロンプトを次に置き換えます。

   ```plaintext
   Install the project dependencies, seed the database, then run the existing db:export script. Show me the command output and summarize the shape and grounding limits of db/catalog.json.
   ```

8. コマンド出力を確認します。Copilot は次に相当するコマンドを実行するはずです。

   ```bash
   npm install
   npm run db:setup
   npm run db:export
   ```

   ![カタログのエクスポートの生成](../../../_images/app-8-generate-catalog-export.png)

9. `db/catalog.json` を開き、タイトル、説明、カテゴリ、パブリッシャー、星評価を持つ 21 個のゲームが含まれていることを確認します。`note` フィールドも確認してください。カタログには資金調達総額、支援者数、支援プラン、発売日は含まれていません。価格、プレイヤー数、プレイ時間も、記載がなければ外部知識で補わず、情報がないものとして扱います。エクスポートが失敗した場合や内容が異なる場合は、先に進む前に Copilot に調査と再実行を依頼します。

   ![Copilot app で開いたカタログのエクスポート](../../../_images/app-8-view-catalog.png)

## Foundry プロジェクトとモデルを設定する

先にチャットでプロジェクトとデプロイを作成しておくことで、Canvas は既存のリソースだけに接続します。

10. **+**、**Terminal** の順に選択し、Azure にサインインします。

    ```bash
    az login
    ```

11. リソースの作成を承認する前に、選択したサブスクリプション、リージョン、クォータ、推定コストを確認します。Azure ポータルで、`rg-tailspin-toys` をワークショップ専用グループの名前として使用できることを確認します。その名前が無関係のリソースや共有リソースに使われている場合は、いったん中断し、専用の名前を決めてから次のプロンプトを使用してください。学習全体を通じて、承認した名前を一貫して使用します。
12. 同じ Issue セッションで、次を入力します。

    ```plaintext
    Use the Microsoft Foundry skill to create a resource group named rg-tailspin-toys and a Foundry project named tailspin-toys.
    ```

    ![Foundry プロジェクトの作成](../../../_images/app-8-foundry-project-created.png)

13. Copilot にモデルの推奨を依頼します。Issue からセッションを開始したため、Issue の受け入れ条件はすでにコンテキストに含まれています。

    ```plaintext
    Use the Microsoft Foundry skill to recommend two or three current chat models in the tailspin-toys project that meet this issue's acceptance criteria. Explain the tradeoffs and wait for me to choose.
    ```

14. Copilot が `microsoft-foundry` スキルを読み込んだことを確認し、トレードオフを踏まえて利用可能なモデルを選びます。Microsoft Foundry のホステッド エージェントのクイックスタートでは、現在 `gpt-5.4-mini` を使用していますが、利用可否とクォータはリージョンによって異なります。

    ![モデルの選択](../../../_images/app-8-select-model.png)

15. 選んだモデルのデプロイを Copilot に依頼し、承認前に対象プロジェクトとコストを確認します。

    ```plaintext
    Deploy the model I selected to the tailspin-toys Foundry project, using the model name as the deployment name.
    ```

> [!TIP]
> モデルの利用可否は変わります。このモジュールに固定で記載されたモデルではなく、Copilot がプロジェクトで利用可能と確認したモデルを選ぶのが適切です。

## Canvas でモデルを検証してスモークテストする

この確認では、エージェントのコードを作成する前にプロジェクトとモデルを検証します。モデルのスモークチェックは、モジュール 2 で実施するホステッド エージェントのグラウンディングテストの代わりにはなりません。

16. **+**、**Canvas**、**Microsoft Foundry (Preview)** の順に選択します。
17. Canvas の右上隅にある **More options** メニューを開き、**Sign in** を選択します。
18. **tailspin-toys** Foundry プロジェクトを選択します。**Models** を展開し、デプロイが想定どおりの名前とステータスで表示されることを確認します。

    ![Canvas でのプロジェクトとモデルの検証](../../../_images/app-8-validate-project-model.png)

19. GitHub Copilot app の同じ Issue セッションで、既存のローカルの Azure サインインを使い、Canvas で確認したモデルデプロイに対して認証付きの小さなリクエストを実行するよう Copilot に依頼します。`db/catalog.json` から実在する 2 つのエントリとカタログの `note` を提供し、その抜粋だけを使って 1 つ勧めるよう求め、抜粋に価格が記載されているかも質問するよう依頼します。推奨が提供したエントリに基づき、応答が価格の情報がないことを認めているか確認します。資格情報はローカルまたはサーバー側に留め、ブラウザーのコードやチャット出力には絶対に含めないでください。エージェントのひな形は必要ありません。
20. 回答のタイトル、パブリッシャー、評価を、提供したエントリと照合します。デプロイをテストできない場合は、Canvas でプロジェクト、デプロイのステータス、アクセス権、クォータを確認し、エラーを Copilot に送ります。詳細を捏造する場合は、抜粋だけを使うという指示を明確にして再試行します。結果を記録しますが、エージェントの受け入れ条件をすべて満たした証拠とは見なさないでください。

> [!NOTE]
> Canvas は再度開いたときも、選択したプロジェクトを記憶しています。各ステージには、ひな形を作成する **Create new hosted agents**、モデル、ツールボックス、スキル、ガードレールを接続する **Build current hosted agent**、ローカル実行と Foundry Agent Service へのデプロイを行う **Deploy and test** があります。

## チェックポイントと次のステップ

次のモジュールに引き継ぐのは、カタログのエクスポートとテスト済みのモデルデプロイです。エージェントのひな形ではありません。

21. このセッションに、Tailspin Toys リポジトリ、現在の worktree ブランチ、Issue にリンクされたセッション、サブスクリプション ID、専用リソースグループ、Foundry プロジェクト、モデルデプロイ名、カタログのエクスポート結果、スモークチェックの証拠を記録します。今後、コストが発生する変更を行うたびに、選択したプロジェクトを確認してください。
22. 同じリポジトリ、worktree ブランチ、Issue セッション、Foundry プロジェクト、モデルデプロイを使い、[エージェントを構築してデプロイする][next-module]に進みます。別のプロジェクトは作成しないでください。ここで中断する場合は、[リソースをクリーンアップする][cleanup]の手順に従います。この段階では `azure.yaml` も `azd` も必要ありません。

[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account
[azure-students]: https://azure.microsoft.com/free/students
[install-azure-cli]: https://learn.microsoft.com/cli/azure/install-azure-cli
[next-module]: ../2-build-and-deploy/
[cleanup]: ../#リソースをクリーンアップする
