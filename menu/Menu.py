import sys
import os
import time

from .utility import clearScreen

class Menu:

    def __init__(self):
        # Wipe screen clean on start
        clearScreen()
    
    # Main Menu
    def showMainMenu(self):
        clearScreen()
        print("Welcome to Tic Tac Toe!")
        print("1 - Create Game")
        print("2 - Join Game")
        print("3 - About")
        print("4 - Quit")
        print("> ", end="") # end prevents auto new line
        choice = input()
        self.parseMainMenuChoice(choice)

    # Parse Main Menu Choice
    # Does python not have switch statements
    def parseMainMenuChoice(self, choice):
        if len(choice) > 1:
            clearScreen()
            print("ERROR: You entered too many characters")
            print("")
            time.sleep(2)
            self.main()

        elif len(choice) < 1:
            clearScreen()
            print("ERROR: Please enter a single number between 1 and 4")
            print("")
            time.sleep(2)
            self.main()

        elif choice == "1":
            print("You chose 1")
            clearScreen()
            self.showCreateGameMenu()

        elif choice == "2":
            clearScreen()
            print("join game here")
            print("add functionality later")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        elif choice == "3":
            self.showAboutScreen()

        elif choice == "4":
            print("")
            print("Oh crap here comes your boss.  Closing in 2 seconds")
            time.sleep(2)
            clearScreen()
            # Figure out how to close the terminal later
            
            # These do not work - only leave terminal in CWD with cleared screen - no biggie
            # os.system("exit")
            # sys.exit(0)
            # os._exit(-1)
            # os.system("quit")
            
        else:
            clearScreen()
            print("ERROR: You entered an incorrect choice")
            print("")
            time.sleep(2)
            self.main()

    # Show Create Game Menu
    def showCreateGameMenu(self):
        clearScreen()
        print("Create a new TTT Game!")
        print("1 - Play Alone :(")
        print("2 - Create LAN Game")
        print("3 - Create Internet Game")
        print("4 - Go Back to Main Menu")
        print("> ", end="") # end prevents auto new line
        choice = input()
        self.parseCreateGameChoice(choice)

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

        elif choice == "1":
            clearScreen()
            print("play single player game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        elif choice == "2":
            clearScreen()
            print("create lane game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        elif choice == "3":
            clearScreen()
            print("create internet game here")
            print("returning to main menu")
            time.sleep(2)
            self.showMainMenu()

        elif choice == "4":
            self.showMainMenu()
            
        else:
            clearScreen()
            print("ERROR: You entered an incorrect choice")
            print("")
            time.sleep(2)
            self.showCreateGameMenu()

    def showAboutScreen(self):
        clearScreen()
        print("You chose 3, the about page - will add more later")
        # Maybe put git hub and creators here
        print("Hit enter to return to the main menu")
        input()
        self.main()

    # Main program starts here
    def main(self):
        self.showMainMenu()