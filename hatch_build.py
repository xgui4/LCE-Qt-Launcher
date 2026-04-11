import subprocess
import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def clean(self, versions):
        if os.name == "posix":
            subprocess.run("./clean.sh", check=True)
        if os.name == "nt":
            subprocess.run("clean.bat", check=True, shell=True)
        return super().clean(versions)

    def initialize(self, version, build_data):
        if os.name == "posix":
            subprocess.run("./prepare.sh", check=True)
            subprocess.run("./build.sh", check=True)
        if os.name == "nt":
            subprocess.run("prepare.bat", check=True)
            subprocess.run("build.bat", check=True, shell=True)
        return super().initialize(version, build_data)