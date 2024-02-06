from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")
first_line = file_contents[0]
print(first_line)
