from .utility import clearScreen

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