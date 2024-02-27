from Seq1 import Seq
print("--- Exercise 7 | Practice 1 ---")
s1 = Seq("AGCAGATAGCTGATCGT")
print(f"Sequence 1 (Length: {s1.len()}): {s1}\nBases: {s1.count()}\nRev: {s1.reverse()}\nComp: {s1.complement()}\n")

s2 = Seq()
print(f"Sequence 2 (Length: {s2.len()}): {s2}\nBases: {s2.count()}\nRev: {s2.reverse()}\nComp: {s2.complement()}\n")


s3 = Seq("uydgbj")
print(f"Sequence 3 (Length: {s3.len()}): {s3}\nBases: {s3.count()}\nRev: {s3.reverse()}\nComp: {s3.complement()}")