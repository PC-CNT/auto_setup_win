# About

Windowsクリーンインストール後の環境構築を自動化したい

## Description

[winget]: https://github.com/microsoft/winget-cli

このスクリプト単体で

- [winget][winget]のインストール
- 一括で[winget][winget]のパッケージをインストール

を行います

## Usage

最初に

- winget_install_list.txt（必須）
- winget_settings.json（任意）

の2つを用意します

winget_install_list.txtにはインストールしたいパッケージのIDを一行ずつ記入します（[examples](./examples/winget/winget_install_list.txt)を参照）

```cmd
.
├── Setup.exe
└── winget
    ├── winget_install_list.txt
    └── winget_settings.json
```

Setup.exeと同じ階層にwingetフォルダーを作成し、
その中にwinget_install_list.txtとwinget_settings.jsonを配置してください。

Setup.exeを管理者権限で実行したら、自動でインストールが開始されます

winget_install_list.txtが存在しない場合は、ファイル選択のダイアログが表示されます

## Build

[Pyinstaller](https://github.com/pyinstaller/pyinstaller)でexe化してます

```cmd
pyinstaller --onefile --uac-admin Setup.py
```

Other

このスクリプトではコマンドを叩く動作を自動で行っているだけなので、パッケージ管理ツール自体やパッケージの中身とは一切関係ありません

## Licence

[MIT Licence](https://opensource.org/licenses/MIT)
