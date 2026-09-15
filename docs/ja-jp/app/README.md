---
slug: ja-jp/app
title: "GitHub Copilot app"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

[**GitHub Copilot app**](https://docs.github.com/copilot/concepts/agents/github-copilot-app) は Copilot CLI を基盤とするデスクトップアプリケーションで、エージェント主導の開発を単一の作業用ワークスペースで実現します。並列エージェントセッション、切り替え可能なセッションモード、共有キャンバス、GitHub Issue と pull request のネイティブ管理機能を備えています。さらに、リベース、レビューのフィードバック、CI の修正、マージまで pull request を導く **Agent Merge** も利用できます。

セットアップを扱うレッスン0～1で、プロジェクトと App のワークスペースを準備します。9つのコアモジュールであるレッスン2～10では、まず星評価を追加する小さな変更と、実際のコードで効果を確認するドキュメント規約に取り組みます。次にフィルター機能を計画・構築し、シェルスクリプトを同梱した quality-checks スキルを作成して実行します。Playwright MCP で機能を観察し、要件とカバレッジを評価する QA カスタムエージェントを作成します。機能全体の PR をレビューして Agent Merge を承認した後、共有トリアージキャンバスを作成してマージします。

ワークショップには4つの PR マイルストーンがあります。星評価、指示とその実証、フィルター機能とスキル・QA プロファイル・テスト、そしてキャンバスです。各マイルストーンは更新済みの `main` から開始し、モジュールごとではなく PR ごとに1つのブランチを使用します。レッスン4～8では、同じフィルター機能のセッション、ワークツリー、ブランチを維持します。キャンバスを再度開く際は Issue のコンテキストを追加するだけで、別の機能や5つ目の PR には着手しません。自動化は次のステップとしてリンクを紹介し、追加の演習にはしません。

## レッスン

| レッスン | トピック | 説明 |
|--------|-------|-------------|
| [0. 前提条件][ex0] | セットアップ | Node.js をインストールし、Tailspin Toys プロジェクトの自分用コピーを作成します |
| [1. Copilot app のインストール][ex1] | セットアップ | アプリをインストールしてプロジェクトを接続し、ワークスペースを確認します |
| [2. 星評価の追加で小さな成果を得る][ex2] | 最初の変更 | 既存の評価と null の場合の表示を追加し、PR 1 をマージします |
| [3. カスタム指示による Copilot のガイド][ex3] | コンテキスト | ドキュメント標準と実際の実証コードを追加し、PR 2 をマージします |
| [4. Plan と Autopilot によるフィルター機能の構築][ex4] | 実装 | 計画を承認し、フィルター機能を実装・検証してチェックポイントを保存します |
| [5. quality-checks スキルの作成と使用][ex5] | 繰り返し実行できるチェック | 同梱するシェルスクリプトを作成、確認、実行します |
| [6. Playwright MCP による機能の検証][ex6] | ブラウザーでの観察 | Customize から MCP を設定し、フィルターの動作を確認します |
| [7. QA エージェントの作成と使用][ex7] | 要件とカバレッジ | 専門家のプロファイルを選択し、最終検証の証拠を収集します |
| [8. 機能の PR の作成とマージ][ex8] | レビューとマージ | フィルター機能、スキル、QA プロファイル、テストをレビューし、PR 3 の Agent Merge を承認します |
| [9. トリアージキャンバスの作成][ex9] | コラボレーション | リポジトリに保存するキャンバスを PR 4 で共有し、Issue のコンテキストを追加します |
| [10. 振り返りと次のステップ][ex10] | まとめ | ワークフロー、成果物、追加のリソースを振り返ります |

## 前提条件

このワークショップに参加する前に、次のものを用意してください。

- [ ] 有効な **Copilot Student、Pro、Pro+、Business、Enterprise** のいずれかのプランが設定された GitHub アカウント
- [ ] **macOS、Linux、Windows** のいずれかを実行するコンピューター
- [ ] コンピューターに[インストールされた Git][install-git]

> [!TIP]
> 有料プランを利用していない場合、認証済みの学生は [GitHub Education][callout-student-plan-education] を通じて GitHub Copilot を無料で利用できます。**Copilot Student** プランには、このワークショップで使用するエージェント、MCP、コードレビュー、Copilot CLI の各機能が含まれているため、すべてのハーネスを完了できます。

> [!NOTE]
> Copilot app は codespace ではなく自分のコンピューターで実行するため、[レッスン 0][ex0] では、アプリをインストールする前に Node.js をインストールし、プロジェクトの自分用コピーを作成します。

> [!NOTE]
> Copilot Business または Copilot Enterprise を使用している場合、アプリを使用するには管理者が **Copilot CLI** ポリシーを有効にする必要があります。

## はじめる

[**レッスン 0「前提条件」から始める →**][ex0]

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students