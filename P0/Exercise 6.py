from Seq0 import *

print('---- Exercise 6 ----')

folder = "../Session-04 folder/"
filename = 'U5'
sequence = seq_read_fasta(folder + filename)

print('Gene' + filename + ':')
print('Gene' + (sequence[:19]))
print('Frag :', seq_reverse(sequence[:19]))