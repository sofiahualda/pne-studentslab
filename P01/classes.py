class Seq:
    def __init__(self, strbases=None):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def check_seq(self):
        if self.strbases == None:
            print("Null sequence is created")
            text1 = "NULL"
            return text1
        for i in self.strbases:
            if i == "A" or i == "C" or i == "T" or i == "G":
                print("New sequence is created!")
                return self.strbases
            else:
                print("INVALID sequence!")
                text2 = "ERROR"
                return text2

    def len(self):
        return len(self.strbases)

    def show(self):
        t = self.strbases
        return t

print("--- Exercise 2 | Practice 1 ---")
s1 = Seq("ACTAGT")
s2 = Seq()
print(f"Sequence 1: {s1.check_seq()}\nSequence 2: {s2.check_seq()}")


