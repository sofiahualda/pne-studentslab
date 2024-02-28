import os
from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 4


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.64"
PORT = 8081
c = Client(IP, PORT)
s = Seq()
GENES = ["U5", "FRAT1", "ADA"]
for gene in GENES:
    filename = os.path.join("..", "sequences", gene + ".txt")
    s.read_fasta(filename)
    msg1 = (f"Sending {gene} to server...")
    print(f"To server: {msg1}")
    print(f"From server: {c.talk(msg1)}")

    msg2 = (f"{s}")
    print(f"To server: {msg2}")
    print(f"From server: {c.talk(msg2)}")


