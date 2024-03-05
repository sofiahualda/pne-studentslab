import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.87"  # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
print("Waiting for clients to connect")

while True:
    (rs, address) = ls.accept()
    print("A client has connected to the server!")

    msg = rs.recv(2048).decode("utf-8")
    print("Message received: " + termcolor.colored(msg, 'green'))

    newflag = "ECHO: " + msg
    rs.send(newflag.encode())
    rs.close()  # to close the socket of the client

# -- Close the socket
ls.close()