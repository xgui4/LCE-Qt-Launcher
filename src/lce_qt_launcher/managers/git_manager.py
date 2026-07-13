import subprocess

from lce_qt_launcher.models.app_data import AppData

def verify_git_installation():
    print(subprocess.getoutput("git --version"))
    
def clone_repo(repo_url : str, path : str, appData : AppData):
    subprocess.run(["git", "clone",  repo_url, path], cwd=appData.appDataDirs[0])
    
def update_repo(appData : AppData):
    subprocess.run(["git", "pull"], cwd=appData.appDataDirs[0])

verify_git_installation()