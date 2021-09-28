Grammar =  {}
start = ""
states = []
Non_Terminals = []
Terminals = []
table = {}
def Read(filename):
	global Grammar,start,Non_Terminals,Terminals
	data = open(filename,"r").readlines()
	productions = data[:-3]
	start = data[-3].strip()
	Non_Terminals = data[-2].strip().split(",")
	Terminals = data[-1].strip().split(",")
	Grammar = {}
	for prod in productions:
		print(prod.strip())
		RHS,LHS = prod.split("->")
		if RHS is Grammar:
			Grammar[RHS].append(*LHS.strip().split("|"))
		Grammar[RHS] = LHS.strip().split("|")
	return Grammar

def First(NT,output):
	if NT == "":
		output.add("_")
		return NT
	if NT[0] in Terminals:
		if NT[0] == '_':
			First(NT.replace(NT[0],""),output)
		output.add(NT[0])
		return NT
	if NT[0] in Non_Terminals:
		for RHS in Grammar[NT[0]]:
			First(NT.replace(NT[0],RHS),output)
		return NT
	if NT[0] == "_":
		First(NT[1:],output)

def Follow(NT,output):
	if NT == start:
		output.add("$")
	for prod in Grammar:
		for RHS in Grammar[prod]:
			if NT in RHS:
				if RHS[-1] == NT:
					Follow(prod)
				First(RHS[RHS.index(NT)+1:],output)
				if '_' in output:
					output.remove("_")
					Follow(prod,output)

def create_table():
	global table
	for nt in Non_Terminals:
		table[nt] = {}
		for t in Terminals:
			table[nt][t] = ""
		print(table[nt])

Read("read.txt")
create_table()

out = set()

# First("S",out)
# print(out)

Follow("A",out)
print(out)