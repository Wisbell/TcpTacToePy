import socket
import pickle
import time
import threading
from TicTacToe import TicTacToe

class Client:

    def __init__(self, host, port):
        # Server host/port
        self.host = host
        self.port = port

        # Client game instance
        self.clientGame = TicTacToe()

        # Initialize socket object
        self.sock = socket.socket()

        # Connect to game server
        self.sock.connect((self.host, self.port))

        # Start getting connection
        self.startClient()

    def startClient(self):
        print("Connected to game server")

        sendThread = threading.Thread(target = self.sendMessage)
        sendThread.daemon = True
        sendThread.start()

        while True:

            data = self.sock.recv(1024)
            data = pickle.loads(data)

            self.clientGame.setGameState(data)
            self.clientGame.renderAll()

            # for stuff in data:
            #     print(stuff)
            # print("Recieved from server: " + str(data))

            # Set game data and render game
            # self.clientGame.setGameState(data)
            # self.clientGame.renderAll()

            print("->", end="")
            message = input()
            # print("message")
            print(message)
            # message = pickle.dumps(message)
            # maybe send all
            self.sock.send(message.encode("utf-8"))

    def sendMessage(self):
        while True:
            print("->", end="")
            msg = input()
            self.sock.send(msg.encode("utf-8"))
