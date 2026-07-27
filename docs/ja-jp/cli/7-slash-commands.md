---
title: "演習 7 - GitHub Copilot CLI のスラッシュ コマンド"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

優れた CLI ツールと同様に、GitHub Copilot CLI には多くの slash command が用意されています。これらのコマンドは、高度な機能、「内部で何が起きているか」に関する情報、追加の設定オプションを提供します。すでに `/clear` でコンテキストのクリアを、`/mcp` で MCP server の確認を行いました。ここでは、`/context`、`/model`、`/share`、`/delegate` など、ほかの強力なコマンドを確認します。

## シナリオ

中核となる CLI フローは完了しました。ここからは追加機能として、セッションの共有、モデルの切り替え、[Copilot cloud agent][about-cloud-agent] へのタスク委任を見ていきます。

この演習では次を使用します。

- `/share` で GitHub gist を作成し、チームとセッションを共有する。
- `/context` で、Copilot CLI が現在使用しているコンテキストを確認する。
- `/model` で利用可能なモデルの一覧を確認し、必要に応じて別のモデルを選択する。
- `/delegate` で、必要に応じてタスクを cloud agent に引き渡す。これには cloud agent が必要で、Copilot Student、Pro、Pro+、Business、Enterprise で利用できます。つまり Copilot Free を除くすべてのプランで利用可能です。

## セッションを共有する

AI ツールを含め、どのツールでも使いこなすにはスキルが必要です。チームで協力し、学びを共有し合うことが、全員の体験を改善し、より質の高いコードを生み出す最善の方法です。そのために、Copilot CLI には `/share` コマンドがあります。`/share` コマンドは、使用した prompt や Copilot がたどったロジックを含むセッションの詳細を、markdown ファイルまたは GitHub gist として生成できます。

チームと共有できる GitHub gist を作成してみましょう。

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
1. Copilot CLI のプロンプト ウィンドウで、次のコマンドを送信します。

    ```
    /share gist
    ```

2. 少し待つと、Copilot が gist を作成し、リンクを表示します。
3. リンクの文字列をコピーします。
4. 新しいブラウザー タブでそのリンクを貼り付け、gist を確認します。送信した prompt、使用した skill と agent、Copilot の思考過程、さらにローカルで実行したコマンドのコードと結果まで記録されていることに注目してください。

`/share` が生成する gist と markdown ファイルは、コードがどのように生成されたかを文書化したり、望ましい結果を得るためにどのような操作を行ったかをチームと共有したりする用途に使えます。

## Copilot CLI のコンテキストを確認する

より大きなタスクや複雑なタスクに取り組むと、モデルの最大 context window に近づくことがあります。window の正確なサイズは、使用しているモデルや Copilot CLI のバージョンによって異なります。context window が上限に達すると、Copilot CLI は自動的に compact を実行し、情報を要約して、現在のタスクに不要と判断した内容を取り除きます。slash command を使えば、現在のコンテキストの状態を確認することも、手動で compact することもできます。では、context window を見てみましょう。

1. Copilot CLI のプロンプト ウィンドウで、次のコマンドを送信します。

    ```
    /context
    ```

2. 少し待つと、Copilot CLI が現在のコンテキストを視覚的に表現した表示を生成します。

    ![Copilot CLI の context window のスクリーンショット](../../_images/cli-7-context-window.png)

3. 表示されているモデル名（画像と異なる場合があります）と、現在使用されている token の割合を確認します。その他の情報では、次の内容が示されています。

    | Title        | Description |
    | ------------ | ------------------------------------------------------ |
    | System/Tools | instruction file、ファイル内容、tool 定義 |
    | Messages     | 自分と Copilot の会話履歴 |
    | Buffer       | Copilot CLI が応答生成のために確保している予約領域 |
    | Free space   | 残りの空き領域 |

4. 次の slash command を Copilot CLI に送信し、会話履歴を compact します。

    ```
    /compact
    ```

5. 完了したら、次のコマンドを送信して現在のコンテキスト統計をもう一度表示します。

    ```
    /context
    ```

6. コンテキストの変化を確認します。現時点では context window がまだ比較的小さいため、大きな変化は見られないかもしれません。

