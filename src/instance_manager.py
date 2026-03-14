from enum import Enum

import subprocess

class InstanceType(Enum):
    GITHUB_RELEASE = 0
    GITHUB_SOURCE = 1
    LOCAL_NO_INSTALL = 2

class Instance:
    def __init__(self, 
                 name : str = "Default", 
                 installation_path : str = "MinecraftLCEClient/", 
                 exe_name : str = "Minecraft.Client.exe",
                 url : str = "https://github.com/smartcmd/MinecraftConsoles", 
                 instance_type : InstanceType = InstanceType.GITHUB_RELEASE,
                 version : str = "nightly",
                 skin_path : str = "",
                 servers : list = {}
                ):
        self.name = name
        self.installation_path = installation_path
        self.exe_name = exe_name
        self.url = url
        self.instance_type = instance_type
        self.version = version
        self.skin_path = skin_path
        self.servers = servers

class InstanceManager:
    def __init__(self, instance : Instance):
        self.instance = instance
    def play(self):
        subprocess.run(self.instance.installation_path + self.instance.exe_name)
