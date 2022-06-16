import os
import subprocess
import time
from pathlib import Path

# =-= Change pdf background to transparent

os.chdir(r"/Users/markolsonse/Documents/mathematics/slideDecks/0-slides")
pdfPath = os.getcwd()

os.chdir(r"/Users/markolsonse/Documents/assets/pngs")
pngPath = os.getcwd()

for filename in Path(pdfPath).rglob("*.pdf"):
    lookup = Path(filename).stem
    if Path(f"{pngPath}/{lookup}.png").is_file():
        pass
    else:
        subprocess.run(["convert", "-density", "300", f"{pdfPath}/{lookup}.pdf{[0]}",f"{pngPath}/{lookup}.png"])
        print(f"New file added {lookup}.png")
#pdf_extensions = ["*.pdf"]
#for pdf_extension in pdf_extensions:
#        for filename in Path(path).rglob(pdf_extension):
#            subprocess.run(["convert", "-density", "300", filename, "-fuzz", "10%", "-transparent", "white",filename])
#else:
#    pass