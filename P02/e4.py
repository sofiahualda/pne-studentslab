import os
from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "192.168.0.29"
PORT = 8080
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

c = Client(IP, PORT)

GENES = ["U5", "FRAT1", "ADA"]

for gene in GENES:
    s = Seq()   # s.__str__()
    filename = os.path.join("..", "sequences", gene + ".txt")
    s.read_fasta(filename)
    msg1 = f"Sending {gene} to server..."
    print(f"To server: {msg1}")
    print(f"From server:\n\n{c.talk(msg1)}")

    msg2 = f"{s}"
    print(f"To server: {msg2}")
    print(f"From server:\n\n{c.talk(msg2)}")
