from Seq1 import Seq
print(f"\n--- Exercise 5 | Practice 1 ---\n")
s1 = Seq("AGCAGATAGCTGATCGT")
s2 = Seq()
s3 = Seq(f"Invalid sequence")

print(f"\nSequence 1 (Length: {s1.len()}): {s1}\n\tA:{s1.count_base('A')} C:{s1.count_base('C')} G:{s1.count_base('G')} T:{s1.count_base('T')}\n")
print(f"Sequence 2 (Length: {s2.len()}): {s2}\n\tA:{s2.count_base('A')} C:{s2.count_base('C')} G:{s2.count_base('G')} T:{s2.count_base('T')}\n")
print(f"Sequence 3 (Length: {s3.len()}): {s3}\n\tA:{s3.count_base('A')} C:{s3.count_base('C')} G:{s3.count_base('G')} T:{s3.count_base('T')}")

"""
seq_list = [Seq(), Seq("TATAC"), Seq("Invalid sequence"]
for i, s in enumerate(seq_list):
    print(f"Sequence: {i + 1}: {s}")
    for b in ['A', 'C', 'G', 'T']:
        print(f"\t{b}: s.count_base(b)}", end = '')
    print()
"""

