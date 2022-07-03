#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
import os
import time
import datetime
#import subprocess
from random import randint
months31Days = [True,"feb28",True,False,True,False,True,True,False,True,False,True]
simbols = " !#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~"
#debug functions
def p(*args,space = 5):
	"""fast print helpful in big log  p(str , [jump lines = 5])"""
	for i in args:
		print(space*"\n",i,"\n"*space)
def rnd(x):
	"""fast random number using random lib rnd(x): return random.randint(0,x)"""
	return randint(0,x)
#short functions
def lenDirInt(dirname):
	"""
	lenDirInt(directory), return int
		counts the number of folders and files in a directory """
	return len(os.listdir(dirname))
#functions
def img2NumName(dirname):
	"""
	img2NumName(dirname),return int
	returns the number of directories every 2 directories
	like , folder with 6 elements
	element0 = 0 = img2NumName(<folder with 0 elements>)
	element1 = 0 = img2NumName(<folder with 1 elements>)
	element2 = 1 = img2NumName(<folder with 2 elements>)
	element3 = 1 = img2NumName(<folder with 3 elements>)
	element4 = 2 = img2NumName(<folder with 4 elements>)
	element5 = 2 = img2NumName(<folder with 5 elements>)
	"""
	try:
		lendir = lenDirInt(dirname)
		if lendir % 2 == 0:
			return lendir/2
		else :
			return (lendir-1)/2
	except:
		lendir = 0
	return lendir
#useful functions
def mayor(num1,num2):
	"""return higher number , of 2 numbers, mayor(num1,num2)"""
	if num1>num2:
		return num1
	else:
		return num2
def menor(num1,num2):
	"""return least number , of 2 numbers, menor(num1,num2)"""
	if num1<num2:
		return num1
	else:
		return num2
def mismaContraseña(password1,password2):
	"""mismaContraseña(password1,password2) return bool
		if are same password of arg 1 and arg 2 , return True if are diferent return False"""
	if password1 == password2:
		return True
	else:
		return False
def minCaracteresPass(password,cantidad):
	"""minCaracteresPass(password,cantidad); return bool
	 is to see if a password meets minimum characters  return True else False """
	if len(password) > cantidad:
		return True
	else:
		return False
def contraseñaSegura(password):
	"""
	contraseñaSegura(str), return True if str have numbers ,strings and symbols else return False
	"""
	haynumeros = False
	hayletras = False
	haysimbolos = False
	numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in password:
		try:
			if i in numeros:
				haynumeros = True
			elif i in letras:
				hayletras = True
			else:
				if type(int(i)) == type(0):
					haynumeros = True
				elif type(str(i)) == type(""):
					hayletras = True				
		except:
			haysimbolos = True
	if haysimbolos and hayletras and haynumeros:
		return True
	else:
		return False
def camposVacios(userName,password1,password2,email,date):
	"""camposVacios(userName,password1,password2,email,date) ,return bool ,if args = "" """
	if userName == "" and password1 == "" and password2 == "" and email == "" and date == "":
		return False
	else:
		return True
def campoVacio(text):
	"""campoVacio(text), return True if text = '' else False"""
	if text == "":
		return True
	else: 
		return False
def esCorreo(email):
	"""esCorreo(string) ,return True if string have '.' and '@'"""
	if "@" in email and "." in email:
		return True
	else:
		return False
def generatePassword():
	"""generatePassword(),return srtring
	generate random string 
	"""
	genPassowrd = ""
	for i in range(0,16):
		if len(genPassowrd) >= 16 and len(genPassowrd)-len(hexStr) <= 16:
			num = rnd.randint(0,9999)
			if 32 > num >126:
				char = chr(num)
				genPassowrd += char
			else:
				hexStr = str(hex(hexStr))
				genPassowrd += hexStr
		else:
			break
	return genPassowrd
def fechaStr2Arr(fecha):
	"""
	fechaStr2Arr(<date as string>) , return date as array
	convert date to array
	"""
	fechaArr = []
	tmp = ""
	for i in str(fecha):
		if i == "," or i == "-" or i == ":" or i =="/":
			fechaArr.append(tmp)
			tmp = ""
		else :
			tmp += i
	else: 
		fechaArr.append(tmp)
	return fechaArr
def hay29feb(año):
	"""
	hay29feb(Yeard) 
	if that yeard have 29 of February,return True"""
	if año % 4 == 0:
		feb29Booll  = True
	else :
		feb29Booll  = False
	return feb29Booll
def dias29feb(años):
	"""
	dias29feb(yeard), return yeard // 4
		to add up the years with February 29
	"""
	diasX29feb = años // 4
	return  diasX29feb 
