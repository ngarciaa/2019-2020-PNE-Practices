from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "10.3.34.194"
PORT = 8081
folder = "../Session-04 folder/"
filename = folder + 'U5'
s = Seq()
s.read_fasta(filename)

c = Client(IP, PORT)

c.debug_talk("Sending U5 Gene to the server")
c.debug_talk(s)