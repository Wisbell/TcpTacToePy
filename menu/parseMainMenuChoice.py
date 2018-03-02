import time
from .utility import clearScreen

# Parse Main Menu Choice
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