class Seq:
    def __init__(self, strbases):
        bases = ['A', 'T', 'C','G']
        for i in strbases :
            if i not in bases :
                print ('ERROR!')
                self.strbases = 'INCORRECT seqquence detected'
                return
        self.strbases = strbases


    def __str__ (self) :
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list) :
    for seq in seq_list :
        print(f"Sequence {seq_list.index(seq)} : (length : {seq.len()}) {seq}")

#main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)

