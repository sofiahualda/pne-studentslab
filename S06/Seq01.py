def are_bases_ok(strbases):
    ok = True
    for c in strbases:
        if c not in Seq.BASES:
            ok = False
            break
    return ok


class Seq:
    BASES = ['A', 'C', 'G', 'T']
    def __init__(self, strbases):
        if are_bases_ok(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT sequence created")
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)




