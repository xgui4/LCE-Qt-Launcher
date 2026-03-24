import subprocess
import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        if os.name == "posix":
            subprocess.run("./build.sh", check=True)
        if os.name == "nt":
            subprocess.run("build.bat", check=True, shell=True)
        return super().initialize(version, build_data)