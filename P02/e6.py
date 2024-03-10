import os
from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT1 = 8080
print(f"Connection to SERVER at {IP}, PORT: {PORT1}")
PORT2 = 8081
print(f"Connection to SERVER at {IP}, PORT: {PORT2}")

c = Client(IP, PORT1)
c2 = Client(IP, PORT2)
s = Seq()
s.read_fasta(os.path.join("..", "sequences", "FRAT1" + ".txt"))
msg1 = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."
c.talk(msg1)
c2.talk(msg1)

body = str(s)
print(f"Gene FRAT1: {body}")

fragments = []
for i in range(0, len(body), 10):
    fragment = body[i:i+10]
    fragments.append(fragment)
    l = 0
    for fragment in fragments:
        l += 1
    if l <= 10:
        if l == 1 or l == 3 or l == 5 or l == 7 or l == 9:
            for_server1 = (f"Fragment {l}: {fragment} ")
            print(f"{for_server1}")
            c.talk(for_server1)
        elif l == 2 or l == 4 or l == 6 or l == 8 or l == 10:
            for_server2 = (f"Fragment {l}: {fragment} ")
            print(f"{for_server2}")
            c2.talk(for_server2)
        else:
            pass