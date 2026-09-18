---
title: "演習 3 - GitHub Copilot CLI でプロジェクト機能を追加する"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

想像のとおり、GitHub Copilot CLI で実行する中心的な作業は、プロジェクトに機能やコードを追加することです。バックログの issue を 1 つ取り上げ、実装を Copilot に手伝ってもらいましょう。

## シナリオ

プロジェクトのフィルタリング機能を完成させるタイミングになりました。バックログにはフィルタリングに関する issue がすでにあり、前の演習でその土台となる helper も追加しています。Copilot に issue の詳細を取得してもらい、既存の作業を考慮しながら、残りの機能を実装してもらいます。

この演習では、次のことを行います。

- プラン モードを使って、フィルタリング機能を実装する計画を生成する。
- Copilot を使って、Web サイトにフィルタリングを追加するためのコードを生成する。

この演習を終えるころには、プロジェクトに新しい機能が追加されています。

## プラン モードを活用する

AI の優れた使い方の 1 つが計画づくりです。何を作りたいかの大まかなイメージはあっても、アイデアを整理したり、抜けや落とし穴を洗い出したりしたい場面はよくあります。AI ツールは、追跡質問を投げかけたり、異なる問題点や不足している要素を一緒に検討したりすることで、考えを明確にする助けになります。このプロセスを支えるために、Copilot CLI にはプラン モードが用意されています。さらに、計画にかけた時間は、設定された要件により適したコードを Copilot が生成する助けにもなります。

まずは、Copilot CLI のプラン モードを活用して新機能の作成プロセスを始めます。

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
1. 次のプロンプトを Copilot CLI に入力し、フィルタリング issue に基づく計画を作成します。

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

2. 計画を作成する過程で、Copilot から追跡質問が表示されることがあります。表示された場合は、自分ならどのように機能を実装するかに基づいて答えてください。
3. 計画が生成されたら、その設計図をレビューします。データ レイヤーや UI の残りの変更に加え、test の生成も推奨されていることに気づくはずです。
4. Copilot CLI は、計画に対して追加のフィードバックを提供する機会を提示します。カーソルを案内された位置まで下げ、提案を入力すると、Copilot がそれを取り込んだ新しいバージョンの計画を作成します。
5. 内容に満足したら、Copilot が提示する選択肢を選び、新機能の実装作業を開始します。

> [!NOTE]
> Copilot は確率的に動作するため、表示されるテキストや選択肢は完全には一致しません。ただし、実装の開始に進む選択肢が表示され、その文言は次のようなものになります。
>
> `Yes, and switch to autopilot mode`.
>
> 上の例のように、Copilot から [autopilot mode](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot) を有効にする選択肢が提示される場合があります。autopilot mode を使うと、各ステップのたびに入力を待たずに、Copilot CLI がタスクを進められます。最初の指示を与えると、タスクが完了したと判断するまで Copilot CLI が各ステップを自律的に実行します。このワークショップでは隔離された環境で動作しているため、autopilot を有効にし、すべてのツールを許可しても問題ありません。

6. Copilot がファイルの生成作業を開始します。

> [!NOTE]
> この操作には数分かかることがあります。Copilot がファイルを編集 / 作成し、test を更新 / 生成し、すべて成功することを確認するために test を実行する様子が表示されます。ここまでに確認した内容を振り返ったり、飲み物を楽しんだりするのにちょうどよい時間です。

## コードをレビューする

AI が生成したコードは、本番環境にマージする前に必ずレビューする必要があります。ここで少し時間を取り、Copilot が新機能の実装で作成 / 変更したファイルを確認しましょう。

1. Copilot CLI で次のコマンドを使い、「diff」またはコード変更を表示します。

    ```
    /diff
    ```

2. 変更されたファイルを確認します。左右の矢印キーで別のファイルに切り替えられます。新しい filter control とクライアント側フィルタリングが実装された games 一覧ページや `src/lib/games.ts`、さらに `games.test.ts` などの test が更新されているはずです。Copilot が既存の helper を完全な実装に合わせて調整した場合は、`publishers.ts` に変更が加わることもあります。

## まとめと次のステップ

Copilot CLI の助けを借りて、Web サイトにフィルタリング機能を追加できました。具体的には次のことを行いました。

- プラン モードを使って、フィルタリング機能を実装する計画を生成する。
- Copilot を使って、Web サイトにフィルタリングを追加するためのコードを生成する。

もちろん、次にやるべきことは、それが正しく動作することを確認することです。pull request を開く前に、[Playwright MCP サーバーで機能をテスト][next-lesson] しましょう。

## リソース

- [Copilot CLI を使う][using-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI のコンテキスト管理][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
