# -*- coding: utf-8 -*-
#!/usr/bin/env python 

from  math import * 
#math lib is for add trigonometric funtions and others math functions log abslote value etc.. 
import random
from random import randint
# is for load random numbers as opcions
from datetime import datetime
# is for generate random state in  prandom for not repite the same number
import time
#p() is fast debug print i use for see error in a big log of errors 
def rnd(x):
	return randint(0,x)
def p(*args):
	for i in args:
		print("\n",i,"\n")
def typenum(rand= random.randrange(0,20),difcult  = random.randrange(1,3),limit = 9999):
	typenum = 0
	choise = rand
	if difcult == "0":pass # this if you need pas option i use in operator as 0 int for need  and  assign to return nothing for add more easy operators
	elif difcult == 0:
		choise = 0
	elif difcult == 1:
		choise = random.randrange(0,3)
	elif difcult == 2:
		choise = random.randrange(0,6)
	elif difcult == 3:
		choise = random.randrange(0,14)
	elif difcult == 4:
		choise = random.randrange(0,20)
	
	#level
	#0
	if choise == 0:
	#1
		typenum = random.randint(-limit,limit)
	elif choise == 1:
		typenum = round(random.random(),3)
	elif choise == 2:
		typenum = round(random.randint(-limit,limit)*0.01,2)
	#2
	elif choise== 3:
		typenum = bin(random.randint(-limit,limit))
	elif choise== 4:
		typenum = str(random.randint(-limit,limit))+"*x"
	elif choise== 5:
		typenum = complex(random.randint(-limit,limit))
	#3
	elif choise== 6:
		typenum = hex(random.randint(-limit,limit))
	elif choise== 7:
		typenum = oct(random.randint(-limit,limit))
	elif  choise== 8:
		typenum = 3.14159265358979323846#pi

	elif choise== 9:
		typenum = 1.41421356237309504#sqrt(2)

	elif choise== 10 :
		typenum =1.73205080756887729352#sqrt(3)

	elif choise== 11:
		typenum =1.61803398874989484820#phi

	elif choise== 12:
		typenum =2.71828182845904523536#e

	elif choise== 13:
		typenum =2.23606797749978969640#sqrt(5)

	elif choise== 14:
		typenum =1.25992104989487316476 #sqrt(2)**3
	#4	
	elif choise== 15:
		typenum = str(random.randint(-limit,limit))+"*x**"+str(random.randrange(0,10))
	elif choise== 16:
		typenum = str(random.randint(-limit,limit))+"*y**"+str(random.randrange(0,10))
	elif choise== 17:
		typenum = str(random.randint(-limit,limit))+"*z"
	elif choise== 18:
		typenum = str(random.randint(-limit,limit))+"z**"+str(random.randrange(0,10))
	elif choise== 19:
		typenum = str(random.randint(-limit,limit))+"*y"
	return str(typenum) 	
def	basicoperators(rand = random.randrange(0,4)):
	#from higher to lower option the difficulty increases
	choise = rand
	if choise== 0:
		operator="+"
	elif choise== 1:
		operator="-"
	elif choise== 2:
		operator="*"
	elif choise== 3:
		operator="/"
	elif choise== 4:
		operator="%"
	return str(operator)
# reason why return the operator as string because will go through the function eval or be print with a number
def avasedoperators(rand = random.randrange(1,6)):
	choise = rand
	lim =15
	limit = 99
	if choise== 0:
		operator = ""# this is for dont mix basic and anvanseds operators and assign to return nothing for add more easy operators
	elif choise== 1:
		operator= "**(1/2)"#this is other form to represet sqrt root 1 is pow and 2 is the root 
	elif choise== 2:
		operator= "**(2)"#pow 2
	elif choise== 3:
		operator= "**("+str(random.randrange(-lim,lim))+"/"+str(random.randrange(-lim,lim))+")"#genrates roots **(pow,root)
	elif choise== 4:
		operator= "**("+str(random.randrange(-lim,lim))+")"#pow
	elif choise== 5:
		operator= "*("+str(typenum(difcult  =0,limit = 9999))+")"		
	return str(operator)
def mathfunctions(rand = random.randrange(0,2)): 
	choise = rand
	lim = 60 
	limit = 9999
	if choise == 0:
		operator= "log("+str(typenum(difcult  =0,limit = limit))+","+str(str(random.randrange(-lim,lim)))+")"
	elif choise == 1:
		operator="log1p("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 2:
		operator= "fabs("+str(typenum(difcult  =0,limit = limit))+")"
	return str(operator)
