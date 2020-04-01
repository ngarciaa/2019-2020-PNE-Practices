import http.client
import json
import termcolor
from Seq1 import Seq

GENES = dict(FRAT1='ENSG00000165879',
             ADA='ENSG00000196839',
             FXN='ENSG00000165060',
             RNU6_269P='ENSG00000212379',
             MIR633='ENSG00000207552',
             TTTY4C='ENSG00000228296',
             RBMY2YP='ENSG00000227633',
             FGFR3='ENSG00000068078',
             KDR='ENSG00000128052',
             ANK2='ENSG00000145362')

for gene in GENES :
    SERVER = 'rest.ensembl.org'
    ENDPOINT =  '/sequence/id/'
    PARAMETERS = '?content-type=application/json'

    REQ = ENDPOINT + GENES[gene] + PARAMETERS
    URL = SERVER + REQ

    print(f"Server : {SERVER}")
    print(f"URL : {URL}")

    #Connect to the server
    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQ)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    #Read the response
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode()

    response = json.loads(data1)

    termcolor.cprint('Gene', 'green', end=' ')
    print(gene)

    termcolor.cprint('Description', 'green', end=' ')
    print(f": {response['desc']}")

    sequence = (response['seq'])
    def sequence_information(bases):
        seq_info = Seq(bases)
        min = 0
        max = ' '

        termcolor.cprint('Total length :', 'green', end='')
        print(seq_info.len())

        for base, count in seq_info.count().items():
            percentage = round(count/seq_info.len()*100, 2)
            termcolor.cprint(f"{base}", 'blue', end=' ')
            print(f"{count} ({percentage}%")

            if min < count :
                min = count
                max = base

        termcolor.cprint('Most frequent base', 'green', end=' ')
        print(max)

    sequence_information(sequence)