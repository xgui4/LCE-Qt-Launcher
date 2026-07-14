from lce_qt_launcher.models.app_data import AppData

from pathlib import Path

import os


def import_inst_file_to_app_data(
    instance_file_path: str, appData: AppData, filename: str = ""
):
    """_summary_ #TODO DO the docstring

    Args:
        instance_file_path (str): _description_
        appData (AppData): _description_
        filename (str, optional): _description_. Defaults to "".
    """
    if filename == "":
        filename_Path = Path(f"{instance_file_path}")
        filename = filename_Path.name
    destinations = os.path.join(appData.appDataDirs[0], "instances", filename)
    os.symlink(instance_file_path, destinations)
