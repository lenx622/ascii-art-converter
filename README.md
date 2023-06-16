# ascii-art-converter

このシステムはPNGやJPGなどの画像ファイルをアスキーアートに変換してtextファイルとして保存するシステムです。

## Requirements

* Docker v20.10.21
* Docker Compose v2.13.0
* GNU Make v3.81

## Installation

1. DockerおよびDocker Composeをインストールします。公式ドキュメンテーションを参照してください。
2. このリポジトリをクローンまたはダウンロードします。
3. リポジトリのルートディレクトリで以下のコマンドを実行し、Dockerイメージをビルドします：
```bash
make build
```

## Usage

変換を実行するには、generateコマンドの後に変換したい画像のファイル名を指定します。

例えば、example.pngを変換するには次のコマンドを使用します：
```bash
make generate FILENAME="example.png"
```

変換後のtxtファイルは`downloads/`に保存されます。

※ 変換する画像ファイルは`images/`ディレクトリ内に配置してください。

