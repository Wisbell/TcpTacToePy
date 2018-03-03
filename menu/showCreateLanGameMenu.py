from .utility import evenColumn
from .utility import clearScreen

def showCreateLanGameMenu(self):
    interfaceList = self.findLocalInterfaces()

    if len(interfaceList) > 0:
        clearScreen()
        print("Choose a local interface or manually enter an IP to start your server!")
        printOptions = evenColumn(interfaceList)
        for item in printOptions:
            print(item)
        print("or")
        print(str(len(printOptions) + 1) + " - \t" + "Manually input IP address")
        print(str(len(printOptions) + 2) + " - \t" + "Go Back")
        print("> ", end="") # end prevents auto new line
        choice = input()
        self.parseLanGameChoice(choice, interfaceList)

    else:
        clearScreen()
        print("Couldn't find any interfaces.  Please manually enter your local IP address you want to host from.")
        print("> ", end="") # end prevents auto new line
        manualIp = input()
        self.parseLanGameChoice(manualIp, None) # Pass None if no choices