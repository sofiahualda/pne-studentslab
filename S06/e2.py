from Seq01 import Seq

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

i = 0
for list in seq_list:
    print(f"Sequence {i} (Length: {list.len()}) {list}")  #para poner la posicion del objeto en la lista tambien podriamos poner seq_list.index(list)
    i += 1







