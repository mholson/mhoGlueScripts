import os
import sys
import subprocess
import getpass
from pathlib import Path
from datetime import datetime

# =-= Choose Computer
os.system("clear")
computerName = getpass.getuser()

# =-= Manual or Automatic Generation of File TagID
os.system("clear")
tagIDChoice = str(input("[m]anual or [a]utomatic tagID to be generated: "))
os.chdir(rf"/Users/{computerName}/GitHub/mhoGlueScripts")
tagPath = os.getcwd()
tagFileText = f"{tagPath}/00-tagID.txt"

if tagIDChoice == "m":
    tagID = str(input("Enter the File ID:"))
    with open(tagFileText) as tagFile:
        if tagID in tagFile.read():
            print(f"The tagID {tagID} is available")
            confirmTagID = str(
                input(f"Would you like to use tagID: [y]es [n]o? "))
            if confirmTagID == "y":
                # Remove first line using GNU-SED
                # This needs to be installed using homebrew
                print(f"The tagID {tagID} has been successfully removed.")
                subprocess.run(["gsed", "-i", rf"/{tagID}/d", tagFileText])
            else:
                sys.exit(
                    f"The tagID {tagID} was not removed. Please run again.")
        else:
            sys.exit(f"The tagID {tagID} is not available. Please run again.")
else:
    with open(tagFileText) as tagFile:
        tagID = tagFile.readline().rstrip()
        for i, l in enumerate(tagFile):
            pass
        numLines = i + 1
        print(
            f"There are currently {numLines} available. \n The next available tagID is {tagID}")
        confirmTagID = str(input(f"Would you like to use tagID: [y]es [n]o? "))
        if confirmTagID == "y":
            # Remove first line using GNU-SED
            # This needs to be installed using homebrew
            print(f"The tagID {tagID} has been successfully removed.")
            subprocess.run(["gsed", "-i", r"1d", tagFileText])
        else:
            tagID = str(input("Enter the File ID:"))
    # TODO build in generator of new file IDs
