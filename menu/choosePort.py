from .utility import clearScreen

def choosePort(self, ip):
    clearScreen()
    print("Please choose an open port to run the game server from")
    print("Usually greater than 5000, but not always")
    print("")
    print("Port: ", end="") # end prevents auto new line
    port = input()
    self.startGame(ip, port)