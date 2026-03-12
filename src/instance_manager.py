from enum import Enum

class InstanceType(Enum):
    GITHUB_RELEASE = 0
    GITHUB_SOURCE = 1
    LOCAL_NO_INSTALL = 2

class Instance:
    def __init__(self, 
                 name : str, 
                 installation_path : str, 
                 exe_name : str,
                 url : str, 
                 instance_type : InstanceType,
                 version : str,
                 skin_path : str,
                 servers : list
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
    def __init__(self):
        pass
