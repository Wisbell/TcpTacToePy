import sys
import os
import time

import netifaces
import winreg
from pprint import pprint

# remove these later if not needed
from .utility import clearScreen
from .utility import evenColumn

from TicTacToe import TicTacToe

class Menu:

    from .showMainMenu import showMainMenu
    from .parseMainMenuChoice import parseMainMenuChoice
    from .showAboutScreen import showAboutScreen
    from .showCreateGameMenu import showCreateGameMenu
    from .findLocalInterfaces import findLocalInterfaces
    from .showCreateLanGameMenu import showCreateLanGameMenu
    from .parseLanGameChoice import parseLanGameChoice
    from .choosePort import choosePort

    def __init__(self):
        # Wipe screen clean on start
        clearScreen()

    def startGame(self, ip, port):
        # import TTT and pass ip and port to the new instance to start
        # START GAME HERE
        print("ip", ip)
        print("port", port)

    def showGetManualIP(self):
        clearScreen()
        print("This feature is incomplete as of now - will return to LAN game menu.")
        print("Please input your local IP you want to host from")
        print("You can use 'ipconfig'(Win) or 'ifconfig'(Unix) in a terminal to find your local IP")
        print("Note: Normally it will look like 192.168.x.x, 10.x.x.x, or 172.x.x.x")
        print("> ", end="") # end prevents auto new line
        choice = input()
        # check if ip is valid ex: 1.1.1.1 to 255.255.255.255
        self.showCreateLanGameMenu()

        #
        # go to game view and start server listening for connection
        #

        pass

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
        # NOT DONE
        elif choice == "1":
            clearScreen()
            print("play single player game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        # LAN game
        # IN PROGRESS
        elif choice == "2":
            clearScreen()
            self.showCreateLanGameMenu()

        # Internet game
        # NOT DONE
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