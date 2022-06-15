import os
import sys
import subprocess
import getpass
from pathlib import Path
import shortuuid
import uuid
from datetime import datetime
from tabulate import tabulate

# =-= Choose Computer
# TODO need to setup default system
os.system("clear")
computerName = getpass.getuser()

# =-= Enter file ID
tagID = str(input("Enter the File ID: "))
# =-= Org File Schema
orgSchema = str(input("Enter the org file schema: "))
print("\n")
# =-= Org File Description
orgTitle = str(input("Enter the org Title:  "))
print("\n")
print(f"=== Classification of File === \n")
# MENU OPTIONS

# PRINT OPTIONS
classMenu = [[r"[0]", "empty", r"[1]", "definition"],
[r"[2]", "example (including exam prob)", r"[3]", "proposition"], 
[r"[4]", "notation", r"[5]", "theorem"],
[r"[6]", "axiom", r"[7]", "algorithm"], 
[r"[8]", "law", r"[9]", "rule"],
[r"[10]", "objective", r"[11]", "property"]]
head = [r"#", "Description", r"#", "Description"]
print(tabulate(classMenu, headers=head, tablefmt="grid"))
# SELECT OPTION
fileClassOption = int(input("Select the Classification: "))
if fileClassOption == 0:
    fileClass = ""
elif fileClassOption == 1:
    fileClass = "definition"
    noteEnvironment = "definition"
    orgTag = ":defn:"
elif fileClassOption == 2:
    fileClass = "example"
    noteEnvironment = "example"
    orgTag = ":soln:"
elif fileClassOption == 3:
    fileClass = "proposition"
    noteEnvironment = "proposition"
    orgTag = ":prop:"
elif fileClassOption == 4:
    fileClass = "notation"
    noteEnvironment = "notation"
    orgTag = ":notn:"
elif fileClassOption == 5:
    fileClass = "theorem"
    noteEnvironment = "theorem"
    orgTag = ":thrm:"
elif fileClassOption == 6:
    fileClass = "axiom"
    noteEnvironment = "axiom"
    orgTag = ":axim:"
elif fileClassOption == 7:
    fileClass = "algorithm"
    noteEnvironment = "algo"
    orgTag = ":algo:"
elif fileClassOption == 8:
    fileClass = "law"
    noteEnvironment = "alaw"
    orgTag = ":laws:"
elif fileClassOption == 9:
    fileClass = "rule"
    noteEnvironment = "arule"
    orgTag = ":algo:"
elif fileClassOption == 10:
    fileClass = "objective"
    noteEnvironment = "objective"
    orgTag = ":objv:"
elif fileClassOption == 11:
    fileClass = "property"
    noteEnvironment = "property"
    orgTag = ":prpt:"
else:
    pass
print(f"===> tagID: {tagID}\n")

# =-= Generate the Markdown File

#os.chdir(rf"/Users/{computerName}/Documents/mhoBrain/Vault/")
os.chdir(rf"/Users/{computerName}/GitHub/mhoOrgRoamGarden/")
orgPath = os.getcwd()
# mdTimeStamp = int(datetime.now().strftime("%s")) * 1000
orgTimeStamp = datetime.now().strftime("%Y-%m-%d")
with open(f"{orgPath}/{orgSchema}-{tagID}.org", "a") as the_file:
    the_file.write(fr":PROPERTIES:" "\n")
    #the_file.write(fr"id: {shortuuid.uuid()}" "\n")
    the_file.write(fr":ID: {uuid.uuid1()}" "\n")
    the_file.write(fr":ROAM_ALIASES: {orgSchema}-{tagID}" "\n")
    the_file.write(fr":END:" "\n")
    the_file.write(fr"#+TITLE: {orgTitle}" "\n")
    the_file.write(fr"#+filetags: {orgTag}" "\n")
    the_file.write(fr"#+DATE: {orgTimeStamp}" "\n")
    the_file.write("\n")
    the_file.write(
        rf"[[~/Documents/assets/orgRoamGardenPNGs/tex.slide.{tagID}.png]]" "\n")
    the_file.write(r"* TeX Files" "\n")
    the_file.write(r"** TeX Core" "\n")
    the_file.write(r"*** English" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.core.{tagID}.tex]]" "\n")
    the_file.write(r"*** Swedish" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.core.sv.{tagID}.tex]]" "\n")
    the_file.write(r"** TeX Note" "\n")
    the_file.write(r"*** English" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.note.{tagID}.tex]]" "\n")
    the_file.write(r"*** Swedish" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.note.sv.{tagID}.tex]]" "\n")
    the_file.write(r"** TeX Slides" "\n")
    the_file.write(r"*** English" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.slide.{tagID}.tex]]" "\n")
    the_file.write(r"*** Swedish" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.slide.sv.{tagID}.tex]]" "\n")
    the_file.write(r"** TeX Exams" "\n")
    the_file.write(r"*** English" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.exam.{tagID}.tex]]" "\n")
    the_file.write(r"*** Swedish" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.exam.sv.{tagID}.tex]]" "\n")
    the_file.write(r"*** Marks GY" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.exam.markGY.{tagID}.tex]]" "\n")
    the_file.write(r"*** Marks IB" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.exam.markIB.{tagID}.tex]]" "\n")
    the_file.write(r"*** Mark Scheme" "\n")
    the_file.write(
        rf"#+transclude: [[file:~/GitHub/mhoTeX/0-tex/tex.exam.ms.{tagID}.tex]]" "\n")
    the_file.write("\n")
    the_file.write(rf"* Dependencies" "\n")
    the_file.write("\n")
    the_file.write(rf"* References" "\n")
    the_file.write("\n")

