import json
import termcolor
from pathlib import Path


jsonstring = Path("people-3.json").read_text()

person = json.loads(jsonstring)

print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age'])

phoneNumbers = person['phoneNumber']

termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

for i, dictnum in enumerate(phoneNumbers):
    termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    termcolor.cprint("\t- Type: ", 'red', end='')
    print(dictnum['type'])
    termcolor.cprint("\t- Number: ", 'red', end='')
    print(dictnum['number'])
