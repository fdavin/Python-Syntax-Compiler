import sys

# baca file python
# dapat dijalankan dengan menuliskan di terminal
# python main.py "<inputFile.py>"
if len(sys.argv) == 2:
    filePath = str(sys.argv[1])
else:
    filePath = 'tesInput.py'

file = open(filePath, 'r')
text = file.read()
print(text)