def avasedfunctions(rand = random.randrange(0,15)): 
	choise = rand
	lim = 60 
	limit = 9999
	if choise == 0:
		operator= "cos("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 1:
		operator="sin("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 2:
		operator= "tan("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 3:
		operator= "acos("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 4:
		operator= "asin("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 5:
		operator= "atan("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 6:
		operator= "atan2("+str(typenum(difcult  =0,limit = limit))+","+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 7:
		operator= "hypot("+str(typenum(difcult  =0,limit = limit))+","+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 8:
		operator= "degrees("+str(typenum(rand = 2,difcult  ="0",limit = limit))+")"
	elif choise == 9:
		operator= "radians("+str(typenum(rand = 2,difcult  ="0",limit = limit))+")"
	elif choise == 10:
		operator= "cosh("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 11:
		operator= "sinh("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 12:
		operator= "tanh("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 13:
		operator= "acosh("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 14:
		operator= "asinh("+str(typenum(difcult  =0,limit = limit))+")"
	elif choise == 15:
		operator= "atanh("+str(typenum(difcult  =0,limit = limit))+")"

	return str(operator)
def Fandoperators(rand = random.randrange(0,10),difcult  = random.randrange(1,4)):
	operator = "+"
	choise = rand
	choiseEXCLUSIVE = 3
	operatorB = 1
	operatorA = 1
	choise = 0
	operatorFB = 0
	operatorFA = 0
	leveDt = 0
	swicth = True
	if difcult == 1 or  difcult == 0 :
		operatorB = 1
		operatorA = 1
		choise = 0
		operatorFB = 0
		operatorFA = 0
		swicth = True
	elif difcult == 2:
		operatorB = 5
		operatorA = 1
		choise = 0
		operatorFB = 0
		operatorFA = 0
		swicth = True
	elif difcult == 3:
		operatorB = 5
		operatorA = 3
		choise = 1
		operatorFB = 0
		operatorFA = 0
		swicth = True
	elif difcult == 4:
		operatorB = 5
		operatorA = 6
		choise = 1
		operatorFB = 0
		operatorFA = 0
		swicth = True
	elif difcult == 5:
		operatorB = 5
		operatorA = 6
		operatorFB = 3
		operatorFA = 0
		choise = 2
		swicth = True
	elif difcult == 6:
		operatorB = 5
		operatorA = 6
		operatorFB = 3
		choise = 2
		swicth = True
	elif difcult == 7:
		operatorB = 5
		operatorA = 6
		operatorFB = 3
		operatorFA = 3
		choise = 3
		swicth = True

	elif difcult == "simplyfie1" or 8 :
		#for i in range():
		operator = basicoperators(random.randrange(2,4))
		choise = 7
	elif difcult == "simplyfie2" or 9:
		operator = avasedoperators(random.randrange(1,3))+basicoperators(random.randrange(2,4))
		choise = 6
	else:# difcult == 8:
		operatorB = 5
		operatorA = 6
		operatorFB = 3
		operatorFA = 15
		choise = 3
	

	if choise == 0:
		pass
	elif choise == 1:
		operator = basicoperators(random.randrange(0,operatorB))
	elif choise == 2 :	
		operator = avasedoperators(random.randrange(1,operatorA))+basicoperators(random.randrange(0,operatorB))
	elif choise == 3 :	
		operator = avasedoperators(random.randrange(1,operatorA))+basicoperators(random.randrange(0,operatorB))+mathfunctions(random.randrange(0,operatorFB))+basicoperators(random.randrange(0,operatorB))
	elif choise == 4:#"simplyfie1":
		operator = basicoperators(random.randrange(0,operatorB))+avasedfunctions(random.randrange(0,operatorFA))+basicoperators(random.randrange(0,operatorB))+avasedoperators(random.randrange(1,operatorA))+basicoperators(random.randrange(0,operatorB))+mathfunctions(random.randrange(0,operatorFB))+basicoperators(random.randrange(0,operatorB))
	elif choise ==5:#"simplyfie2":
		operator = basicoperators(random.randrange(2,3))
	elif choise ==6:
		operator = avasedoperators(random.randrange(1,2))+basicoperators(random.randrange(2,3))

	return str(operator)

"""
import numpy as np
def arrays(rand = random.randrange(0,6)):
	if choise== 7:
		typenum = np.random.randint(limit, size=(3,3))
#disabled for now for future parts of the project
"""
def quantity(levelop= 2,leveDt=1,limit=9999):


	for level in [levelop,leveDt]:
		if level == 0:
			optionypenums = 0
			rand = 2
		elif level == 1:
			optionypenums = 4
			rand = random.randrange(2,3)
		elif level == 2:
			rand = random.randrange(2,6)
			optionypenums = 6
		else:# level == 3:
			rand = random.randrange(2,8)
			optionypenums =10
	operation = ""
	now = int(datetime.now().strftime('%S'))
	for i in range(rand):
		selctnum = random.randrange(0,10)
		optionypenums = random.randrange(0,10)
		if i == 0:
			operation += typenum(difcult = leveDt,limit=limit)
		else:
			operation += Fandoperators(difcult =levelop)
			operation += typenum(difcult = leveDt,limit=limit)

	return operation
#unknowns = lambda a, b, c: ((-b + ((b * b) - (4 * a * c))**1/2) / (2 * a), (-b - (((b * b) - (4 * a * c)))**(1/2)) / (2 * a))#is cuadraticformula is called for find unknowns in a fromula
def ecuation(levelop= 2,leveDt=1,limit=9999):
	ecu1 = str(quantity(levelop,leveDt,limit))
	ecu2 = str(quantity(levelop,leveDt,limit))
	if "x" in ecu1 or "x" in ecu2 or "y" in ecu1 or "y" in ecu2 or "z" in ecu1 or "z" in ecu2:
		strecuation = ecu1+" = "+ecu2 
		return strecuation
	else:
		return ecu1				
