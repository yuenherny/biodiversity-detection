import os
from pathlib import Path
import subprocess


ROOT_PATH = Path(__file__).resolve().parent
DATA_PATH = ROOT_PATH / "data"

if not DATA_PATH.exists():
    DATA_PATH.mkdir(parents=True)

if not (DATA_PATH / "fish-tracking-dataset.zip").exists():

    commands = [
        "kaggle datasets download -d trainingdatapro/fish-tracking-dataset",
        "unzip fish-tracking-dataset.zip",
    ]

    for command in commands:
        subprocess.run(command, shell=True, check=True, cwd=DATA_PATH)