from Seq1 import Seq

print ('-----Exercise 8------')
s1 = Seq ('ACTGA')
s2 = Seq()
s3 = Seq('Invalid Sequence')
bases = ['A', 'C', 'T', 'G']

print (f'Sequence 1 : Length : {s1.len()} {s1}')
print('\tBases ;', s1.count())
print('\tRev :', s1.reverse())
print('\tComp:', s1.complement())


print(f'\nSequence 2 : Length : {s2.len()} {s2}')
print('\tBases ;', s2.count())
print('\tRev :', s2.reverse())
print('\tComp:', s2.complement())


print(f'\nSequence 3 : Length : {s3.len()} {s3}')
print('\tBases ;', s3.count())
print('\tRev :', s3.reverse())
print('\tComp:', s3.complement())
