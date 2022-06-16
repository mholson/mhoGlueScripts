import os
import subprocess
import getpass
from pathlib import Path

# Get Computer Name
computerName = getpass.getuser()

# Choose compile options

createPython = input("Would you like to compile the python images? (Y/N): ")

createTikz = input("Would you like to compile the tikz images? (Y/N): ")

createPngs = input("Would you like to generate the png images? (Y/N): ")


if createPngs == "Y":
    os.chdir(rf"/Users/{computerName}/Documents/mhoBrain/vault/assets/")
    pngPath = os.getcwd()
else:
    pass

if createPython == "Y":
    os.chdir(rf"/Users/{computerName}/Documents/assets/python/")
    pythonPath = os.getcwd()

    # =-= create list of python image files
    pythonTexFiles = [file.name for file in Path(pythonPath).iterdir() if file.name.startswith('imgs.python') and file.name.endswith(".tex")] 
    pythonFiles = [file.name for file in Path(pythonPath).iterdir() if file.name.startswith('imgs.python') and file.name.endswith(".py")]
    # =-= tex the files
    for filename in pythonTexFiles:
        subprocess.run(["xelatex", "-interaction=nonstopmode", filename])
    for filename in pythonTexFiles:
        subprocess.run(["/usr/local/texlive/2021/texmf-dist/scripts/pythontex/pythontex3.py", filename])
    for filename in pythonTexFiles:
        subprocess.run(["xelatex", "-interaction=nonstopmode", filename])
    for filename in pythonFiles:
        subprocess.run(["python3", filename])

    if createPngs == "Y":
        # =-= generate the pngs
        pythonPdfFiles = [file.name for file in Path(pythonPath).iterdir() if file.name.startswith('imgs.python') and file.name.endswith(".pdf")] 

        for filename in pythonPdfFiles:
            lookup = Path(filename).stem
            subprocess.run(["convert", "-density", "300", f"{pythonPath}/{lookup}.pdf{[0]}",f"{pngPath}/{lookup}.png"])
        else:
            pass
else:
    pass

if createTikz == "Y":
    os.chdir(rf"/Users/{computerName}/Documents/assets/tikz/")
    tikzPath = os.getcwd()

    # =-= create list of tikz image files
    tikzTexFiles = [file.name for file in Path(tikzPath).iterdir() if file.name.startswith('imgs.tikz') and file.name.endswith(".tex")] 

    # =-= tex the files
    for filename in tikzTexFiles:
        subprocess.run(["xelatex", "-interaction=nonstopmode", filename])

    if createPngs == "Y":
        tikzPdfFiles = [file.name for file in Path(tikzPath).iterdir() if file.name.startswith('imgs.tikz') and file.name.endswith(".pdf")] 

        for filename in tikzPdfFiles:
            lookup = Path(filename).stem
            subprocess.run(["convert", "-density", "300", f"{tikzPath}/{lookup}.pdf{[0]}",f"{pngPath}/{lookup}.png"])
else: 
    pass

# =-= clean the directory

extensions = ["*.aux", "*.bar", "*.dvi", "*.bbl", "*.blg", "*.lb", "*.fdb_latexmk", "*.snm", "*.foo", "*.fls", "*.mw", "*.toc", "*.lb", "*.nav", "*.synctex.gz", "*.vrb", "*.out", "*.log", "*.pytxcode", "*.sagetex.sage", "*.sagetex.sage.py", "*.sagetex.sout", "*.synctex.gz", "*.sagetex.scmd", "*.synctex(busy)", "*.ilg", "*.ind", "*.bcf", "*.xdy", "*.run.xml", "*.lof", "*.lot", "*.idx", "*.xdv"]
for extension in extensions:
    if createPython == "Y":
        for filename in Path(pythonPath).rglob(extension):
            subprocess.run(["rm", filename])
    if createTikz == "Y":
        for filename in Path(tikzPath).rglob(extension):
            subprocess.run(["rm", filename])
