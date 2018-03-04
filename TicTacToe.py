class TicTacToe:

    # gameSettings = {
    #     "boardState": None,
    #     "currentPlayer": None,
    #     "firstPlayer": None,
    #     "hostIP": None,
    #     "port": None
    # }

    # add game args later
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.boardState = None
        self.firstPlayer = None
        self.currentPlayer = None

        # run setupGame function to setup game

        # after that render the game
        pass
    
    # Empty space default to keep board format flush
    boardState = {
        "A1": " ",
        "B1": " ",
        "C1": " ",
        "A2": " ",
        "B2": " ",
        "C2": " ",
        "A3": " ",
        "B3": " ",
        "C3": " ",
    }

    # X or O
    currentPlayer = ""
    firstPlayer = ""

    # Network Settings
    hostIP = ""
    port = None

    def setupGame(self):
        pass

    def renderNetworkInfo(self):
        pass

    def renderBoard(self, boardState):
        print("   A   B   C ")
        print("1  {} | {} | {}".format(boardState["A1"], boardState["B1"], boardState["C1"]))
        print("  -----------")
        print("2  {} | {} | {}".format(boardState["A2"], boardState["B2"], boardState["C2"]))
        print("  -----------")
        print("3  {} | {} | {}".format(boardState["A3"], boardState["B3"], boardState["C3"]))

    def renderMessageBoard(self):
        pass

    def renderAll(self):
        pass

        # clear screen

        # Render Network Settings

        # Render Board

        # Render Message Board

    # needs board argument
    def makePlay(self):
        pass

    # change player each time a person take a turn
    def setPlayer(self, letter):
        self.currentPlayer = letter


# Notes
# Add chat screen
#   input field can take in msg arg to make a msg liek '/m ' - 'quit' to quit - 'A1' to make play
# Add quit functionality
#  type in quit and it takes you to home screen