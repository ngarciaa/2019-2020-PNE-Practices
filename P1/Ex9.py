from Seq1 import Seq

print ('-----Exercise 9------')
folder = "../Session-04 folder/"
filename = folder + "U5"
s = Seq()
s.read_fasta(filename)

print (f'Sequence 1 : Length : {s.len()} {s}')
print('\tBases ;', s.count())
print('\tRev :', s.reverse())
print('\tComp:', s.complement())