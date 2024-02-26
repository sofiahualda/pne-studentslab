from Seq1 import Seq
print("--- Exercise 7 | Practice 1 ---")
s1 = Seq("AGCAGATAGCTGATCGT")
print(f"Sequence 1 (Length: {s1.len()}): {s1.check_seq()}\nBases: {s1.count()}\nRev: {s1.reverse()}\n")

s2 = Seq()
print(f"Sequence 2 (Length: {s2.len()}): {s2.check_seq()}\nBases: {s2.count()}\nRev: {s2.reverse()}\n")


s3 = Seq("uydgbj")
print(f"Sequence 3 (Length: {s3.len()}): {s3.check_seq()}\nBases: {s3.count()}\nRev: {s3.reverse()}")
