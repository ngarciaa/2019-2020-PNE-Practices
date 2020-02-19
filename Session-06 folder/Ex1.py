class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        bases = ['A', 'T', 'C','G']
        for i in strbases :
            if i not in bases :
                print ('ERROR!')
                self.strbases = 'INCORRECT seqquence detected'
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__ (self) :
        return self.strbases

    def len(self):
        return len(self.strbases)


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")