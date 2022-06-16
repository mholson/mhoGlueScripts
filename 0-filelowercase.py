import os
import subprocess
from pathlib import Path

namePath = os.getcwd()

for file in os.listdir(namePath):
    os.rename(file, file.lower())
