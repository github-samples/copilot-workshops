---
title: "演習 8 - 振り返りと次のステップ"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

ここ数回の演習で、GitHub Copilot CLI の最も一般的なユース ケースのいくつかを確認しました。具体的には次の内容です。

- GitHub やほかの MCP server と連携する。
- instruction file を使ってコード生成を導く。
- skill を実装して、Copilot CLI のツールボックスに tool を追加する。
- custom agent を呼び出して、より高度で複雑なタスクに対応する。
- slash command を使ってセッションを管理し、必要に応じて `/delegate` で cloud agent に橋渡しする。

ここでは、いくつかの slash command、ベスト プラクティス、次のステップについて確認します。

## slash command

Copilot CLI には、多数の slash command が用意されています。設定を変更したり、内部で起きていることを確認したりできるコマンドも含まれます。すでに、現在のコンテキストをクリアして新しい chat を始める `/clear` と、MCP server を確認 / 管理する `/mcp` を使いました。役立つ追加コマンドとしては次のようなものがあります。

| Command            | 説明 |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir`         | Copilot の trusted list にディレクトリを追加する |
| `/clear`, `/new`   | 会話履歴をクリアして新しく始める |
| `/compact`         | 会話履歴を要約し、context window の使用量を減らす |
| `/context`         | context window の token 使用量と可視化を表示する |
| `/diff`            | 現在のディレクトリで行われた変更をレビューする |
| `/model`           | 使用する AI model を選択する（Claude Sonnet、GPT-5 など） |
| `/plan <prompt>`   | コーディング前に実装計画を作成する |
| `/review <prompt>` | code review agent を実行して変更を分析する |
| `/delegate`        | タスクを Copilot cloud agent に委任して非同期で処理する |
| `/session`         | セッション情報と workspace の概要を表示する |
| `/share`           | セッションを markdown ファイルまたは GitHub gist に共有する |
| `/skills`          | capability を拡張する skill を管理する |
| `/usage`           | セッションの使用状況メトリクスと統計を表示する |

> [!TIP]
> `/help` を使うと、利用可能な command とキーボード shortcut の完全な一覧を表示できます。

## ベスト プラクティス

AI ツールを使うときは、基盤となる仕組みが出力品質を左右します。しっかりした instruction file、custom agent、agent skill のいずれも重要な役割を果たします。このワークショップでは、それらをそれぞれ確認しました。[awesome-copilot][awesome-copilot] はテンプレートのよい情報源であり、Copilot 自身にこれらのひな形を作らせて出発点にすることもできます。

基盤と同じくらい、コンテキストも重要です。何を作りたいのか、なぜ必要なのか、どのように進めたいのかを明確に伝えることで、出力は大きく変わります。Copilot の助けになる情報があるなら、できるだけ渡してください。

## 次のステップ

どのツールでも、スキルを高める最善の方法は使い続けることです。本番コード、趣味のコード、何年も頭の中にあったけれどまだ形にしていない小さなアプリなど、さまざまな場面で活用してください。学びをチームと共有し、チームからも学んでください。そして、いつものようにドキュメントを確認しましょう。

GitHub Copilot エコシステムをさらに試してみたい場合は、[VS Code ハーネス][vscode-harness-link] または [Cloud agent ハーネス][cloud-harness-link] を確認してください。

## リソース

- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI を使う][using-copilot-cli]
- [Awesome Copilot リポジトリ][awesome-copilot]
- [Custom instructions ガイド][repo-instructions]
- [Agent Skills ドキュメント][agent-skills]
- [カスタム エージェント ドキュメント][custom-agents]
- [MCP 仕様][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/

[vscode-harness-link]: ../../vscode/
[cloud-harness-link]: ../../cloud/
