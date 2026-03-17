from enum import Enum

from downloader import Downloader
from build_info import BuildInfo

from subprocess import TimeoutExpired

import subprocess

_GITHUB_RELEASE_STR = "/releases/download/"

class InstanceType(Enum):
    GITHUB_RELEASE = 0
    REMOTE_GIT_SOURCE = 1
    LOCAL_INSTALLATION = 2
    LOCAL_SOURCE_CODE = 3

class Instance:
    def __init__(self, 
                 name : str = "Default", 
                 installation_path : str = "MinecraftLCEClient/", 
                 exe_name : str = "Minecraft.Client.exe",
                 archive_file : str = "LCEWindows64.zip",
                 url : str = "https://github.com/smartcmd/MinecraftConsoles", 
                 instance_type : InstanceType = InstanceType.GITHUB_RELEASE,
                 version : str = "nightly",
                 skin_path : str = "",
                 servers : list = {}
                ):
        self.name = name
        self.installation_path = installation_path
        self.archive_file = archive_file
        self.exe_name = exe_name
        self.repo_url = url
        self.instance_type = instance_type
        self.version = version
        self.skin_path = skin_path
        self.servers = servers

    def get_download_url(self) -> str:
        if self.instance_type == InstanceType.GITHUB_RELEASE:
            return self.repo_url + \
                    _GITHUB_RELEASE_STR + \
                    self.version + "/" + \
                    self.archive_file
        if self.instance_type == InstanceType.REMOTE_GIT_SOURCE:
            return f"{self.repo_url}.git"
        if self.instance_type == InstanceType.LOCAL_INSTALLATION:
            return RuntimeError("Error ! Ressource Cannot be downloaded. Reason : Ressource is local")
        else:
            return RuntimeError("Not implemented yet!")

class InstanceManager:
    def __init__(self, instance : Instance, build_info : BuildInfo):
        self.instance = instance
        self._downloader = Downloader(build_info)
        self._build_info = build_info
    def play(self) -> str:
        try:
            game_process = subprocess.run(self.instance.installation_path, self.instance.exe_name)
        except TimeoutExpired as err: 
            print(f"Error : process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}")
            return f"Error : process of lauching instance {self.instance.name} Failed. Reason : Timeout Expired.\n traceback : {err.with_traceback}"
        except PermissionError as err:
            print(f"Error : Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}")
            return f"Error : Cannot launch {self.instance.name}. Reason : Permission Denied.\n traceback : {err.with_traceback}"
        
        else:
            return f"Client closed with code {game_process.returncode}"  
    def install_instance(self) -> str:
        if self.instance in [InstanceType.GITHUB_RELEASE, InstanceType.REMOTE_GIT_SOURCE]:
            self._downloader.download_instance(self.instance)
        else:
            return "Already Installed, skip installation."
