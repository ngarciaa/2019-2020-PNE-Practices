import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT =  '/info/ping'
PARAMETERS = '?content-type=application/json'

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

ping = response['ping']

if ping==1 :
    print('PING OK! The database is running')


