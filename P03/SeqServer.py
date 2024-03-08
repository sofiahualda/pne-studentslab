from Seq1 import Seq
import os
import socket
import termcolor


class Server:
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.bind((IP, PORT))
        ls.listen()

        print("Seq server configured!")
        while True:
            print(f"Waiting for clients...")
            (rs, address) = ls.accept()
            msg = rs.recv(2048).decode("utf-8")
            response = self.what_appears_on_clients(msg)
            send_bytes = str.encode(response)
            rs.send(send_bytes)
            rs.close()
    def what_appears_on_clients(self, msg):
        if msg == "PING":
            print("Ping command!\nOK!")
            return "OK"

        elif msg.startswith("GET"):
            GENES = ["U5", "RNU6_269P", "FXN", "FRAT1", "ADA"]
            number = -1
            for gene in GENES:
                s = Seq(gene)
                s.read_fasta(os.path.join("..", "sequences", gene + ".txt"))
                number += 1
                index = GENES.index(gene)
                if 0 <= number <= 4:
                    if msg == f"GET {index}":
                        termcolor.cprint("GET", 'green')
                        gene = str(s)
                        print(gene)
                        return gene



server = Server()