def answertime( expresion ,Vtime):
	for x in range(limit):
		if Vtime == False:
			Vtime = limit*len(str(limit))	
		else:
			try:
				Vtime = Vtime
				
			except :
				Vtime = limit*len(str(limit))
			if not Vtime:
				Vtime = limit*len(str(limit))
	answer = str(eval(expresion))
	time.sleep(Vtime)
	return answer
def answer(expresion):
	try:
		answer = str(eval(expresion))
	except :
		answer = "coming soon"
#coming soon can solove ecuation of frist grade and second grade this is the impresión

	return answer
#============= more  forms for create problems  and practice  =============
def simplyfie(level,limit = 999):
	limit = limit
	null = 0
	operation = ""
	
	if level == 0:
		levelop= "simplyfie1"
		leveDt = 0
		rand = random.randrange(2,3)
		optionypenums = 0
		#difcult = "simplyfie1"
	elif level == 1:

		levelop = "simplyfie2"
		leveDt = 0
		rand = random.randrange(2,5)
		optionypenums = 0
	elif level == 2:
		levelop = "simplyfie2"
		leveDt = 2
		rand = random.randrange(2,7)
		optionypenums = 0
	else:
		print("try low level")
	now = int(datetime.now().strftime('%S'))
	psdop = prandom(valorInicial=now,multiplicador=now+2,mod = 6,veces=26)#26 is num of operators
	listop = psdop.vector()

	psdtynum = prandom(valorInicial=now,multiplicador=now+7,mod = 7,veces=7)#16
	listpsdtnum = psdtynum.vector()

	for i,selctnum,optionypenums in zip(range(rand),listpsdtnum,listop):
		if i == 0:
			operation += typenum(selctnum,difcult = leveDt,limit=limit)
		else:
			operation += Fandoperators(optionypenums,difcult = levelop)
			operation += typenum(selctnum,difcult = leveDt,limit=limit)

	return operation
def simplyfieH():
	return """If you have a numerical result that is a 
	fraction, simplifying means finding an 
	equivalent fraction with a lower numerator and 
	denominator in absolute value than the given fraction.
	http://www.matematicatuya.com/NIVELACION/ALGEBRA/Simplificar/"""
#============= help funtions for user =============
#is for learn with errors
def partexpresion(expresion):
#i use to separe signs ["+","-","*","/","%","**","(1/2)","**(2)"]
	i = 0
	nums = []
	numspos = []
	signspos = []
	signs = []
	expresion = list(expresion)
	knownsigns = ["+","-","*","/","%","**","(1/2)","**(2)","cos","tan","sin","acos","atan","asin","cosh","tanh","sinh","atan2","hypot","degrees","fabs"]
	numbersb10 = [str(b10) for b10 in range(10)]
	for parts in expresion:
		for sign,numberb10 in zip(knownsigns,numbersb10):
			if sign == parts:
				signs.append(sign)
				signspos.append(i)
				
			elif numberb10 == parts:
				nums.append(numberb10)
				numspos.append(i)

		i += 1
	p("numpos"+str(numspos),"num"+str(nums),"signspos"+str(signspos),"signs"+str(signs),expresion)
	#return 

#is for learn with errors

def error(expresion, answer):
	#try:
		answer = eval(answer)
		expresion = eval(expresion)
		S_answer = str(eval(str(answer)))
		S_expresion = str(eval(str(expresion)))
		#partexpresion(str(expresion))
		if S_expresion !=  S_answer:
			signerrorP = answer*1
			signerrorM = answer*-1

			if expresion == signerrorM or signerrorP == expresion:
				teori = """
	you have a error in sign 
	signs sumation
	+ (+) + = +
	- (+) - = -
	- (+) + =  if - > that + num = - or if + > that - num = + 
	+ (+) - =  if - > that + num = - or  if + > that - num = +
	signs multiplication
	+ (*) + = +
	- (*) - = + 
	- (*) + = -
	+ (*) - = - 
	"""
				return teori
			#elif
			return """
			can round with round(answer,float digits to round) 
			"""
		else:
			teori = "dont have corrections"
			return teori
	#except:
		#teori = "you are test not developed levels if you need solution can test lower levels"
		#return teori
def help():
	mesage = """
			fabs = is asbsolute value is a equivalent math operator |x|
			log1p(x) =  natural logarithm of 1+x
			hypot = sqrt(x*x + y*y)
			cos = cos() funtion
			sin = sin() funtion
			tan = tan() funtion
			"""
def setsH():
	mesage =""" set1.union(set2) or set1 | set2 = set1 U set2 , set1 union set2 """
def ecuationDS(operators = rnd(10),datatypes = rnd(5),quantity = 1):
	exercises = []
	for i in range (0,quantity):
		exercises.append(ecuation(operators,datatypes))
	return exercises