import socket

IP = "10.3.34.237"
PORT = 8080

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

        print(f"Recived message : {msg}")

        # Step 6 : Send a response message to the client
        response = "Hi! I am a happy server"
        cs.send(response.encode())

        cs.close()


