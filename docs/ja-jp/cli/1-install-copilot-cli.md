---
title: "演習 1 - GitHub Copilot CLI をインストールする"
authors:
  - geektrainer
lastUpdated: 2026-09-11
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

1. Codespace に戻り、セットアップの完了を待ちます。
2. <kbd>Ctrl</kbd>+<kbd>\`</kbd> を押してターミナル ウィンドウを開きます。
3. VS Code ウィンドウの下部にターミナル パネルが表示されます。

## 学習用環境を確認する

Codespace のターミナルで、ワークショップ教材のリポジトリではなく、自分の Tailspin Toys リポジトリにいることを確認します。`README.md` と `package.json` を読み、セットアップとチェックのコマンドを確認してください。現在の Tailspin Toys には Node.js 22.13 以降、プロジェクトの依存関係、E2E テスト用の Playwright Chromium が必要です。

```bash
pwd
git remote -v
node --version
gh auth status
```

GitHub CLI（`gh`）は PR と CI の確認に役立ちます。認証されていない場合は、`gh auth login` を実行してブラウザーの案内に従います。このリポジトリでブランチをプッシュし、PR を作成・マージできるアカウントであることを確認してください。組織のポリシーによっては、別のレビュアーが必要です。コードの変更を始める前に、リポジトリのセットアップ手順に従って不足している前提条件を解消し、インストール内容を確認してから承認します。

CLI は起動したチェックアウトで動作します。会話を始めても、独立したワークツリーが自動的に作成されるわけではありません。このワークショップでは PR マイルストーンごとに1つのブランチを使います。先に星評価と指示の実証をマージし、演習4～8では同じフィルター機能のブランチを維持します。

## Copilot CLI をインストールする

Copilot CLI は [npm][install-npm]、[WinGet][install-winget]、[Homebrew][install-homebrew] でインストールできます。GitHub Codespaces には Node.js があらかじめインストールされているため、この演習では npm を使って Copilot CLI をインストールします。

1. ターミナルで、Node.js がインストールされており、バージョン要件を満たしていることを確認します。

   ```bash
   node --version
   ```

   CLI 自体の要件が異なる場合でも、Tailspin Toys にはバージョン 22.13 以上が必要です。バージョンが古い場合は、学習用リポジトリのセットアップ手順に従ってください。

2. npm を使って codespace に Copilot CLI をグローバル インストールします。

   ```bash
   npm install -g @github/copilot
   ```

3. バージョンを確認してインストールを検証します。

   ```bash
   copilot --version
   ```

   バージョン番号（例: `v1.0.XX`）が表示されるはずです。

> [!NOTE]
> 権限エラーでインストールに失敗した場合は、不慣れなコマンドを管理者権限で再実行せず、npm の設定を確認するか、ワークショップの講師に相談してください。

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

   ```plaintext
   このプロジェクトにはどのようなファイルがありますか。
   ```

4. Copilot がリポジトリを探索し、プロジェクト構造の概要を返すはずです。
5. `/help` コマンドを試して、利用可能な slash command を確認します。

   ```text
   /help
   ```

6. Copilot のプロンプトで次のコマンドを入力して、このセッションを終了します。最初の変更には新しいセッションを使います。

   ```text
   /exit
   ```

## モードと権限を理解する

Copilot CLI は起動したディレクトリと Git ブランチで作業します。ディレクトリを信頼するとリポジトリのコンテキストを利用できるようになりますが、すべてのツール操作の承認とは異なります。ファイル変更、シェルコマンド、GitHub 操作の権限要求を確認してください。

コードの演習は、学習用リポジトリのルートから次のコマンドで開始します。

```bash
copilot --enable-all-github-mcp-tools
```

GitHub MCP サーバーは組み込まれています。このフラグで Issue や PR の作業に使うすべてのツールを公開しますが、認証、リポジトリの権限、ツールの承認は引き続き必要です。このフラグだけでコミットや PR を承認するわけではありません。

<kbd>Shift</kbd>+<kbd>Tab</kbd> で通常の **Interactive**、**Plan**、**Autopilot** モードを切り替えます。リクエストを送る前にモード表示を確認してください。最初の変更では Interactive を維持し、フィルター機能は計画してから構築します。カスタマイズの作成とレビューの前には、明示的に Interactive に戻します。

> [!CAUTION]
> モードと権限の設定は別です。Autopilot は自律的に作業を続け、`--allow-all` とその別名 `--yolo` はすべてのツール、パス、URL の権限を付与します。このワークショップでは、毎回のセッションを無制限の権限で始める必要はありません。Codespace 内でも、アクセスを許可する前に範囲を確認してください。

## まとめと次のステップ

おめでとうございます。GitHub Copilot CLI のインストールと認証が完了しました。次のことを学びました。

- npm を使って Copilot CLI をインストールする。
- GitHub アカウントで認証する。
- Copilot CLI が作業できるようにディレクトリを信頼する。
- インストールが正しく動作していることを確認する。

Copilot CLI をインストールできたので、[演習 2 - 星評価を追加して小さな成果を得る][next-lesson]で、レビューしやすい小さな変更を行います。

## リソース

- [GitHub Copilot CLI のインストール][install-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI を使う][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
