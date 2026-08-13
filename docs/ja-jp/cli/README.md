---
slug: ja-jp/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** は、ターミナルで GitHub Copilot をエージェント型のコーディング アシスタントとして利用できるようにします。コードベースを探索し、コードを生成し、コマンドを実行し、外部ツールに接続できます。すべてコマンド ラインから行えるため、グラフィカル エディターに切り替えずに作業の流れを保てます。

これらの演習では、Copilot CLI のインストールと認証から始め、カスタム命令でプロジェクトのコンテキストを与えたうえで、プラン モードを使って意図的に機能を実装します。続いて Playwright MCP サーバーを接続し、実際のブラウザーでその機能をテストします。その後、再利用可能な agent skill と custom agent で Copilot を拡張します。最後に、コンテキスト管理、モデル選択、共有に使う slash command を確認し、作成した内容を振り返ります。

## 演習

| 演習 | トピック | 説明 |
|----------|-------|-------------|
| [0. 前提条件][ex0] | セットアップ | リポジトリと codespace を作成する |
| [1. Copilot CLI のインストール][ex1] | インストール | Copilot CLI をインストールして認証する |
| [2. カスタム命令][ex2] | コンテキスト | 命令を追加し、Copilot CLI がどのように従うかを確認する |
| [3. コード生成][ex3] | コード生成 | プラン モードを使って機能を生成する |
| [4. Playwright MCP によるテスト][ex4] | 外部ツール | Playwright MCP サーバーを追加し、ブラウザーで機能をテストする |
| [5. エージェント スキル][ex5] | スキル | 専門スキルで Copilot を強化する |
| [6. カスタム エージェント][ex6] | エージェント | カスタム エージェントを確認して使用する |
| [7. スラッシュ コマンド][ex7] | CLI 機能 | コンテキスト、モデル、共有、cloud agent への任意の委任を確認する |
| [8. 振り返り][ex8] | まとめ | 重要な概念と次のステップを確認する |

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
[ex2]: 2-custom-instructions/
[ex3]: 3-generating-code/
[ex4]: 4-mcp/
[ex5]: 5-agent-skills/
[ex6]: 6-custom-agents/
[ex7]: 7-slash-commands/
[ex8]: 8-review/
