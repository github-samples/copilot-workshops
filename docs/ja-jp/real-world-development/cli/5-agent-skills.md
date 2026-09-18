---
title: "演習 5 - エージェント スキルを使う"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

アプリ開発では、build の生成、test の実行、pull request の作成といった繰り返し可能なタスクがよく発生します。**Agent skill** を使うと、Copilot やほかの AI agent に対して、それらのタスクをどのように実行すべきかを示すガイダンスを与えられます。skill は、agent が必要に応じて読み込める instruction、script、resource のフォルダーです。[Agent Skills は open standard][agent-skills-repo] であり、さまざまな agent が利用しています。そのため、同じ skill を Copilot Chat の agent mode、Copilot cloud agent、Copilot CLI、GitHub Copilot app の間で共有できます。

skill はプロジェクトの `.github/skills` フォルダー、またはグローバルな `~/.copilot/skills` に配置します。各 skill はフォルダー単位で、YAML frontmatter（`name` と `description`）を持つ `SKILL.md` ファイルと、その後に続く markdown の instruction で構成されます。

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

skill には、script、asset、参照資料を含むサブフォルダーを追加することもできます。全体の構造は [agent skills specification][agent-skills-spec] で説明されています。

> [!TIP]
> skill は動的に読み込まれます。どの skill が適用されるかは、agent が `description` フィールドを基に判断します。明確でシナリオに即した説明にすることが、使われる skill と無視される skill を分けます。

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
team の pull request が、定められた仕様に確実に従うよう skill を使う方法を見ていきましょう。

## シナリオ

チームでは pull request（PR）に対して、次の要件を定めています。

- 明確な commit message にし、ファイルは論理的にグループ化する。
- PR を作成する前に、すべての test が通過している必要がある。
- 各 PR には次のセクションを含める必要がある。
    - 変更を行った理由の説明。
    - 変更したファイルの概要。
    - 重要なコード ブロックの抜粋。
    - 行った変更の詳細をまとめた説明。

チームでは、Copilot を使ってコードや PR を生成しているため、AI ツールがこれらの要件に従うことを確実にしたいと考えています。

この演習では、次のことを行います。

- pull request 作成用に既存の skill を確認する。
- AI agent がどのように skill を利用するかを学ぶ。
- skill の助けを借りて、ガイドラインに沿った PR を作成する。

## skill を実行する

skill は、agent が必要だと判断したときに動的に読み込まれます。どの skill を使うかの判断は、`SKILL.md` ファイル内の description によって決まります。そのため、skill の用途を明確に定義した説明を書くことが重要です。

## PR skill を確認する

Tailspin Toys には PR 作成に関する要件があるため、AI ツールがこれらのガイドラインに従った PR を生成できるように skill が用意されています。どのような動作をするか理解するために、その skill を確認しましょう。

1. `.github/skills/make-contribution/SKILL.md` を開きます。
2. name と description を確認します。description では、pull request の作成や commit の作成を求められたときに使うべき scenario が示されていることに注目してください。
3. skill 全体を読みます。branch の作成方法、commit の作り方、pull request の内容に関するルールが定義されていることを確認します。

## skill を使う

先ほど触れたとおり、skill は Copilot CLI によって自動的に呼び出されます。そのため、必要なのは Copilot に PR を作成するよう依頼することだけです。

> [!TIP]
> **Copilot CLI セッションを開始する**
>
> 以下の演習を始める前に、codespace に戻ってターミナルを開きます（まだ開いていない場合は <kbd>Ctrl</kbd>+<kbd>\`</kbd>）。次に、`--yolo` と `--enable-all-github-mcp-tools` を付けて Copilot CLI を起動します。
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 新しく開始する代わりに、このプロジェクトの直近のセッションを引き継ぐには `copilot --yolo --enable-all-github-mcp-tools --continue` を実行します。前の演習から Copilot CLI がすでに実行中であれば、`/clear` を送ってクリーンな会話を開始してください。
>
> `--enable-all-github-mcp-tools` を付けると、現在のセッションで GitHub MCP の読み取り / 書き込みツールが有効になります。これにより、ワークショップの流れの中で Copilot がバックログを読み取り、pull request を開けるようになります。

> [!CAUTION]
> `--yolo` は完全な自動権限（`--allow-all-tools`、`--allow-all-paths`、`--allow-all-urls`）を有効にします。Codespace や VM のような分離された環境でのみ使用し、日常的な開発の既定値として alias しないでください。詳しくは [Allowing and denying tool use][allow-all-warning] を参照してください。

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
1. 次のプロンプトを使って、Copilot に PR を作成するよう依頼します。

    ```
    Can you please create a pull request for me!
    ```

2. Copilot がリクエストを受け付けます。しばらくすると、Copilot が **make-contribution** skill を利用していることが表示されます。

3. その後、Copilot は skill の instruction に従います。まず test を実行し、その後 branch、commit、最終的には PR を作成します。
4. PR が作成されたら、リポジトリに戻って PR を開きます。セクションが skill で定められたガイドラインに従い、チームの要件に一致していることを確認してください。
5. 次の演習に進む前に、このフィルタリング PR とアクセシビリティ作業を分けておけるよう、ローカル workspace を `main` から新しい branch にリセットします。

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## まとめと次のステップ

agent skill の助けを借りて、文書化された要件に沿う新しい PR を作成できました。次のことを行いました。

- pull request 作成用に既存の skill を確認する。
- AI agent がどのように skill を利用するかを学ぶ。
- skill の助けを借りて、ガイドラインに沿った PR を作成する。

skill はタスク向けに最適ですが、より高度な作業には [カスタム エージェント][next-lesson] を活用したくなります。次はそれを確認しましょう。

## リソース

- [Agent Skills について][about-agent-skills]
- [Agent Skills 仕様][agent-skills-spec]
- [Agent Skills リポジトリ][agent-skills-repo]
- [awesome-copilot の Agent Skills][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
