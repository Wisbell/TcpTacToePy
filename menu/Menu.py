import sys
import os
import time

from .utility import clearScreen

class Menu:

    from .showMainMenu import showMainMenu
    from .parseMainMenuChoice import parseMainMenuChoice
    from .showAboutScreen import showAboutScreen
    from .showCreateGameMenu import showCreateGameMenu

    def __init__(self):
        # Wipe screen clean on start
        clearScreen()

    def showCreateLanGame(self):
        # Find out what OS user is running
        # Get a list of interfaces and list them with number, interface name, ip address
        # tell user in message to choose from the list their local network ip

        # when user make a choice go to empty game and show starting of server in
        # message box

        # start server
        # start client
        pass

    def parseLanGameChoice(self):
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
        elif choice == "1":
            clearScreen()
            print("play single player game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        # LAN game
        elif choice == "2":
            clearScreen()
            print("create lan game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

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