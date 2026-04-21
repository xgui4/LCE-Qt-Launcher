from lce_qt_launcher.managers.downloader import Downloader
from lce_qt_launcher.build_info import BuildInfo

import lce_qt_launcher.views.term_service as term_service

from PySide6.QtNetwork import (
    QNetworkReply
)

from enum import Enum
from subprocess import TimeoutExpired

import subprocess
import json
import os

class InstanceSource(Enum):
    GITHUB_RELEASE = 0
    FORGEJO_RELEASE = 1
    REMOTE_GIT_SOURCE = 2
    LOCAL_INSTALLATION = 3
    LOCAL_SOURCE_CODE = 4

def from_int_to_InstanceSource(value : int)-> InstanceSource:
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
        case _: raise RuntimeError(f"{value} is an Incorrect InstanceSource Type")

def from_str_to_InstanceSource(string : str)-> InstanceSource:
    match string:
        case "InstanceSource.GITHUB_RELEASE":
            return InstanceSource.GITHUB_RELEASE
        case "InstanceSource.FORGEJO_RELEASE":
            return InstanceSource.FORGEJO_RELEASE
        case "InstanceSource.REMOTE_GIT_SOURCE ":
            return InstanceSource.REMOTE_GIT_SOURCE 
        case "InstanceSource.LOCAL_INSTALLATION":
            return InstanceSource.LOCAL_INSTALLATION
        case "InstanceSource.LOCAL_SOURCE_CODE":
            return InstanceSource.LOCAL_SOURCE_CODE
        case _: raise RuntimeError(f"{string} is an Incorrect InstanceSource Type")

class InstanceType(Enum):
    CLIENT_VANILLA = 0
    CLENT_MODDED = 1
    SERVER_VANILLA = 2
    SERVER_MODDED = 3

def from_int_to_InstanceType(value : int)-> InstanceType:
    match value:
        case 0:
            return InstanceType.CLIENT_VANILLA
        case 1:
            return InstanceType.CLENT_MODDED
        case 2:
            return InstanceType.SERVER_VANILLA
        case 3:
            return InstanceType.SERVER_MODDED
        case _: raise RuntimeError(f"{value} is an Incorrect InstanceType Type")

def from_str_to_InstanceType(string : str)-> InstanceType:
    match string:
        case "InstanceType.CLIENT_VANILLA":
            return InstanceType.CLIENT_VANILLA
        case "InstanceType.CLENT_MODDED":
            return InstanceType.CLENT_MODDED
        case "InstanceType.SERVER_VANILLA":
            return InstanceType.SERVER_VANILLA
        case "InstanceType.SERVER_MODDED":
            return InstanceType.SERVER_MODDED
        case _: raise RuntimeError(f"{string} is an Incorrect Instance Type")

_DEFAULT_INST_NAME = "Default"
_DEFAULT_INSTALLATION_PATH = "MinecraftLCEClient"
_DEFAULT_USERNAME = "Steve"
_DEFAULT_EXE_NAME = "Minecraft.Client.exe"
_DEFAULT_ARCHIVE_FILE = "LCEWindows64.zip"
_DEFAULT_REPO_URL = "https://github.com/MCLCE/MinecraftConsoles"
_DEFAULT_INST_SOURCE = InstanceSource.GITHUB_RELEASE
_DEFAULT_INST_TYPE = InstanceType.CLIENT_VANILLA
_DEFAULT_INST_SOURCE_STRING = "InstanceSource.GITHUB_RELEASE"
_DEFAULT_INST_TYPE_STRING = "InstanceType.CLIENT_VANILLA"
_DEFAULT_IMAGE = ":/assets/minecraft.png"
_DEFAULT_NEWS_FEED  = "https://github.com/MCLCE/minecraftconsoles/commits"
_DEFAULT_VERSION = "nightly"
_DEFAULT_SKIN_PATH = ""
_DEFAULT_SERVERS: list[str] = []

