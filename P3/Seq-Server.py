from Seq1 import Seq
import socket
import termcolor


IP = "127.0.0.1"
PORT = 8080

seq_list = [('ACGTAGCA'), ('ATGACAGA'), ('ATGACGAT'), ('TAGACTAG')]

# Step 1 : Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

            count_base = ""
            for base, count in seq_info.count().items() :
                s_base = str(base) + ":" + str(count) + "(" + str(count/seq_info.len()*100) + "%)" + '\n'
                count_base += s_base

            response =('Sequence :'+ str(seq_info) +'\n' + 'Total length :'+ str(seq_info.len())+ '\n' + count_base)

            print(response)

            cs.send(response.encode())

        elif 'COMP' in msg :
            seq_comp = Seq(msg[msg.find(" ")+1:])
            termcolor.cprint('COMP', 'green')
            response = seq_comp.complement() + '\n'
            print (response)

            cs.send(response.encode())

        elif 'REV' in msg :
            seq_rev = Seq(msg[msg.find(" ")+1:])
            termcolor.cprint('REV', 'green')
            response = seq_rev.reverse() + '\n'
            print (response)

            cs.send(response.encode())

        elif 'GENE' in msg :
            gene = str(msg[msg.find(" ") + 1:])
            folder = "../Session-04 folder/"
            n = Seq()
            n.read_fasta(folder + gene)
            response = str(n) + '\n'
            print(response)

            cs.send(response.encode())


        cs.close()