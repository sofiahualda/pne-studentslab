from pathlib import Path
def are_bases_ok(strbases):
    ok = True
    for c in strbases:
        if c not in Seq.BASES:
            ok = False
            break
    return ok


class Seq:
    BASES = ['A', 'C', 'G', 'T']
    def __init__(self, strbases = None):
        if strbases is None or len(strbases) == 0:     # con == no
            self.strbases = "NULL"
            print("NULL sequence created")
        elif are_bases_ok(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == None:
            return 0
        else:
            for i in self.strbases:
                if i == "A" or i == "C" or i == "T" or i == "G":
                    return len(self.strbases)
                else:
                    return 0

    def count_base(self, base):
        self.base = base
        if self.strbases == None or base not in self.strbases:
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        d = {'A': "", 'C': "", 'G': "", 'T': ""}
        for key in d:
            if self.strbases == None:
                return 0
            if key == "A" or key == "C" or key == "T" or key == "G":
                d[key] = self.strbases.count(key)
            if not key in self.strbases:
                d[key] = 0
        return d


    def reverse(self):
        if self.strbases == None:
            return "NULL"
        else:
            for i in self.strbases:
                if i == "A" or i == "C" or i == "T" or i == "G":
                    seq_n = self.strbases[:len(self.strbases)]
                    return seq_n[::-1]
                else:
                    return "ERROR"

    def complement(self):
        complement = ""
        if self.strbases == None:
            return "NULL"
        else:
            for base in self.strbases:
                if base == "A":
                    complement += "T"
                elif base == "G":
                    complement += "C"
                elif base == "C":
                    complement += "G"
                elif base == "T":
                    complement += "A"
                else:
                    return "ERROR"
        return complement

    def read_fasta(self, filename):
        self.filename = filename
        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]
        dna_sequence = ""
        for line in body:
            dna_sequence += line
        self.strbases = dna_sequence

    def max_base(self):
        bases_list = ['A', 'C', 'G', 'T']
        bases_d = {}
        for b in bases_list:
            bases_d[b] = self.count_base(b)
        max_base = max(bases_d, key=bases_d.get)
        return max_base

    def info(self):
        seq = f"Sequence: {self.strbases}\n"
        seq += f"Total length: {self.len()}\n"
        for base, count in self.count().items():               # base = key; count = value; en cada vuelta devuelve una pareja, pero no porque en el mismo orden
            if self.len() != 0:
                percentage = (count * 100) / self.len()        # diccionarios: no tienen un orden predefinido; las listas si
            else:
                percentage = 0
            seq += f"{base}: {count}\n ({percentage} %"
        return seq
