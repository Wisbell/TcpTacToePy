import socket
import pickle
import pprint
import threading
from TicTacToe import TicTacToe

class Server:

    def __init__(self, host, port, hostLetter, goesFirst):
        print("Server started")

        self.host = host

        self.port = port

        self.hostLetter = hostLetter

        self.goesFirst = goesFirst

        self.finishedServing = False

        # Store player client info
        self.clientList = []

        # Create instance of TTT game
        self.game = TicTacToe()

        # Create socket instance - Creates default TCP
        self.s = socket.socket()

        # Timeout every 0 seconds to listen for key exception and create non blocking socket
        # self.s.settimeout(0)
        # self.s.setblocking(0)

        # Bind host/port to socket
        self.s.bind((host, port))

        # Start server listening for connections
        self.s.listen(2)

        # Start getting connection
        self.startServer()

    def startServer(self):
        print("Listening for connections on port " + str(self.port))
        # While game is not finished, run server
        while not self.finishedServing:

            try: 
                
                # Listen for connections if less than two players
                if (len(self.clientList)) < 2:

                    print("Waiting for a client . . .")

                    # Set up client vars when connection accepted
                    client, addr = self.s.accept()
                    print("Connection from: ", addr)

                    # Send initial game state
                    self.sendGameState(client)

                    # Create threads for each client to create nonblocking behavior
                    clientThread = threading.Thread(target=self.clientHandler, args=(client, addr))
                    clientThread.daemon = True
                    clientThread.start()

                    # Add client info to player list
                    print("Adding player to server")
                    self.addPlayerToClientList(client, addr)

                # If both players are connected - start game
                elif(len(self.clientList)) == 2:
                    self.game.gameReady = True
                    # send data to clients that game is ready

                    # tell game instance game is ready to be played
                    # players can set their letter on the board
                    # if it is their turn

                elif self.game.gameFinished == True:
                    pass
                    # stop the server and return user to main menu?

            except KeyboardInterrupt:
                client.close()
                self.shutdown = True
                continue

            except:
                continue

    def clientHandler(self, client, address):
        while True:
            # Recieve data from client
            data = client.recv(1024)
            data = data.decode("utf-8")

            print("Recieved: " + data)

            # Check message for game state changes or add message to message list

    def addPlayerToClientList(self, client, address):
        print("Set player called")
        if len(self.clientList) == 0:
            self.clientList.append((client, address, self.hostLetter))
        else:
            if self.clientList[0][2] == "X":
               self.clientList.append((client, address, "O")) 
            else:
                self.clientList.append((client, address, "X")) 

        pprint.pprint(self.clientList)

    def sendGameState(self, client):
         # Serialize game state
        serialState = pickle.dumps(self.game.getGameState())

        # Send entire game state to client
        client.sendall(serialState)

    