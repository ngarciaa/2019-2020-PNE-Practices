import http.server
import socketserver
import termcolor
import json
import http.client
from Seq1 import *
import pathlib


PORT = 8080
SERVER = 'rest.ensembl.org'

socketserver.TCPServer.allow_reuse_address = True

def read_file(filename) :
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body

def list_species(ENDPOINT) :
    conn = http.client.HTTPConnection(SERVER)
    PARAMETERS = '?content-type=application/json'
    try:
        conn.request("GET", ENDPOINT + PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response = json.loads(data1)['species']
    return response

def karyotype(ENDPOINT, msg) :
    conn = http.client.HTTPConnection(SERVER)
    PARAMETERS = '?content-type=application/json'
    NEW_PARAMETERS = msg + PARAMETERS
    try:
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response = json.loads(data1)['karyotype']

    return response

def chromosome_length(ENDPOINT, msg, chrom):
    conn = http.client.HTTPConnection(SERVER)
    PARAMETERS = '?content-type=application/json'
    NEW_PARAMETERS = msg + '/' + chrom + PARAMETERS
    try:
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response = json.loads(data1)['length']

    return response

def gene_seq(gene):
    conn = http.client.HTTPConnection(SERVER)
    ENDPOINT = '/xrefs/symbol/homo_sapiens/'
    PARAMETERS = '?content-type=application/json'
    NEW_PARAMETERS = gene + PARAMETERS
    try:
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response1 = json.loads(data1)[0]['id']

    return response1

def get_seq (response1):
    conn = http.client.HTTPConnection(SERVER)
    ENDPOINT = "/sequence/id"
    PARAMETERS = '?content-type=application/json'
    NEW_PARAMETERS ='/' + response1 + PARAMETERS
    try :
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response2 = json.loads(data1)['seq']

    return response2

def gene_info(ENDPOINT, gene):
    conn = http.client.HTTPConnection(SERVER)
    PARAMETERS = '?content-type=application/json'
    NEW_PARAMETERS = gene + PARAMETERS
    try:
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response = json.loads(data1)

    return response

def gene_calc(s):
    c = s.count()
    length = s.len()
    list_values = list(c.values())
    list1 = []
    for value in list_values:
        list1.append(f"{value} {round(value/length*100), 2} %")

    list_key = list(c.keys())
    dicti = dict(zip(list_key, list1))

    return dicti

def gene_list(ENDPOINT, chromo, start, end) :
    conn = http.client.HTTPConnection(SERVER)
    PARAMETERS = '?feature=gene;content-type=application/json'
    NEW_PARAMETERS = chromo + ':' + start + '-' + end + PARAMETERS
    try:
        conn.request("GET", ENDPOINT + NEW_PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()
    response = json.loads(data1)
    return response

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        list_resource = self.path.split('?')
        resource = list_resource[0]

        if resource == '/' :
            file = 'index.html'
            error_code = 200
            contents = read_file(file)

        elif resource == '/listSpecies' :
            try :
                pair = self.path.find('=')
                msg = self.path[pair +1:]

                ENDPOINT =  '/info/species'
                response = list_species(ENDPOINT)
                length = len(response)
                count = 0
                contents = f"""
                                              <!DOCTYPE html>
                                              <html lang = "en">
                                              <head>
                                              <meta charset = "utf-8" >
                                              <title> List Species </title >
                                              </head >
                                              <body style="background-color: lightpink;">
                                            """

                contents += f"<h2>The total number of species in the ensemble are {length}</h2>"
                contents += f"<h2>The limit you have selected is : {msg} </h2>"
                contents += f"<h2>The name of the species are : </h2>"

                if msg == "" :

                    for species in response :
                        name = species['display_name']
                        contents += f"<p> {name} </p>"

                else :
                    number = msg
                    while count < int(number):
                        count += 1
                        name = response[count]['display_name']
                        contents += f"<p> {name} </p>"

                contents += f"""
                                        </p>
                                        <a href="http://127.0.0.1:8080/">Main Page </a>
                                      </body>
                                       </html> """
                error_code = 200

            except KeyError :
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/karyotype':
            try :
                pair = self.path.find('=')
                msg = self.path[pair + 1:]
                ENDPOINT = '/info/assembly/'
                response = karyotype(ENDPOINT, msg)
                contents = f"""
                                                                      <!DOCTYPE html>
                                                                      <html lang = "en">
                                                                      <head>
                                                                      <meta charset = "utf-8" >
                                                                      <title> Karyotype </title >
                                                                      </head >
                                                                      <body style="background-color: lightpink;">
                                                                    """
                contents += f"<h2>The names of the crhomosomes of the specie {msg} are : </h2>"

                for chrom in response :
                    contents += f"<p> {chrom}</p>"

                contents += f"""
                                                       </p>
                                                       <a href="http://127.0.0.1:8080/">Main Page </a>
                                                     </body>
                                                   </html> """
                error_code = 200

            except KeyError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/crhomosomeLength' :
            try :
                ENDPOINT = '/info/assembly/'
                separate = self.path.split('&')
                pair = separate[0].find('=')
                msg = separate[0][pair + 1:]
                pair2 = separate[1].find('=')
                chrom = separate[1][pair2 + 1:]
                response = chromosome_length(ENDPOINT, msg, chrom)
                contents = f"""
                                                                                  <!DOCTYPE html>
                                                                                  <html lang = "en">
                                                                                  <head>
                                                                                  <meta charset = "utf-8" >
                                                                                  <title> Chromosome Length </title >
                                                                                  </head >
                                                                                  <body style="background-color: lightpink;">
                                                                                """
                contents += f"<p>The length of the chromosome is : {response} </p>"
                contents += f"""
                                                                   
                                                                   <a href="http://127.0.0.1:8080/">Main Page </a>
                                                                 </body>
                                                               </html> """
                error_code = 200
            except KeyError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/geneSeq':
            try :
                pair = self.path.find('=')
                gene = self.path[pair + 1:]
                response1 = gene_seq(gene)
                response2 = get_seq(response1)
                contents = f"""
                                    <!DOCTYPE html>
                                     <html lang = "en">
                                     <head>
                                     <meta charset = "utf-8" >
                                     <title> Get Sequence</title >
                                     </head >
                                     <body style="background-color: lightpink;">
                                      """

                contents +=f"<p>The sequence of the gene {gene} is {response2} </p>"
                contents += f"""
                                    <a href="http://127.0.0.1:8080/">Main Page </a>
                                    </body>
                                    </html> """
                error_code = 200
            except IndexError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/geneInfo':
            try :
                ENDPOINT = "/lookup/symbol/homo_sapiens/"
                pair = self.path.find('=')
                gene = self.path[pair + 1:]
                response = gene_info(ENDPOINT, gene)
                length = response['end'] - response['start']
                contents = f"""
                                                    <!DOCTYPE html>
                                                     <html lang = "en">
                                                     <head>
                                                     <meta charset = "utf-8" >
                                                     <title> Gene Information</title >
                                                     </head >
                                                     <body style="background-color: lightpink;">
                                                      """
                contents += f"<p>The gene {gene} starts at {response['start']}</p>"
                contents += f"<p>The gene {gene} ends at {response['end']}</p>"
                contents += f"<p>The gene {gene} is in the chromosome {response['seq_region_name']}</p>"
                contents += f"<p>The id of the gene {gene} is {response['id']}</p>"
                contents += f"<p>The length of the gene {gene} is {length}</p>"
                contents += f"""
                                           <a href="http://127.0.0.1:8080/">Main Page </a>
                                           </body>
                                           </html> """
                error_code = 200

            except KeyError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/geneCalc':
            try :
                pair = self.path.find('=')
                gene = self.path[pair + 1:]
                response1 = gene_seq(gene)
                s = get_seq(response1)
                seq = Seq(s)
                response = gene_calc(seq)
                a = list(response.keys())
                b= list(response.values())

                contents = f"""
                               <!DOCTYPE html>
                               <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                <title> Gene Calculations</title >
                                </head >
                                <body style="background-color: lightpink;">
                                """

                contents +=f"<p>The length of the gene {gene} is {seq.len()}</p>"

                for base in response.keys():
                    index = a.index(base)
                    contents += f"<p> Base {a[index]} --> {b[index]}</p>"

                contents += f"""
                                                     <a href="http://127.0.0.1:8080/">Main Page </a>
                                                     </body>
                                                     </html> """
                error_code = 200

            except IndexError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        elif resource == '/geneList':
            try :
                ENDPOINT = "/overlap/region/human/"
                separate = self.path.split('&')
                pair = separate[0].find('=')
                chromo = separate[0][pair + 1:]
                pair2 = separate[1].find('=')
                start = separate[1][pair2 + 1:]
                pair3 = separate[2].find('=')
                end = separate[2][pair3 + 1:]

                response = gene_list(ENDPOINT, chromo, start, end)

                contents = f"""
                                           <!DOCTYPE html>
                                           <html lang = "en">
                                            <head>
                                            <meta charset = "utf-8" >
                                            <title> Gene List</title >
                                            </head >
                                            <body style="background-color: lightpink;">
                                            """
                contents += f"<p>The genes in the chromosome {chromo} in range {start} - {end} are : </p>"
                for gene in response :
                    contents += f"<p>{gene['external_name']}</p>"

                contents += f"""
                                                                        <a href="http://127.0.0.1:8080/">Main Page </a>
                                                                        </body>
                                                                        </html> """
                error_code = 200

            except TypeError:
                file = 'error.html'
                error_code = 404
                contents = read_file(file)

        else :
            file = 'error.html'
            error_code = 404
            contents = read_file(file)

        self.send_response(error_code)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()