from lce_qt_launcher.models.app_data import AppData

import subprocess

DATA_STRING : str = "https://code.nolog.cz/xgui4/lce-qt-launcher-data"

def clone_data(appData : AppData, url : str = DATA_STRING):
    app_data_path : str = appData.appDataDirs[0]

    subprocess.run(["git", "clone",  url, app_data_path])