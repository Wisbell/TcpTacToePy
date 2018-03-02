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

## Old ver

   # # Check OS and call built in terminal clear command for that OS
    # def clearScreen(self):
    #     # dark side
    #     if sys.platform == "win32":
    #         os.system("cls")
    #     # join the dark side, mac users - jk grey jedi own go linux
    #     elif sys.platform == "linux" or sys.platform == "darwin":
    #         os.system("clear")