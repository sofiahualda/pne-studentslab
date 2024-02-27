import os
from Seq1 import Seq
print("\n--- Exercise 9 | Practice 1 ---\n")
filename = os.path.join("..", "sequences", "U5.txt")
s = Seq.read_fasta(filename)
s.read_fasta(filename)

print(f"Sequence: (Length: {Seq.len(s)}) {print(s)}\n\tBases: {s.count()}\n\tRev: {s.reverse()}\n\tComp: {s.complement()}")







