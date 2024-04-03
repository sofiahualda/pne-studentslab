import socket
from pathlib import Path
import termcolor


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")
    read_fileA= Path("html/info/A.html").read_text()
    read_fileC = Path("html/info/C.html").read_text()
    read_fileG = Path("html/info/G.html").read_text()
    read_fileT = Path("html/info/T.html").read_text()
    read_file_error = Path("html/error.html").read_text()
    read_file_index = Path("html/index.html").read_text()


    if "info/A" in req_line:
        body = read_fileA
    elif "info/C" in req_line:
        body = read_fileC
    elif "info/G" in req_line:
        body = read_fileG
    elif "info/T" in req_line:
        body = read_fileT
    elif "" in req_line:
        body = read_file_index
    else:
        body = read_file_error
    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())




ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Green server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()