from Seq1 import Seq
import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

seq_list = [('ACGTAGCA'), ('ATGACAGA'), ('ATGACGAT'), ('TAGACTAG')]

# Step 1 : Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2 : Bind the socket to server's IP and PORT
ls.bind ((IP, PORT))

# Step 3 : Convert into a listening socket
ls.listen()
print('Server is configured !')

while True :
    try :
        # Step 4 : Wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt :
        print('Server is done')
        ls.close()
        exit()
    else :

        # Step 5 : Reciving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        if msg == 'PING':
            termcolor.cprint('PING command!', 'green')
            print ('OK!\n')


            # Step 6 : Send a response message to the client
            response = ('OK!\n')
            cs.send(response.encode())

        elif 'GET' in msg :
            seq_number = int(msg[-1])
            termcolor.cprint('GET', 'green')
            print('\n')

            response = seq_list[seq_number]
            print(response)

            cs.send(response.encode())

        elif 'INFO' in msg :
            seq_info = Seq(msg[msg.find(" "):])
            termcolor.cprint('INFO', 'green')
            response = seq_info.count()
            print ('Sequence :', seq_info)
            print ('Total length :', seq_info.len())
            print (seq_info.count())

            print (response , '\n')

            cs.send(response.encode())

        cs.close()