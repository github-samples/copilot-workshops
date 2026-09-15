---
title: "レッスン 10 - 振り返りと次のステップ"
description: "App の9つのコアモジュール、4つの PR マイルストーン、再利用可能な品質管理ワークフローを振り返り、追加のリソースを確認します。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

ここ数回のレッスンでは、GitHub Copilot app を使い、アイデアから機能のマージまでを実践しました。取り組んだ内容は次のとおりです。

- リポジトリを接続し、アプリのワークスペースと用意されたバックログを確認した。
- 直接指定したタスクと Issue からセッションを開始し、Plan モードと Autopilot モードでエージェントの動作を制御した。
- カスタム指示でエージェントをガイドし、シェルスクリプトを含む再利用可能なスキルの作成を依頼して、スクリプトを確認した後、lint、単体テスト、エンドツーエンドテスト、型チェックを実行した。
- Playwright MCP server を使い、実際のブラウザーで作業をテストした。
- 要件、カバレッジ、スキルのスクリプトの結果、ブラウザーでの証拠を評価する QA カスタムエージェントを作成して選択した。
- 共有キャンバスでエージェントと共同作業した。
- 最初の PR を自分で明示的にマージし、その後、機能とキャンバスの PR ワークフローで **Agent Merge** を承認した。

セットアップのレッスン0～1から、9つのコアモジュールであるレッスン2～10に進みました。成果物と次のステップを振り返りましょう。この振り返りで追加の実習タスクを始めることはありません。

## リリースしたもの

ワークショップには4つの PR マイルストーンがあり、それぞれ更新済みの `main` から作成した専用のブランチを使用します。

1. **星評価:** ゲームカードに既存の `starRating` と明示的な未評価状態を表示します。
2. **指示と実証:** ドキュメント規約を追加し、小さな実際のコード変更で効果を検証します。
3. **フィルター機能と品質管理ワークフロー:** Issue を実装し、シェルスクリプトを同梱した `quality-checks` スキルと QA プロファイルを作成して、関連するテストも含めます。
4. **リポジトリに保存したトリアージキャンバス:** 別の機能を自動実装せず、Issue のコンテキストを追加するボードを共有します。

レッスン4～8では、同じフィルター機能のセッション、ワークツリー、ブランチを使用しました。チェックポイントコミットで PR 3 内の進捗を保存し、スキル、MCP 設定、QA のために別の機能ブランチは必要ありませんでした。後のマイルストーンは、前の PR がマージされ、新しいセッションのブランチを `origin/main` から更新した後にのみ開始しました。

## 検証方法の違い

最初の機能では既存の npm チェックを使用しました。フィルター機能では手動のブラウザー確認を追加しました。スキルは同梱のスクリプトで4つのチェックを繰り返し実行できるようにし、MCP はエージェントによる直接のブラウザー観察を追加し、QA は要件とカバレッジを最終検証と組み合わせました。PR では、提出するリビジョンに適用できる場合にのみ QA の証拠を再利用しました。

追加するテストは実際の不足を補うものにします。新しいテストが不要な QA 実行も正しい結果になり得ます。ツールの不足、スキップされたチェック、失敗は明示すべき阻害要因であり、成功ではありません。マージを承認する前にコードと証拠をレビューし、変更後は関連する証拠を更新してください。

## ベストプラクティス

AI ツールを使用するときは、その周辺の基盤が出力の品質を左右します。このワークショップでは指示、スキル、QA プロファイルを作成しました。これらをレビューし、セッション間で再利用してください。カスタムエージェントは専門家としての役割と指示を定義し、利用可能なツールは設定とハーネスの権限によって決まります。スキルは、必要に応じて読み込む再利用可能なタスクの指示、実行可能なスクリプト、補助リソースをまとめます。カスタムエージェントも、スキルに同梱されたものを含め、スクリプトを実行できます。説得力のある説明だけを信頼せず、実際のスクリプト実行とカスタムエージェントの選択を確認してください。

タスクに合わせて**モードとモデル**を選択します。構築前にアプローチを検討するには **Plan**、対象を絞った変更で作業に関与し続けるには **Interactive**、範囲が明確で分離されたタスクに限って **Autopilot** を使用します。定型的な編集には高速なモデルを選び、複雑な作業には推論能力が高く、より多くの推論を行うモデルを選びます。

基盤と同じくらい、コンテキストも重要です。何を、なぜ、どのように構築するかを明確に説明すると、出力は大きく変わります。アイデアを本格的なセッションに移す前に範囲を決める場所として、Quick chats が役立ちます。

## さらに確認する機能

コアワークフローを学習しました。ほかにも確認する価値がある機能があります。

- 完全なセッションを必要としない、その場限りの簡単な質問に使用する **Quick chats**。
- 最近の作業の要約など、定期的またはオンデマンドのタスクに使用する [**Automations**][using-automations]。導入前にスケジュール、権限、範囲をレビューしてください。自動化の作成は次のステップであり、このワークショップの一部ではありません。
- 構築前に問題について対話し、重要なフィードバックを得るための **Rubber duck**。
- ロール、その tools、指示をまとめ、繰り返し使用する専門的な作業に対応する [**Custom agents**][custom-agents]。
- セッションで起きたことの記録を生成する [`/chronicle`][chronicle]。
- Ollama、Foundry Local、LM Studio を介したローカルモデルなど、独自のプロバイダーのモデルを使用する [Bring your own key (BYOK)][byok]。
- GitHub がホストする分離環境でセッションを実行する [Cloud sandboxes][sandboxes]。
- アプリを直接リポジトリ、セッション、プロンプトの画面で開く [Deep links][deep-links]。

## 次のステップ

ツールを使いこなす最良の方法は、使い続けることです。実稼働コード、趣味のコード、長年構想していながら構築できていなかった小さなアプリなどに活用してください。学んだことをチームと共有し、チームからも学びましょう。そして、引き続きドキュメントを確認してください。

GitHub Copilot エコシステムをさらに学ぶには、[VS Code ハーネス][vscode-harness]、[Copilot CLI ハーネス][cli-harness]、[Cloud agent ハーネス][cloud-harness]を確認してください。

## リソース

- [GitHub Copilot app について][about-copilot-app]
- [GitHub Copilot app の概要][getting-started]
- [GitHub Copilot app のカスタマイズ][customize]
- [Automations の使用][using-automations]
- [Canvas extensions の操作][canvas-docs]
- [クラウドサンドボックスとローカルサンドボックスについて][sandboxes]

[previous-lesson]: ../9-canvases/
[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links