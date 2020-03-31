import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

Seq_get = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML
        contents = Path('error.html').read_text()
        code = 404

        if verb == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('form-4.html').read_text()
            code = 200

        elif verb == "/ping":
            contents = """
                   <!DOCTYPE html>
                   <html lang = "en">
                   <head>
                   <meta charset = "utf-8" >
                     <title> PING </title >
                   </head >
                   <body style="background-color: pink;">
                   <h2> PING OK!</h2>
                   <p> The SEQ2 server in running... </p>
                   <a href="/">Main page</a>
                   </body>
                   </html>
                   """
        elif verb == "/get":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, value = pairs[0].split("=")
            n = int(value)
            sequence = Seq_get[n]

            # -- Generate the html code
            contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="utf-8">
                        <title> GET </title>
                    </head>
                    <body style="background-color: yellow;">
                    <h2>Sequence number {n}</h2>
                    <p> {sequence} </p>
                    <a href="/">Main page</a>
                    </body>
                    </html>
                    """
            code = 200

        elif verb == "/gene":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, gene = pairs[0].split("=")

            s = Seq()
            s.read_fasta(FOLDER + gene + ".txt")
            Gene = str(s)
            # -- Generate the html code
            contents = f"""
                                   <!DOCTYPE html>
                                   <html lang = "en">
                                   <head>
                                   <meta charset = "utf-8" >
                                     <title> GENE </title >
                                   </head >
                                   <body style="background-color: lightblue;">
                                   <h2> Gene: {gene}</h2>
                                   <textarea readonly rows="20" cols="80"> {Gene} </textarea>
                                <br>
                                   <br>
                                   <a href="/">Main page</a>
                                   </body>
                                   </html>
                                   """
            error_code = 200

        elif verb == "/operation":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, seq = pairs[0].split("=")
            # -- Get the two elements of the operation
            name, oper = pairs[1].split("=")

            # -- Create the sequence
            s = Seq(seq)

            if oper == "comp":
                result = s.complement()
            elif oper == "rev":
                result = s.reverse()
            else:
                length = s.len()
                count_A = s.count_base('A')
                percentaje_A = "{:.1f}".format(100 * count_A / length)
                count_C = s.count_base('C')
                percentaje_C = "{:.1f}".format(100 * count_C / length)
                count_G = s.count_base('G')
                percentaje_G = "{:.1f}".format(100 * count_G / length)
                count_T = s.count_base('T')
                percentaje_T = "{:.1f}".format(100 * count_T / length)

                result = f"""
                        <p>Total length: {length}</p>
                        <p>A: {count_A} ({percentaje_A}%)</p>
                        <p>C: {count_C} ({percentaje_C}%)</p>
                        <p>G: {count_G} ({percentaje_G}%)</p>
                        <p>T: {count_T} ({percentaje_T}%)</p>"""

            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> OPERATION </title >
                                </head >
                                <body style="background-color: lightgreen;">
                                <h2> Sequence </h2>
                                <p>{seq}</p>
                                <h2> Operation: </h2>
                                <p>{oper}</p>
                                <h2> Result: </h2>
                                <p>{result}</p>
                                <br>
                                <br>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            error_code = 200

        # Generating the response message
        self.send_response(code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()