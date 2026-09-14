---
slug: ja-jp/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** は、ターミナルで GitHub Copilot をエージェント型のコーディング アシスタントとして利用できるようにします。コードベースを探索し、コードを生成し、コマンドを実行し、外部ツールに接続できます。すべてコマンド ラインから行えるため、グラフィカル エディターに切り替えずに作業の流れを保てます。

演習0～1のセットアップ後、演習2～10の9つのコアモジュールに取り組みます。星評価を追加する小さな変更から始め、ドキュメントの指示を整備し、**Plan** と **Autopilot** モードでフィルター機能を構築します。続いて再利用可能な quality-checks スキルを作成し、Playwright MCP で動作を検証し、QA エージェントを作成して機能をリリースします。最後に CLI の操作方法を確認し、作成した内容を振り返ります。

## 演習

| 演習 | トピック | 説明 |
|----------|-------|-------------|
| [0. 前提条件][ex0] | セットアップ | リポジトリと codespace を作成する |
| [1. Copilot CLI のインストール][ex1] | インストール | Copilot CLI をインストールして認証する |
| [2. 星評価を追加して小さな成果を得る][ex2] | 最初の変更 | 既存の評価を表示し、検証して PR 1 をマージする |
| [3. カスタム指示で Copilot を導く][ex3] | コンテキスト | ドキュメント規約を追加して実証し、PR 2 をマージする |
| [4. Plan と Autopilot でフィルター機能を構築する][ex4] | 実装 | 計画をレビューし、Autopilot を承認してテストし、チェックポイントを保存する |
| [5. quality-checks スキルを作成して使用する][ex5] | スキル | シェルスクリプトを同梱したチェックを生成、確認、実行する |
| [6. Playwright MCP で機能を検証する][ex6] | ブラウザーツール | 実際のブラウザーでフィルターの動作を観察する |
| [7. QA エージェントを作成して使用する][ex7] | エージェント | 要件とカバレッジを評価し、最終的な証拠を集める |
| [8. 機能の PR を作成してマージする][ex8] | リリース | フィルター機能と再利用可能なカスタマイズを PR 3 でまとめてレビューする |
| [9. スラッシュコマンドと CLI オプションを確認する][ex9] | CLI の操作 | コンテキスト、モデル、セッション、共有先を確認する |
| [10. 振り返りと次のステップ][ex10] | まとめ | 共通の資産と3つの PR マイルストーンを振り返る |

## ブランチと pull request

3つの pull request をマージします。星評価、指示と小さな実証、そしてフィルター機能と quality-checks スキル・QA プロファイル・関連テストです。最初の2つの PR は、それぞれマージしてから更新済みの `main` で次のマイルストーンを始めます。

演習4～8では1つの機能ブランチとチェックアウトを共有します。途中でチェックポイントコミットを保存してください。スキルの作成、MCP の設定、QA の選択で新しい機能ブランチは作成しません。演習9では別の機能や PR を開始せず、操作方法を確認します。

## 前提条件

このワークショップに参加する前に、次を準備してください。

- [ ] **Copilot Student、Pro、Pro+、Business、Enterprise** のいずれかの有効なプランがある GitHub アカウント
- [ ] ターミナル / コマンド ライン操作の基本的な知識
- [ ] インストール済みで設定済みの Git

> [!TIP]
> 有料プランがありませんか。認証済みの学生は [GitHub Education][callout-student-plan-education] を通じて GitHub Copilot を無料で利用できます。**Copilot Student** プランには、このワークショップで使用する agent、MCP、code review、Copilot CLI の機能が含まれているため、すべての harness を完了できます。

[callout-student-plan-education]: https://github.com/education/students

> [!NOTE]
> Copilot Business または Copilot Enterprise を使用している場合は、管理者が Copilot CLI を有効にしていることを確認してください。

## はじめる

**[演習 0: 前提条件から始める →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-custom-instructions/
[ex4]: 4-build-filtering/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-slash-commands/
[ex10]: 10-review/
