import sys
import re
import cyk

# baca file python
# dapat dijalankan dengan menuliskan di terminal
# python main.py "<inputFile.py>"
if len(sys.argv) == 2:
    filePath = str(sys.argv[1])
else:
    filePath = 'tesInput.py'

# read file
file = open(filePath, 'r')
text = file.read()

# tokenized code
tokenized = re.findall(r"\w+(?:'\w+)*|[^\w\s]", text)
result = [x for x in tokenized]

cyk.LoadCNF("cnf.txt")

# CYK
table = cyk.cyk(result)

if (cyk.checkValidity(table, "S")):
    print("Verdict accepted! Compile success!")
else:
    print("Compile error, wrong syntax!")