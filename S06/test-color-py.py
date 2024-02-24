import termcolor
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
termcolor.cprint("LIST 1: ", 'blue')
termcolor.cprint(f"{print_seqs(seq_list1)}", 'blue')


seq_list2 = generate_seqs("AC", 5)
termcolor.cprint("LIST 2: ", 'green')
termcolor.cprint(f"{print_seqs(seq_list2)}", 'green')






