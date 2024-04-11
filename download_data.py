from pathlib import Path
import subprocess


ROOT_PATH = Path(__file__).resolve().parent
DATA_PATH = ROOT_PATH / "data"

if DATA_PATH.exists():
    print("Data folder already exists")
else:
    DATA_PATH.mkdir(parents=True)

if (DATA_PATH / "fish-tracking-dataset.zip").exists():
    print("Dataset has already been downloaded")
else:
    commands = [
        "kaggle datasets download -d trainingdatapro/fish-tracking-dataset",
        "unzip fish-tracking-dataset.zip",
    ]

    for command in commands:
        subprocess.run(command, shell=True, check=True, cwd=DATA_PATH)