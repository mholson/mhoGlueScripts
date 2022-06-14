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
#macChoice = str(input("Choose computer [w]ork [l]aptop [d]esktop: "))
#if macChoice == "w":
#    computerName = "markolson"
#elif macChoice == "l":
#    computerName = "markolsonse"
#%else:
computerName = getpass.getuser()

# =-= Manual or Automatic Generation of File TagID
os.system("clear")
tagIDChoice = str(input("[m]anual or [a]utomatic tagID to be generated: "))
os.chdir(rf"/Users/{computerName}/GitHub/mhoGlueScripts")
tagPath = os.getcwd()
tagFileText = f"{tagPath}/00-tagID.txt"

if tagIDChoice == "m":
    tagID = str(input("Enter the File ID: "))
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
        # for i, l in enumerate(tagFile):
        #    pass
        #numLines = i + 1
        #print(f"There are currently {numLines} available. \n ")
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

# =-= Org File Schema
orgSchema = str(input("Enter the org file schema: "))
print("\n")
# =-= Org File Description
orgTitle = str(input("Enter the org Title:  "))
print("\n")
# =-= TeX File Description
texFileDescChoice = str(input("Enter TeX Title [1] Use Org Title [2] Custom "))
if texFileDescChoice == "1":
    texTitle = orgTitle
else:
    texTitle = str(input("Enter the *.md TeX Link Description: "))
print("\n")
# =-= Choose Directory to Generate TeX Files
os.chdir(rf"/Users/{computerName}/GitHub/mhoTeX/0-tex/")
texPath = os.getcwd()

# Generate the Core Files
with open(f"tex.core.{tagID}.tex", "x") as the_file:
    the_file.write("")
with open(f"tex.core.sv.{tagID}.tex", "x") as the_file:
    the_file.write("")

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
elif fileClassOption == 2:
    fileClass = "example"
    noteEnvironment = "example"
elif fileClassOption == 3:
    fileClass = "proposition"
    noteEnvironment = "proposition"
elif fileClassOption == 4:
    fileClass = "notation"
    noteEnvironment = "notation"
elif fileClassOption == 5:
    fileClass = "theorem"
    noteEnvironment = "theorem"
elif fileClassOption == 6:
    fileClass = "axiom"
    noteEnvironment = "axiom"
elif fileClassOption == 7:
    fileClass = "algorithm"
    noteEnvironment = "algo"
elif fileClassOption == 8:
    fileClass = "law"
    noteEnvironment = "alaw"
elif fileClassOption == 9:
    fileClass = "rule"
    noteEnvironment = "arule"
elif fileClassOption == 10:
    fileClass = "objective"
    noteEnvironment = "objective"
elif fileClassOption == 11:
    fileClass = "property"
    noteEnvironment = "property"
else:
    pass
print(f"===> tagID: {tagID}\n")

