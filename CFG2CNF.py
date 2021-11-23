import sys, itertools

left, right = 0, 1

K, V, Productions = [],[],[]
variablesJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z",
"A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "W2", "X2", "Y2", "Z2"]

def createDict(productions, variables, terms):
	result = {}
	for production in productions:
		if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
			result[production[right][0]] = production[left]
	return result

def isUnitary(rule, variables):
	if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
		return True
	else :
		return False

def isSimple(rule):
	if rule[left] in V and rule[right][0] in K and len(rule[right]) == 1:
		return True
	else :
		return False

for nonTerminal in V:
	if nonTerminal in variablesJar:
		variablesJar.remove(nonTerminal)

# Add S0->S rule
def START(productions, variables):
	variables.append('S0')
	return [('S0', [variables[0]])] + productions

# Remove rules containing both terms and variables, like A->Bc, replacing by A->BZ and Z->c
def TERM(productions, variables):
	newProductions = []
	dictionary = createDict(productions, variables, K)
	for production in productions:
		if isSimple(production):
			newProductions.append(production)
		else:
			for term in K:
				for index, value in enumerate(production[right]):
					if term == value and not term in dictionary:
						dictionary[term] = variablesJar.pop()
						V.append(dictionary[term])
						newProductions.append( (dictionary[term], [term]) )
						production[right][index] = dictionary[term]
					elif term == value:
						production[right][index] = dictionary[term]
			newProductions.append( (production[left], production[right]) )
			
	return newProductions

#Eliminate non unitry rules
def BIN(productions, variables):
	result = []
	for production in productions:
		k = len(production[right])
		if k <= 2:
			result.append( production )
		else:
			newVar = variablesJar.pop(0)
			variables.append(newVar+'1')
			result.append( (production[left], [production[right][0]]+[newVar+'1']) )
			i = 1
			for i in range(1, k-2 ):
				var, var2 = newVar+str(i), newVar+str(i+1)
				variables.append(var2)
				result.append( (var, [production[right][i], var2]) )
			result.append( (newVar+str(k-2), production[right][k-2:k]) ) 
	return result
	
def findOutlaws(target, productions):
	outlaws, newproduct = [],[]
	for production in productions:
		if target in production[right] and len(production[right]) == 1:
			outlaws.append(production[left])
		else:
			newproduct.append(production)		
	return outlaws, newproduct

def rewrite(target, production):
	result = []
	positions = [i for i,x in enumerate(production[right]) if x == target]
	for i in range(len(positions)+1):
 		for element in list(itertools.combinations(positions, i)):
 			tadan = [production[right][i] for i in range(len(production[right])) if i not in element]
 			if tadan != []:
 				result.append((production[left], tadan))
	return result

#Delete non terminal rules
def DEL(productions):
	newSet = [] 
	outlaws, productions = findOutlaws('e', productions)
	for outlaw in outlaws:
		for production in productions + [e for e in newSet if e not in productions]:
			# if outlaw is present in the right side of a rule
			if outlaw in production[right]:
				# the rule is rewrited in all combination of it, rewriting "e" rather than outlaw
				newSet = newSet + [e for e in  rewrite(outlaw, production) if e not in newSet]

	#add unchanged rules and return
	return newSet + ([productions[i] for i in range(len(productions)) 
							if productions[i] not in newSet])

def unit_routine(rules, variables):
	unitaries, result = [], []
	for aRule in rules:
		if isUnitary(aRule, variables):
			unitaries.append( (aRule[left], aRule[right][0]) )
		else:
			result.append(aRule)
	for uni in unitaries:
		for rule in rules:
			if uni[right]==rule[left] and uni[left]!=rule[left]:
				result.append( (uni[left],rule[right]) )
	
	return result

def UNIT(productions, variables):
	i = 0
	result = unit_routine(productions, variables)
	tmp = unit_routine(result, variables)
	while result != tmp and i < 1000:
		result = unit_routine(tmp, variables)
		tmp = unit_routine(result, variables)
		i+=1
	return result

global CNF
CNF = {}

def convertToMap (Production):
	for i in range (len(Production)):
		s = ''
		for j in range (len(Productions[i][1])):
			s = s + Productions[i][1][j]
		CNF.update({s : Productions[i][0]})


def cleanAlphabet(expression):
	return expression.replace('  ',' ').split(' ')

def cleanProduction(expression):
	result = []
	#remove spaces and stop on ";"
	rawRulse = expression.replace('\n','').split(';')
	
	for rule in rawRulse:
		# stop every rule on "->" create multiple production if there are more than 1 term on a variable
		leftSide = rule.split(' -> ')[0].replace(' ','')
		rightTerms = rule.split(' -> ')[1].split(' | ')
		for term in rightTerms:
			result.append( (leftSide, term.split(' ')) )
	return result

def loadModel(modelPath):
	file = open(modelPath).read()
	K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
	V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
	P = (file.split("Productions:\n")[1])

	return cleanAlphabet(K), cleanAlphabet(V), cleanProduction(P)

def writeFormat(rules):
	dictionary = {}
	for rule in rules:
		if rule[left] in dictionary:
			dictionary[rule[left]] += ' | '+' '.join(rule[right])
		else:
			dictionary[rule[left]] = ' '.join(rule[right])
	result = ""
	for key in dictionary:
		result += key+" -> "+dictionary[key]+"\n"
	return result

if __name__ == '__main__':
	if len(sys.argv) > 1:
		modelPath = str(sys.argv[1])
	else:
		modelPath = 'cfg.txt'
	
	K, V, Productions = loadModel( modelPath )
	Productions = START(Productions, variables=V)
	Productions = TERM(Productions, variables=V)
	Productions = BIN(Productions, variables=V)
	Productions = DEL(Productions)
	Productions = UNIT(Productions, variables=V)
	convertToMap(Productions)
	print("CNF created to cnf.txt")
	open('cnf.txt', 'w').write(	writeFormat(Productions) )
