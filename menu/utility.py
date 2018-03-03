import sys
import os 
 
 # Check OS and call built in terminal clear command for that OS
def clearScreen():
    # dark side
    if sys.platform == "win32":
        os.system("cls")
    # join the dark side, mac users - jk grey jedi own go linux
    elif sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")

def evenColumn(dict):
    evenColumn = []
    maxLength = 0

    for key in dict: # too many vals
        if len(key) > maxLength:
            maxLength = len(key)

    for i, (key, value) in enumerate(dict.items()):
        if len(key) < maxLength:
            evenColumn.append(str(i + 1) + " - " + "\t" + str(key) + makeSpaces(maxLength-len(key)) + ": " + value)
        else:
            evenColumn.append(str(i + 1) + " - " + "\t" + str(key) + ": " + value)

    return evenColumn

def makeSpaces(num):
    spaces = []

    while num > 0:
        spaces.append(" ")
        num = num - 1

    return "".join(spaces)