if fileClassOption == 0:  # Empty: used for non-specific information.
    with open(f"tex.note.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\label{{{tagID}}}\index{{TAG!{tagID}}}\index{{{texTitle}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
    # Generate tex.slide file
    with open(f"tex.slide.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
    with open(f"tex.slide.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
elif fileClassOption == 2:  # Examples: Questions with Answers
    # This will automatically generate an exam file.
    # Generate the answer core file
    with open(f"tex.core.soln.{tagID}.tex", "x") as the_file:
        the_file.write("")
    with open(f"tex.exam.ms.{tagID}.tex", "x") as the_file:
        the_file.write("")
    with open(f"tex.exam.marksGY.{tagID}.tex", "x") as the_file:
        the_file.write("")
    # Generate tex.note file
    with open(f"tex.note.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\begin{{{noteEnvironment}}}\label{{{tagID}}}\index{{TAG!{tagID}}}\index{{{fileClass.capitalize()}!{texTitle}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write(fr"\end{{{noteEnvironment}}}" "\n")
        the_file.write(fr"\begin{{solution}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.soln.{tagID}}}" "\n")
        the_file.write(fr"\end{{solution}}" "\n")
    # Generate initial tex.exam files
    with open(f"tex.exam.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\question[\input{{0-tex/tex.exam.marksGY.{tagID}}}] \input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write(fr"\begin{{\solnboxtype}}[\stretch{1}]" "\n")
        the_file.write(fr"\tagid{{{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.exam.ms.{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.soln.{tagID}}}" "\n")
        the_file.write(fr"\end{{\solnboxtype}}" "\n")
    with open(f"tex.exam.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\question[\input{{0-tex/tex.exam.marksGY.{tagID}}}] \input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write(fr"\begin{{\solnboxtype}}[\stretch{1}]" "\n")
        the_file.write(fr"\tagid{{{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.exam.ms.{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.soln.{tagID}}}" "\n")
        the_file.write(fr"\end{{\solnboxtype}}" "\n")
    # Generate tex.slide file
    with open(f"tex.slide.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\prob \input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write("\\framebreak")
        the_file.write("\n")
        the_file.write(fr"\soln")
        the_file.write(fr"\input{{0-tex/tex.core.soln.{tagID}}}" "\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
    with open(f"tex.slide.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\prob \input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
        
elif (fileClassOption == 3 or fileClassOption == 5 or fileClassOption == 8 or fileClassOption == 9 or fileClassOption == 11):  # Propositions with Proofs
    # Generate the answer core file
    with open(f"tex.core.proof.{tagID}.tex", "x") as the_file:
        the_file.write("")
    # Generate tex.note file
    with open(f"tex.note.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\begin{{{noteEnvironment}}}[{texTitle}]\label{{{tagID}}}\index{{TAG!{tagID}}}\index{{{fileClass.capitalize()}!{texTitle}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write(fr"\end{{{noteEnvironment}}}" "\n")
        the_file.write(fr"\begin{{proof}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.proof.{tagID}}}" "\n")
        the_file.write(fr"\end{{proof}}" "\n")

    # Generate tex.slide files
    with open(f"tex.slide.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write("\\framebreak")
        the_file.write("\n")
        the_file.write(fr"\proof")
        the_file.write(fr"\input{{0-tex/tex.core.proof.{tagID}}}" "\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
    with open(f"tex.slide.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
elif texTitle == "" and fileClassOption != 2:
    # Generate tex.note file
    with open(f"tex.note.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\begin{{{noteEnvironment}}}\label{{{tagID}}}\index{{TAG!{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write(fr"\end{{{noteEnvironment}}}" "\n")
    with open(f"tex.note.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\begin{{{noteEnvironment}}}\label{{{tagID}}}\index{{TAG!{tagID}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write(fr"\end{{{noteEnvironment}}}" "\n")
    # Generate tex.slide files
    with open(f"tex.slide.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
    with open(f"tex.slide.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{fileClass.capitalize()}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
else:
    # Generate tex.note file
    with open(f"tex.note.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\begin{{{noteEnvironment}}}[{texTitle}]\label{{{tagID}}}\index{{TAG!{tagID}}}\index{{{fileClass.capitalize()}!{texTitle}}}" "\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write(fr"\end{{{noteEnvironment}}}" "\n")
    # Generate tex.slide files
    with open(f"tex.slide.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")
    with open(f"tex.slide.sv.{tagID}.tex", "a") as the_file:
        the_file.write(
            fr"\documentclass[\string~/GitHub/mhoTeX/tex.deck.main.tex]{{subfiles}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\begin{{document}}" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"\begin{{frame}}{{{fileClass.capitalize()}}}{{{texTitle}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\input{{0-tex/tex.core.sv.{tagID}}}" "\n")
        the_file.write("\n")
        the_file.write(fr"\end{{frame}}" "\n")
        the_file.write(
            fr"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(
            fr"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" "\n")
        the_file.write(fr"\end{{document}}")

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
    the_file.write(fr"#+DATE: {orgTimeStamp}" "\n")
    the_file.write("\n")
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

subprocess.run(["git", "commit", "-a", rf"{orgPath}/{orgSchema}-{tagID}.org"])
