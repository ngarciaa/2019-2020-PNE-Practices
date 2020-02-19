from Seq1 import Seq

print ('-----Exercise 2------')
s1 = Seq ('ACTGA')
s2 = Seq()
s3 = Seq('Invalid Sequence')
bases = ['A', 'C', 'T', 'G']

print (f'\nSequence 1 : Length : {s1.len()} {s1}')
for base in bases:
    print(base + ':', s1.count_base (base), end=" ")

print(f'\nSequence 2 : Length : {s2.len()} {s2}')
for base in bases :
    print(base + ':', s2.count_base(base), end=" ")

print(f'\nSequence 3 : Length : {s3.len()} {s3}')
for base in bases :
    print(base + ':', s3.count_base(base), end=" ")