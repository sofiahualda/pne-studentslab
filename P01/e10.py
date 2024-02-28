import os
from Seq1 import Seq
print("\n--- Exercise 10 | Practice 1 ---\n")

list_seq = ['U5','ADA', 'FRAT1', 'FXN', 'RNU6_269P']
for list in list_seq:
    filename = os.path.join("..", "sequences", list + ".txt")
    try:
        s = Seq()
        s.read_fasta(filename)
        print(f"Gene {list}: Most frequent base: {s.max_base()}\n")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")