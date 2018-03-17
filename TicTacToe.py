from menu.utility import clearScreen
from time import sleep
import sys

class TicTacToe:

    # def __init__(self, host, port):
    def __init__(self):
        # self.host = host
        # self.port = port
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
        self.messageBoard = [
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    ".",
                                    "Waiting on another player . . ."
                                ]
        self.goesFirst = None     # X or O
        self.currentPlayer = None # X or O
        self.gameFinished = False # Is the game done?
        self.stateChange = False  # Has message or board change
        self.gameReady = False    # Game maker has chosen letter and which letter goes first
        self.serverReady = False  # Has the server started?
        # self.startGame()          # Initial render and setup

    def getGameState(self):
        return {
            "boardState": self.boardState,
            "messageBoard": self.messageBoard,
            "currentPlayer": self.currentPlayer,
            "goesFirst": self.goesFirst,
            "gameFinished": self.gameFinished,
        }

    def setGameState(self, newState):
        self.boardState = newState["boardState"]
        self.messageBoard = newState["messageBoard"]
        self.currentPlayer = newState["currentPlayer"]
        self.gameFinished = newState["gameFinished"]
        self.goesFirst = newState["goesFirst"]

    # def renderSetup(self):
    #     # set x or o first
    #     print("Do you want to be X or O?")
    #     print("Letter: ",end="")
    #     letter = input()
    #     # let first player who started the game choose who goes first
    #     print("Who goes first X or O?")
    #     print("First: ", end="")
    #     first = input()
    
    #     self.goesFirst = first
    #     self.currentPlayer = letter
    #     self.gameReady = True

    #     self.renderAll()

    # def startGame(self):
    #     # Render initial view
    #     self.renderAll()

    #     # Start searching for state changes
    #     self.runGame()

    #     if self.gameReady == True:
            
    #         if self.serverReady == False:
    #             pass
    #             # gameServer = 
    #     # Start up Server - if game is set up
    #         # tell message board server is starting

    #     # Wait for other player connection to server 
    #         # tell user on message board

    # NOT DONE - ADD CLEAR MSG COMMAND, ADD QUIT COMMAND
    def processMessages(self, message):
        
        # Just spaces - do nothing
        if len(message.split()) == 0:
            pass

        # Clear
        elif len(message.split()) == 1 and message.split()[0] == "clear":
            self.messageBoard = []

        # Quit
        elif len(message.split()) == 1 and message.split()[0] == "quit":
            sys.exit(0)

        # Set
        elif message.split(None, 1)[0] == "set":

            # All set commands should take at least 3 params
            if len(message.split()) < 3:
                self.messageBoard.append("Please input valid set command")
                self.messageBoard.pop(0)

            elif message.split()[1] == "board":
                self.messageBoard.append("setting board")
                self.messageBoard.pop(0)

            else:
                self.messageBoard.append("Please input valid set command")
                self.messageBoard.pop(0)

        else:
            self.messageBoard.append(message)
            if len(self.messageBoard) > 10:
                self.messageBoard.pop(0)

        self.stateChange = True # Update view

    # def renderServerInfo(self):
    #     print("Host: " + self.host)
    #     print("Port: " + str(self.port))

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

        for message in self.messageBoard:
            print(message)

    def renderInputField(self):
        print("> ", end="")
        message = input()
        self.processMessages(message)

    def renderAll(self):
        clearScreen()
        # self.renderServerInfo()
        # print("")
        self.renderBoard(self.boardState)
        print("")

        self.renderMessageBoard()
        # self.renderInputField()

    def setBoardLetter(self, position):
        self.boardState[position] = self.currentPlayer

    # Change player each time a person take a turn
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

# Add quit functionality
#  type in quit and it takes you to home screen