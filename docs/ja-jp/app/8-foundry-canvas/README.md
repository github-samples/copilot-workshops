---
title: "オプション: Foundry を組み込む"
slug: ja-jp/app/8-foundry-canvas
description: "Microsoft Foundry Canvas を使ってカタログに基づく Backer Concierge を構築します。各段階で安全に中断できます。"
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev:
  link: /copilot-workshops/ja-jp/app/9-review/
  label: 振り返りと次のステップ
next:
  link: /copilot-workshops/ja-jp/app/8-foundry-canvas/1-project-and-model/
  label: プロジェクトとモデルを準備する
---

このオプションの学習では、GitHub Copilot app の Microsoft Foundry Canvas を使い、Tailspin Toys に **Backer Concierge** を追加します。カタログに基づくモデルの実験から始め、ホステッド エージェントの構築、ローカル Web サイトへの統合へと進みます。

## 学習の流れ

各モジュールの最後にはチェックポイントがあり、安全に中断できます。学習全体を通じて、同じ Tailspin Toys リポジトリ、worktree ブランチ、Issue にリンクされたセッション、Foundry プロジェクト、モデルデプロイを使用します。

- [プロジェクトとモデルを準備する][module-1]では、カタログで扱える情報の範囲を定め、プロジェクトとモデルデプロイを作成し、Canvas で確認します。
- [エージェントを構築してデプロイする][module-2]では、Backer Concierge のひな形を作成してローカルでテストし、ホステッド エージェントをデプロイして再テストします。
- [エージェントをサイトに接続する][module-3]では、資格情報を保護するローカルプロキシ、アクセシビリティに配慮したチャットウィジェット、エンドツーエンドテスト、Agent merge を追加します。

> [!IMPORTANT]
> Microsoft Foundry Canvas とホステッド エージェントはパブリックプレビュー段階です。
>
> この学習では、モデルデプロイや、モジュール 2 以降のホステッド エージェントなど、課金対象の Azure リソースを作成します。リソースを作成する前に、サブスクリプション、リージョン、クォータ、推定コストの承認が必要です。プロジェクトとモデルの作成だけで中断する場合も、クリーンアップが必要です。

1. [プロジェクトとモデルを準備する][module-1]から始めます。作業は、このワークショップのコンテンツリポジトリではなく、Tailspin Toys リポジトリで進めてください。
2. プロジェクトとモデル、ホステッド エージェントのデプロイ、完全な統合のいずれか、選んだ段階で中断する際は、モジュールのチェックポイントを記録します。実験を終えたら、以下の共通のクリーンアップ手順に従ってください。クリーンアップ後に再開するには、削除したリソースを復元し、構成を再確認する必要があります。

## リソースをクリーンアップする

クリーンアップの内容は、どの段階まで進んだかによって異なります。プロジェクトとモデルだけを作成した場合、`azure.yaml`、`azd` 環境、ホステッド エージェントは必要ありません。

> [!WARNING]
> リソースの削除は破壊的な操作です。ここで削除できるのは、このワークショップ専用のリソースだけです。共有リソースグループは絶対に削除しないでください。代わりに、リソースの所有者と協力し、ワークショップのリソースを個別に削除するのが安全です。

1. 起動したローカルの Agent Inspector、Azure Function、Astro 開発サーバーのプロセスを、それぞれのターミナルで停止します。Azure リソースを削除する前に、必要なチェックポイントの詳細を記録します。
2. Azure ポータルで、アクティブなサブスクリプション ID、ワークショップ用リソースグループの正確な名前、その中のすべてのリソースを確認します。Foundry プロジェクトとモデルデプロイが今回の実習用であることを確認します。サブスクリプション、所有者、内容が不明確な場合は、確認できるまでクリーンアップを中断してください。
3. 中断する段階に応じたクリーンアップ方法を選びます。モジュール 1 だけを完了した場合は、次の手順を飛ばして手順 5 に進みます。クリーンアップだけのために `azure.yaml` を作成したり、`azd` を初期化したりしないでください。モジュール 2 または 3 で Canvas を使ってデプロイした場合は、手順 4 に進みます。
4. ホステッド エージェントをデプロイした場合は、ルートに `azure.yaml` がある同じ Tailspin Toys worktree でターミナルを開きます。選択した `azd` 環境が今回の実習のサブスクリプションとリソースを対象にしていることを確認し、削除対象のリソースを確認します。すべての対象がワークショップ専用の場合に限り、次を実行します。

   ```bash
   azd down --purge
   ```

5. プロジェクトとモデルだけを作成した場合、または `azd down` の実行後もワークショップ専用のリソースグループが残っている場合は、ポータルでサブスクリプション、グループ名、リソースの全一覧を再確認します。グループ全体が今回の実習専用で、名前が正確に `rg-tailspin-toys` である場合は、次を実行します。名前が異なる場合は、確認済みの専用グループ名に置き換えてください。共有グループの場合は、このコマンドを実行せず、所有者と調整してリソースを個別にクリーンアップします。

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

6. Azure ポータルで削除の完了を確認します。`--no-wait` は削除が完了する前に処理を返します。ワークショップのモデルデプロイとホステッド エージェントのリソースが削除されたことを確認し、共有リソースを削除せずに、残っている課金対象のワークショップリソースに対処します。
7. 選んだチェックポイントの記録とクリーンアップが完了したら、[振り返りと次のステップ][core-review]に戻ります。

## リソース

Microsoft のドキュメントで、Canvas、ホステッド エージェントのデプロイ、およびそれらのアクセス許可について説明されています。

- [Microsoft Foundry Canvas とは][foundry-canvas]
- [Foundry Canvas で最初のホステッド エージェントをデプロイする][hosted-agent-quickstart]
- [ホステッド エージェントのアクセス許可][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../9-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
