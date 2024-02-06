from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
list_contents.pop(0) # removes header

#La siguiente sentencia utiliza la funcion join de str, que un en un string todos los elementos de una tupla
print(len(''.join(list_contents)))

#Another option
index = file_contents.find("\n") #find the first ºn, that separated the header from the body
file_contents = (file_contents[index:]).replace("\n", "") #replace all \n from the header on
print(len(file_contents))

