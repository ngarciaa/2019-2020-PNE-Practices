from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "10.3.34.194"
PORT1 = 8081
PORT2 = 8082
folder = "../Session-04 folder/"
filename = folder + 'FRAT1'
s = Seq()
s.read_fasta(filename)

# Fragments
FRAGMENT1 = 'FRAGMENT 1 :'
FRAGMENT2 = 'FRAGMENT 2 :'
FRAGMENT3 = 'FRAGMENT 3 :'
FRAGMENT4 = 'FRAGMENT 4 :'
FRAGMENT5 = 'FRAGMENT 5 :'
FRAGMENT6 = 'FRAGMENT 6 :'
FRAGMENT7 = 'FRAGMENT 7 :'
FRAGMENT8 = 'FRAGMENT 8 :'
FRAGMENT9 = 'FRAGMENT 9 :'
FRAGMENT10 = 'FRAGMENT 10 :'
fragments = [FRAGMENT1, FRAGMENT2, FRAGMENT3, FRAGMENT4, FRAGMENT5, FRAGMENT6, FRAGMENT7, FRAGMENT8, FRAGMENT9, FRAGMENT10]

i = 0
f = 0
while f < len(fragments) :
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

r = 0
while r < len(fragments) :
    if r % 2 == 0 or r == 0 :
        c1.talk(fragments[r])
    else :
        c2.talk(fragments[r])
    r += 1

print ('Gene FRAT1 :', s)
for frag in fragments :
    print (frag)
