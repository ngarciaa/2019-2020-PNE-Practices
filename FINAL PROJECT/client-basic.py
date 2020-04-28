import http.client


SERVER = 'localhost'
PORT = 8080
endpoints = ['/', '/listSpecies?limit=2', '/listSpecies?limit=', '/listSpecies?limit=0', '/listSpecies?limit=noelia',
             '/karyotype?specie=pig', '/karyotype?specie=human', '/karyotype?specie=coronavirus',
             '/chromosomeLength?specie=human&chromo=X','/chromosomeLength?specie=human&chromo=z', '/chromosomeLength?specie=coronavirus&chromo=1', '/error']

count = 0

for ENDPOINT in endpoints:
    count += 1
    URL = SERVER + ENDPOINT

    print('* TEST', count ,':\n')
    print('- INPUT: ')
    print(URL, '\n')
    print('- OUTPUT: ')

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method.
    try:
        conn.request("GET", ENDPOINT)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    print(data1, '\n')