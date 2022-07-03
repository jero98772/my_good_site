#!/usr/bin/env python
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.webUtils import generatePassword,readtxtline,readLine,blogNames,filesInFolders,updateBlog,writetxt,writeText,blogNames,blogsNames,clearName,writeblog,doHtml,deleteAndMove
from core.tools.cryptotools import enPassowrdHash,genToken
from core.tools.flaskUtils import joinWebpage ,joinWebpageNoaa,joinWebpageGas,joinWebpageDataBase_csv,distributedWebWithIframe
from core.tools.teleUtils import webIsOniline
from .wwwofPage import wwwof
from .wwwofPage import app as appwwwof
from .proyectsPage import proyects
from .proyectsPage import app as appproyects
import os
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

EXCLUDEDCHARACTER = "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
BLOGWEBDIR = "/blog/"
TEMPLATE = "core/templates/template.html"
BLOGPATH = "core/templates/blog/"
AUTHORFILE = "data/dataBfeelLog/authorfile.txt"
TOKENPATH = "data/dataBfeelLog/token.txt"
WHATISFILE = "data/dataBfeelLog/whatisfile.txt"
BLOGFILE = "core/blogs.py"
INDEX = "/blog.html"
TOKEN = readLine(TOKENPATH)
AUTHOR = readLine(AUTHORFILE)
USE = readLine(WHATISFILE)
try:
	BLOGS = blogNames(BLOGPATH)
except:
	os.mkdir(BLOGPATH)
BLOGSFILES = filesInFolders(BLOGPATH)
SUPORTEDLANGUAGES = ["No translate","spanish","english","german","basque","italian","russian"]
if os.path.isfile(BLOGFILE):
	try:
		from .blogs import blogs 
		from .blogs import app as appblogs 
		joinWebpage(BLOGSFILES,appblogs,app,url=BLOGWEBDIR)
	except:
		updateBlog(BLOGSFILES,BLOGFILE)


