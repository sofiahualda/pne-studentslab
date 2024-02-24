class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence is created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    def show(self):
        print(f"Indexes: {self.strbases}\n")




class Gene:
    def __init__(self, strbases, name = ""):
        super().__init__(strbases)
        self.name = name
        print("New gene created!")

    def __str__(self):
        return self.name + "-" + self.strbases