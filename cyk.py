import re

# Regex List
regexList = [r'[A-z0-9]*', r'[0-9]*', r'[A-Za-z_][A-Za-z_0-9]*']

# Maps regex into valid key
regexMap = {
    r'[A-z0-9]*' : ["string"],
    r'[0-9]*' : ["number"],
    r'[A-Za-z_][A-Za-z_0-9]*' : ["variable"],
}

grammar = {}
# Load CNF File
def LoadCNF(rulesPath):
    file = open(rulesPath).read()
    rawRules = file.split('\n')
    for i in range (len(rawRules)-1):
        A = rawRules[i].split(' -> ')[0]
        B = rawRules[i].split(' -> ')[1]
        B = B.replace(" ","")
        C = B.split('|')
        for j in range (len(C)):
            value = grammar.get(C[j])
            if (value == None):
                grammar.update({C[j] : [A]})
            else :
                grammar[C[j]].append(A)

def cyk(tokens):
    n = len(tokens)
    cykTable = [[[] for j in range(i)] for i in range(n,0,-1)]
    # Initialize first row cykTable
    for i in range(n):
        # If key valid
        try:
            cykTable[0][i].extend(grammar[tokens[i]])
        # If key invalid
        except KeyError:
            for pattern in regexList:
                if(re.match(pattern, tokens[i])):
                    for regexType in regexMap[pattern]:
                        try:
                            cykTable[0][i].extend(grammar[regexType])
                        except KeyError:
                            continue 
    # Iterate Bottom Up
    for i in range(1,n):
        for j in range(n-i):
            for k in range(i):
                # Test for combinations
                for prod1 in cykTable[i-k-1][j]:
                    for prod2 in cykTable[k][j+i-k]:
                        try:
                            cykTable[i][j]=grammar[prod1+prod2]
                        except KeyError:
                            continue
    # Check if tokens can be reached from startsymbol
    return ("S" in cykTable[-1][-1])