import os
import sys
import requests
import subprocess
import shutil
import logging



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
        path_json = (os.path.join((os.getenv("LOCALAPPDATA")), (r"Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\settings.json")))
        subprocess.Popen(["start", path_json], shell=True)
        logger.info(f"path_json:{path_json}")


    def mainprocess(self):
        self.setup()
        # self.install_winget()
        if not (shutil.which("winget")):
            self.install_winget()
        else:
            print("winget is already installed.")
        self.setting_winget()
        print("Done.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    Main().mainprocess()
