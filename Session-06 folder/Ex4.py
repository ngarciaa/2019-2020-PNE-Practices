import termcolor
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

def print_seqs(seq_list, color) :
    for seq in seq_list :
        termcolor.cprint(f"Sequence {seq_list.index(seq)} : (length : {seq.len()}) {seq}", color )

def generate_seqs(pattern, number) :
    sequences = []
    for i in range(1, number+1):
        sequences.append(Seq(pattern*i))
    return sequences

#main program
seq_list1 = generate_seqs('A', 3)
seq_list2 = generate_seqs('AC', 5)



termcolor.cprint('List 1 :', 'green')
print_seqs(seq_list1, 'green')

print()
termcolor.cprint('List 2 :', 'blue')
print_seqs(seq_list2, 'blue')