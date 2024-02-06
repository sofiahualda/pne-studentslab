from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

first_line = file_contents.find("\n")
file_contents1 = file_contents[first_line:]
file_contents1 = file_contents1.replace("\n", "")
print("Body of the U5.txt file: ", file_contents1)

#LA FORMA CORRECTA:
#list_contents = file_contents.split("\n")
#for i in range(1, len(list_contents)):
#    print(list_contents[i])
