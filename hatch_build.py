import subprocess
import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):  # pyright: ignore[reportMissingTypeArgument]
    def clean(self, versions) -> None:  # pyright: ignore[reportMissingParameterType]
        if os.name == "posix":
            _ = subprocess.run("./scripts/clean.sh", check=True)
        if os.name == "nt":
            _ = subprocess.run(
                [
                    "powershell",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    "scripts\\clean.ps1",
                ],
                check=True,
                shell=True,
            )
        return super().clean(versions)

    def initialize(self, version, build_data) -> None:  # pyright: ignore[reportMissingParameterType]
        if os.name == "posix":
            _ = subprocess.run("./scripts/build.sh", check=True)
        if os.name == "nt":
            _ = subprocess.run(
                [
                    "powershell",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    "scripts\\build.ps1",
                ],
                check=True,
                shell=True,
            )
        return super().initialize(version, build_data)
