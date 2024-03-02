from Client0 import Client
PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.64"
PORT = 8081
print(f"Connection to SERVER at {IP}, PORT: {PORT}")
c = Client(IP, PORT)
...
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
...
