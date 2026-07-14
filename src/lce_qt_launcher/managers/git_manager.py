import subprocess
# from zipfile import ZipFile

from lce_qt_launcher.models.app_data import AppData

DEFAULT_DATA_ZIP_URL = "archive/master.zip"


def verify_git_installation(cmd: str) -> bool:
    """_summary_ #TODO DO the docstring

    Args:
        cmd (str): _description_

    Returns:
        bool: _description_
    """
    try:
        subprocess.run(cmd)
        return True
    except RuntimeError:
        return False


def clone_repo(repo_url: str, path: str, appData: AppData) -> None:
    """_summary_ #TODO DO the docstring

    Args:
        repo_url (str): _description_
        path (str): _description_
        appData (AppData): _description_
    """
    # if verify_git_installation("git --version"):
        # subprocess.run(["git", "clone", repo_url, path], cwd=appData.appDataDirs[0])
    subprocess.run(["git", "clone", repo_url, path], cwd=appData.appDataDirs[0])
    # else:
    #     repo_url = repo_url.replace(".git", DEFAULT_DATA_ZIP_URL)
    #     subprocess.run(f"curl {repo_url} -o repository.zip", cwd=appData.appDataDirs[0])
        

def update_repo(appData: AppData) -> None:
    """_summary_ #TODO DO the docstring

    Args:
        appData (AppData): _description_
    """
    subprocess.run(["git", "pull"], cwd=appData.appDataDirs[0])
