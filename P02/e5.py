import os
from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 5


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.64"
PORT = 8081
print(f"Connection to SERVER at {IP}, PORT: {PORT}")
c = Client(IP, PORT)
s = Seq()
s.read_fasta(os.path.join("..", "sequences", "FRAT1" + ".txt"))
msg1 = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."
body = str(s)




















