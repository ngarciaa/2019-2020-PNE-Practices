from Seq0 import *
print ('----Exercise 8----')

folder = "../Session-04 folder/"
bases = ['A','C', 'T', 'G']
genes = ['U5', 'ADA' , 'FRAT1', 'FXN', 'RNU6_269P']

for file in genes :
    sequence = seq_read_fasta(folder + file)
    dict_bases = seq_count(sequence)
    min_value = 0
    greater_number_base = ''
    for base, value in dict_bases.items() :
        while value > min_value:
            min_value = value
            greater_number_base = base
    print('Gene', file, ':most frequent base :', greater_number_base)