app.secret_key = str(enPassowrdHash(generatePassword()))
class webpage():
	app.secret_key = TOKEN
	print("\n* Configuration token:\n"+TOKEN+"\n","go to :\n\n\tlocalhost:9600"+BLOGWEBDIR+TOKEN+"/\n\nto get acces to configuration , rember your token is\n\n\t"+TOKEN,"\n")
	urlWwwof = "/wwwof/"
	urlProyects = "/proyects/"
	wwwofDireccions = ["calcupH","drawFISHTANK","divePC","curapeces","fishproyectsEN","fishproyectsES","notasCurapeces","howproyects/howcalcupH_js","howproyects/howcurapeces","howproyects/howDrawfishtank","howproyects/howfishdb","data_basecsv"]
	proyectsDireccions = ["aircolombia","htmlpower","htmlpower/little_recursion","htmlpower/iframe_power","pm25predict","pm25predict/pm25predictUnloquer","pm25predict/pm25predictCanairio","pandemaths","pandemathsout","DsoonMath","criptools","criptools/criptoretos","criptools/cesar","criptools/hashs","criptools/criptoolsencblog","criptools/rsa","criptools/criptophone","img2asciiart","gas","gas_login","gasinfo","noaa"]#,"gas/threads"]
	try:
		distributedWebLink = readtxtline("data/distributionScript/web.txt")#REMBER the url cannot end with "/"
		if webIsOniline(distributedWebLink):
			otherwwwofDireccions= ["curapeces","data_basecsv"]
			otherproyectsDireccions =["pm25predict","pm25predict/pm25predictUnloquer"]
			list(map(wwwofDireccions.remove,otherwwwofDireccions))
			list(map(proyectsDireccions.remove,otherproyectsDireccions))
			distributedWebWithIframe(urlWwwof,otherwwwofDireccions,app,distributedWebLink)
			distributedWebWithIframe(urlProyects,otherproyectsDireccions,app,distributedWebLink)
		joinWebpage(urlWwwof,wwwofDireccions,appwwwof,app)
		joinWebpage(urlProyects,proyectsDireccions,appproyects,app)
	except:
		joinWebpage(urlWwwof,wwwofDireccions,appwwwof,app)
		joinWebpage(urlProyects,proyectsDireccions,appproyects,app)
		joinWebpageGas(urlProyects,appproyects,app)
		joinWebpageDataBase_csv(urlWwwof,appwwwof,app)
		joinWebpageNoaa(urlProyects,appproyects,app)
	@app.route(urlWwwof)
	def wwwofIndex():
		"""web for some proyects about fishes"""
		return appwwwof
	@app.route(urlProyects)
	def proyectsIndex():
		"""web for some proyects not about fishes"""
		return appproyects
	@app.route("/")
	def index():
		"""way join all the codes in one"""
		return render_template("index.html")
	@app.route("/donacionbtc.html")
	def donacionBtc():
		return render_template("donacionbtc.html")
	@app.route("/BetterMap.html")
	def BetterMap():
		#webdireccions as variables
		urlWwwof = "/wwwof/"
		urlProyects = "/proyects/"
		return render_template("BetterMap.html",wl =urlWwwof, pl =urlProyects)
	@app.route("/mySiteMap.html")
	def mySiteMap():
		#webdireccions as variables
		urlWwwof = "/wwwof/"
		urlProyects = "/proyects/"
		return render_template("mySiteMap.html",waterMap =urlWwwof, spaceMap =urlProyects)
	@app.route("/blog.html")
	def blog():
		"""join ways of expressing myself in front of different things"""
		session["author"] = AUTHOR
		updateBlog(BLOGSFILES,BLOGFILE)
		return render_template("/blog/blogmenu.html", url= BLOGWEBDIR,topics = BLOGS, name = AUTHOR )
	@app.route("/blog/blog1.html")
	def blog1():
		"""thoughts about something"""
		return render_template("blog/blog/blog1.html")
	@app.route("/blog/blog2.html")
	def blog2():
		"""things a little more important for me"""
		return render_template("blog/blog/blog2.html")
	@app.route("/blog/blog3.html")
	def blog3():
		"""I recommend you about diferents topics"""
		return render_template("blog/blog/blog3.html")
	@app.route("/blog/blog4.html")
	def blog4():
		"""figures or gallery of ascii art"""
		return render_template("blog/blog/blog4.html")
	@app.route(BLOGWEBDIR+"blog5.html")
	def blog5():
		"""good humans that I admire"""
		return render_template("blog/blog/blog5.html")
	@app.route(BLOGWEBDIR+"blog6.html")
	def blog6():
		"""projects that call my attention that I want to share"""
		return render_template("blog/blog/blog6.html")
	@app.route(BLOGWEBDIR+"blog7.html")
	def blog7():
		""" travel to others proyects ... with <iframe>"""
		return render_template("blog/blog/blog7.html")
	@app.route(BLOGWEBDIR+"manifest.html")
	def manifest():
		"""me and some cultures of my interest ,I build my Manifest and I read those ofI read those of others others"""
		return render_template("blog/blog/manifest.html")
	@app.route(BLOGWEBDIR+"inventor_de_una_solucion.html")
	def main_inventor():
		""" little history """
		return render_template("blog/inventor_de_una_solucion/main.html")
	@app.route(BLOGWEBDIR+"inventor_de_una_solucion/1.html")
	def main_inventor1():
		""" a little history , 1 chapter """
		return render_template("blog/inventor_de_una_solucion/1.html")
	@app.route(BLOGWEBDIR+"proyectos.html")
	def proyectos():
		"""proyects links"""
		return render_template("blog/proyectos.html")
	@app.route('/ChatSO.html')
	def ChatSO():
		""" access to irc channel #jero98772 with irc kiwi """
		return render_template('ChatSO.html')
	@app.route("/enlaces.html")
	def enlaces():
		return render_template("blog/temp/presentacion_euskadi.html")
		
	@app.route(BLOGWEBDIR+"/config.html")
	def config():
		return render_template("blog/config/configmenu.html")
	@app.route(BLOGWEBDIR+"token.html",methods=['POST','GET'])
	def token():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				if request.form.get('new Token'):
					newToken = genToken()
					writeText(TOKENPATH,newToken,"w")
					session["loged"] = False
					return "you new Token is :\n\t"+newToken
				if request.form.get('custom Token'):
					writeText(TOKENPATH,request.form['customTokenValue'],"w")
					session["loged"] = False
					return "remember, save your token"
				return redirect(INDEX)
			return render_template("blog/config/token.html")

	@app.route(BLOGWEBDIR+TOKEN+"/",methods=['POST','GET'])
	def trueLoged():
		msg = ""
		if request.method == "POST":
			if request.form["key"] == TOKEN:
				session["loged"] = True
				return redirect(BLOGWEBDIR+"token.html")
			else:
				msg = "Invalid token"
		return render_template("blog/config/addkey.html",error=msg)
	@app.route(BLOGWEBDIR+"/add.html",methods=['POST','GET'])	
	def add():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				txtp =request.form["txtp"]
				txtq = request.form["txtq"]
				txtid = request.form["id"]
				name = request.form["destiantion"]
				if os.path.isdir(BLOGPATH+name):#translate because is dir 
					files = os.listdir(BLOGPATH+name)
					for file in files:
						if file[0].isupper():
							mainLangue = file[0].lower()+file[1:-5]
							content = doHtml(txtp,txtq,txtid,AUTHOR)
							writeblog(BLOGPATH+name+"/"+file,content)	
						else:
							transalateTo = file[:-5]
					else:
						txtp_translated = webTranslate(txtp,mainLangue,transalateTo)
						txtq_translated = webTranslate(txtq,mainLangue,transalateTo)
						content = doHtml(txtp_translated,txtq_translated,txtid,AUTHOR)
						writeblog(BLOGPATH+name+"/"+transalateTo+".html",content)
				else:
					content = doHtml(txtp,txtq,txtid,AUTHOR)
					writeblog(BLOGPATH+name+".html",content)
			return render_template("blog/config/addData.html",blogs = blogsNames(BLOGPATH))
	@app.route(BLOGWEBDIR+"/createNewTopic.html",methods=['POST','GET'])	
	def CreateNewTopic():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			msg = ""
			if request.method == "POST":
				name = str(request.form["name"])
				nameIsOk ,errormsg = clearName(name,EXCLUDEDCHARACTER,BLOGS)
				if nameIsOk:
					name = changeName(name)
				try :
					translateTo = request.form["translate_to"]
				except:
					translateTo = SUPORTEDLANGUAGES[0]
				translateFrom = request.form["translate_from"]
				if translateTo == translateFrom:
					msg = "you can not translate from "+translateTo+" to "+translateFrom
				if SUPORTEDLANGUAGES[0] == translateTo or translateTo == translateFrom:
					msg = " was create a topic without trasnlate option"
					writeblog(BLOGPATH+name+".html","")
				else:
					os.mkdir(BLOGPATH+name)
					writeblog(BLOGPATH+name+"/"+translateFrom[0].upper()+translateFrom[1:]+".html","")
					writeblog(BLOGPATH+name+"/"+translateTo+".html","")
			return render_template("blog/config/createNewTopic.html" ,languages = SUPORTEDLANGUAGES, msg = msg)

	@app.route(BLOGWEBDIR+"/deleteFiles.html",methods = ["POST","GET"])
	def deleteFiles():		
		msg = ""
		if request.method == "POST":
			deletechecks = request.form.getlist("delete")
			deleteAndMove(deletechecks,BLOGPATH,BLOGS) 
			deletemsg = str(deletechecks)[2:-2]
			msg =  "file removed are :"+deletemsg
		return render_template("blog/config/deleteFiles.html",blogs = BLOGS,msg = msg)
	@app.route(BLOGWEBDIR+"/author.html",methods=['POST','GET'])
	def author():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				newAuthor = request.form['author']
				#upadateAuthor(AUTHOR,newAuthor,TEMPLATE)
				writeText(AUTHORFILE,newAuthor,"w")
				return redirect(INDEX)
			return render_template("blog/config/author.html",defautlAuthor = AUTHOR)
	@app.route(BLOGWEBDIR+"/thisSite.html",methods=['POST','GET'])
	def thisSite():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				whatis = request.form['this']
				#upadateAuthor(USE,whatis,TEMPLATE)
				writeText(WHATISFILE,whatis,"w")
				return redirect(INDEX)
			return render_template("blog/config/thisSite.html",defautlUse = USE)


