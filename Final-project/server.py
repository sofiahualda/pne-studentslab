import http.server
from http import HTTPStatus
import socketserver
import termcolor
import http.client
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import json

port = 8080
html_folder = "html"
enseml_server = "rest.enseml.org"
resource_to_ensembl_request = {
    '/listSpecies': {'resource': "/info/species", 'parameters': "content-type=application/json"}
}

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def server_request(SERVER, URL):
    ok = True
    data = None
    try:
        connection = http.client.HTTPSConnection(SERVER)
        connection.request("GET", URL)
        response = connection.getresponse()
        if response.status == HTTPStatus.OK:
            json_str = response.read().decode()
            data = json.loads(json_str)
    except Exception:
        ok = False
    return ok, data

def handle_error(endpoint, msg):
    dict_with_errors = {
        'endpoint': endpoint,
        'message': msg
    }
    return read_html_file("error.html").render(context=dict_with_errors)

def list_species(endpoint, params):
    request = resource_to_ensembl_request[endpoint]
    URL = f"{request['resource']}?{request['parameters']}"
    ok, data = server_request(enseml_server, URL)
    if not ok:
        limit = None
        if 'limit' in params:
            limit = int(params['limit'][0])
        species = data['species']   # list of dictionaries
        name_species = []           # each specie is a dictionary
        for specie in species[:limit]:
            name_species.append(specie['display_name'])
        context = {
            'number of species': len(species),
            'limit': limit,
            'name_species': name_species
        }
        contents = read_html_file("list_species").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, "Error in communication with the Ensembl server")
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path
        print(f"Endpoint: {endpoint}")
        parameters = parse_qs(parsed_url.query)
        print(f"Parameters: {parameters}")

        code = HTTPStatus.OK
        type_of_content = "text/html"
        contents = ""
        if endpoint == "/":
            contents = read_html_file("index.html").render()
        elif endpoint == "/listSpecies":
            code, contents = list_species(endpoint, parameters)
        elif endpoint == "/karyotype":
            pass
        elif endpoint == "/chromosomeLength":
            pass
        else:
            contents = handle_error(endpoint, "Resource not available")

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', type_of_content)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)

Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:

    print("Serving at PORT", port)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
