from Client0 import Client

print ('PRACTICE 3 ; EXERCISE 7')

IP = "127.0.0.1"
PORT = 8080

c = Client (IP, PORT)

print('Connections to SERVER at IP:', IP, 'and PORT', PORT)

print('Testing GET...')
c.talk('GET 0')
c.talk('GET 1')
c.talk('GET 2')
c.talk('GET 3')
c.talk('GET 4')

print('Testing INFO...')
