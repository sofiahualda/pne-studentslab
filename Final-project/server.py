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
ensembl_server = "rest.ensembl.org"
resource_to_ensembl_server = {
    '/listSpecies': {'resource': "/info/species", 'params': "content-type=application/json"},
    '/karyotype': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/chromosomeLength': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/geneSeq': {'resource': "/sequence/id", 'params': "content-type=application/json"},
    '/geneInfo': {'resource': "/overlap/id", 'params': "feature=gene;content-type=application/json"},
    '/geneList': {'resource': "/overlap/region/human", 'params': "content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"}
}


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def request_to_server(SERVER, URL):
    ok = True
    data = None
    try:
        connection = http.client.HTTPConnection(SERVER)
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


def list_species(parameters):
    endpoint = '/listSpecies'
    request = resource_to_ensembl_server[endpoint]
    URL = f"{request['resource']}?{request['params']}"
    ok, data = request_to_server(ensembl_server, URL)
    if ok:
        limit = None
        if 'limit' in parameters:
            limit = int(parameters['limit'][0])
        print(data)
        species = data['species']   # list of dictionaries
        name_species = []           # each specie is a dictionary
        for specie in species[:limit]:
            name_species.append(specie['display_name'])
        context = {
            'number_species': len(species),
            'limit': limit,
            'name_species': name_species
        }
        contents = read_html_file("list_species.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, "The communication with the Ensembl server failed")
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def karyotype(parameters):
    endpoint = '/karyotype'
    request = resource_to_ensembl_server[endpoint]
    specie = parameters['species'][0]
    URL = f"{request['resource']}/{specie}?{request['params']}"
    ok, data = request_to_server(ensembl_server, URL)
    if ok:
        context = {
            'specie': specie,
            'karyotype': data['karyotype']
        }
        contents = read_html_file("karyotype.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, "The communication with the Ensembl server failed")
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def chromosome_length(parameters):
    endpoint = '/chromosomeLength'
    request = resource_to_ensembl_server[endpoint]
    specie = parameters['species'][0]
    chromo_requested = parameters['chromo'][0]
    URL = f"{request['resource']}/{specie}?{request['params']}"
    ok, data = request_to_server(ensembl_server, URL)
    if ok:
        total_chromosomes = data['top_level_region']
        length = None
        for chromosome in total_chromosomes:
            if chromosome['name'] == chromo_requested:
                length = chromosome['length']
                break
        context = {
            'specie': specie,
            'chromosome_requested': chromo_requested,
            'length': length
        }
        contents = read_html_file("chromosome_length.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, "The communication with the Ensembl server failed")
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def obtain_id(gene):
    resource = "/homology/symbol/human/" + gene
    parameters = "content-type=application/json;format=condensed"
    URL = f"{resource}?{parameters}"
    ok, data = request_to_server(ensembl_server, URL)
    id_of_gene = None
    if ok:
        id_of_gene = data['data'][0]['id']
    return id_of_gene


def geneSeq(parameters):
    endpoint = '/geneSeq'
    gene_requested = parameters['gene'][0]
    id_of_gene = obtain_id(gene_requested)
    if id_of_gene is not None:
        request = resource_to_ensembl_server[endpoint]
        URL = f"{request['resource']}/{id_of_gene}?{request['params']}"
        ok, data = request_to_server(ensembl_server, URL)
        if ok:
            resulting_sequence = data['seq']
            context = {
                'gene_requested': gene_requested,
                'resulting_sequence': resulting_sequence
            }
            contents = read_html_file("geneSeq.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, "The communication with the Ensembl server failed")
            code = HTTPStatus.SERVICE_UNAVAILABLE
    else:
        contents = handle_error(endpoint, "The requested gene was not found")
        code = HTTPStatus.NOT_FOUND
    return code, contents

def geneInfo(parameters):
    endpoint = '/geneInfo'
    gene_requested = parameters['gene'][0]
    id_of_gene = obtain_id(gene_requested)
    if id_of_gene is not None:
        request = resource_to_ensembl_server[endpoint]
        URL = f"{request['resource']}/{id_of_gene}?{request['params']}"
        ok, data = request_to_server(ensembl_server, URL)
        if ok:
            data = data[0]
            start = data['start']
            end = data['end']
            length = end - start
            chromosome_name = data['assembly_name']
            context = {
                'gene_requested': gene_requested,
                'start': start,
                'end': end,
                'length': length,
                'chromosome_name': chromosome_name,
                'id_of_gene': id_of_gene
            }
            contents = read_html_file("geneInfo.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, "The communication with the Ensembl server failed")
            code = HTTPStatus.SERVICE_UNAVAILABLE
    else:
        contents = handle_error(endpoint, "The requested gene was not found")
        code = HTTPStatus.NOT_FOUND
    return code, contents

def geneCalc(parameters):
    endpoint = '/geneSeq'
    gene_requested = parameters['gene'][0]
    id_of_gene = obtain_id(gene_requested)
    if id_of_gene is not None:
        request = resource_to_ensembl_server[endpoint]
        URL = f"{request['resource']}/{id_of_gene}?{request['params']}"
        ok, data = request_to_server(ensembl_server, URL)
        if ok:
            resulting_sequence = data['seq']
            total_len = len(resulting_sequence)
            c_a = f"{((resulting_sequence.count('A') / total_len) * 100):.1f}%"
            c_c = f"{((resulting_sequence.count('C') / total_len) * 100):.1f}%"
            c_g = f"{((resulting_sequence.count('G') / total_len) * 100):.1f}%"
            c_t = f"{((resulting_sequence.count('T') / total_len) * 100):.1f}%"
            context = {
                    'gene_requested': gene_requested,
                    'total_length': total_len,
                    'c_a': c_a,
                    'c_g': c_g,
                    'c_c': c_c,
                    'c_t': c_t
                }
            contents = read_html_file("geneCalc.html").render(context=context)
            return contents

def

def geneList(parameters):
    endpoint = '/geneList'
    chromo_requested = parameters['chromo'][0]
    start_requested = parameters['start'][0]
    end_requested = parameters['end'][0]
    request = resource_to_ensembl_server[endpoint]
    URL = f"{request['resource']}/{chromo_requested}:{start_requested}-{end_requested}?{request['params']}"
    ok, data = request_to_server(ensembl_server, URL)
    if ok:
        data = data[0]
        for dict in data:
            if dict['end'] == end_requested and dict['start'] == start_requested:
                id_of_gene = dict['id']
    pass




socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path
        print(f"Endpoint: {endpoint}")
        parameters = parse_qs(parsed_url.query)
        print(f"Parameters: {parameters}")

        code = HTTPStatus.OK
        type_of_content = "text/html"
        if endpoint == "/":
            contents = read_html_file("index.html").render()
        elif endpoint == "/listSpecies":
            code, contents = list_species(parameters)
        elif endpoint == "/karyotype":
            code, contents = karyotype(parameters)
        elif endpoint == "/chromosomeLength":
            code, contents = chromosome_length(parameters)
        elif endpoint == "/geneSeq":
            code,contents = geneSeq(parameters)
        elif endpoint == "/geneInfo":
            code, contents = geneInfo(parameters)
        elif endpoint == "/geneCalc":
            contents = geneCalc(parameters)
        elif endpoint == "/geneList":
            code, contents = geneList(parameters)
        else:
            contents = handle_error(endpoint, "Resource not available")
            code = HTTPStatus.NOT_FOUND

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', type_of_content)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)

with socketserver.TCPServer(("", port), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