def dias2mes(dias):
	"""
	dias2mes(<numbers of days>):return months 
		how many days in a number of months
	"""
	meses = 0
	i = 0
	while mes >= i :
		mesI = i%12
		if months31Days[30+mesI] == 31:
			meses += 1
		elif months31Days[30-2] == "feb28":
			meses += 1
		else:
			meses += 1
		i+=1
	return meses
def meses2Dias(mes):
	"""
	meses2Dias(months): return days
		quantity days have that month 31,30,28...29  
	"""
	dias = 0
	i = 0
	while mes >= i :
		mesI = i%12
		if months31Days[mesI]:
			dias += 31
		elif months31Days[mesI] == "feb28":
			dias += 28
		else:
			dias += 30
		i+=1
	return dias
def hoyArr():
	"""
	return date as array
	"""
	hoy = fechaStr2Arr(str(datetime.datetime.today().strftime('%Y-%m-%d')))
	return hoy
def hoyStr():
	"""
	return date as string
	"""
	hoy = str(datetime.datetime.today().strftime('%Y-%m-%d'))
	return hoy
def hoyminsArr():
	"""
	return date and hours and minutes as array
	"""
	hoy = fechaStr2Arr(datetime.datetime.today().strftime("%m/%d/%Y, %H:%M"))
	return hoy
def hoyminsStr():
	"""
	return date and hours and minutes as string
	"""
	hoy = datetime.datetime.today().strftime("%m/%d/%Y, %H:%M")
	return hoy
def ahora():
	"""
	return date and hours and minutes as string
	"""
	return str(datetime.datetime.now())
def diasTotales(dia):
	"""
	diasTotales(<date with days ,months and yeards as array[yeards,months,days]>)
	return total days of date
	"""
	años = int(dia[0])
	añosTotales = años * 365
	meses = int(dia[1])
	dias = int(dia[2])
	diasDeMeses = meses2Dias(meses)
	if años == 0:
		diasTotales =  diasDeMeses + dias
	else:	
		dias += dias29feb(años)
		diasTotales = añosTotales + dias + diasDeMeses 
	return diasTotales
def minsTotales(dia):
	"""
	diasTotales(<date and hours and minutes >)
	return total minute of date	
	"""
	#fechaStr2Arr(dia)
	diasTotalesVar = diasTotales(dia[:3])
	minsTotales = (((diasTotalesVar)*24)+int(dia[3])*60)+int(dia[4]) 
	return minsTotales	
def diferneciaFecha(date,date2):
	"""
	diferneciaFecha(date,date2)
	return difference of days of the 2 dates as int
	"""
	date = diasTotales(date)
	date2 = diasTotales(date2)
	if date2 > date:
		difference= date2 - date 
	else:
		difference = date - date2
	return difference
def Mas1Dia(lastDate):
	"""
	Mas1Dia(<date>)
	return True if date is different to date now
	"""
	newDate = hoyArr()
	difference = diferneciaFecha(lastDate,newDate)
	if difference == 0 :
		return True
	else:
		return False
def deleteFish(path):
	"""
	deleteFish(path) , delete a img of fish ,for data_basecsv
	"""
	if os.path.isfile(path+"fish") :			
		os.remove(path+"fish")
def deleteWithExt(path,ext):
	"""
	deleteWithExt(<file path>,<file extencion>) , delete file with file extencion
	"""
	if os.path.isfile(path+ext) :			
		os.remove(path+ext)
def deletefiles(path):
	"""
	deletefiles(path) , delete records of pandemaths
	"""
	if os.path.isfile(path+".txt"):
		os.remove(path+".txt")
	if os.path.isfile(path+".json"):
		os.remove(path+".json")
	if os.path.isfile(path+".png") :			
		os.remove(path+".png")
def readtxtline(name):
	"""
	readtxtline(name), return frist line of file as string
	"""
	with open(name, 'r') as file:
		return str(file.readline())
def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
def readtxtstr(name):
	"""
	readtxtstr(name) , return txt content as string
	"""
	content = ""
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content += str(i).replace("\n","")
	return content
def writetxt(name,content,mode="w"):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name+".txt", mode) as file:
		file.write(content)
		file.close()
def writeText(name,content,option = "a"):
	content = str(content)
	with open(name, option) as file:
		file.write(content)
		file.close()
def yesno(msg):
	"""
	yesno(msg) ,if msg == yes return True else return False 
	"""
	if msg.lower() == "yes":
		return True
	else:
		return False
def isEmpty(*args):
	"""
	isEmpty(*args), return True if all variable are filled
	"""
	for i in args:
		if i != "":
			return True  
		else:
			return False
			break
def allReplaceSimbols(txt):
	"""
	allReplaceSimbols(<string>) ,if have any delelte simbol that , return  string as integer
	"""
	for i in simbols:
		if i in txt:
			txt = txt.replace(i,"")
	return int(txt)
def date2int(date):
	"""
	date2int(date) convert date to int
	"""
	date = str(date)
	intdate = date.replace(":","").replace("/","").replace(",","").replace(" ","")
	return int(intdate)
def limitsize(size,limit):
	"""
	limitsize(size,limit) return size if greater than limit return new size  
	"""
	size = int(size)
	if size < int(limit):
		return size
	else:
		return int(size/len(str(size)))
def setLimit(value,limit):
	"""
	setLimit(value,limit) , return value or limit value
	"""
	if value < limit:
		return value
	else:
		return limit
def getExt(filename):
	"""
	getExt(filename) return extecion of file 
	"""
	isPoint = False
	for i in str(filename):
		if i == ".":
			ext = "."
			isPoint = True
		elif isPoint:
			if i == "'":
				break
			ext += i
	return ext
def getName(string,sep="/"):
	return string[len(string)-(string[::-1]).index(sep):] 
def img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
	"""
	img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]) ,return a  matrix img as str
	"""
	import cv2
	from numpy import asarray 
	dataFile = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
	imgresized  = cv2.resize(dataFile , (size, size))
	imgstr = ""
	#imgstr = asarray(imgresized , dtype= str)
	for count in range(len(imgresized)):
		for cont in range(len(imgresized[count]))  :
				if imgresized[count,cont]//intensity == replaceItem:
					#imgstr[count,cont]= items[0]
					imgstr += items[0]
				else:
					#imgstr[count,cont] = items[1]
					imgstr += items[1]
		imgstr += "\n"
	outfig = [imgresized,imgstr]
	return outfig 
def setUpdate(dataname, data):
	"""
	generate update sentece for sqlite3 
	"""
	sentence = dataname[0]+" = "+ '"'+data[0]+'"'
	for i ,ii in zip(dataname[1:] , data[1:]):
		sentence += ','+i+" = "+ '"'+ii+'"'
	return sentence
def concatenateStrInList(arr):
	"""
	concatenates the numbers of a string, the elements of an array : return  integer
	"""
	intAsString = ""
	for i in arr:
		intAsString += i
	return int(intAsString)
def getImg(url,imgname):
	"""
	get image form url 
	"""
	import requests
	imgrequ = requests.get(url).content
	with open(imgname, "wb") as file:
		file.write(imgrequ)
def fresample(data,fs,resample = 4):
	data = data[::resample]
	fs = fs//resample
	return data,fs
