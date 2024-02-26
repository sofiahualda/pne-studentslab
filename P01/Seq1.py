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
        if self.strbases == None:
            return 0
        else:
            return len(self.strbases)


    def show(self):
        t = self.strbases
        return t

    def count_base(self, base):
        self.base = base
        if self.strbases == None or not base in self.strbases:
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        d = {}
        if self.strbases == None:
            return 0
        for base in self.strbases:
            if base == "A" or base == "C" or base == "T" or base == "G":
                d[base] = self.strbases.count(base)
            if not base in self.strbases:
                d[base] = 0
        return d