import subprocess

from lce_qt_launcher.models.app_data import AppData

DEFAULT_DATA_ZIP_URL = "archive/master.zip"

def verify_git_installation():
    print(subprocess.getoutput("git --version"))
    
def clone_repo(repo_url : str, path : str, appData : AppData):
    if verify_git_installation():
        subprocess.run(["git", "clone",  repo_url, path], cwd=appData.appDataDirs[0])
    else:
        pass
    
def update_repo(appData : AppData):
    subprocess.run(["git", "pull"], cwd=appData.appDataDirs[0])