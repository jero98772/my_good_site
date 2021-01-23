#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.webUtils import generatePassword,readtxtline
from core.tools.cryptotools import enPassowrdHash
from core.tools.flaskUtils import joinWebpage ,joinWebpageGas,joinWebpageDataBase_csv,distributedWebWithIframe
from core.tools.teleUtils import webIsOniline
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
	proyectsDireccions = ["aircolombia","htmlpower","htmlpower/little_recursion","htmlpower/iframe_power","pm25predict","pm25predict/pm25predictUnloquer","pm25predict/pm25predictCanairio","pandemaths","pandemathsout","DsoonMath","criptools","criptools/criptoretos","criptools/cesar","criptools/hashs","criptools/criptoolsencblog","criptools/rsa","criptools/criptophone","img2asciiart","gas","gas_login"]
	#forgottenproyects = ["gas/actualisar<string:id>","gas/editar<string:id>","gas/eliminar/<string:id>"]
	try:
		distributedWebLink = readtxtline("data/distributionScript/web.txt")
		if webIsOniline(distributedWebLink):
			otherwwwofDireccions= ["curapeces","data_basecsv"]
			otherproyectsDireccions =["pm25predict","pm25predict/pm25predictUnloquer"]
			DistributedWebWithIframe(urlWwwof,otherwwwofDireccions,app,distributedWebLink)
			DistributedWebWithIframe(urlProyects,otherproyectsDireccions,app,distributedWebLink)
			map(wwwofDireccions.remove,otherwwwofDireccions)
			map(proyectsDireccions.remove,otherproyectsDireccions)
			print(wwwofDireccions,proyectsDireccions)
		joinWebpage(urlWwwof,wwwofDireccions,appwwwof,app)
		joinWebpage(urlProyects,proyectsDireccions,appproyects,app)
	except:
		joinWebpage(urlWwwof,wwwofDireccions,appwwwof,app)
		joinWebpage(urlProyects,proyectsDireccions,appproyects,app)
		joinWebpageGas(urlProyects,appproyects,app)
		joinWebpageDataBase_csv(urlWwwof,appwwwof,app)
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
		return render_template("/blog/blogmenu.html") 
	@app.route("/blog/blog1.html")
	def blog1():
		"""thoughts about something"""
		return render_template("blog/blog1.html")
	@app.route("/blog/blog2.html")
	def blog2():
		"""things a little more important for me"""
		return render_template("blog/blog2.html")  
	@app.route("/blog/blog3.html")
	def blog3():
		"""I recommend you about diferents topics"""
		return render_template("blog/blog3.html")  
	@app.route("/blog/blog4.html")
	def blog4():
		"""figures or gallery of ascii art"""
		return render_template("blog/blog4.html")
	@app.route("/blog/blog5.html")
	def blog5():
		"""good humans that I admire"""
		return render_template("blog/blog5.html")  
	@app.route("/blog/blog6.html")
	def blog6():
		"""projects that call my attention that I want to share"""
		return render_template("blog/blog6.html")
	@app.route("/blog/blog7.html")
	def blog7():
		""" travel to others proyects ... with <iframe>"""
		return render_template("blog/blog7.html")
	@app.route("/blog/manifest.html")
	def manifest():
		"""me and some cultures of my interest ,I build my Manifest and I read those ofI read those of others others"""
		return render_template("blog/manifest.html")
	@app.route('/ChatSO.html')
	def ChatSO():
		""" access to irc channel #jero98772 with irc kiwi """
		return render_template('ChatSO.html')
#	@app.route('/entrevistas.html')
#	def entrevistas():
#		return render_template('blog/entrevistas.html')
 