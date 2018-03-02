from .utility import clearScreen

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
