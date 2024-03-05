import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.34"  # this IP address is local, so only requests from the same machine are possible


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

i = 1
num_con = 0
list_clients = []
while True:
    (rs, address) = ls.accept()
    print("Waiting for clients to connect")
    print(f"Connection", i, "Client IP, PORT: ", address)


    num_con += 1
    list_clients.append(address)


    msg = rs.recv(2048).decode("utf-8")
    print("Message received: " + termcolor.colored(msg, 'green'))

    newflag = "ECHO: " + msg
    rs.send(newflag.encode())

    index_list = 0
    if num_con == 5:
        for element in list_clients:
            index_list += 1
            print(f"Client", index_list, element)
    else:
        rs.close()
    i += 1

ls.close()