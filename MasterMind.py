import random

class MasterMind():
	def __init__(self,NumberOfColors,LenOfCode):
		self.numberOfColors = NumberOfColors
		self.lenOfCode = LenOfCode
		self.code =[]
		for x in range(0,self.lenOfCode):
			self.code.append(random.randint(1,self.numberOfColors))
	def __str__(self):
		ret= 'Code is '
		for x in range(0,self.lenOfCode):
			ret += str(self.code[x]) +" "
		return ret
	def CheckCode(self,Code):
		'''This will check the code and the items that are correct I t will return as 0'''
		ret = []
		if(len(Code) != self.lenOfCode):
			ret = None
		for x in range(0,len(Code)):
			if Code[x] == self.code[x]:
				ret.append(0)
			else:
				ret.append(Code[x])
		return ret




if __name__=="__main__":
	Masterminde = MasterMind(4,4)
	print Masterminde
	ret = Masterminde.CheckCode([1,2,3,4])
	print ret
