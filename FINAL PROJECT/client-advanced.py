import http.client


SERVER = 'localhost'
PORT = 8080
endpoints = ['/',
             '/listSpecies?limit=2', '/listSpecies?limit=', '/listSpecies?limit=0', '/listSpecies?limit=noelia',
             '/listSpecies?limit=2&json=1', '/listSpecies?limit=&json=1', '/listSpecies?limit=noelia&json=1',
             '/karyotype?specie=pig', '/karyotype?specie=human', '/karyotype?specie=coronavirus',
             '/karyotype?specie=coronavirus&json=1','/karyotype?specie=human&json=1', '/karyotype?specie=pig&json=1',
             '/chromosomeLength?specie=human&chromo=X','/chromosomeLength?specie=human&chromo=z', '/chromosomeLength?specie=coronavirus&chromo=1',
             '/chromosomeLength?specie=human&chromo=X&json=1', '/chromosomeLength?specie=human&chromo=z&json=1', '/chromosomeLength?specie=coronavirus&chromo=1&json=1',
             '/geneSeq?gene=FRAT1','/geneSeq?gene=ADA', '/geneSeq?gene=12','/geneSeq?gene=noelia',
             '/geneSeq?gene=FRAT1&json=1','/geneSeq?gene=ADA&json=1',  '/geneSeq?gene=12&json=1', '/geneSeq?gene=noelia&json=1'
             '/geneInfo?gene=FRAT1', '/geneInfo?gene=ADA','/geneInfo?gene=12', '/geneInfo?gene=noelia',
             '/geneInfo?gene=FRAT1&json=1','/geneInfo?gene=ADA&json=1',  '/geneInfo?gene=12&json=1', '/geneInfo?gene=noelia&json=1',
             '/geneCalc?gene=FRAT1','/geneCalc?gene=ADA', '/geneCalc?gene=12', '/geneCalc?gene=noelia',
             '/geneCalc?gene=FRAT1&json=1','/geneCalc?gene=ADA&json=1',  '/geneCalc?gene=12&json=1', '/geneCalc?gene=noelia&json=1',
             '/geneList?chromo=1&start=0&end=30000', '/geneList?chromo=noelia&start=0&end=30000','/geneList?chromo=1&start=0&end=1',
             '/geneList?chromo=1&start=0&end=30000&json=1','/geneList?chromo=noelia&start=0&end=3000&json=1', '/geneList?chromo=1&start=0&end=1&json=1',
             '/error']
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