def noaaTool(name,imgfolder,doResample=False):
	print(name,imgfolder)
	import scipy.io.wavfile as wav
	import scipy.signal as signal
	import numpy as np
	from PIL import Image
	import matplotlib.pyplot as plt
	fs, data = wav.read(name)
	if doResample:
		fresample(data,fs,resample = 4)
	data_crop = data[20*fs:21*fs]
	analytical_signal = signal.hilbert(data)
	data_am = np.abs(analytical_signal)
	frame_width = int(0.5*fs)
	w, h = frame_width, data_am.shape[0]//frame_width
	image = Image.new('RGB', (w, h))
	px, py = 0, 0
	#fill image
	for p in range(data_am.shape[0]):
		lum = int(data_am[p]//32 - 32)
		if lum < 0: lum = 0
		if lum > 255: lum = 255
		image.putpixel((px, py), (0, lum, 0))
		px += 1
		if px >= w:
			#if (py % 50) == 0:
			#    print(f"Line saved {py} of {h}")
			px = 0
			py += 1
			if py >= h:
				break
	image = image.resize((w, 4*h))
	plt.imshow(image)
	#plt.show()
	filename=getName(name).replace(".wav",".png")
	plt.savefig(imgfolder+filename)
	return (imgfolder+filename).replace("core/static/","")
def blogNames(path,tag = ".html"):
	folderFiles = os.listdir(path)
	files = []
	for i in folderFiles:
		if i[-5:] != tag:
			name =  [i+"__"+ii for ii in os.listdir(path+i)] 
			files += name
		else: 
			files +=  [i]
	return files

def filesInFolders(path,tag = ".html"):
	folderFiles = os.listdir(path)
	files = []
	for i in folderFiles:
		if i[-5:] != tag:
			name =  [i+"/"+ii for ii in os.listdir(path+i)] 
			files += name
		else: 
			files +=  [i]
	return files
def blogsNames(path,tag = ".html"):
	blogs = os.listdir(path)
	names = []
	for i in blogs:
		if i[-5:] == tag:
			names.append(i[:-5])
		else:
			names.append(i)
	return names
def getPrimaryLanguage(languages):
	for language in languages:
		if language[0].isupper():
			return language
			break
def clearName(txt,exludeChars,notavailablenames,limit=0,errorMsg = ["the name have some exlude characters , plese only use numeric and upper or lower case letters","the name exlucde the number of characters, limit is: "]):
	if txt in notavailablenames:
		msg = errorMsg[0]
		okName = False
	if exludeChars != "":
		for i in txt:
			if i in exludeChars:
				msg = errorMsg[0]
				okName = False
				break
			else: 
				msg = ""
				okName = True	
	if len(txt) > limit :
		okName = False
		msg = errorMsg[1]+str(limit)+" of characters"
	return okName ,msg
def createFile(name,content=""):
	content =str(content)
	with open(name, 'x') as file:
		file.write(" ")
		file.close()
def changeName(txt):
	newname = ""
	if txt[-1:] == " ":
		newname = txt[:-1]
	newname.replace(" ","_")
	return newname
def deleteFiles(path,selectedFiles):
	for i in selectedFiles:
		os.remove(path+file)
def moveFiles(path,name,replacechar = "__"):
	topicName = name[:name.index(replacechar)]
	folderFile =  path+topicName+"/"
	numOfFiles = len(os.listdir(folderFile))
	print(numOfFiles)
	if numOfFiles == 1:
		createFile(folderFile[:-1]+".html", readFile(folderFile+topicName))
def deleteAndMove(deletename,path,names,replacechar="__"):
	for file in deletename:
		print(path,file)
		if "__" in file:
			fileName = file.replace("__","/")
			dirName = file[:file.index("__")]
			numOfFiles = len(os.listdir(path+dirName+"/"))
			print(numOfFiles)
			if numOfFiles == 2:os.remove(path+fileName)
			if numOfFiles == 1:os.remove(path+fileName);os.rmdir(path+dirName)			
		else:
			os.remove(path+file)
def upadateAuthor(author,newAuthor,path ):
	newContent = readFile(path).replace(author,newAuthor)
	writetxt(path,newContent,option="w")
def webTranslate(txt,writeIn,translateTo):
	"""
	webTranslate(txt,writeIn,translateTo )
	  - txt			  -text to trasnlate
	  - writeIn		  -in which language is it written
	  - translateTo	  -language to be translated
	rember language prefix
	en -> english
	es -> spanish 
	...
	"""
	from deep_translator import GoogleTranslator 
	translatedTxt = GoogleTranslator(source=writeIn, target=translateTo).translate(txt)
	return translatedTxt
def manageTranslate(writeIn,translateTo):
	try:
		translateTo[translateTo.index(writeIn)] = ""
	except:
		pass 
def doHtmlInit(name,content):
	return f"""
<!DOCTYPE html>
<html lang="en">
	<meta charset="UTF-8"> 
	<head>
		<title>blog {name}</title>
	</head>
	<body>
			<h1>{name}</h1>
			<br>
		<center>
			<hr>
			{content}
		</center>
	</body>
</html>
	"""
def doHtml(txtp,txtq,id,who):
	now = time.ctime()
	return f"""
<div id="{id}">
<h2>{txtp}</h2>
<br>
<table width = "420">
	<tr>
		<td>
			<p>{txtq}</p>
		</td>
	</tr>
</table>
<p>{now},by {who}.</p>
</div>
<hr>
"""
def readFile(name):
	with open(name, 'r') as file:
		content = ""
		for i in file.readlines():
			content += str(i).replace("\n","")
		return content
def readLine(name):
	with open(name, 'r') as file:
		return file.readline()
def readCode(name):
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content += str(i)
		return content

def genTokenFile(filename):
	try :
		if readLine(filename) == "":
			pass
	except:
		writetxt(filename,genToken())
def manyblogs(path):
	return len(os.listdir(path))
def blogsview(path,app):
	blogpath = path[path.index("templates/")+len("templates/"):] 
	blogs = os.listdir(path)
	for blog in blogs:
		@app.route("/"+blogpath+str(blog), endpoint=blog[:-5] )
		def site():
			return render_template(blogpath+blog) 
	return site()
def genBlogPreview(name,path=""):
	txt = f'\n\t@app.route("/blog/{name}")\n\tdef {str(name[:-5]).replace("/","")}():\n\t\treturn render_template("blog/{name}")'
	return txt
def updateBlog(dirs,dataDir):
    newCode = """from flask import Flask, render_template
app = Flask(__name__)
class blogs():"""
    for i in dirs:
        newCode += genBlogPreview(i)
    writeText(dataDir,newCode,"w")
    #tryng to move to emacs is ... a disasters with tabs 
def writeblog(name,content,option = "ab+",replaceTo="<!--addition-->"):
	if content == "":
		initTemplate = "{% extends  'template.html'%}{% block content %}"
		endTemplate = "{% endblock %}"
		content = initTemplate+content+replaceTo+endTemplate
		newContent =  content 
	else:
		newContent = readFile(name).replace(replaceTo,content+replaceTo)
	writeText(name,newContent,option="w")