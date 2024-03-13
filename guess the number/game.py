import random
import socket

class NumberGuesser:

    def __init__(self):
        self.secret_number = str(random.randint(1, 100))
        self.attempts = 0
        print(self.secret_number)

    def guess(self, number):
        self.number = number
        while number != self.secret_number:
            self.attempts += 1
            if number < self.secret_number:
                return "Higher"
            elif number > self.secret_number:
                return "Lower"
        return f"You won after {str(self.attempts)} attempts"


PORT = 8080
IP = "127.0.0.1"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.bind((IP, PORT))
serversocket.listen()
print("SEQ Server configured!")
print("\nWaiting for clients...")
n = NumberGuesser()    # object = instance
flag = True
while True:
    (clientsocket, address) = serversocket.accept()
    number = clientsocket.recv(2048).decode("utf-8")
    response = n.guess(number)
    send_bytes = str.encode(response)
    clientsocket.send(send_bytes)
    if response.startswith("You"):
        clientsocket.close()
        serversocket.close()
        flag = False




