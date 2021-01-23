#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from core.tools.webUtils import generatePassword ,deleteFish,getExt,img2NumName
from core.tools.cryptotools import enPassowrdHash
from core.tools.dbInteracion import dbInteracion
from core.tools.flaskUtils import multrequest
from core.tools.libWithoutSuport import clearimg
import os
app = Flask(__name__)
app.secret_key = str(enPassowrdHash(generatePassword()))
dbName = "wwwof"
tableFishes = "fishes"
dbpath = "data/dataBases/"+dbName
webpage = "/wwwof/"
imgdir = "core/static/img/wwwof/data_basecsv/"
fishdata =  ["common","scientific","ph","h","liters","cm","tempC","food","reproduction","lighting","temperament","livingEnv","swim","location","description"]
class wwwof():
	@app.route(webpage)
	def index():
		return render_template("wwwof/index.html")
	@app.route(webpage+"howproyects/howcalcupH_js.html")
	def howcalcupH_js():
		return render_template("wwwof/howproyects/howcalcupH_js.html")
	@app.route(webpage+"howproyects/howcurapeces.html")
	def howcurapeces():
		return render_template("wwwof/howproyects/howcurapeces.html")
	@app.route(webpage+"howproyects/howDrawfishtank.html")
	def howDrawfishtank():
		return render_template("wwwof/howproyects/howDrawfishtank.html")
	@app.route(webpage+"howproyects/howfishdb.html")
	def howfishdb():
		return render_template("wwwof/howproyects/howfishdb.html")
	@app.route(webpage+"notasCurapeces.html")
	def notasCurapeces():
		return render_template("wwwof/notes/notasCurapeces.html") 
	@app.route(webpage+"fishproyectsES.html")
	def fishproyectsES():
		return render_template("wwwof/notes/fishproyectsES.html")
	@app.route(webpage+"fishproyectsEN.html")
	def fishproyectsEN():
		return render_template("wwwof/notes/fishproyectsEN.html") 
	@app.route(webpage+"calcupH.html")
	def calcuph():
		return render_template("wwwof/calcuPH/ph.html") 
	@app.route(webpage+"drawFISHTANK.html")
	def drawFISHTANK():
		return render_template("wwwof/drawFISHTANK/drawFISHTANK.html") 
	@app.route(webpage+"divePC.html")
	def divePC():
		return render_template("wwwof/divePC/divePC.html")
	@app.route(webpage+"curapeces.html" , methods=['GET','POST'])
	def curapeces():
		imgdir = "core/static/img/wwwof/curapeces/"
		sickness = ""
		try:
			from core.wwwof.curapeces import predict
			fPredict = predict()
			checkPredict = predict()
			if request.method == 'POST':
				file = request.files["file"]
				ext = getExt(file)
				fileName = imgdir+str(img2NumName(imgdir))+"fish"+ext
				file.save(fileName)
				#remeber clear background
				clearimg(fileName)
				fPredict.pez = file
				checkPredict.pez = file
				diases= fPredict.predict()
				checkDiases = checkPredict.predict()
				outSickness = fPredict.ChosePredeictionEn(diases)
				checkSickness = fPredict.ChosePredeictionEn(checkDiases)
				if outSickness == checkSickness :
					sickness = outSickness
				else:
					sickness = "please try again"
		except:
			sickness = "Error 500, you need a model for predict diase of that fish. is a error form server please report to curapeces@gmail.com"
		return render_template('wwwof/curapeces/curapeces.html',prediccion=sickness)
	@app.route(webpage+"data_basecsv.html", methods=['GET','POST'])
	def data_basecsv():
		imgspath = []
		db = dbInteracion(dbpath)
		db.connect(tableFishes)
		rows = db.allData()
		if request.method == 'POST':
			data = multrequest(fishdata)
			photo = request.files["photo"]
			#photoname = photo[15:-17:]#15 and 17 is an interval when say the name of img like ["<FileStorage: '15]img.jpeg[-17' ('image/jpeg')>"]
			photo.save(imgdir+str(db.getLastId()+1)+"fish")
			db.putNewFishes(fishdata,data)
			return redirect(webpage)
		return render_template("wwwof/data_basecsv/data_basecsv.html", fishes=rows ,imgs = imgspath)#,form = db) 
	@app.route(webpage+"data_basecsv/delete/<string:id>", methods = ['GET','POST'])
	def delete(id):
		db = dbInteracion(dbpath)
		db.connect(tableFishes)
		db.wwwofdelete(id)
		deleteFish(str(id))
		flash('you delete that')
		return redirect("wwwof/data_basecsv.html")
	@app.route(webpage+'data_basecsv/update_fish/<string:id>', methods = ['GET','POST'])
	def update_fish(id):
		imgdir = "core/static/img/wwwof/data_basecsv/"
		db = dbInteracion(dbpath)
		db.connect(tableFishes)
		if request.method == 'POST':
			data = multrequest(fishdata)
			try:
				photo = request.files["photo"]
				if photo != None:
					deleteFish(imgdir+id)
					photo.save(imgdir+str(id)+"fish")
			except:
				pass
			db.wwwofUpdate(fishdata,data,id)
		return redirect(webpage+'data_basecsv.html')
	@app.route(webpage+'data_basecsv/<string:id>', methods = ['POST', 'GET'])
	def get_fish(id):
		db = dbInteracion(dbpath)
		db.connect(tableFishes)
		rows = db.getId(id)
		return render_template('wwwof/data_basecsv/updatefish.html', fish = rows[0])#, imgpath=imgchange)
