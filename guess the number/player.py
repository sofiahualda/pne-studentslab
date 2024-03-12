import socket
class Client:         #crear cliente con ip y port del servidor

    def __init__(self, IP: str, PORT: int):    #ip y port del servidor
        self.IP = IP
        self.PORT = PORT

    def __str__(self):
        return f"Connection to SERVER at {self.IP}, PORT: {self.PORT}"

    def talk(self, number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.IP, self.PORT))

        s.send(str.encode(number))

        response = s.recv(2048).decode("utf-8")

        s.close()

        return response


IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
response = c.talk('60')
print(response)
