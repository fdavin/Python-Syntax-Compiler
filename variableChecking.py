numbers = [chr(i) for i in range(48, 58)]
alfabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + ['_']
asciiAllChars = [chr(i) for i in range(33, 127)]
asciiChars = [char for char in asciiAllChars if char not in numbers and char not in alfabets]

# print(numbers)
# print(alfabets)
# print(asciiChars)

dfa = {0:{},
       1:{},
       2:{}}

for number in numbers:
    dfa[0][number] = 2
    dfa[1][number] = 1
    dfa[2][number] = 2

for asciiChar in asciiChars:
    dfa[0][asciiChar] = 2
    dfa[1][asciiChar] = 2
    dfa[2][asciiChar] = 2

for alfabet in alfabets:
    dfa[0][alfabet] = 1
    dfa[1][alfabet] = 1
    dfa[2][alfabet] = 2

def tokenDFACheck(tokenCheck):
    state = 0
    for char in tokenCheck:
        state = dfa[state][char]
    return state

def checkingNamingVariable(variables):
    for variable in variables:
        if tokenDFACheck(variable) == 2:
            print("Nama variable {} salah".format(variable))
            break