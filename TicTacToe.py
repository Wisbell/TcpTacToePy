class TicTacToe:
    
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

    def renderBoard(self, boardState):
        print("   A   B   C ")
        print("1  {} | {}  | {}".format(boardState["A1"], boardState["B1"], boardState["C1"]))
        print("  -----------")
        print("2  {} | {}  | {}".format(boardState["A2"], boardState["B2"], boardState["C2"]))
        print("  -----------")
        print("3  {} | {}  | {}".format(boardState["A3"], boardState["B3"], boardState["C3"]))

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