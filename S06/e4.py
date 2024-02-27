import termcolor
from Seq01 import Seq


def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        s = Seq(pattern * i)
        seq_list.append(s)
    return seq_list


def print_seqs(seq_list, color):
    i = 0
    for list in seq_list:
        termcolor.cprint(f"Sequence:, {i}: (Length: {list.len()}) {seq_list[i]}", color)
        i += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("LIST 1: ", 'blue')
print_seqs(seq_list1, 'blue')


termcolor.cprint("LIST 2: ", 'green')
print_seqs(seq_list2, 'green')






