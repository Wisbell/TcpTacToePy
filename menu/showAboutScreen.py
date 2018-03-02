from .utility import clearScreen

def showAboutScreen(self):
    clearScreen()
    print("You chose 3, the about page - will add more later")
    # Maybe put git hub and creators here
    print("Hit enter to return to the main menu")
    input()
    self.main()