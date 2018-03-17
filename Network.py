import socket
import pickle




# Initialize with host and port
# host = "192.168.2.1"
# port = 5000
class Server:

    def __init__(self, host, port):

        # Create socket instance - Creates default TCP
        self.s = socket.socket()

        # Bind host/port to socket
        self.s.bind((host, port))

        # Start server listening for connections
        self.s.listen()

        # Start getting connection
        self.startLoop()

    def startLoop(self):
        while True:
            client, addr = self.s.accept()

            print("client", client)
            print("addr", addr)

    def getGameState(self):
        # Add functionality to get current game state

        data = {
            "boardState": { "A1": " ", "B1": " ", "C1": " ",
                            "A2": " ", "B2": " ", "C2": " ",
                            "A3": " ", "B3": " ", "C3": " "
                            },
            "messageBoard": [
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                "."
            ]
        }

        return data

        
def Main():

    client, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        # recieve 1024 bytes at a time in buffer
        # decode data into string from raw bytes
        # data = client.recv(1024).decode("utf-8")

        # if not data:
        #     break
        
        # print("From connected user: " + data)

        # data = data.upper()
        # print("Sending: " + data)
        # # encode back into raw bytes
        # client.send(data.encode("utf-8"))

        # serialize as json
        serial_data = pickle.dumps(data)

        # send to client
        client.send(serial_data)

        # break

    client.close()

if __name__ == "__main__":
    Main()