import http.client
import json
import termcolor

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

gene = 'MIR633'

SERVER = 'rest.ensembl.org'
ENDPOINT =  '/sequence/id/'
PARAMETERS = GENES[gene]+ '?content-type=application/json'

URL = SERVER + ENDPOINT + PARAMETERS

print(f"Server : {SERVER}")
print(f"URL : {URL}")

#Connect to the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMETERS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

#Read the response
r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode()

response = json.loads(data1)

sequence = response['seq']
description = response['desc']

termcolor.cprint('gene', 'green', end=' ')
print(gene)

termcolor.cprint('description', 'green', end=' ')
print(description)

termcolor.cprint('bases', 'green', end=' ')
print(sequence)




