class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence is created!")
    def __str__(self):
        return self.strbases
    def check_seq(self):
        for i in self.strbases:
            if i == "A" or i == "C" or i == "T" or i == "G":
                return self.strbases
            else:
                text = "ERROR"
                return text
    def len(self):
        return len(self.strbases)
    def show(self):
        t = self.strbases
        return t

print("---Exercise 1 | Practice 1 ---")
sequence = Seq("ACTGA")
print(f"Sequence 1: (Length: {Seq.len(sequence)}) {sequence}")




