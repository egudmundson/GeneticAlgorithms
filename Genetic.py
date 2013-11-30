import random
from MasterMind import MasterMind

def CrossOver(parent1,parent2):
	Probability = random.random()
	ret = [[],[]]
	if(Probability > .60):
		location= random.randint(0, len(parent1))
		
		for x in range(0,location):
			ret[0].append(parent1[x])
			ret[1].append(parent2[x])
		for x in range(location,len(parent1)):
			ret[0].append(parent2[x])
			ret[1].append(parent1[x])
	else:
		ret = [parent1,parent2]
	return ret

def Mutate(parent1,numberOfColors):
	location = random.randint(0,len(parent1)-1)
	parent1[location] = random.randint(1,numberOfColors)
	return parent1


def Selection(PopulationList,CodeCheck,PopSize,NumberOfColors):
	popSum = 0;
	for x in PopulationList:
		popSum += Fitness(x,CodeCheck)
	sumOfProb = 0
	probList = []
	if(popSum == 0):
		popSum = 1
	for x in PopulationList:
		fitness = Fitness(x,CodeCheck)
		if(fitness == 0):
			fitness = .1
		probability =  fitness/float(popSum)
		probList.append((x,probability))
		sumOfProb += probability
	pop = [];
	while ( len(pop) < PopSize):	
		Selected1=[]
		Selected2 = []
		probability1 = random.random()
		probability2 = random.random()
		for x in probList:
			if( x[1] > probability1):
				Selected1.append(x[0])
			if( x[1] > probability2):
				Selected2.append(x[0])
		if( len(Selected1) == len(Selected2)):
			for x in range(0,len(Selected1)):
				ret =CrossOver(Selected1[x],Selected2[x])
				pop.append(ret[0])
				pop.append(ret[1])
		elif len(Selected1) < len(Selected2):
			if(len(Selected1) == 0):
				for x in range(0,len(Selected2)):
					pop.append(Selected2[x])
			else:	
				for x in range(0,len(Selected1)):
					ret=CrossOver(Selected1[x],Selected2[x])
					pop.append(ret[0])
					pop.append(ret[1])
		else:
			if(len(Selected2) == 0):
				for x in range(0,len(Selected1)):
					pop.append(Selected1[x])
			else:
				for x in range(0,len(Selected2)):
					ret=CrossOver(Selected1[x],Selected2[x])
					pop.append(ret[0])
					pop.append(ret[1])

		for x in range(0,len(pop)):
			if( random.random()< .05):
				if(pop[x] == []):
					pop.remove([])
				pop[x] = Mutate(pop[x],NumberOfColors)
			
	return pop


				
def Fitness(Person,CodeCheck):
	Fit = 0;
	ret = CodeCheck(Person)
	for x in ret:
		if(x == 0):
			Fit+=1
	return Fit
def GenerateStartList(Len,NumberOfColors):
	ret = []
	while(len(ret) < 3):
		current = []
		for x in range(0,Len):
			current.append(random.randint(1,NumberOfColors))
		ret.append(current)
	return ret

StartList = [[1,2,3,4],[1,3,2,4],[4,2,3,4]]
Colors = 4
CodeLen = 4
while(Colors < 20):
	while(CodeLen < 7):
		StartList = GenerateStartList(CodeLen,Colors)
		codeCheck = MasterMind(Colors,CodeLen)
		Generation = 0
		while(1):
			ret = Selection(StartList, codeCheck.CheckCode,100,Colors)
			done= None
			for x in ret:
				value = Fitness(x,codeCheck.CheckCode)
				if(value ==CodeLen):
					done = x
			if(done):
				print "Code is %s"%done
				break;
			else:
				StartList = ret
				Generation+=1
       		print "Found in %d number of Generations with a length of %d and number of Colors = %d "%(Generation,CodeLen,Colors)
       		CodeLen +=1
	Colors +=1
	CodeLen = 4
	
