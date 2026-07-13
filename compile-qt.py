import os
import subprocess


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