from Seq1 import Seq
print("--- Exercise 5 | Practice 1 ---")
s1 = Seq("AGCAGATAGCTGATCGT")
print(f"Sequence 1 (Length: {s1.len()}): {s1.check_seq()}\nA: {s1.count_base('A')} C: {s1.count_base('C')} G: {s1.count_base('G')} T: {s1.count_base('T')}")
s2 = Seq()
print(f"Sequence 2 (Length: {s2.len()}): {s2.check_seq()}\nA: {s2.count_base('A')} C: {s2.count_base('C')} G: {s2.count_base('G')} T: {s2.count_base('T')}")
s3 = Seq("uydgbj")
print(f"Sequence 3 (Length: {s3.len()}): {s3.check_seq()}\nA: {s3.count_base('A')} C: {s3.count_base('C')} G: {s3.count_base('G')} T: {s3.count_base('T')}")

