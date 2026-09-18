---
slug: ja-jp/vscode/7-foundry-toolkit
title: "省略可能: Foundry を組み込む"
description: "VS Code と Microsoft Foundry Toolkit を使い、根拠に基づいて回答する Backer Concierge を 3 つのモジュールで構築します。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

| [← 前のレッスン: GitHub Copilot の作業を反復して改善する][previous-lesson] |
|:--|

必須の VS Code コースは演習 6 で完了です。この省略可能な拡張演習では、VS Code の GitHub Copilot Chat と Microsoft Foundry Toolkit を使って Tailspin のカタログを Backer Concierge に活用し、ホスト型エージェントとしてデプロイして、ローカルプロキシ経由でサイトに接続します。

## シナリオ

支援者からは、フィルターでは答えられない質問が寄せられます。git の言葉遊びが好きな人に合うゲームはどれか、あるパズルゲームが別のゲームより自分に向いている理由は何か、といった質問です。Tailspin Toys には、カタログに実在するタイトルを勧め、必要に応じて確認の質問をし、資金調達額などの情報がないときはそのことを率直に伝えて信頼を得るコンシェルジュが必要です。

## モジュール

各モジュールは、動作を確認できるチェックポイントで終わります。3 つのモジュールを通して、同じ受講者用リポジトリ、機能ブランチ、Foundry プロジェクトを使います。モジュールの間でプロジェクトを作り直すことはありません。

| モジュール | 完了時のチェックポイント |
|--------|-----------------------|
| [1. プロジェクトとモデルを準備する][module-1] | カタログをエクスポートし、デプロイ済みモデルが根拠に基づいて回答するためのルールに従うことを検証済み |
| [2. エージェントを構築してデプロイする][module-2] | ローカルエージェントをデバッグし、ホスト型エージェントをテスト済み |
| [3. エージェントをサイトに接続する][module-3] | ローカルプロキシとアクセシビリティに対応したウィジェットをエンドツーエンドでテスト済み |

> [!IMPORTANT]
> Microsoft Foundry Toolkit とホスト型エージェントはパブリックプレビューです。これらのモジュールでは、モデルのデプロイやホスト型エージェントなど、課金対象の Azure リソースを作成します。サブスクリプションの権限、リージョンでの提供状況、クォータ、費用によっては参加が制限される場合があります。

## 始める前に

この拡張演習では、ワークショップのドキュメント用リポジトリではなく、自分の Tailspin Toys リポジトリを使います。

1. 省略可能な機能に着手する前に、必須演習の作業を保存、コミット、プッシュ済みであることを確認します。
2. [プロジェクトとモデルを準備する][module-1]から始めます。再開する場合は、Tailspin Toys リポジトリを `foundry-agent-vscode` ブランチで開き直し、**Foundry Toolkit** > **My Resources** に `tailspin-toys` プロジェクトとそのモデルデプロイが残っていることを確認します。
3. どのモジュールで終了する場合も、次のモジュール用に意図的にリソースを残し、継続的な費用を受け入れるのでなければ、[リソースをクリーンアップする][cleanup]の手順に従います。

## リソースをクリーンアップする

どのチェックポイントであっても、試すのを終えたら、不要な費用が発生しないように Azure リソースを削除します。クリーンアップでは後続のモジュールで必要なリソースも削除されるため、その後に続ける場合は作り直しが必要です。

> [!WARNING]
> `rg-tailspin-toys` を削除するのは、このリソースグループがこの演習専用で、残しておきたいリソースが含まれていない場合だけにしてください。共有リソースグループを削除すると、無関係なリソースも削除されます。
>
> モジュール 1 で別のリソースグループ名を承認した場合は、以下のすべてのコマンドで `rg-tailspin-toys` をその名前に置き換えてください。

1. 起動した Agent Inspector のデバッグセッション、Azure Functions ホスト、Astro 開発サーバーを、それぞれのターミナルで停止します。
2. モジュール 2 でホスト型エージェントをデプロイした場合は、`azure.yaml` がある生成済みエージェントディレクトリでターミナルを開き、同じ `azd` 環境を選択してから次のコマンドを実行します。

   ```bash
   azd down --purge
   ```

3. 選択されているサブスクリプションと、ワークショップのリソースグループがまだ存在するかどうかを確認します。

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   コマンドが `false` を返した場合、クリーンアップは完了です。`true` を返した場合は、グループ内のリソースを調べます。

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   残っているリソースがすべてこの演習のものであることを確認します。モジュール 1 で終了した場合は、`azd` サービスをデプロイしていなくても、Foundry プロジェクトとモデルのクリーンアップが必要です。

4. ワークショップ専用のリソースグループがまだ存在し、削除する予定のリソースだけが含まれている場合は、次のコマンドを実行します。

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. `--no-wait` は削除の完了前に制御を返すため、次のコマンドが `false` を返すまで繰り返し実行します。

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## リソース

- [Visual Studio Code 向け Foundry Toolkit][foundry-toolkit]
- [Microsoft Foundry エージェント拡張機能の概要][foundry-extension]

| [次のモジュール: プロジェクトとモデルを準備する →][module-1] |
|--:|

[previous-lesson]: ../6-iterating/
[module-1]: 1-project-and-model/
[module-2]: 2-build-and-deploy/
[module-3]: 3-connect-to-site/
[cleanup]: #リソースをクリーンアップする
[foundry-toolkit]: https://code.visualstudio.com/docs/intelligentapps/overview
[foundry-extension]: https://learn.microsoft.com/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension
