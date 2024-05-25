import http.client
import json
from http import HTTPStatus

server = "127.0.0.1"
port = 8080

conn = http.client.HTTPConnection(server, port)

#listSpecies
try:
    conn.request("GET", "/listSpecies?limit=&json=1")
except ConnectionRefusedError:
    print("Connection to the Server failed")
    exit()
response = conn.getresponse()
print(f"{response.status} {response.reason}")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    species = data['name_species']
    for specie in species:
        print(specie)
print()

#karyotype
try:
    conn.request("GET", "/karyotype?species=human&json=1")
except ConnectionRefusedError:
    print("Connection to the Server failed")
    exit()
response = conn.getresponse()
print(f"{response.status} {response.reason}")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    karyotype = data['karyotype']
    for element in karyotype:
        print(element)
print()