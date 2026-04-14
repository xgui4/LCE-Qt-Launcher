import subprocess
import os
from typing import override

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):  # pyright: ignore[reportMissingTypeArgument]
    @override
    def clean(self, versions) -> None:  # pyright: ignore[reportMissingParameterType]
        if os.name == "posix":
            _ = subprocess.run("./scripts/clean.sh", check=True)
        if os.name == "nt":
            _ = subprocess.run("scripts/clean.cmd", check=True, shell=True)
        return super().clean(versions)

    @override
    def initialize(self, version, build_data) -> None:  # pyright: ignore[reportMissingParameterType]
        if os.name == "posix":
            _ = subprocess.run("./scripts/prepare.sh", check=True)
            _ = subprocess.run("./scripts/build.sh", check=True)
        if os.name == "nt":
            _ = subprocess.run("prepare.cmd", check=True)
            _ = subprocess.run("build.cmd", check=True, shell=True)
        return super().initialize(version, build_data)