from Seq1 import Seq
print("\n--- Exercise 8 | Practice 1 ---\n")
s1 = Seq("AGCAGATAGCTGATCGT")
s2 = Seq()
s3 = Seq("Invalid sequence")

print(f"\nSequence 1 (Length: {s1.len()}): {s1}\n\tBases: {s1.count()}\n\tRev: {s1.reverse()}\n\tComp: {s1.complement()}\n")
print(f"Sequence 2 (Length: {s2.len()}): {s2}\n\tBases: {s2.count()}\n\tRev: {s2.reverse()}\n\tComp: {s2.complement()}\n")
print(f"Sequence 3 (Length: {s3.len()}): {s3}\n\tBases: {s3.count()}\n\tRev: {s3.reverse()}\n\tComp: {s3.complement()}")