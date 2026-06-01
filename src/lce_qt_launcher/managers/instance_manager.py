# FIXME : Make Instance mode indpendant
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lce_qt_launcher.app_context import AppContext

from lce_qt_launcher import instance_extension_str
import lce_qt_launcher.views.term_service as term_service

from PySide6.QtNetwork import QNetworkReply
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox

from enum import Enum
from subprocess import TimeoutExpired

import subprocess
import json
import os

SCHEME_VERSION = "https://raw.githubusercontent.com/xgui4/LCE-Qt-Launcher/refs/heads/dev/schemas/x-application-lce_inst_config.json"


class InstanceSource(Enum):
    """_summary_ The 4 Type of Instances (2 functional, the othes coming soon)"""

    GITHUB_RELEASE = 0
    FORGEJO_RELEASE = 1
    REMOTE_GIT_SOURCE = 2
    LOCAL_INSTALLATION = 3
    LOCAL_SOURCE_CODE = 4


def from_int_to_InstanceSource(value: int) -> InstanceSource:
    """_summary_ Convert Into to Instance Source

    Args:
        value (int): _description_ the int to convert

    Raises:
        RuntimeError: _description_ Raise if a incorrect int is specified

    Returns:
        InstanceSource: _description_ The InstanceSource from the int
    """
    match value:
        case 0:
            return InstanceSource.GITHUB_RELEASE
        case 1:
            return InstanceSource.FORGEJO_RELEASE
        case 2:
            return InstanceSource.REMOTE_GIT_SOURCE
        case 3:
            return InstanceSource.LOCAL_INSTALLATION
        case 4:
            return InstanceSource.LOCAL_SOURCE_CODE
        case _:
            raise RuntimeError(f"{value} is an Incorrect InstanceSource Type")


def from_str_to_InstanceSource(string: str) -> InstanceSource:
    """_summary_ Convert str to Instance Source

    Args:
        string (str): _description_ the string to convert

    Raises:
        RuntimeError: _description_ Raise if a incorrect str is specified

    Returns:
        InstanceSource: _description_ The InstanceSource from the str
    """
    match string:
        case "InstanceSource.GITHUB_RELEASE" | "0":
            return InstanceSource.GITHUB_RELEASE
        case "InstanceSource.FORGEJO_RELEASE" | "1":
            return InstanceSource.FORGEJO_RELEASE
        case "InstanceSource.REMOTE_GIT_SOURCE" | "2":
            return InstanceSource.REMOTE_GIT_SOURCE
        case "InstanceSource.LOCAL_INSTALLATION" | "3":
            return InstanceSource.LOCAL_INSTALLATION
        case "InstanceSource.LOCAL_SOURCE_CODE" | "4":
            return InstanceSource.LOCAL_SOURCE_CODE
        case _:
            raise RuntimeError(f"{string} is an Incorrect InstanceSource Type")

_DEFAULT_INST_NAME = "New Default (pieeebot neoLegacy)"
_DEFAULT_INSTALLATION_PATH = "{appInstancePath}/.new-default"
_DEFAULT_USERNAME = "Steve"
_DEFAULT_ARCHIVE_FILE = "neoLegacyWindows64.zip"
_DEFAULT_EXE_NAME = "neoLegacyWindows64/Minecraft.Client.exe"
_DEFAULT_REPO_URL = "https://github.com/neoStudiosLCE/neoLegacy"
_DEFAULT_INST_SOURCE = InstanceSource.GITHUB_RELEASE
_DEFAULT_INST_SOURCE_STRING = "InstanceSource.GITHUB_RELEASE"
_DEFAULT_IMAGE = ":/assets/neoLegacy.png"
_DEFAULT_NEWS_FEED = "https://github.com/neoStudiosLCE/neoLegacy/commits/main/"
_DEFAULT_VERSION = "v1.0.4b"


