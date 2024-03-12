import random
import socket

class NumberGuesser:

    def __init__(self):
        self.secret_number = str(random.randint(1, 100))
        print(self.secret_number)

    def guess(self, number):
        self.number = number
        attempts = 0
        while number != self.secret_number:
            if number == self.secret_number:
                return f"You won after {attempts} attempts"
            elif number < self.secret_number:
                return "Higher"
            elif number > self.secret_number:
                return "Lower"
            attempts += 1
        return attempts



PORT = 8080
IP = "127.0.0.1"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.bind((IP, PORT))
serversocket.listen()
print("SEQ Server configured!")


flag = True
while True:
    print("\nWaiting for clients...")
    (clientsocket, address) = serversocket.accept()
    number = clientsocket.recv(2048).decode("utf-8")
    n = NumberGuesser()  # object = instance
    response = n.guess(number)
    send_bytes = str.encode(response)
    clientsocket.send(send_bytes)
    if response.startswith("You"):
        clientsocket.close()
        flag = False