class Instance:
    def __init__(self, 
                 name : str = _DEFAULT_INST_NAME, 
                 installation_path : str = _DEFAULT_INSTALLATION_PATH, 
                 username : str = _DEFAULT_USERNAME,
                 exe_name : str = _DEFAULT_EXE_NAME,
                 archive_file : str = _DEFAULT_ARCHIVE_FILE,
                 repo_url : str = _DEFAULT_REPO_URL, 
                 image : str = _DEFAULT_IMAGE,
                 instance_source : InstanceSource = _DEFAULT_INST_SOURCE,
                 instance_type : InstanceType = _DEFAULT_INST_TYPE, 
                 news_feed : str = _DEFAULT_NEWS_FEED,
                 version : str = _DEFAULT_VERSION,
                 skin_path : str = _DEFAULT_SKIN_PATH,
                 servers : list[str] = _DEFAULT_SERVERS
                ) -> None:
        self.name: str = name
        self.installation_path: str = installation_path
        self.username: str = username
        self.archive_file: str = archive_file
        self.exe_name: str = exe_name
        self.repo_url: str = repo_url
        self.instance_source: InstanceSource = instance_source
        self.instance_type : InstanceType = instance_type
        self.image : str = image
        self.news_feed : str = news_feed
        self.version: str = version
        self.skin_path: str = skin_path
        self.servers: list[str] = servers

    def load_inst_from_dict(self, inst_dict: dict[str, str]) -> None:
        self.name = inst_dict.get("name", _DEFAULT_INST_NAME)
        self.installation_path = inst_dict.get("installation_path",_DEFAULT_INSTALLATION_PATH)
        self.username = inst_dict.get("username", _DEFAULT_USERNAME)
        self.exe_name = inst_dict.get("exe_name", _DEFAULT_EXE_NAME)
        self.archive_file = inst_dict.get("archive_file", _DEFAULT_ARCHIVE_FILE)
        self.repo_url = inst_dict.get("repo_url", _DEFAULT_REPO_URL)
        self.instance_source = from_str_to_InstanceSource(inst_dict.get("instances_source", _DEFAULT_INST_SOURCE_STRING))
        self.instance_type = from_str_to_InstanceType(inst_dict.get("instance_type", _DEFAULT_INST_TYPE_STRING))
        self.image = inst_dict.get("image", _DEFAULT_IMAGE)
        self.news_feed = inst_dict.get("news_feed", _DEFAULT_NEWS_FEED)
        self.version = inst_dict.get("version", _DEFAULT_VERSION)
        # self.skin_path = inst_dict.get("skin_path", _DEFAULT_SKIN_PATH)
        # self.servers = inst_dict.get("servers", _DEFAULT_SERVERS)

    def get_download_url(self) -> str:
        download_release_url = "/releases/download/"
        if self.instance_source == InstanceSource.GITHUB_RELEASE or self.instance_source == InstanceSource.FORGEJO_RELEASE:
            return self.repo_url + \
                    download_release_url + \
                    self.version + "/" + \
                    self.archive_file
        if self.instance_source == InstanceSource.REMOTE_GIT_SOURCE:
            return f"{self.repo_url}.git"
        if self.instance_source == InstanceSource.LOCAL_INSTALLATION:
            raise RuntimeError("Error ! Local Installation does not have a download URL")
        else:
            raise RuntimeError("Not implemented yet!")        

class InstanceManager:
    def __init__(self, instance : Instance, build_info : BuildInfo):
        self.instance: Instance = instance
        self._downloader: Downloader = Downloader(build_info)
        self._build_info: BuildInfo = build_info
    def play(self) -> str:
        try:
            game_process = subprocess.run(os.path.join(self.instance.installation_path, self.instance.exe_name))
        except TimeoutExpired as err: 
            term_service.print_error(f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}")
            return f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}"
        except PermissionError as err:
            term_service.print_error(f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}")
            return f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}"
        else:
            return f"Client closed with code {game_process.returncode}"  
    def install_instance(self) -> QNetworkReply:
        try:
            if self.instance.instance_source in [InstanceSource.GITHUB_RELEASE, InstanceSource.FORGEJO_RELEASE]:
                return self._downloader.download_inst_async(self.instance)
            else:
                raise RuntimeWarning("Not implemented YET") #TODO : implementing other type
        except RuntimeError as e:
            raise e

    def save_instance(self, save_file : str) -> None: 
        json_string : str = ""
        try:
            json_string = json.dumps(vars(self.instance), indent=4,)
        except:
            json_string = json.dumps(obj=vars(self.instance), indent=4, default=str)
        if not save_file.endswith(self._build_info.instance_extension):
            save_file: str = save_file + self._build_info.instance_extension
        with open(file=save_file, mode='w') as f:
            _ = f.write(json_string)
    
    def load_instance(self, save_file : str) -> None:
        with open(file=save_file, mode='r') as json_file:
            json_data = json.load(json_file)   
            #if json_data == dict[str, str]:
            inst_dict : dict[str, str] = json_data  
            #else:
            #    raise RuntimeError("Invalid Dictionary")
            self.instance.load_inst_from_dict(inst_dict)
