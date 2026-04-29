import os
import subprocess

if os.name == "posix":
    _ = subprocess.run("./scripts/run.sh", check=True)
if os.name == "nt":
    _ = subprocess.run("scripts\\run.cmd", check=True, shell=True)