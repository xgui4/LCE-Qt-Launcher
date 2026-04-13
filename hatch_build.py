import subprocess
import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def clean(self, versions):
        if os.name == "posix":
            subprocess.run("./scripts/clean.sh", check=True)
        if os.name == "nt":
            subprocess.run("scripts/clean.cmd", check=True, shell=True)
        return super().clean(versions)

    def initialize(self, version, build_data):
        if os.name == "posix":
            subprocess.run("./scripts/prepare.sh", check=True)
            subprocess.run("./scripts/build.sh", check=True)
        if os.name == "nt":
            subprocess.run("scripts/prepare.cmd", check=True)
            subprocess.run("scripts/build.cmd", check=True, shell=True)
        return super().initialize(version, build_data)