from Seq1 import Seq

print ('-----Exercise 6------')
s1 = Seq ('ACTGA')
s2 = Seq()
s3 = Seq('Invalid Sequence')
bases = ['A', 'C', 'T', 'G']

print (f'\nSequence 1 : Length : {s1.len()} {s1}')
print(s1.seq_count())

print(f'\nSequence 2 : Length : {s2.len()} {s2}')
print(s2.seq_count())

print(f'\nSequence 3 : Length : {s3.len()} {s3}')
print(s3.seq_count())