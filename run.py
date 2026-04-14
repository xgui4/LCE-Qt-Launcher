import os
import subprocess

if os.name == "posix":
    subprocess.run("./scripts/run.sh", check=True)
if os.name == "nt":
    subprocess.run("run.cmd", check=True, shell=True)