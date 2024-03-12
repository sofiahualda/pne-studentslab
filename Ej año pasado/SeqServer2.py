from Seq12 import Seq
import os
import socket
import termcolor


class Server:
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            serversocket.listen()
            print("SEQ Server configured!")
            while True:
                # accept connections from outside
                print("\nWaiting for clients...")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                # Send the message from the server
                response = self.what_appears_on_clients(msg)
                send_bytes = str.encode(response)
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    def what_appears_on_clients(self, msg):

        if msg == "PING":
            print("Ping command!\nOK!")
            return "OK"

        elif msg.startswith("GET"):
            GENES = ["U5", "FRAT1", "FXN", "RNU6_269P", "ADA"]
            for gene in GENES:
                index = GENES.index(gene)
                if 0 <= index <= 4:
                    if msg == f"GET {index}":
                        s = Seq()
                        s.read_fasta(os.path.join("..", "sequences", gene + ".txt"))
                        termcolor.cprint("GET", 'green')
                        print(str(s))
                        return str(s)

        elif msg.startswith("INFO"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            total_len = seq.len()
            a_a = f"A: {seq.count_base('A')} ({((seq.count_base('A') / total_len) * 100):.1f}%)"
            a_c = f"C: {seq.count_base('C')} ({((seq.count_base('C') / total_len) * 100):.1f}%)"
            a_g = f"G: {seq.count_base('G')} ({((seq.count_base('G') / total_len) * 100):.1f}%)"
            a_t = f"T: {seq.count_base('T')} ({((seq.count_base('T') / total_len) * 100):.1f}%)"
            print(f"Sequence: {seq}\nTotal length: {total_len}\n{a_a}\n{a_c}\n{a_g}\n{a_t}")
            return f"Sequence: {seq}\nTotal length: {total_len}\n{a_a}\n{a_c}\n{a_g}\n{a_t}"
            # podríamos hacer la función info en la clase Seq
            # gene = msg.split(" ")
            # gene = gene[1]
            # seq = Seq(gene)
            # response = seq.info()

        elif msg.startswith("COMP"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            termcolor.cprint("COMP", 'green')
            print(seq.complement())
            return seq.complement()

        elif msg.startswith("REV"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            termcolor.cprint("REV", 'green')
            print(seq.reverse())
            return seq.reverse()

        elif msg.startswith("GENE"):
            gene = msg.split(" ")
            gene = gene[1]
            GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            if gene in GENES:
                termcolor.cprint("GENE  ", 'green')
                s = Seq()
                s.read_fasta(os.path.join("..", "sequences", gene + ".txt"))
                print(str(s))
                return str(s)

        elif msg.startswith("MULT"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            response = str(seq.multiplication())
            print(response)
            return response


s = Server()