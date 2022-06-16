import os
# import shutil
import subprocess
import time
from pathlib import Path

# =-= Change pdf background to transparent

os.chdir(r"/Users/markolsonse/Documents/assets/temp-remove-bg")
path = os.getcwd()
pdf_extensions = ["*.pdf"]
for pdf_extension in pdf_extensions:
        for filename in Path(path).rglob(pdf_extension):
            subprocess.run(["convert", "-density", "300", filename, "-fuzz", "10%", "-transparent", "white",filename])
else:
    pass