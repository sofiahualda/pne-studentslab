from Seq01 import Seq

def print_seqs(seq_list):
    i = 0
    for list in seq_list:
        print(f"Sequence: ", i)
        print(f"Length: {Seq.len(list)}")
        print(f"Indexes: {Seq.show(list)}\n")
        i += 1


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)




