from Seq1 import Seq
import http.client
import json
from http import HTTPStatus
import termcolor

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}
gene_name = input("Write the gene name: ")

if gene_name in genes.keys():

    server = 'rest.ensembl.org'
    resource = '/sequence/id/ENSG00000207552'
    params = '?content-type=application/json'
    url = server + resource + params

    print()
    print(f"Server: {server}")
    print(f"Url: {url}")

    conn = http.client.HTTPConnection(server)

    try:
        conn.request("GET", resource + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    response = conn.getresponse()
    print(f"Response receiced!: {response.status} {response.reason}")
    if response.status == HTTPStatus.OK:
        data_str = response.read().decode("utf-8")
        data = json.loads(data_str)
        print()
        print(f"{termcolor.cprint("Gene: ", "green", end=gene_name)}")
        print(f"{termcolor.cprint("Description: ", "green", end=data['desc'])}")
        s = str(data['seq'])
        GENE = Seq(s)
        print(f"Total length: {GENE.len()}\n {GENE.info()}\nMost Frequent Base: {GENE.max_base()}")