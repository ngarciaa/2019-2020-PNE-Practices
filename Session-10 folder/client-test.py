from Client0 import Client
import termcolor

IP = "10.3.34.139"
PORT = 8082

c = Client(IP, PORT)

for i in range(5):
    print('To Server: ', end="")
    termcolor.cprint(f"Message {i}", 'blue')
    print('From Server: ', end="")
    termcolor.cprint(c.debug_talk(f"ECHO: Message {i}"))