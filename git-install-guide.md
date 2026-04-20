# Git のインストールと教材のダウンロード

本講義の演習教材は GitHub のリポジトリで配布します。教材を自分のパソコンにダウンロードするには、Git というツールが必要です。本ガイドでは、Git のインストールから教材のダウンロードまでの手順を説明します。

本講義では、教材のダウンロードは初回の1回のみ行います。教材の更新・修正は Moodle 経由で通知します（`git pull` などの追加操作は不要です）。

---

## 1. Git とは

Git は、ファイルの変更履歴を管理するためのツールです。GitHub はその Git を使って、インターネット上でファイルを共有できるサービスです。本講義では「GitHub に公開されている教材フォルダをまるごと自分のパソコンにコピーする」ためだけに Git を使います。

---

## 2. Git のインストール

### Windows をお使いの方

1. 公式サイト <https://git-scm.com/download/win> からインストーラーをダウンロードします
2. ダウンロードした `.exe` を実行します
3. インストーラーのオプションはすべて既定のまま「Next」で進めて構いません。特に以下の画面はそのまま進めてください
    - Adjusting your PATH environment → "Git from the command line and also from 3rd-party software"（既定）
    - Choosing the default editor → 任意のもの（こだわりがなければ既定のまま）
    - Line ending conversions → "Checkout Windows-style, commit Unix-style line endings"（既定）
4. インストール完了後、スタートメニューから「Git Bash」というアプリが起動できれば成功です

### macOS をお使いの方

ターミナル.app を起動して、以下を実行します。

```bash
xcode-select --install
```

ダイアログが出たら「インストール」を押してください。すでにインストール済みの場合は「already installed」と表示されますので、そのまま次に進んでください。

---

## 3. インストールの確認

Windows の方は「Git Bash」、macOS の方は「ターミナル.app」を起動して、以下を入力し Enter を押します。

```bash
git --version
```

`git version 2.x.x` のように表示されれば準備完了です。

---

## 4. 教材のダウンロード

### 手順

1. ターミナル（Git Bash または ターミナル.app）を開きます
2. 教材を置きたいフォルダへ移動します。迷う場合はホームフォルダの直下で構いません
3. 以下のコマンドを1つ実行します（科目ごとに URL が異なります）

| 科目 | コマンド |
|---|---|
| データ収集とクリーニング | `git clone https://github.com/hgphys/dcc.git` |
| ネットワーク科学と経済Ⅰ | `git clone https://github.com/hgphys/ns1.git` |
| 機械学習Ⅰ | `git clone https://github.com/hgphys/ml1.git` |

実行すると、現在のフォルダの直下に科目名のフォルダ（`dcc`, `ns1`, `ml1`）が作られ、教材一式がダウンロードされます。

### ダウンロードは初回のみ

教材の修正があった場合は Moodle で通知します。リポジトリを再度ダウンロードする操作は不要です。すでにダウンロード済みのフォルダをそのまま使ってください。

---

## 5. Anaconda Prompt で git を使いたい場合（Windows）

Anaconda Prompt を普段使っている方は、その中で git を使うこともできます。以下のいずれかの方法を選んでください。

### 方法A: 「2. Git のインストール」を完了している場合

Anaconda Prompt を開き直して `git --version` を実行してみてください。バージョンが表示されればそのまま使えます（インストール時に PATH が追加されているため）。

### 方法B: conda で git をインストールする

Anaconda Prompt で以下を実行します。

```bash
conda install git
```

その後 `git --version` が通れば成功です。なおこの方法では、その conda 環境内でのみ git が使えます。

本講義では、教材ダウンロードは Git Bash（Windows）または ターミナル.app（macOS）で行うことを前提に説明しています。Anaconda Prompt での利用は任意です。

---

## 6. よくあるトラブル

### `git: command not found` と表示される

Git がインストールされていないか、ターミナルが Git を見つけられていません。インストール後、ターミナルを一度閉じて開き直してください。

### SSL certificate problem / SSL 証明書のエラー

大学のネットワークなどプロキシが設定された環境で起こる場合があります。個人のネットワーク（自宅の Wi-Fi、モバイル回線）で再度試してください。

### Permission denied / 権限がありません

書き込み権限のないフォルダで `git clone` を実行している可能性があります。`Documents` や `Desktop` など、自分が書き込める場所に移動してから実行してください。

### ユーザー名が日本語のアカウントでエラーが出る

Windows でユーザー名に日本語が含まれていると、Anaconda や Git Bash でエラーが出る場合があります。半角英数字のユーザー名で新規アカウントを作るか、インストール先を `C:\tools` のような半角パスに変更してください（Anaconda のインストール時と同じ注意点です）。

### `fatal: destination path '...' already exists and is not an empty directory`

同じ名前のフォルダがすでに存在します。以前にダウンロード済みであればそのフォルダを使ってください。再ダウンロードしたい場合は、既存のフォルダを削除してから `git clone` を実行します。

---

## 7. まとめ

- Git をインストール（Windows は Git for Windows、macOS は `xcode-select --install`）
- ターミナルで `git --version` が通れば準備完了
- 教材ダウンロードは `git clone <リポジトリURL>` を1回だけ実行
- 教材の更新は Moodle で通知、再ダウンロードは不要

質問がある場合は Moodle または授業時にお知らせください。
