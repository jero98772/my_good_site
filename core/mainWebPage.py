#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.webUtils import generatePassword
from core.tools.cryptotools import enPassowrdHash
from core.tools.flaskUtils import joinWebpage ,joinWebpageGas,joinWebpageDataBase_csv
from .wwwofPage import wwwof 
from .wwwofPage import app as appwwwof
from .proyectsPage import proyects 
from .proyectsPage import app as appproyects
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = str(enPassowrdHash(generatePassword()))
class webpage():
	urlWwwof = "/wwwof/"
	urlProyects = "/proyects/"
	wwwofDireccions = ["calcupH","drawFISHTANK","divePC","curapeces","fishproyectsEN","fishproyectsES","notasCurapeces","howproyects/howcalcupH_js","howproyects/howcurapeces","howproyects/howDrawfishtank","howproyects/howfishdb","data_basecsv"]
	proyectsDireccions = ["aircolombia","htmlpower","htmlpower/little_recursion","htmlpower/iframe_power","pm25predict","pm25predict/pm25predictUnloquer","pm25predict/pm25predictCanairio","pandemaths","pandemathsout","criptools","criptools/criptoretos","criptools/cesar","criptools/hashs","criptools/criptoolsencblog","criptools/rsa","img2asciiart","gas","gas_login"]
	#forgottenproyects = ["gas/actualisar<string:id>","gas/editar<string:id>","gas/eliminar/<string:id>"]
	joinWebpage(urlWwwof,wwwofDireccions,appwwwof,app)
	joinWebpage(urlProyects,proyectsDireccions,appproyects,app)
	joinWebpageGas(urlProyects,appproyects,app)
	joinWebpageDataBase_csv(urlWwwof,appwwwof,app)
	@app.route(urlWwwof)
	def wwwofIndex():
		return appwwwof
	@app.route(urlProyects)
	def proyectsIndex():
		return appproyects
	@app.route("/")
	def index():
		return render_template("index.html")
	@app.route("/donacionbtc.html")
	def donacionBtc():
		return render_template("donacionbtc.html")
	@app.route("/mySiteMap.html")
	def mySiteMap():
		#webdireccions as variables	
		urlWwwof = "/wwwof/"
		urlProyects = "/proyects/"
		return render_template("mySiteMap.html",waterMap =urlWwwof, spaceMap =urlProyects)
	@app.route("/blog.html")
	def blog():
		return render_template("/blog/blogmenu.html") 
	@app.route("/blog/blog1.html")
	def blog1():
		return render_template("blog/blog1.html")
	@app.route("/blog/blog2.html")
	def blog2():
		return render_template("blog/blog2.html")  
	@app.route("/blog/blog3.html")
	def blog3():
		return render_template("blog/blog3.html")  
	@app.route("/blog/blog4.html")
	def blog4():
		return render_template("blog/blog4.html")
	@app.route("/blog/blog5.html")
	def blog5():
		return render_template("blog/blog5.html")  
	@app.route("/blog/blog6.html")
	def blog6():
		return render_template("blog/blog6.html")
	@app.route("/blog/blog7.html")
	def blog7():
		return render_template("blog/blog7.html")
	@app.route("/blog/manifest.html")
	def manifest():
		return render_template("blog/manifest.html")
	@app.route('/ChatSO.html')
	def ChatSO():
		return render_template('ChatSO.html')
	@app.route('/entrevistas.html')
	def entrevistas():
		return render_template('blog/entrevistas.html')
 