class Instance(QObject):
    """_summary_ An config and inform an instance of Minecraft LCE Installed or to install"""

    def __init__(
        self,
        name: str = _DEFAULT_INST_NAME,
        installation_path: str = _DEFAULT_INSTALLATION_PATH,
        username: str = _DEFAULT_USERNAME,
        exe_name: str = _DEFAULT_EXE_NAME,
        archive_file: str = _DEFAULT_ARCHIVE_FILE,
        repo_url: str = _DEFAULT_REPO_URL,
        image: str = _DEFAULT_IMAGE,
        instance_source: InstanceSource = _DEFAULT_INST_SOURCE,
        news_feed: str = _DEFAULT_NEWS_FEED,
        version: str = _DEFAULT_VERSION,
        steam_link: str = "N/A",
    ) -> None:
        super().__init__(parent=None, objectName="Instance")
        self.name: str = name
        self.installation_path: str = installation_path
        self.username: str = username
        self.archive_file: str = archive_file
        self.exe_name: str = exe_name
        self.repo_url: str = repo_url
        self.instance_source: InstanceSource = instance_source
        self.image: str = image
        self.news_feed: str = news_feed
        self.version: str = version
        self.steam_link: str = steam_link

    def load_inst_from_dict(self, inst_dict: dict[str, str]) -> None:
        """_summary_ Load A JSON to a empty Instance Object to import it

        Args:
            inst_dict (dict[str, str]): _description_
        """
        self.name = inst_dict.get("name", _DEFAULT_INST_NAME)
        self.installation_path = inst_dict.get(
            "installation_path", _DEFAULT_INSTALLATION_PATH
        )
        self.username = inst_dict.get("username", _DEFAULT_USERNAME)
        self.exe_name = inst_dict.get("exe_name", _DEFAULT_EXE_NAME)
        self.archive_file = inst_dict.get("archive_file", _DEFAULT_ARCHIVE_FILE)
        self.repo_url = inst_dict.get("repo_url", _DEFAULT_REPO_URL)
        self.instance_source = from_str_to_InstanceSource(
            inst_dict.get("instances_source", _DEFAULT_INST_SOURCE_STRING)
        )
        self.image = inst_dict.get("image", _DEFAULT_IMAGE)
        self.news_feed = inst_dict.get("news_feed", _DEFAULT_NEWS_FEED)
        self.version = inst_dict.get("version", _DEFAULT_VERSION)
        self.steam_link = inst_dict.get("steam_link", "N/A")

    def get_download_url(self) -> str:
        """_summary_ Get the download URL of a Instance

        Raises:
            RuntimeError: _description_ Error ! Local Installation does not have a download URL when trying to obtain a URL from a local installation
            RuntimeError: _description_ Not implemented yet! if the state is not implemented yey.

        Returns:
            str: _description_
        """
        download_release_url = "/releases/download/"
        if (
            self.instance_source == InstanceSource.GITHUB_RELEASE
            or self.instance_source == InstanceSource.FORGEJO_RELEASE
        ):
            return (
                self.repo_url
                + download_release_url
                + self.version
                + "/"
                + self.archive_file
            )
        if self.instance_source == InstanceSource.REMOTE_GIT_SOURCE:
            return f"{self.repo_url}.git"
        if self.instance_source == InstanceSource.LOCAL_INSTALLATION:
            raise RuntimeError(
                "Error ! Local Installation does not have a download URL"
            )
        else:
            raise RuntimeError("Not implemented yet!")

    def to_dict(self) -> dict[str, str]:
        dict_to_return: dict[str, str] = {
            "$schema": SCHEME_VERSION,
            "name": self.name,
            "installation_path": self.installation_path,
            "username": self.username,
            "exe_name": self.exe_name,
            "archive_file": self.archive_file,
            "repo_url": self.repo_url,
            "instance_source": self.instance_source.name,
            "image": self.image,
            "news_feed": self.news_feed,
            "version": self.version,
            "steam_link": self.version
        }
        return dict_to_return

    def display(self) -> None:
        print(f"Name : {self.name}")
        print("=============================")
        print(f"installation path : {self.installation_path}")
        print(f"username : {self.username}")
        print(f"executable name : {self.exe_name}")
        print(f"archive file : {self.archive_file}")
        print(f"repo url : {self.repo_url}")
        print(f"image : {self.image}")
        print(f"instance source : {self.instance_source.value}")
        print(f"news_feed : {self.news_feed}")
        print(f"version : {self.version}")
        print(f"steam link : {self.steam_link}")


class InstanceManager:
    """_summary_ The Manager for Instances objects"""

    def __init__(self, instance: Instance, appContext: AppContext):
        self.instance: Instance = instance
        from lce_qt_launcher.managers.downloader import Downloader
        self._downloader: Downloader = Downloader(appContext)

    def play(self) -> str:
        """_summary_ Launch an Instance

        Returns:
            str: _description_ error message or status and exit codes
        """
        return_code: int = 0
        try:
            client_path: str = os.path.join(self.instance.installation_path, self.instance.exe_name)
            try:
                game_process_temp = subprocess.run(
                    [client_path, "-name", self.instance.username]
                )
                return_code = game_process_temp.returncode
            except OSError as e:
                if os.name == "posix":
                    game_process_temp = subprocess.run(
                        ["wine", client_path, "-name", self.instance.username]
                    )
                    return_code = game_process_temp.returncode
                else:
                    QMessageBox.critical(None, "Instance Error", str(e.args))
        except TimeoutExpired as err:
            term_service.print_error(
                f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}"
            )
            return f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}"
        except PermissionError as err:
            term_service.print_error(
                f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}"
            )
            return f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}"
        else:
            return f"Client closed with code {return_code}"

    def install_instance(self) -> QNetworkReply | str:
        """_summary_ Install the selected Instance
        Returns:
            QNetworkReply: _description_ : the QtNetwork Reply Object of the download process
        """
        # FIXME do others types
        if self.instance.instance_source in [
            InstanceSource.GITHUB_RELEASE,
            InstanceSource.FORGEJO_RELEASE,
        ]:
            return self._downloader.download_inst_async(self.instance)
        return "Not implemented yet"

    def save_instance(self, save_file: str) -> None:
        """_summary_ Save the install with a specified save file and location

        Args:
            save_file (str): _description_ specified save file and location
        """
        full_save_file = save_file
        json_string: str = ""
        try:
            json_string = json.dumps(
                vars(self.instance),
                indent=4,
            )
        except:
            # FIXME do not use a bare except : https://docs.astral.sh/ruff/rules/bare-except/
            json_string = json.dumps(obj=vars(self.instance), indent=4, default=str)
        if not save_file.endswith(instance_extension_str):
            full_save_file: str = save_file + instance_extension_str
        with open(file=full_save_file, mode="w") as f:
            _ = f.write(json_string)

    def load_instance(self, save_file: str) -> None:
        """_summary_ Load an instance with a specified save file and location
        Args:
            save_file (str): _description_ specified save file and location
        """
        with open(file=save_file, mode="r") as json_file:
            json_data = json.load(json_file)
            inst_dict: dict[str, str] = json_data
            self.instance.load_inst_from_dict(inst_dict)

    def is_installable(self) -> bool:
        """_summary_  assert if instance is installable"""
        # Note : Right now the remote git location is not installable via this launcher, it will added in the next version
        if self.instance.instance_source in [
            InstanceSource.FORGEJO_RELEASE,
            InstanceSource.GITHUB_RELEASE,
        ]:
            return True
        else:
            return False

    def expanded_path(self, appContext : AppContext) -> str:
        return self.instance.installation_path.replace("{appInstancePath}", appContext.instancePath)