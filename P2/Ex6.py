from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "10.3.34.194"
PORT = 8081
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
fragments = [FRAGMENT1, FRAGMENT2, FRAGMENT3, FRAGMENT4, FRAGMENT5]
i = 0
f = 0
while f < 5 :
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

c = Client(IP, PORT)

c.talk(fragments[0])
c.talk(fragments[1])
c.talk(fragments[2])
c.talk(fragments[3])
c.talk(fragments[4])

print ('Gene FRAT1 :', s)
for frag in fragments :
    print (frag)
