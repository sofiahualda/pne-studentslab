import os
from Seq1 import Seq
from Client0 import Client
PRACTICE = 2
EXERCISE = 5


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "192.168.0.29"
PORT = 8080
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

c = Client(IP, PORT)
s = Seq()

s.read_fasta(os.path.join("..", "sequences", "FRAT1" + ".txt"))
print(f"Gene FRAT1: {s}")
msg1 = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."
c.talk(msg1)
body = str(s)


fragments = []
for i in range(0, len(body), 10):
    fragment = body[i:i+10]
    fragments.append(fragment)
    l = 0
    for fragment in fragments:
        l += 1
    if l <= 5:
        msg2 = (f"Fragment {l}: {fragment} ")
        print(f"{msg2}")
        c.talk(msg2)
    else:
        pass
























