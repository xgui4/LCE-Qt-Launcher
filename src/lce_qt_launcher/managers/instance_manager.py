from lce_qt_launcher.downloader import Downloader
from lce_qt_launcher.build_info import BuildInfo

import lce_qt_launcher.term_service as term_service

from enum import Enum
from subprocess import TimeoutExpired

import subprocess
import json
import os

_GITHUB_RELEASE_STR = "/releases/download/"

class InstanceSource(Enum):
    GITHUB_RELEASE = 0
    REMOTE_GIT_SOURCE = 1
    LOCAL_INSTALLATION = 2
    LOCAL_SOURCE_CODE = 3

# class InstanceType(Enum):
#    CLIENT_VANILLA = 0
#    CLENT_MODDED = 1
#    SERVER_VANILLA = 2
#    SERVER_MODDED = 3

DEFAULT_INSTANCE_NAME = "Default"
DEFAULT_INSTALLATION_PATH = "MinecraftLCEClient"
DEFAULT_USERNAME = "Steve"
DEFAULT_EXE_NAME = "Minecraft.Client.exe"
DEFAULT_ARCHIVE_FILE = "LCEWindows64.zip"
DEFAULT_URL = "https://github.com/MCLCE/MinecraftConsoles"
DEFAULT_INSTANCE_SOURCE = InstanceSource.GITHUB_RELEASE
DEFAULT_VERSION = "nightly"
DEFAULT_SKIN_PATH = ""
DEFAULT_SERVERS = ""

class Instance:
    def __init__(self, 
                 name : str = DEFAULT_INSTANCE_NAME, 
                 installation_path : str = DEFAULT_INSTALLATION_PATH, 
                 username : str = DEFAULT_USERNAME,
                 exe_name : str = DEFAULT_EXE_NAME,
                 archive_file : str = DEFAULT_ARCHIVE_FILE,
                 url : str = DEFAULT_URL, 
                 instance_source : InstanceSource = DEFAULT_INSTANCE_SOURCE,
                 #instance_type : InstanceType = InstanceType.CLIENT_VANILLA, 
                 version : str = DEFAULT_VERSION,
                 skin_path : str = DEFAULT_SKIN_PATH,
                 servers : list = DEFAULT_SERVERS
                ):
        self.name: str = name
        self.installation_path: str = installation_path
        self.username: str = username
        self.archive_file: str = archive_file
        self.exe_name: str = exe_name
        self.repo_url: str = url
        self.instance_source: InstanceSource = instance_source
        # self.instance_type = instance_type
        self.version: str = version
        self.skin_path: str = skin_path
        self.servers: list = servers

    def load_instance_from_dict(self, inst_dict: dict):
        self.name = inst_dict.get("name", DEFAULT_INSTANCE_NAME)
        self.installation_path = inst_dict.get("installation_path",DEFAULT_INSTALLATION_PATH)
        self.username = inst_dict.get("username", DEFAULT_USERNAME)
        self.exe_name = inst_dict.get("exe_name", DEFAULT_EXE_NAME)
        self.archive_file = inst_dict.get("archive_file", DEFAULT_ARCHIVE_FILE)
        self.url = inst_dict.get("url", DEFAULT_URL)
        self.instance_source = inst_dict.get("instances_source", DEFAULT_INSTANCE_SOURCE)
        self.version = inst_dict.get("version", DEFAULT_VERSION)
        self.skin_path = inst_dict.get("skin_path", DEFAULT_SKIN_PATH)
        self.servers = inst_dict.get("servers", DEFAULT_SERVERS)

    def get_download_url(self) -> str:
        if self.instance_source == InstanceSource.GITHUB_RELEASE:
            return self.repo_url + \
                    _GITHUB_RELEASE_STR + \
                    self.version + "/" + \
                    self.archive_file
        if self.instance_source == InstanceSource.REMOTE_GIT_SOURCE:
            return f"{self.repo_url}.git"
        if self.instance_source == InstanceSource.LOCAL_INSTALLATION:
            raise RuntimeError("Error ! Ressource Cannot be downloaded. Reason : Ressource is local")
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
    def install_instance(self) -> None:
        if self.instance.instance_source in [InstanceSource.GITHUB_RELEASE, InstanceSource.REMOTE_GIT_SOURCE]:
            return self._downloader.download_instance(self.instance)
        else:
            raise RuntimeWarning("Already Installed")

    def save_instance(self, save_file : str):
        try:
            json_string: str = json.dumps(vars(self.instance))
        except TypeError:
            json_string: str = json.dumps(vars(self.instance), default=str)
        if not save_file[0].endswith(self._build_info.instance_extension):
            save_file: str = save_file[0] + self._build_info.instance_extension
        os.makedirs(os.path.dirname(save_file), exist_ok=True)
        with open(save_file[0], 'w') as f:
            _ = f.write(json_string)
    
    def load_instance(self, save_file : str) -> None:
        if not save_file.endswith(self._build_info.instance_extension):
            save_file = os.path.join(save_file, ".lce_inst")
        inst_dict : dict = {}
        with open(save_file, 'r') as json_file:
            inst_dict = json.load(json_file)
            self.instance.load_instance_from_dict(inst_dict)
