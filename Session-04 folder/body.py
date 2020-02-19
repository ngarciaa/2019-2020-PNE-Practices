
from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5"

# -- Open and read the file
file_contents = Path(FILENAME).read_text().split('\n')[1:]


# -- Print the contents on the console
print ("\n".join(file_contents))