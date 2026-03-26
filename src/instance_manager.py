from enum import Enum

from src.downloader import Downloader
from src.build_info import BuildInfo

import src.term_service as term_service

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

class Instance:
    def __init__(self, 
                 name : str = "Default", 
                 installation_path : str = "MinecraftLCEClient/", 
                 username : str = "Steve",
                 exe_name : str = "Minecraft.Client.exe",
                 archive_file : str = "LCEWindows64.zip",
                 url : str = "https://github.com/smartcmd/MinecraftConsoles", 
                 instance_source : InstanceSource = InstanceSource.GITHUB_RELEASE,
                 #instance_type : InstanceType = InstanceType.CLIENT_VANILLA, 
                 version : str = "nightly",
                 skin_path : str = "",
                 servers : list = {}
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

    def get_download_url(self) -> str:
        if self.instance_source == InstanceSource.GITHUB_RELEASE:
            return self.repo_url + \
                    _GITHUB_RELEASE_STR + \
                    self.version + "/" + \
                    self.archive_file
        if self.instance_source == InstanceSource.REMOTE_GIT_SOURCE:
            return f"{self.repo_url}.git"
        if self.instance_source == InstanceSource.LOCAL_INSTALLATION:
            _ = RuntimeError("Error ! Ressource Cannot be downloaded. Reason : Ressource is local")
        else:
            _ = RuntimeError("Not implemented yet!")        

class InstanceManager:
    def __init__(self, instance : Instance, build_info : BuildInfo):
        self.instance: Instance = instance
        self._downloader: Downloader = Downloader(build_info)
        self._build_info: BuildInfo = build_info
    def play(self) -> str:
        try:
            game_process = subprocess.run(self.instance.installation_path + self.instance.exe_name)
        except TimeoutExpired as err: 
            term_service.print_error(f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}")
            return f"process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}"
        except PermissionError as err:
            term_service.print_error(f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}")
            return f"Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}"
        else:
            return f"Client closed with code {game_process.returncode}"  
    
    def install_instance(self):
        if self.instance.instance_source in [InstanceSource.GITHUB_RELEASE, InstanceSource.REMOTE_GIT_SOURCE]:
            return self._downloader.download_instance(self.instance)
        else:
            return "Already Installed, skip installation."

    def save_instance(self, save_file : str):
        try:
            json_string = json.dumps(vars(self.instance))
        except TypeError:
            json_string = json.dumps(vars(self.instance), default=str)

        if not save_file[0].endswith(self._build_info.instance_extension):
            save_file[0] = save_file[0] + self._build_info.instance_extension
    
        os.makedirs(os.path.dirname(save_file[0]), exist_ok=True)
        
        with open(save_file[0], 'w') as f:
            _ = f.write(json_string)
    
    def load_instance(self, save_file : str):
        term_service.print_information("Not Implemented Yet!")
        if not save_file.endswith(self._build_info.instance_extension):
            save_file = os.path.join(save_file, ".lce_inst")

        with open(save_file, 'r') as f:
            json_file = f.read(save_file)

        self.instance = json.load(json_file)
