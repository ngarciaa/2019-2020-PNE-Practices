
from pathlib import Path

FILENAME = "ADA"

file_contents = Path(FILENAME).read_text().split("\n")[1:]

new_file = "".join(file_contents)

print(len(new_file))