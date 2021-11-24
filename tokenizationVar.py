import sys
import re

if len(sys.argv) == 2:
    filePath = str(sys.argv[1])
else:
    filePath = 'tesInputVar.py'
file = open(filePath, 'r')
text = file.read()

def tokenizedVar(text):
    # pengambilan variable dari file input
    delete_com = re.sub(r"([^\"]#.*$)", "", text, flags = re.M)
    lines = re.split(r'[\n\r]+', delete_com)
    operator = ['+', '-', '*', '/']
    keywords = ['if', 'elif', 'while']
    variables = []

    for line in lines:
        tokens = re.findall(r"[\w']+|[^\w\s']", line)
        if '=' in tokens:
            idxEqual = tokens.index('=')
            tempVar = ""
            for token in tokens:
                if token == '=' or tokens[idxEqual - 1] in operator or token in keywords:
                    break
                tempVar += token
            variables.append(tempVar)
        elif 'def' in tokens:
            tempVar = ""
            i = 1
            while(tokens[i] != '('):
                tempVar += tokens[i]
                i += 1
            variables.append(tempVar)
        elif 'class' in tokens:
            tempVar = ""
            i = 1
            while(tokens[i] != ':'):
                tempVar += tokens[i]
                i += 1
            variables.append(tempVar)

    variables = [var for var in variables if var != ""]
    # variabel berisi assign variabel biasa (eg. a = 5), nama class, nama fungsi
    # belum dapat memuat variabel operasi seperti a += 5, nama parameter fungsi
    return variables
