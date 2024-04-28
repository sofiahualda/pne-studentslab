import http.server
from http import HTTPStatus
import socketserver
import termcolor
import http.client
from pathlib import Path
import jinja2 as j
import json

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        server = 'rest.ensembl.org'
        resource = ''
        params = '?content-type=application/json'
        url = server + resource + params
        print()
        print(f"Server: {server}")
        print(f"Url: {url}")
        conn = http.client.HTTPConnection(server)

        response = conn.getresponse()
        print(f"Response receiced!: {response.status} {response.reason}")
        if response.status == HTTPStatus.OK:
            try:
                conn.request("GET", resource + params)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            termcolor.cprint(self.requestline, 'green')
            if resource == "/":
                contents = Path('html/index.html').read_text()
            if resource == "/listSpecies":
                data_str = response.read().decode("utf-8")
                data = json.loads(data_str)
                dict = data['species']
                number_species = len(dict)
                names_species = dict.keys()
                contents = read_html_file("list.html").render(context={"number": number_species, "limit": str(0), "names": names_species})
                if "limit=" in resource:
                    limit_number = resource.isdigit()
                    contents = read_html_file("list.html").render(context={"number": number_species, "limit": str(limit_number), "names": names_species})
            else:
                contents = Path("html/error.html").read_text()
                self.send_response(404)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
            return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()