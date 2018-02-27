import sys
import os
import time


class Menu:

    def __init__(self):
        # Wipe screen clean on start
        self.clearScreen()
    
    # Main Menu
    def showMenu(self):
        print("Welcome to Tic Tac Toe!")
        print("1 - Create Game")
        print("2 - Join Game")
        print("3 - About")
        print("4 - Quit")

    # Does python not have switch statements
    def parseChoice(self, choice):
        if len(choice) > 1:
            self.clearScreen()
            print("ERROR: You entered too many characters")
            print("")
            self.main()

        elif len(choice) < 1:
            self.clearScreen()
            print("ERROR: Please enter a single number between 1 and 4")
            print("")
            self.main()

        elif choice == "1":
            print("You chose 1")

        elif choice == "2":
            print("You chose 2")

        elif choice == "3":
            print("You chose 3, the about page - will add more later")
            # Maybe put git hub and creators here
            print("Hit enter to return to the main menu")
            input()
            self.clearScreen()
            self.main()

        elif choice == "4":
            print("Oh crap here comes your boss.  Closing in 3 seconds")
            time.sleep(3)
            self.clearScreen()
            # Figure out how to close the terminal later
            # These do not work - only leave terminal in CWD with cleared screen
            # os.system("exit")
            # sys.exit(0)
            # os._exit(-1)
            # os.system("quit")
            
        else:
            self.clearScreen()
            print("ERROR: You entered an incorrect choice")
            print("")
            self.main()

    # Check OS and call built in terminal clear command for that OS
    def clearScreen(self):
        # dark side
        if sys.platform == "win32":
            os.system("cls")
        # join the dark side, mac users - jk grey jedi own go linux
        elif sys.platform == "linux" or sys.platform == "darwin":
            os.system("clear")

    # Start
    def main(self):
        self.showMenu()
        print("> ", end="")
        choice = input()
        self.parseChoice(choice)