> [!NOTE]
> Copilot CLI は、コンテキストがいっぱいになると自動的に compact を実行します。容量が 100% に近づくと、その割合がプロンプト ウィンドウの上に表示されます。通常は非同期に compact を実行するため、処理中でも Copilot との対話を続けられます。ただし、処理中の操作が数秒間ブロックされる場合があります。

### コンテキストに関するベスト プラクティス

ほとんどのセッションでは、Copilot 自身が効率的にコンテキストを管理するため、特別な指示は必要ありません。ただし、状況によっては履歴を手動でクリアまたは compact したいことがあります。

- アプリケーションの別の部分や、無関係なタスクに切り替える場合は、古い無関係なコンテキストで Copilot を混乱させないよう `/clear` を使って新しい会話を始められます。
- 最大 context window に近づいている場合は、`/compact` を手動で実行して、そのタイミングを制御できます。

> [!CAUTION]
> 繰り返しになりますが、ほとんどの場合は Copilot が直接操作なしでコンテキストを管理します。古い情報のせいで少し混乱しているように見えるときや、これから無関係なタスクに切り替えるときに、手動コマンドの利用を検討してください。

## モデルを選択する

モデルにはそれぞれ異なる強みがあり、開発者によって好みも異なります。Copilot CLI では、使用したいモデルの一覧表示と選択ができます。

1. 次の slash command を Copilot CLI に送信し、モデル一覧を表示します。

    ```
    /model
    ```

2. モデルの一覧を確認します。各モデルには、名前とリクエスト単位のコスト修正値が表示されます。
3. 必要であれば新しいモデルを選択します。終了したい場合は <kbd>Esc</kbd> を押します。

> [!CAUTION]
> Copilot CLI では、モデル選択が保持されます。

## cloud agent に委任する（任意）

ターミナルで作業を続けながら、時間のかかるタスクは Copilot cloud agent に任せたい場面があります。`/delegate` コマンドを使うと、現在の Copilot CLI セッションを GitHub.com に送信できます。cloud agent がそのセッションを引き継ぎ、非同期で作業し、完了すると pull request を開きます。

> [!NOTE]
> `/delegate` には cloud agent が必要です。これは Copilot Student、Pro、Pro+、Business、Enterprise で利用でき、Copilot Free では利用できません。アクセスできない場合は、このセクションを読んでからハンズオン手順はスキップしてください。

1. ワークショップ全体のコンテキストがまとめて委任されないよう、まず現在のセッションをクリアします。

    ```
    /clear
    ```

2. 小さく、スコープが明確な prompt を送信します。たとえば、バックログにある stretch goal のページネーションを委任できます。

    ```
    Implement pagination on the game list page so it shows a fixed number of games per page with Previous and Next controls, and add tests.
    ```

3. 次の slash command を送信して、セッションを cloud agent に引き渡します。続いて、委任したい prompt を確認します。

    ```
    /delegate
    ```

4. ブラウザーで [Copilot agents](https://github.com/copilot/agents) を開き、進捗を確認します。
5. この harness では、pull request が完了するまで待つ必要はありません。後で戻って確認できます。非同期 agent 作業の管理をより深く知りたい場合は、[Cloud agent ハーネス][cloud-harness-link] に進んでください。

## まとめと次のステップ

Copilot CLI の slash command を使うと、設定の変更、セッションの共有、Copilot の内部状態に関する情報の取得ができます。このレッスンでは、次の機能を使ったり確認したりしました。

- `/share` で GitHub gist を作成し、チームとセッションを共有する。
- `/context` で、Copilot CLI が現在使用しているコンテキストを確認する。
- `/model` で利用可能なモデルの一覧を確認し、必要に応じて別のモデルを選択する。
- `/delegate` が cloud agent への任意の橋渡しになることを学ぶ。

利用できる slash command はもちろんこれ以外にもあり、Copilot CLI にはまだ多くの機能があります。最後に、[ここまでに学んだことを振り返り][next-lesson]、学習を続けるための次のステップを確認して締めくくりましょう。

## リソース

- [Copilot CLI を使う][using-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI のコンテキスト管理][context-management]
- [Copilot CLI でセッションを共有する][share-sessions]
- [Copilot CLI でモデルを選択する][selecting-models]

[previous-lesson]: ../6-custom-agents/
[next-lesson]: ../8-review/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
[share-sessions]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#share-sessions
[selecting-models]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#select-an-llm

[cloud-harness-link]: ../../cloud/
