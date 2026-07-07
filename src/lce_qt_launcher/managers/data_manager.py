from lce_qt_launcher.models.app_data import AppData

import subprocess

DEFAULT_DATA_URL: str = "https://code.nolog.cz/xgui4/lce-qt-launcher-data"


def clone_data(appData: AppData, url: str = DEFAULT_DATA_URL):
    app_data_path: str = appData.appDataDirs[0]

    subprocess.run(["git", "clone", url, app_data_path])
