import sys
import os
import time

import netifaces
import winreg
from pprint import pprint

from .utility import clearScreen
from .utility import evenColumn

class Menu:

    from .showMainMenu import showMainMenu
    from .parseMainMenuChoice import parseMainMenuChoice
    from .showAboutScreen import showAboutScreen
    from .showCreateGameMenu import showCreateGameMenu
    from .findLocalInterfaces import findLocalInterfaces
    from .showCreateLanGameMenu import showCreateLanGameMenu

    def __init__(self):
        # Wipe screen clean on start
        clearScreen()

    # def showCreateLanGameMenu(self):
    #     interfaceList = self.findLocalInterfaces()

    #     if len(interfaceList) > 0:
    #         print("Choose a local interface or manually enter an IP to start your server!")
    #         printOptions = evenColumn(interfaceList)
    #         for item in printOptions:
    #             print(item)
    #         print("or")
    #         print(str(len(printOptions) + 1) + " - \t" + "Manually input IP address")
    #         print("> ", end="") # end prevents auto new line
    #         choice = input()
    #         self.parseLanGameChoice(choice, printOptions)

    #     else:
    #         print("Couldn't find any interfaces.  Please manually enter your local IP address you want to host from.")
    #         print("> ", end="") # end prevents auto new line
    #         manualIp = input()
    #         self.parseLanGameChoice(manualIp, None) # Pass None if no choices

    def parseLanGameChoice(self, choice, interfaces):
        print("choice", choice)
        # print("interfaces", interfaces)

        if interfaces == None:
            pass # ip will be whatever the user entered
        else:
            print("interfaces", interfaces)
            # get ip from interface list
        

          # when user make a choice go to empty game and show starting of server in
        # message box

        # start server
        # start client

    # Parse Create Game Choice
    def parseCreateGameChoice(self, choice):
        if len(choice) > 1:
            clearScreen()
            print("ERROR: You entered too many characters")
            print("")
            time.sleep(2)
            self.showCreateGameMenu()

        elif len(choice) < 1:
            clearScreen()
            print("ERROR: Please enter a single number between 1 and 4")
            print("")
            time.sleep(2)
            self.showCreateGameMenu()

        # single player
        elif choice == "1":
            clearScreen()
            print("play single player game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        # LAN game
        elif choice == "2":
            clearScreen()
            self.showCreateLanGameMenu()
            # print("create lan game here")
            # print("returning to main menu")
            # time.sleep(2)
            # self.showMainMenu()

        # Internet game
        elif choice == "3":
            clearScreen()
            print("create internet game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        # main menu
        elif choice == "4":
            self.showMainMenu()
            
        else:
            clearScreen()
            print("ERROR: You entered an incorrect choice")
            print("")
            time.sleep(2)
            self.showCreateGameMenu()

    # Main program starts here
    def main(self):
        self.showMainMenu()