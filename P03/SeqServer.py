from Seq1 import Seq
import os
import socket
import termcolor


PORT = 8080
IP = "127.0.0.1"


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()

print("Seq server configured!")
print(f"Waiting for clients...")
while True:
    (rs, address) = ls.accept()
    msg = rs.recv(2048).decode("utf-8")

    if msg == "PING":
        print("Ping command!\nOK!")
        newflag = "OK!"
        rs.send(newflag.encode())
        print(f"\nWaiting for clients...")


    GENES = ["U5", "RNU6_269P", "FXN", "FRAT1", "ADA"]
    number = 0
    for gene in GENES:
        s = Seq()
        s.read_fasta(os.path.join("..", "sequences", gene + ".txt"))
        number += 1
        if 0 <= number <= 4:
            if msg == f"GET {number}":
                termcolor.cprint("GET", 'green')
                gene = str(s)
                print(gene)
                newflag = str(s)
                rs.send(newflag.encode())
                print(f"\nWaiting for clients...\n")












    rs.close()



    # -- Close the socket
ls.close()

