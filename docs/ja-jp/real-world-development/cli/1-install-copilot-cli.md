---
title: "演習 1 - GitHub Copilot CLI をインストールする"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[GitHub Copilot CLI][about-copilot-cli] は、ターミナルで動作する強力なエージェント型コーディング アシスタントです。コードベースの探索、コード生成、コマンド実行、外部ツールとの連携をすべてコマンド ラインから行えます。タスクを任せたり、変更を依頼したりしながら、集中を保って作業できます。最初のステップは、想像どおりツールをインストールすることです。幸い、すでによく知っているツールを使って実行できます。

この演習では、次のことを学びます。

- npm を使って GitHub Copilot CLI をインストールする。
- GitHub アカウントで認証する。
- インストールを確認する。

## シナリオ

チームでは、増え続けるバックログに対応するために AI agent を使い始めています。Copilot CLI はその機能をターミナルに持ち込みます。ターミナルは、多くの開発者が日常的に作業する場所です。この演習では、インストールと認証を済ませ、ワークショップの残りで使える状態にします。

## Codespace でターミナルを開く

Copilot CLI をインストールする前に、codespace でターミナル ウィンドウを開く必要があります。

1. まだ開いていない場合は、codespace に戻ります。
2. <kbd>Ctrl</kbd>+<kbd>\`</kbd> を押してターミナル ウィンドウを開きます。
3. VS Code ウィンドウの下部にターミナル パネルが表示されます。

## Copilot CLI をインストールする

Copilot CLI は [npm][install-npm]、[WinGet][install-winget]、[Homebrew][install-homebrew] でインストールできます。GitHub Codespaces には Node.js があらかじめインストールされているため、この演習では npm を使って Copilot CLI をインストールします。

1. ターミナルで、Node.js がインストールされており、バージョン要件を満たしていることを確認します。

   ```bash
   node --version
   ```

   バージョン 22 以上（例: `v22.x.x`）が表示されるはずです。

2. npm を使って codespace に Copilot CLI をグローバル インストールします。

   ```bash
   npm install -g @github/copilot
   ```

3. バージョンを確認してインストールを検証します。

   ```bash
   copilot --version
   ```

   バージョン番号（例: `v1.0.XX`）が表示されるはずです。

> [!TIP]
> 権限エラーが発生した場合は、一部のシステムで `sudo npm install -g @github/copilot` の使用が必要になることがあります。ただし、GitHub Codespaces では通常必要ありません。

## GitHub で認証する

初回起動時に、Copilot CLI は GitHub アカウントでの認証を求めます。

1. Copilot CLI を起動します。

   ```bash
   copilot
   ```

2. 現在ログインしていない場合は、認証を求めるプロンプトが表示されます。Copilot CLI は device code を表示し、URL にアクセスするよう案内します。
3. 画面の指示に従います。
   - 提示された URL をブラウザーで開く
   - 求められたら device code を入力する
   - Copilot CLI が GitHub アカウントにアクセスできるよう承認する
4. 認証が完了すると、質問やコマンドを受け付ける Copilot CLI のプロンプトが表示されます。

> [!NOTE]
> Codespace では、GitHub のセッションを通じてすでに認証されている場合があります。Copilot CLI が認証を求めずに起動した場合は、そのまま進めて問題ありません。

## ディレクトリを信頼し、正しく動作していることを確認する

初めて Copilot CLI のプロンプトが表示されたので、このワークショップのリポジトリを信頼済みにし、Copilot CLI が正しくインストールされ、接続されていることを確認しましょう。

1. Copilot CLI からこのフォルダー内のファイルを信頼するか確認されたら、次の 3 つの選択肢が表示されます。
   - **Yes, proceed**: このセッションのみ信頼する
   - **Yes, and remember this folder for future sessions**: 永続的に信頼する
   - **No, exit (Esc)**: ファイルへのアクセスを許可しない
2. このワークショップでは、このリポジトリで継続して作業するため、**Yes, and remember this folder for future sessions** を選択します。
3. Copilot に簡単な質問をして、正しく動作していることを確認します。

   ```
   What files are in this project?
   ```

4. Copilot がリポジトリを探索し、プロジェクト構造の概要を返すはずです。
5. `/help` コマンドを試して、利用可能な slash command を確認します。

   ```
   /help
   ```

6. ターミナルで次のコマンドを入力して Copilot CLI を終了します。後続の演習で再び Copilot CLI に戻ります。

   ```
   exit
   ```

## まとめと次のステップ

おめでとうございます。GitHub Copilot CLI のインストールと認証が完了しました。次のことを学びました。

- npm を使って Copilot CLI をインストールする。
- GitHub アカウントで認証する。
- Copilot CLI が作業できるようにディレクトリを信頼する。
- インストールが正しく動作していることを確認する。

Copilot CLI をインストールできたので、次は Copilot にプロジェクトのコンテキストを与えます。[演習 2 - Copilot CLI のカスタム命令][next-lesson] に進んでください。

## リソース

- [GitHub Copilot CLI のインストール][install-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI を使う][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-custom-instructions/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
