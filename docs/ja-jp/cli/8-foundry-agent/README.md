---
slug: ja-jp/cli/8-foundry-agent
title: "オプション: Foundry を組み込む"
description: "モデルを準備し、カタログに基づくエージェントを構築してデプロイし、Tailspin Toys に接続する全 3 モジュールのシリーズです。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
---

このオプション シリーズでは、GitHub Copilot CLI と Microsoft Foundry Skill を使って、Tailspin Toys のカタログを会話型アシスタントに変えます。3 つのモジュールを通じて、プロジェクトとモデルのセットアップから、ホスト型エージェントの作成、実際に動作する Web サイトとの統合まで進めます。

このシリーズでは、次の内容に取り組みます。

- Azure 環境を準備し、カタログを使ってモデルをテストする。
- ホスト型の Backer Concierge エージェントのひな形を作成し、テストしてデプロイする。
- ローカルのサーバー側プロキシとチャット ウィジェットを通じて、エージェントを Web サイトに接続する。

## シナリオ

Tailspin Toys の支援者はカテゴリやパブリッシャーでゲームを探せますが、それらのフィルターだけでは、誰もが次に遊ぶゲームを見つけられるとは限りません。たとえば、*Git の言葉遊びが好きな人には、どのゲームが向いているだろう？*と考える支援者もいます。こうした質問には、ドロップダウンの選択肢だけでは答えられません。

Tailspin Toys は、会話を通じて支援者がゲームを見つけられる **Backer Concierge** を求めています。Tailspin のカタログからゲームを勧め、好みが曖昧な場合は短い確認の質問を 1 つ行い、追加の質問を受けたときには以前のおすすめを覚えている必要があります。

支援者には信頼できる回答が必要です。コンシェルジュはカタログにある情報だけを使い、詳細が不明な場合はそのことを明確に伝える必要があります。ゲーム、パブリッシャー、評価、資金調達総額、支援者数、価格、プレイ人数、プレイ時間、発売日を作り上げてはいけません。

## 次のステップを選ぶ

各モジュールは、同じ Tailspin Toys リポジトリ、ブランチ、Foundry プロジェクトで前のモジュールの成果を引き継ぎます。それぞれ、実際に動作する状態まで完成させて終了します。

| モジュール | 取り組む内容 | 完了時の状態 |
| --- | --- | --- |
| [1. プロジェクトとモデルを準備する][project-model] | ツールをセットアップし、カタログをエクスポートして、モデルを選択してテストする | カタログに関する質問に正しく答える、デプロイ済みのモデル |
| [2. エージェントを構築してデプロイする][build-deploy] | エージェントのひな形を作成し、動作をテストして Foundry にデプロイする | 正常に動作するホスト型の Backer Concierge |
| [3. エージェントを Web サイトに接続する][connect-site] | ローカルのプロキシとチャット ウィジェットを構築し、一連の流れをテストする | ローカルの Web サイトから利用できるコンシェルジュ |

> [!IMPORTANT]
> Microsoft Foundry のホスト型エージェントはパブリック プレビューです。
>
> このシリーズでは、モデルのデプロイやホスト型エージェントなど、課金対象の Azure リソースを作成します。リソースを作成する前に、選択したサブスクリプション、リージョン、クォータ、推定コストを確認する必要があります。最初または 2 番目のモジュールで終了する場合も、[クリーンアップの手順][cleanup]に従ってください。

1. オプション シリーズを始めるには、[プロジェクトとモデルを準備する][project-model]に進みます。セットアップの手順も含まれています。
2. 中核となるワークショップを終えたい場合は、[振り返りと次のステップ][review]に進みます。

## リソースをクリーンアップする

どのチェックポイントで試行を終える場合も、不要なコストを避けるために Azure リソースを削除してください。クリーンアップでは後続のモジュールに必要なリソースも削除するため、その後に続行するにはリソースを再作成する必要があります。

> [!CAUTION]
> `rg-tailspin-toys` を削除してよいのは、この演習専用であり、保持する必要のあるリソースが含まれていない場合だけです。共有リソース グループを削除すると、無関係のリソースも削除されます。

1. 起動したローカルのエージェント、Function、Astro 開発サーバーがある場合は、それぞれのターミナルで <kbd>Ctrl</kbd>+<kbd>C</kbd> を押して停止します。
2. Copilot CLI を終了します。モジュール 2 でエージェントのひな形を作成した場合は、同じ `azd` 環境を使い、Tailspin Toys リポジトリのルートから次を実行します。

    ```bash
    azd down --purge
    ```

3. `az account show` で選択中のサブスクリプションを確認します。そのサブスクリプションの `rg-tailspin-toys` を調べ、残っているリソースがすべてこの演習に属することを確認します。モジュール 1 で終了した場合は、`azd` サービスのひな形をまだ作成していなくても、Foundry プロジェクトとモデルをクリーンアップする必要があります。
4. ワークショップ専用のリソース グループがまだ存在し、削除する予定のリソースだけが含まれている場合は、次を実行します。

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. Azure ポータルで、リソース グループの削除が完了したことを確認します。`--no-wait` を指定したコマンドは、削除が完了する前に戻ります。

## リソース

- [Azure Skills Plugin][azure-skills]
- [コーディング エージェントで Microsoft Foundry Skill を使う][foundry-skill]
- [Microsoft Foundry Skill で最初のホスト型エージェントをデプロイする][hosted-agent-quickstart]
- [ホスト型エージェントのアクセス許可][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../9-review/
[cleanup]: #リソースをクリーンアップする
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
