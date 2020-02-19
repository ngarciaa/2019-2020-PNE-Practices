
from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P"

# -- Open and read the file
file_contents = Path(FILENAME).read_text().split("\n")[0]  #split para separarlo en líneas y [0] para coger solo la primera

# -- Print the contents on the console
print(file_contents)