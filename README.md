# About

Windowsクリーンインストール後の環境構築を自動化したい

## Description

[winget]: https://github.com/microsoft/winget-cli

このスクリプト単体で

- [winget][winget]のインストール
- 一括で[winget][winget]のパッケージをインストール

を行います

## Usage

### winget

wingetでは

- winget_list.json（インストールするパッケージが書いてある。**必須**）
- winget_settings.json（wingetの設定ファイル。**任意**）

の2つを使用します

クリーンインストールする前に

```cmd
winget export -o winget_list.json
```

上記のコマンドを実行してwinget_list.jsonを作成しておきます

winget_settings.jsonは必須でありませんが、必要であれば[公式のドキュメント](https://github.com/microsoft/winget-cli/blob/master/doc/Settings.md)を参考にして記入してください

```cmd
.
├── Setup.exe
└── winget
    ├── winget_list.json
    └── winget_settings.json
```

Setup.exeと同じ階層にwingetフォルダーを作成し、
その中にwinget_list.jsonとwinget_settings.jsonを配置してください。

Setup.exeを管理者権限で実行したら、自動でインストールが開始されます

- winget_list.jsonが存在しない場合はファイル選択のダイアログが表示されます
- winget_settings.jsonが存在しない場合はデフォルトの設定が適用されます

## Build

[Pyinstaller](https://github.com/pyinstaller/pyinstaller)でexe化してます

```cmd
pyinstaller --onefile --uac-admin Setup.py
```

## Other

このスクリプトではコマンドを叩く動作を自動で行っているだけなので、パッケージ管理ツール自体やパッケージの中身とは一切関係ありません

## Licence

[MIT Licence](https://opensource.org/licenses/MIT)
