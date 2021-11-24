import sys
import re
import cyk
import tokenizationVar as tokVar
import variableChecking as var

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
delete_com = re.sub(r"([^\"]#.*$)", "", text, flags = re.M)
tokenized = re.findall(r"\w+(?:'\w+)*|[^\w\s]", delete_com)
#print(delete_com)
# print(tokenized)

cyk.LoadCNF("cnf.txt")

# CYK
table = cyk.cyk(tokenized)

if (cyk.checkValidity(table, "S")):
    print("Verdict accepted! Compile success!")
else:
    print("Compile error, wrong syntax!")

variables = tokVar.tokenizedVar(text)
var.checkingNamingVariable(variables)
