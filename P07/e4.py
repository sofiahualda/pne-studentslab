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

if gene_name in genes:
    id = genes[gene_name]
    server = 'rest.ensembl.org'
    resource = f'/sequence/id/{id}'
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
    print()
    if response.status == HTTPStatus.OK:
        data_str = response.read().decode("utf-8")
        data = json.loads(data_str)
        f"{termcolor.cprint("Gene: ", "green", end=gene_name)}"
        f"{termcolor.cprint("\nDescription: ", "green", end=data['desc'])}"
        print()
        s = str(data['seq'])
        GENE = Seq(s)
        total_len = GENE.len()
        termcolor.cprint("Total length: ", 'green', end=str(total_len))
        a_a = termcolor.cprint("\nA: ", 'blue', end=str(f"{GENE.count_base('A')} ({((GENE.count_base('A') / total_len) * 100):.1f}%)\n"))
        a_c = termcolor.cprint("C: ", 'blue', end=str(f"{GENE.count_base('C')} ({((GENE.count_base('C') / total_len) * 100):.1f}%)\n"))
        a_g = termcolor.cprint("G: ", 'blue', end=str(f"{GENE.count_base('G')} ({((GENE.count_base('G') / total_len) * 100):.1f}%)\n"))
        a_t = termcolor.cprint("T: ", 'blue', end=str(f"{GENE.count_base('T')} ({((GENE.count_base('T') / total_len) * 100):.1f}%)\n"))
