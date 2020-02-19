class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__ (self) :
        return self.strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    pass

# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
g = Gene("ACCTG")

print(f"Sequence 1 : {s1}")
print(f"Sequence 2 : {s2}")
print(f"Sequence G : {g}")
l1 = s1.len()
print(f"The len of the sequence 1 is {l1}")
print(f"The len of the sequence 2 is {s2.len()}")
print(f"The len of the sequence G is {g.len()}")