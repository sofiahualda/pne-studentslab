import os
from Seq1 import Seq
print("\n--- Exercise 9 | Practice 1 ---\n")
s = Seq()
GENE = "U5"
filename = os.path.join("..", "sequences", GENE + ".txt")
try:
    s.read_fasta(filename)
    print(f"Sequence: (Length: {s.len()}) {s}\n\tBases: {s.count()}\n\tRev: {s.reverse()}\n\tComp: {s.complement()}")
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")








