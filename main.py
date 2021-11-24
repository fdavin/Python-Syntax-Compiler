import sys
import re
import cyk
import tokenizationVar as tokVar
import variableChecking as var

# Baca file python
# dapat dijalankan dengan menuliskan di terminal
# python main.py "<inputFile.py>"
# Jika tidak ada inputFile, maka program berjalan sesuai default
# dan melakukan kompilasi tesInput.py
if len(sys.argv) == 2:
    filePath = str(sys.argv[1])
else:
    filePath = 'tesInput.py'

file = open(filePath, 'r')
text = file.read()

# Tokenisasi kode input
delete_com = re.sub(r"([^\"]#.*$)", "", text, flags = re.M)
tokenized = re.findall(r"\w+(?:'\w+)*|[^\w\s]", delete_com)

# Kompilasi sintaks menggunakan CYK
cyk.LoadCNF("cnf.txt")
table = cyk.cyk(tokenized)
if (table):
    print("Kompilasi sukses! Semua sintaks sudah benar.")
else:
    print("Kompilasi gagal... Terdapat sintaks yang belum benar.")

# Cek validitas variabel menggunakan DFA
variables = tokVar.tokenizedVar(text)
var.checkingNamingVariable(variables)