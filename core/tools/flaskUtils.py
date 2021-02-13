#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from flask import request,render_template_string
def multrequest(items):	
	values = []
	for item in items:		
		item = request.form.get(item)
		try:
			item = float(item)
		except:	
			item = str(item)
		values.append(item)
	return values
def joinWebpageGas(url,webApp,acualapp):	
	@acualapp.route(url+'gas/editar<string:id>', methods = ['POST', 'GET'])
	def gassdelete(id):
		return webApp
	@acualapp.route(url+"gas/eliminar/<string:id>", methods = ['GET','POST'])
	def get_gas(id):
		return webApp
	@acualapp.route(url+'gas/actualisar<string:id>', methods = ['GET','POST'])
	def update_gas(id):
		return webApp
def joinWebpageDataBase_csv(url,webApp,acualapp):
	url += "data_basecsv/" 
	print(url)
	@acualapp.route(url+'delete/<string:id>', methods = ['GET','POST'])
	def delete(id):
		return webApp
	@acualapp.route(url+'update_fish/<string:id>', methods = ['GET','POST'])
	def update_fish(id):
		return webApp
	@acualapp.route(url+'<string:id>', methods = ['GET','POST'] )
	def get_fish(id):
		return webApp
def joinWebpage(url,direccions,webApp,acualapp):	
		for webroute in direccions:		
			@acualapp.route(url+str(webroute)+".html", endpoint=webroute , methods=['GET','POST'])
			def site():
				return webApp
		return site()
def distributedWebWithIframe(url,direccions,webApp,runWeb):
	for webroute in direccions:		
		print(webroute)
		@webApp.route(url+str(webroute)+".html", endpoint=webroute , methods=['GET','POST'])
		def site():
			return render_template_string("{% extends  '"+url+"template.html'%}{% block content %}<iframe src='"+str(runWeb)+url+str(webroute)+".html#webContent"+"' scrolling='no' class='frameDistrution'> </iframe> {% endblock %}")
		return site()