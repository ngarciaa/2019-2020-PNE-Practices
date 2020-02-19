class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases='NULL'):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == 'NULL' :
            print ('Null sequence created')
            self.strbases = 'NULL'
            self.length = 0
        elif strbases == 'Invalid Sequence' :
            print('INVALID seq')
            self.strbases = 'ERROR'
            self.length = 0
        else :
            self.strbases = strbases
            print("New sequence created!")
            self.length = len(self.strbases)

    def __str__ (self) :
        return self.strbases

    def len(self):
        return self.length

    def count_base(self, base):
        return self.strbases.count(base)

    def seq_count(self):
        bases = ['A', 'C', 'T', 'G']
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dicti = dict(zip(bases, count_bases))
        return dicti

    def seq_reverse(self):
        return self[::-1]