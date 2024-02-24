from Seq01 import Seq
def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        seq_list.append(pattern * i)
    return seq_list

def print_seqs(seq_list):
    i = 0
    for list in seq_list:
        print(f"Sequence:", i, f"(Length: {len(list)})", f" {seq_list[i]}")
        i += 1


seq_list1 = generate_seqs("A", 3)
print("LIST 1: ")
print_seqs(seq_list1)

seq_list2 = generate_seqs("AC", 5)
print("LIST 2: ")
print_seqs(seq_list2)









