from Client0 import Client

PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

server_ip = "127.0.0.1"
server_port = 8080

c = Client(server_ip, server_port)
print(c)

print("* Testing PING...")
print(f"{c.talk("PING")}\n")

print("* Testing GET...")
N = 5
for n in range(N):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response}")
print()
# print(f"GET 0: {c.talk("GET 0")}\nGET 1: {c.talk("GET 1")}\nGET 2: {c.talk("GET 2")}\nGET 3: {c.talk("GET 3")}\nGET 4: {c.talk("GET 4")}\n")

print("* Testing INFO...")
print(f"{c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")}\n")

print("* Testing COMP...")
print(f"COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA\n{c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")}\n")

print("* Testing REV...")
print(f"REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA\n{c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")}\n")

print(f"* Testing GENE...")
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in GENES:
    print(f"GENE {gene}")
    response = c.talk(f"GENE {gene}")
    print(response)
    print()
# print(f"GENE U5\n{c.talk("GENE U5")}\n\nGENE ADA\n{c.talk("GENE ADA")}\n\nGENE FRAT1\n{c.talk("GENE FRAT1")}\n\nGENE FXN\n{c.talk("GENE FXN")}\n\nGENE RNU6_269P\n{c.talk("GENE RNU6_269P")}")

print("* Testing MULT...")
print(f"{c.talk("MULT AGAGCGT")}")