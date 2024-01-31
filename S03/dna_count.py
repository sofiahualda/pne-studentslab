sequence = input("Enter a sequence: ").upper()
dict_dna = {}
for i in sequence:
    if i == "A":
        if i not in dict_dna:
            dict_dna["A"] = 1
        else:
            dict_dna["A"] += 1
    elif i == "G":
        if i not in dict_dna:
            dict_dna["G"] = 1
        else:
            dict_dna["G"] += 1
    elif i == "C":
        if i not in dict_dna:
            dict_dna["C"] = 1
        else:
            dict_dna["C"] += 1
    elif i == "T":
        if i not in dict_dna:
            dict_dna["T"] = 1
        else:
            dict_dna["T"] += 1
print("Introduce the sequence: ", sequence)
total_length = len(sequence)
print("Total length: ", total_length)
print(dict_dna)
