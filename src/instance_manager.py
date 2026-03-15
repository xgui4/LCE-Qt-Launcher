from enum import Enum

from downloader import Downloader

_GITHUB_RELEASE_STR = "/releases/download/"

import subprocess

class InstanceType(Enum):
    GITHUB_RELEASE = 0
    GIT_SOURCE_CODE = 1
    LOCAL_NO_INSTALL = 2

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
        if self.instance_type == InstanceType.GIT_SOURCE_CODE:
            return f"{self.repo_url}.git"
        if self.instance_type == InstanceType.LOCAL_NO_INSTALL:
            return RuntimeError("Error ! Ressource Cannot be downloaded. Reason : Ressource is local")
        else:
            return RuntimeError("Not implemented yet!")

class InstanceManager:
    def __init__(self, instance : Instance):
        self.instance = instance
        self._downloader = Downloader()
    def play(self):
        subprocess.run(self.instance.installation_path + self.instance.exe_name)
    def install(self):
        self._downloader.download_client(self.instance); 
