from menu.utility import clearScreen
from time import sleep

class TicTacToe:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.boardState = {
                            "A1": " ",
                            "B1": " ",
                            "C1": " ",
                            "A2": " ",
                            "B2": " ",
                            "C2": " ",
                            "A3": " ",
                            "B3": " ",
                            "C3": " "
                        }
        self.firstPlayer = None # X or O goes first
        self.currentPlayer = None
        self.gameFinished = False # Is the game done?
        self.mostRecentMessages = [
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    "- Setting up Game -"
                                ]
        self.stateChange = False
        self.setupGame()
    
    def setupGame(self):
        # Render initial view
        self.renderAll()

        # Start searching for state changes
        self.runGame()

        # Start up Server
            # tell message board server is starting

        # Wait for other player connection to server 
            # tell user on message board

    # NOT DONE - ADD CLEAR MSG COMMAND, ADD QUIT COMMAND
    def processMessages(self, message):

        # add clear

        # add quit
 
        # Check if it starts with set
        # If not set just add message to message board
        if message.split(None, 1)[0] != "set":
            self.mostRecentMessages.append(message)
            self.mostRecentMessages.pop(0)

        # Process set commands
        elif message.split(None, 1)[0] == "set":

            # All set commands should take at least 3 params
            if len(message.split()) < 3:
                self.mostRecentMessages.append("Please input valid set command")
                self.mostRecentMessages.pop(0)

            elif message.split()[1] == "board":
                self.mostRecentMessages.append("setting board")
                self.mostRecentMessages.pop(0)

            else:
                self.mostRecentMessages.append("Please input valid set command")
                self.mostRecentMessages.pop(0)

        self.stateChange = True # Update view

    def renderServerInfo(self):
        print("Host: " + self.host)
        print("Port: " + str(self.port))

    def renderBoard(self, boardState):
        print("   A   B   C ")
        print("1  {} | {} | {}".format(boardState["A1"], boardState["B1"], boardState["C1"]))
        print("  -----------")
        print("2  {} | {} | {}".format(boardState["A2"], boardState["B2"], boardState["C2"]))
        print("  -----------")
        print("3  {} | {} | {}".format(boardState["A3"], boardState["B3"], boardState["C3"]))

   # Get all recent messages and render
    def renderMessageBoard(self):
        print("Messages")
        print("--------")

        for message in self.mostRecentMessages:
            print(message)

    def renderInputField(self):
        print("> ", end="")
        message = input()
        self.processMessages(message)

    def renderAll(self):
        clearScreen()
        self.renderServerInfo()
        print("")
        self.renderBoard(self.boardState)
        print("")
        self.renderMessageBoard()
        self.renderInputField()

    def setBoardLetter(self, position):
        self.boardState[position] = self.currentPlayer

    # change player each time a person take a turn
    def setCurrentPlayer(self):
        if self.currentPlayer == "X":
            self.currentPlayer = "O"
        else:
            self.currentPlayer = "X"

    def runGame(self):

        while self.gameFinished == False:
            sleep(.1)
            if self.stateChange == True:
                self.stateChange = False
                self.renderAll()

# Notes
# Add chat screen
#   input field can take in msg arg to make a msg liek '/m ' - 'quit' to quit - 'A1' to make play
# Add quit functionality
#  type in quit and it takes you to home screen