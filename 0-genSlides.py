import os
import subprocess
import getpass
from pathlib import Path

#  =-= Get Computer Name
computerName = getpass.getuser()

# =-= Setup Directories

os.chdir(rf"/Users/{computerName}/Documents/mhoBrain/vault/assets/")
pngPath = os.getcwd()

os.chdir(rf"/Users/{computerName}/Documents/mathematics/mathNotes/0-tex/")
texPath = os.getcwd()

# =-= create list of slide files

#slideTexFiles = [file.name for file in Path(texPath).iterdir() if file.name.startswith('tex.slide') and file.name.endswith(".tex")] 

# =-= tex the files

#for filename in slideTexFiles:
#    #subprocess.run(["xelatex", "-interaction=nonstopmode", filename])
#    subprocess.run(["xelatex", filename])

# =-= clean the directory

extensions = ["*.aux", "*.bar", "*.dvi", "*.bbl", "*.blg", "*.lb", "*.fdb_latexmk", "*.snm", "*.foo", "*.fls", "*.mw", "*.toc", "*.lb", "*.nav", "*.synctex.gz", "*.vrb", "*.out", "*.log", "*.pytxcode", "*.sagetex.sage", "*.sagetex.sage.py", "*.sagetex.sout", "*.synctex.gz", "*.sagetex.scmd", "*.synctex(busy)", "*.ilg", "*.ind", "*.bcf", "*.xdy", "*.run.xml", "*.lof", "*.lot", "*.idx", "*.xdv"]
for extension in extensions:
    for filename in Path(texPath).rglob(extension):
        subprocess.run(["rm", filename])

# =-= create the pngs
slidePdfFiles = [file.name for file in Path(texPath).iterdir() if file.name.startswith('tex.slide') and file.name.endswith(".pdf")] 

for filename in slidePdfFiles:
    lookup = Path(filename).stem
    subprocess.run(["convert", "-density", "300", f"{texPath}/{lookup}.pdf{[0]}",f"{pngPath}/{lookup}.png"])
