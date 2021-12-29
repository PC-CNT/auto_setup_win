import os
import sys
import requests
import subprocess
import shutil
import logging
# import json

#! VSCodeで実行するときはF5じゃないとsubprocess関連のコードがﾀﾋぬ

class Main:
    #* ここで定義する変数はクラス変数になると噂されている
    # current_dir = os.path.dirname(os.path.abspath(__file__))


    def __init__(self):
        #* ここで定義する変数はインスタンス変数になると噂されている
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.current_dir)
        logger.info(f"Current dir:{self.current_dir}")


    def setup(self):
        return


    def install_winget(self):
        url_winget = ("https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle")

        req_winget = requests.get(url_winget)

        #* カレントディレクトリにwinget.msixbundleを保存
        os.makedirs("winget", exist_ok=True)
        with open((os.path.join("winget/", "winget.msixbundle")), "wb") as f:
            for chunk in req_winget.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        #* Pythonから直接Powershellを叩けないのでcmd経由でpowershellコマンドを実行する
        powershell_command = ("Add-AppxPackage -Path " + (os.path.join(self.current_dir, "winget", "winget.msixbundle")))
        subprocess.run((f"powershell -Command {powershell_command}"), shell=True)


    def setting_winget(self):
        default_settings_json = (os.path.join((os.getenv("LOCALAPPDATA")), (r"Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\settings.json")))
        if os.path.exists(self.current_dir + "/winget/winget_settings.json"):
            shutil.copyfile(self.current_dir + "/winget/winget_settings.json", default_settings_json)
            logger.info("settings.jsonをコピーしました")
        # subprocess.Popen(["start", default_settings_json], shell=True)
        logger.info(f"default_settings_json:{default_settings_json}")


    def winget_install_software(self):
        """パッケージのIDが書かれたテキストをforで回してwinget installを実行する

        winget import でjsonから一括インストールすることもできるが、現バージョン（v1.1.12653）では同じ名前のパッケージが存在した場合に
        「複数のパッケージが入力条件に一致しました。入力内容を修正してください。」という警告が出てインストールされないので
        あらかじめIDをリストにしてから完全一致検索で指定してインストールする方法をとる
        """
        #? path_import_json = os.path.abspath(os.path.join("winget/", "winget_list.json"))
        #? logger.info(f"path_import_json:{path_import_json}")
        #? subprocess.run(f"winget import {path_import_json}", shell=True)
        path_install_list = os.path.abspath(os.path.join("winget/", "winget_install_list.txt"))
        logger.info(f"path_install_list:{path_install_list}")
        with open(path_install_list, "r") as f:
            for id in f:
                subprocess.run(f"winget install --accept-package-agreements --accept-source-agreements -h -e --id  {id.strip()}", shell=True)

    def mainprocess(self):
        self.setup()
        # self.install_winget()
        if not (shutil.which("winget")):
            self.install_winget()
        else:
            print("winget is already installed.")
        self.setting_winget()
        self.winget_install_software()

        print("Done.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    Main().mainprocess()
