---
title: "レッスン 5 - quality-checks スキルのカスタマイズと使用"
description: "既存の quality-checks スキルを確認し、報告形式をカスタマイズして、フィルター機能の検証に使用します。"
authors:
  - geektrainer
lastUpdated: 2026-09-11
---

コードを書く作業には、単にコードを書く以上のことが含まれます。コードが動作することは手動で検証し、指示ファイルを使用して標準に従っていることも確認しました。しかし、テストや lint、継続的インテグレーション (CI) のその他の作業はどうでしょうか。

このようなタスクには、**エージェントスキル**が最適です。スキルを使用すると、こうした処理を適切に実行する方法を Copilot が理解できます。

このレッスンでは、次の内容を学習します。

- 既存の `quality-checks` スキルと同梱のスクリプトを確認する。
- 結果の報告形式をカスタマイズする。
- スキルを実行し、出力をレビューする。

## シナリオ

Tailspin Toys には、pull request (PR) を作成する前に必ず実行する必要がある単体テストと E2E テストがあります。これらを正しく一貫して実行することが重要です。チームはすでにテスト実行用のエージェントスキルを作成していますが、読みやすい出力に改善したいと考えています。

## 指示、スクリプト、リソース

エージェントスキルは、再利用可能なタスクの指示、実行可能なスクリプト、補助リソースをまとめたもので、エージェントが必要に応じて読み込みます。基本的には、スキル名のフォルダーと、その中の `SKILL.md` という Markdown ファイルで構成されます。Markdown には、スキルの名前と説明を定義するフロントマター、スキルの動作概要、呼び出すタイミングのガイダンスが含まれます。フォルダーには、スキルの呼び出し時に使用するスクリプトやその他のリソースを収めたサブフォルダーも追加できます。

> [!NOTE]
> スキルに追加のフォルダーやファイルは必須ではありません。この例では、`npm` コマンドを使ってテストと linter を実行するため、追加の補助ファイルは必要ありません。

スキルをプロジェクトの `.github/skills` フォルダーに置くと、チーム内で共有および再利用できるリポジトリアセットになります。または、通常は `~/.copilot/skills` にある Copilot のルートフォルダーにも配置できます。

## スキルを確認する

Tailspin Toys チームがテストと linter の実行用に作成した `quality-checks` というスキルを確認します。

1. **Files** キャンバスをまだ開いていない場合は、レビューパネルで **+**、**File** の順に選択します。
2. `.github/skills/quality-checks/SKILL.md` を検索します。
3. 冒頭の `name` と `description` を読みます。Copilot はこの説明を使い、スキルを呼び出すタイミングを判断します。
4. 指示を読み、テストと lint のプロセスを Copilot にどのように案内しているかを確認します。

## 変更前にスキルを実行する

スキルはスラッシュ (`/`) コマンドで直接呼び出すことも、自然言語で呼び出すこともできます。このスキルの説明には、テストまたは lint の実行を依頼されたときに使用することが示されています。Copilot にテストの実行を依頼して、スキルを実行しましょう。

1. モードのドロップダウンから **Interactive** を選択し、Copilot が Interactive モードになっていることを確認します。
2. 次のプロンプトを使って Copilot にテストと linter の実行を依頼し、スキルを呼び出します。

    ```plaintext
    Run the tests and linters.
    ```

3. 最後に表示されるレポートを確認します。

## 報告形式をカスタマイズする

実行したテスト、成功率と失敗率、実行にかかった時間を示す、よりわかりやすいレポートが必要です。Copilot がそのレポートを作成するようにスキルを更新しましょう。

1. **Files** キャンバスに戻ります。
2. まだ開いていない場合は、`.github/skills/quality-checks/SKILL.md` を開きます。
3. ファイルの末尾にある **Results output formatting** という見出しを見つけます。
4. その見出しのすぐ下に次の内容を追加し、指定した形式で結果を表示するようにします。

    ```markdown
    Upon completion of all tests, generate a report that provides a quick overview of both success and failure of the tests, and how long they took to ran. In particular, we need sections for:

    - Unit tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - End to end tests, total number of tests, number succeeded, number failed, a percentage thereof, and the amount of time testing took.
    - Linting, number of lines scanned, number of violations, and the percentage of lines of code that meet the linting requirements.
    ```

ファイルは自動的に保存されます。

## 更新したスキルを実行する

変更したスキルを実際に試してみましょう。先ほどとまったく同じプロンプトを使用します。

1. モードのドロップダウンから **Interactive** を選択し、Copilot が Interactive モードになっていることを確認します。
2. 次のプロンプトを使って Copilot にテストと linter の実行を依頼し、スキルを呼び出します。

    ```plaintext
    Run the tests and linters.
    ```

3. 最後に表示されるレポートを確認します。

## まとめと次のステップ

既存のエージェントスキルをカスタマイズして使用しました。このレッスンでは、次の作業を行いました。

- `quality-checks` スキルと同梱のスクリプトを確認した。
- 結果の報告形式をカスタマイズした。
- スキルを実行し、出力をレビューした。

この変更は、フィルター機能と一緒に機能の PR に含めます。次は、[Playwright MCP server を通じて][next-lesson] Copilot がサイトを直接操作できるようにします。

## ほかのスキルの例

これらのコミュニティの例は参考資料であり、追加のタスクではありません。採用する前に前提条件と動作を確認してください。

- [Agent Skills 仕様][skill-spec]。
- [コントリビューションのワークフロー: `make-repo-contribution`][contribution-example]。
- [要件文書: `prd`][prd-example]。
- [図と同梱のエクスポートスクリプト: `drawio`][drawio-example]。
- [ブラウザーテスト: `webapp-testing`][browser-example]。

上流のコントリビューション例の名前は `make-repo-contribution` です。古い Tailspin テンプレートでは、異なる名前の `make-contribution` を使用していました。このワークショップは、どちらのコントリビューション用スキルにも依存しません。

[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
