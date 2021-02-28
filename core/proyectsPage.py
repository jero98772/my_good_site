#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.webUtils import generatePassword , deletefiles ,minsTotales,hoyminsArr,writetxt,readtxt,readtxtstr,hoyminsStr,isEmpty,yesno,date2int,deleteWithExt,img2asciiart,limitsize,getExt ,setLimit ,setUpdate ,concatenateStrInList
from core.tools.flaskUtils import multrequest ,multrequestStr
from core.tools.cryptotools import enPassowrdHash,enPassowrdStrHex ,cifrarcesar ,descifrarcesar ,chars ,rndkey ,encryptAES ,decryptAES,encryptRsa,decryptRsa,getrndPrime ,isPrime,genprimes ,genKey,encpalabranum,decpalabranum
from core.tools.libWithoutSuport import shortcut
from core.tools.dbInteracion import dbInteracion
app = Flask(__name__)
app.secret_key = str(enPassowrdHash(generatePassword()))
DBPATH = "data/dataBases/"
dbNameCriptoblog = DBPATH + "encblog"
DBNAMEGAS = DBPATH + "gas_db"
TABLEGAS = "gastos"
DATANAMEGAS = ["item","category","thread","price","amount","date"]
class proyects():
	WEBPAGE = "/proyects/"
	@app.route(WEBPAGE)
	def index():
		return render_template("/proyects/index.html")
	@app.route(WEBPAGE+"aircolombia.html")
	def aircolombia():
		return render_template("/proyects/aircolombia/aircolombia.html")
	@app.route(WEBPAGE+"htmlpower.html")
	def htmlpower():
		return render_template("/proyects/htmlpower/mainhtmlpower.html")	
	@app.route(WEBPAGE+"htmlpower/little_recursion.html")
	def little_recursion():
		return render_template("/proyects/htmlpower/little_recursion.html")	
	@app.route(WEBPAGE+"htmlpower/iframe_power.html")
	def iframe_power():
		return render_template("/proyects/htmlpower/iframe_power.html")	
	@app.route(WEBPAGE+"pm25predict.html")
	def pm25predict():
		return render_template('/proyects/pm25predict/pm25predict.html')	
	@app.route(WEBPAGE+"pm25predict/pm25predictUnloquer.html")
	def pm25predictUnloquer():
		from core.proyects.pm25Predict.pm25Predict import genpredsunloquer
		hoy = hoyminsArr()
		ahora = minsTotales(hoy)
		ultimoRegistro = "data/pm25Predict/registros/ultimoRegistroUnloquer"#+".txt"
		nombres = "data/pm25Predict/sensors_names/sensors_unloquer"#+".txt"
		horas = 60*2
		host = "aqa.unloquer.org"
		plazo = readtxt(ultimoRegistro)
		plazo = int(plazo[0]) 
		status = "le fatlta " + str( plazo-ahora )+" minutos para una nueva predccion"
		if horas <= (plazo-ahora):
			db = ["aqa","v80","aqamobile"]
			working = genpredsunloquer(db[0],host) +genpredsunloquer(db[1],host) +genpredsunloquer(db[2],host)
			writetxt(ultimoRegistro,ahora+(horas))
			deletefiles(nombres)
			writetxt(nombres,working)
			status += "predicion disponible en 2 horas "
		else:
			status += "proccima predicion disponible en 2 horas "
		working = eval(readtxtstr(nombres))
		return render_template('/proyects/pm25predict/pm25predictUnloquer.html',names = working,msg = status )	
	@app.route(WEBPAGE+"pm25predict/pm25predictCanairio.html")
	def pm25predictCanairio():
		"""

		in procees

		from core.proyects.pm25Predict.pm25Predict import genpredscanairio
		hoy = hoyminsArr()
		ahora = minsTotales(hoy)
		ultimoRegistro = "data/pm25Predict/registros/ultimoRegistroCanairio"#+".txt"
		nombres = "data/pm25Predict/sensors_names/sensors_canairio"#+".txt"
		horas = 60*2
		plazo = readtxt(ultimoRegistro)
		print(plazo)
		plazo = int(plazo[0]) 
		status = "le fatlta " + str( plazo-ahora )+" minutos para una nueva predccion"
		genpredscanairio("las 'tablas' de las bases de datos de canairio")
		if True:#horas <= (plazo-ahora):
			
			db = []
			working = genpredscanairio(db[0]) +genpredscanairio(db[1]) +genpredscanairio(db[2])
			writetxt(ultimoRegistro,ahora+(horas))
			deletefiles(nombres)
			writetxt(nombres,working)
			status += "predicion disponible en 2 horas "
		else:
			status += "proccima predicion disponible en 2 horas "
		working = eval(readtxtstr(nombres))
		"""
		return render_template('/proyects/pm25predict/pm25predictCanairio.html',names = working,msg = status )	
	@app.route(WEBPAGE+"pandemaths.html",methods=['GET','POST'])
	def pandemaths():
		from core.proyects.PandeMaths.pandemaths import new_simulation ,load_template
		from core.proyects.PandeMaths import pandemaths 
		pandemathsVars = ['total_population','infected_starting','days','daily_rate_interaction','average_rate_duration','probability_of_contagion','recovery_rate','template_set']
		pathAndName ="core/static/reports/"
		pandemaths.reports_path = pathAndName
		deletefiles(pathAndName+"PandeMaths-report/PandeMaths-report")
		if request.method == 'POST':
			pandemathsData = list(map(int,multrequest(pandemathsVars)))
			template = request.form['template']
			if template== "load template":
				simulation_name = "OPEN"
				new_simulation(pandemathsData[0], pandemathsData[1], pandemathsData[2], pandemathsData[3], None, None,None, simulation_name, pandemathsData[0])
			elif template == "new simulation":
				load_template(pandemathsData[0], pandemathsData[1], pandemathsData[2], pandemathsData[3], pandemathsData[0],pandemathsData[7])
		return render_template("proyects/pandemaths/pandemaths.html")
	@app.route(WEBPAGE+"pandemathsout.html",methods=['GET','POST'])
	def pandemathsout():
		pathAndName = "core/static/reports/PandeMaths-report"
		text = ""
		with open(pathAndName+"/PandeMaths-report.txt", "r") as f:
			data = f.readlines()
		return render_template("proyects/pandemaths/out.html",text=data )
	@app.route(WEBPAGE+"DsoonMath.html",methods=['GET','POST'])
	def dsoonmath():
		out = []
		from core.proyects.DsoonMath.DsoonMath import ecuationDS 
		rnd_equation = ecuationDS()
		vals = ["operators","datatypes","quantity"]
		if request.method == 'POST':
			data = list(map(int,multrequest(vals)))
			out = ecuationDS(data[0],data[1],data[2])
		return render_template("proyects/DsoonMath/DsoonMath.html",surpriseEc = rnd_equation, out= out)
	@app.route(WEBPAGE+"criptools.html")
	def criptools():
		return render_template("proyects/criptools/criptools.html") 
	@app.route(WEBPAGE+"criptools/criptoretos.html")
	def criptoretos():
		return render_template("proyects/criptools/criptoretos.html")
	@app.route(WEBPAGE+"criptools/rsa.html",methods=['GET','POST'])
	def criptoolsrsa():
		timeNow = hoyminsStr()
		limit = int(date2int(timeNow))
		msg = ""
		encordecOptions = ["encript,with key","decript,with key","encript,with primes numbers","decript,with primes numbers"]
		data = ["text","n","private","public","prime1","prime2","encordec"]
		num1 , num2 = genprimes(limit)
		newN, publica , privada = genKey(num1 , num2)
		primes = [num1,num2] 
		if request.method == 'POST':
			dataGet = multrequest(data)
			inMsg = dataGet[0]
			n = dataGet[1]
			if dataGet[len(data)-1] == encordecOptions[0]:
				privateKey = dataGet[2]
				msg = encryptRsa(inMsg,privateKey,n)
			elif dataGet[len(data)-1] == encordecOptions[1]:
				publicKey = dataGet[3]
				msg = decryptRsa(inMsg,publicKey,n)
			elif dataGet[len(data)-1] == encordecOptions[2]:
				prime1 = int(dataGet[4])
				prime2 = int(dataGet[5])
				n, publicKey , privateKey = genKey(prime1 , prime2)
				msg = encryptRsa(inMsg,privateKey,n)
			elif dataGet[len(data)-1] == encordecOptions[3]:
				prime1 = int(dataGet[4])
				prime2 = int(dataGet[5])
				n, publicKey , privateKey = genKey(prime1 , prime2)
				msg = decryptRsa(inMsg,publicKey,n)
		return render_template("proyects/criptools/rsa.html" ,out = msg,primes = primes,n = newN , private = privada, public = publica)
	@app.route(WEBPAGE+"criptools/criptoolsencblog.html",methods=['GET','POST'])
	def criptoolsencblog(): 
		dataencblog = ["dataenc","publicmsg","ispublicmsg","pass"]
		num = 33
		cleardata = []
		encblogtable = "encritablog"
		db = dbInteracion(dbNameCriptoblog)
		db.connect(encblogtable)
		dataenc = db.encBlog("dataenc")
		publicmsg = db.encBlog("publicmsg")
		keys = db.encBlog("pass")
		for i,ii,iii in zip(dataenc,publicmsg,keys):
			try:
				decmsg = decryptAES(list(i)[0],list(iii)[0])
			except:
				decmsg = str(list(i)[0])
			cleardata.append([decmsg,list(ii)[0]])
		security = db.numitems("dataenc")
		security = list(security[0])[0]
		num *= security + num
		genkey = enPassowrdStrHex(rndkey()+num)
		key = genkey 
		if request.method == 'POST':
			secret = str(request.form["secret"])
			mensage = str(request.form["mensage"])
			ispublic = str(request.form["ispublic"])
			ispublic = yesno(ispublic)
			key = str(request.form["key"])
			if isEmpty(secret,mensage,ispublic):
				msg = str(encryptAES(secret,key))
				if ispublic :
					if isEmpty(key):
						key = enPassowrdStrHex(genkey)
					else:
						key = enPassowrdStrHex(key)
				else:
					key = ""
				data = [msg,mensage,ispublic,key]
				db.putNewMsgsBlog(dataencblog,data)
		return render_template("proyects/criptools/criptoolsencblog.html",keypass = key ,data = cleardata) 
	@app.route(WEBPAGE+"criptools/hashs.html", methods=['GET','POST'])
	def criptoolshash():
		msg = ""
		if request.method == 'POST':
			sha256 = str(request.form["sha256"])
			msg = enPassowrdStrHex(sha256)
		return render_template("proyects/criptools/hashs.html",returnsha = msg) 
	@app.route(WEBPAGE+"criptools/cesar.html" ,methods=['GET','POST'])
	def cesar():
		mensaje = ""
		key = rndkey()
		charshtml = chars
		if request.method == 'POST':
			option = str(request.form["optioncesar"])
			key = int(request.form["key"])
			cesartext = str(request.form["cesartext"])
			charshtml = str(request.form["chars"])
			if option == "cifrate":
				mensaje   = cifrarcesar(cesartext, key,str( charshtml))
			elif option == "desifrate":
				mensaje  = descifrarcesar(cesartext, key,str( charshtml))
			else:
				mensaje = ""
		return render_template("proyects/criptools/cesar.html",charshtml = charshtml,resulthtml = mensaje,htmlkey=key) 
	@app.route(WEBPAGE+"criptools/criptophone.html",methods=['GET','POST'])
	def criptophone():
		newmsg = ""
		options = ["encode","decode"]
		if request.method == 'POST':
			option = str(request.form["option"])
			message = str(request.form["message"])
			if option == options[0]:
				newmsg = encpalabranum(message)
			else:
				newmsg = decpalabranum(message)
		return render_template("/proyects/criptools/criptophone.html",out = newmsg)
	@app.route(WEBPAGE+"img2asciiart.html",methods=['GET','POST'])
	def img2ascii():
		outfig = ""
		size = 15
		imgdir = "core/static/img/proyects/img2ascii/"
		name = "tmp"
		defaurltFill = "@"
		defaurltNoFill = "._."
		intensity = 255
		replaceValue = 0
		defaultvalues = [defaurltFill,defaurltNoFill,replaceValue,intensity]
		fillvalues = [defaurltFill,defaurltNoFill]
		values = ["fillItem","noFillItem","size","intensity","replaceValue"]
		if request.method == 'POST':
			imgfile = request.files["imgfile"]
			data = multrequest(values)
			ext = getExt(str(imgfile))
			size = int(limitsize(int(data[2]),100))
			defaultvalues = [data[0],data[1],data[4],data[3]]
			fillvalues = [data[0],data[1]]
			fileName = imgdir+name+ext
			imgfile.save(fileName)
			outfig = img2asciiart(fileName,size,data[3] , data[4],fillvalues)
			deleteWithExt(imgdir+name,ext)
		return render_template("proyects/img2asciiart/img2asciiart.html",out = outfig,size = size ,defaultvalues = defaultvalues )
	"""#proyects without my suport#"""
	@app.route(WEBPAGE+"gasinfo.html")
	def gasinfo():
			return render_template("proyects/gas/gasinfo.html")
	@app.route(WEBPAGE+"gas.html", methods = ['GET','POST'])
	def gas():
		priceCol = "price"
		data = []
		db = dbInteracion(DBNAMEGAS)
		timenow = hoyminsStr()
		if not session.get('loged'):
			return render_template('proyects/gas/gas_login.html')	
		else:
			user = session.get('user')
			encpwd = session.get('encpwd')
			db.connect(TABLEGAS+user)
			item_id =  db.getID()
			rows = db.getDataGas()
			keys = len(DATANAMEGAS)*[encpwd]
			pricesum = 0
			decdata =[]
			i = 0
			for row in rows:
				decdata.append([concatenateStrInList(item_id[i])]+list(map(decryptAES,row,keys)))
				pricesum += float(decdata[i][4])*float(decdata[i][5])
				i += 1
			try :
				priceavg = pricesum / len(rows)
			except :
				priceavg = "no data" 
			if request.method == 'POST':
				data = multrequest(DATANAMEGAS)
				data = list(map(encryptAES , data, keys))
				data = list(map(str , data))
				db.addGas(DATANAMEGAS,data)
				return redirect("/proyects/gas.html")
			return render_template("proyects/gas/gas.html",purchases = decdata,now=timenow,sum=pricesum,avg=priceavg)	
	"""
	@app.route(WEBPAGE+'gas/threads.html', methods = ['GET','POST'])
	def gasThreads():
		threadsNames = []
		user = session.get('user')
		encpwd = session.get('encpwd')
		keys = len(DATANAMEGAS)*[encpwd]
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		threads = db.getDistinctColumnGAS("thread")
		threads = list(map(decryptAES,threads,keys))
		for thread in threads:
			if thread not in threadsNames:
				threadsNames.append(thread)
		return render_template("proyects/gas/gas_threads.html" , threads = threadsNames)
	@app.route(WEBPAGE+'gas/filter<string:thread>', methods = ['GET','POST'])
	def gasFilter(thread):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		threads = db.getDistinctWhere(thread)
		pricesum = db.getSum(priceCol)
		priceavg = db.getAvg(priceCol)
		threadName = thread
		return render_template("proyects/gas/thread.html" ,threads = threads , threadName = threadName)
	"""
	@app.route(WEBPAGE+"gas_login.html", methods=['GET', 'POST'])
	def gaslogin():	
		usr = request.form['username']
		pwd = request.form["password"]
		encpwd = enPassowrdStrHex(pwd+usr)
		protectpwd = enPassowrdStrHex(pwd)
		GASLOGINTABLE = "logingastos"
		db = dbInteracion(DBNAMEGAS)
		db.connect(GASLOGINTABLE)
		if db.findUser(usr) and db.findPassword(protectpwd)  :
			session['loged'] = True
			session['user'] = usr
			session['encpwd'] = encpwd
			return redirect("/proyects/gas.html")
		else:
			flash('wrong password!')
		return proyects.gas()
	@app.route(WEBPAGE+'gas/actualisar<string:id>', methods = ['GET','POST'])
	def update_gas(id):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		key = session.get('encpwd')
		keys = len(DATANAMEGAS)*[key]
		if request.method == 'POST':
			data = multrequest(DATANAMEGAS)
			encdata = list(map(encryptAES , data, keys))
			encdata = list(map(str,encdata))
			del key,keys,data
			sentence = setUpdate(DATANAMEGAS,encdata)
			db.updateGas(sentence,id)
			flash(' Updated Successfully')
		return redirect('/proyects/gas.html')
	@app.route(WEBPAGE+'gas/editar<string:id>', methods = ['POST', 'GET'])
	def get_gas(id):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		key = session.get('encpwd')
		keys = len(DATANAMEGAS)*[key]
		rows = db.getDataGasWhere("item_id",id)[0]
		idData = [id]+list(map(decryptAES,rows,keys))
		del key,keys , user , rows
		return render_template('proyects/gas/gas_update.html', purchase = idData )
	@app.route(WEBPAGE+"gas/eliminar/<string:id>", methods = ['GET','POST'])
	def gassdelete(id):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		db.deleteWhere("item_id",id)
		flash('you delete that')
		return redirect('/proyects/gas.html')