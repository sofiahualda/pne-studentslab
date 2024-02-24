class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence is created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    def check_seq(self):
        for i in self.strbases:
            if i == "A" or i == "C" or i == "T" or i == "G":
                return self.strbases
            else:
                text = "ERROR"
                return text

    def show(self):
        print(f"Indexes: {self.strbases}\n")


s1 = Seq("ACTGGTACTGAC")
check_s1 = s1.check_seq()
s2 = Seq("hi")
check_s2 = s2.check_seq()
print(f"Sequence 1: {check_s1}\nSequence 2: {check_s2}")


