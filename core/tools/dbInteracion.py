#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
import sqlite3
class dbInteracion():
	def __init__(self,dbName):
		self.dbName = str(dbName)
	def connect(self,tableName):
		self.tableName = str(tableName)
		self.connecting = sqlite3.connect(self.dbName)
		self.cursor = self.connecting.cursor()
		return self.cursor
	def userAvailable(self,user,item):
		self.user = str(user)
		self.item = str(item)
		self.cursor.execute(" SELECT {0} FROM {1}".format(self.item,self.tableName))
		self.users = self.cursor.fetchall()
		for i in range(len(self.users)):
			if self.user in self.users[i]:
				return False
			else:
				return True 
	def saveUser(self,user,password,email,birthday):
		self.user = str(user)
		self.email = str(email)
		self.password = str(password)
		self.birthday = str(birthday)
		self.insertUser = "INSERT INTO {0}(username, email, password, birthday) VALUES( ?, ?, ?, ? );".format(self.tableName)
		self.cursor.execute(self.insertUser,(self.user,self.email,self.password,self.birthday))
		self.cursor.connection.commit()
	def createUser(self):
		self.tableUserFeels = 'CREATE TABLE "{0}Sentimientos" (sentimiento1 TEXT, sentimiento2 TEXT ,sentimiento3 TEXT, sentimiento4 TEXT, sentimiento5 TEXT, sentimiento6 TEXT, val1 INTEGER , val2 INTEGER , val3 INTEGER , val4 INTEGER , val5 INTEGER, val6 INTEGER);'.format(self.user)
		self.tableUserFeelsRnd = 'CREATE TABLE "{0}Sentimientosrnd" (rndsentimiento1 TEXT, rndsentimiento2 TEXT ,rndsentimiento3 TEXT, rndsentimiento4 TEXT, rndsentimiento5 TEXT, rndsentimiento6 TEXT, val1rnd INTEGER , val2rnd INTEGER , val3rnd INTEGER , val4rnd INTEGER , val5rnd INTEGER, val6rnd INTEGER);'.format(self.user)
		self.tableUserExp = 'CREATE TABLE "{0}Exp" (experiencia TEXT ,expbuenaOmala TEXT, modalidad TEXT,quesucedio TEXT ,quelaincio TEXT , lugarexp TEXT , momento TEXT ,dia TEXT , preocupado TEXT );'.format(self.user)
		self.tableUserOthers = 'CREATE TABLE "{0}Otros" (insultobool INTEGER ,cantidadpersonasinsulto INTEGER  ,quepaso TEXT, insultadobool INTEGER , cantidadpersonasinsultado INTEGER , porque TEXT , quepersonas TEXT ); '.format(self.user)
		self.cursor.execute(self.tableUserFeels)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserFeelsRnd)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserExp)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserOthers)
		self.cursor.connection.commit()
	def findUser(self,user):
		self.user = str(user)
		self.userTuple = (self.user,)
		self.dbcomand =  "SELECT usr FROM {0} Where usr =  ? ".format(self.tableName)
		self.cursor.execute(self.dbcomand,self.userTuple)
		self.userHash = self.cursor.fetchall()
		try:
			if self.userHash[0] == self.userTuple :
				return True
			else :
				return False
		except:
			return False
	def findPassword(self,password):
		self.password = str(password)
		self.passwordTulple = (self.password,)
		self.dbcomand =  "SELECT pwd FROM {0} Where pwd =  ? ".format(self.tableName)
		self.cursor.execute(self.dbcomand,self.passwordTulple)
		self.passwordHash = self.cursor.fetchall()
		try:
			if  self.passwordHash[0] == self.passwordTulple:
				return True
			else :
				return False
		except:
			return False
	def yesterday(self,user):
		self.user = str(user)
		self.dbcomand =  "SELECT dia FROM ?Exp ORDER BY DESC LIMIT 1"
		self.cursor.execute(self.dbcomand,self.user)
		self.lastday = self.cursor.fetchall()
		return self.lastday
		"""	
	def putDays(self,user):
		self.user = str(user)
		self.dbcomand =  "SELECT dia FROM ?Exp ORDER BY DESC LIMIT 1"
		self.cursor.execute(self.dbcomand,self.user)
		self.lastday = self.cursor.fetchall()
		return self.lastday
		"""
	def allData(self):
		dbcomand = " SELECT * FROM {0} ;".format(self.tableName)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def getID(self):
		dbcomand = " SELECT * FROM {0} ;".format(self.tableName)
		self.cursor.row_factory = lambda cursor, row: list(str(int(row[0])))#
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
		self.cursor.row_factory = sqlite3.Row
	def getColumn(self,row):
		dbcomand = " SELECT {0} FROM {1} ;".format(row,self.tableName)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def getDataWhere(self,row,equals):
		dbcomand = " SELECT * FROM {0} WHERE {1} = {2} ;".format(self.tableName,row,equals)
		self.cursor.execute(self.dbcomand)
		self.alldata = self.cursor.fetchall()
		return alldata
	def getSum(self,row):
		dbcomand = " SELECT sum({0}) FROM {1} ;".format(row,self.tableName)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def getDistinctColumn(self,row):
		dbcomand = " SELECT DISTINCT {0} FROM {1} ;".format(row,self.tableName)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def getAvg(self,column):
		dbcomand = " SELECT avg({0}) FROM {1} ;".format(column,self.tableName)
		self.cursor.execute(self.dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def deleteWhere(self,column,equals):
		dbcomand = " DELETE FROM {0} WHERE {1} = {2} ;".format(self.tableName,column,str(equals))
		self.cursor.execute(dbcomand)
		self.cursor.connection.commit()
	def putNewFishes(self,dbItems,data):
		self.dbItems = dbItems
		self.data = data
		self.dbcomand = str("INSERT INTO {0} {1}  VALUES {2} ;".format(self.tableName,tuple(self.dbItems),tuple(self.data)))
		self.cursor.execute(self.dbcomand)
		self.cursor.connection.commit()
	def wwwofdelete(self,item):
		self.item = item
		self.dbcomand = str('DELETE  FROM {0} WHERE id = {1};'.format(self.tableName,self.item))
		self.cursor.execute(self.dbcomand)
		self.cursor.connection.commit()
	def wwwofUpdate(self,params,updateItem,item):
		self.item = item
		self.params = params
		self.updateItem = updateItem
		self.dbcomand = str(self.params[0])+" = '"+str(self.updateItem[0])+"'"
		for i ,j in zip(self.params[1:],self.updateItem[1:]):
				self.dbcomand += ","+str(i)+" = '"+str(j)+"'"
		self.dbcomand = "UPDATE {0} SET {1} WHERE id = {2} ".format(self.tableName,self.dbcomand, self.item) 
		self.cursor.execute(self.dbcomand)
		self.cursor.connection.commit()
	def getId(self,item):
		dbcomand = 'SELECT * FROM {0} WHERE id = {1}'.format(self.tableName,item)
		self.cursor.execute(dbcomand)
		idFish = self.cursor.fetchall()
		return idFish
	def getLastId(self):
		dbcomand = 'SELECT max(id) FROM {0} '.format(self.tableName)
		self.cursor.execute(dbcomand)
		lastid = self.cursor.fetchall()
		lastid = int(list(lastid[0])[0])
		return lastid
	def numitems(self,item):
		dbcomand = 'SELECT  length({0}) FROM {1} '.format(item ,self.tableName)
		self.cursor.execute(dbcomand)
		numItems = self.cursor.fetchall()
		return numItems
	def putNewMsgsBlog(self,dbItems,data):
		dbcomand = str("INSERT INTO {0} {1}  VALUES {2} ;".format(self.tableName,tuple(dbItems),tuple(data)))
		self.cursor.execute(dbcomand)
		self.cursor.connection.commit()
	def encBlog(self,value):
		dbcomand = 'SELECT {0} FROM {1} ;'.format(value,self.tableName)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def addGas(self,dbItems,data ):
		dbcomand = str("INSERT INTO {0} {1}  VALUES {2} ;".format(self.tableName,tuple(dbItems),tuple(data)))
		self.cursor.execute(dbcomand)
		self.cursor.connection.commit()
	def getDataGasWhere(self,row,equals):
		dbcomand = " SELECT * FROM {0} WHERE {1} = {2} ;".format(self.tableName,row,equals)
		self.cursor.row_factory = lambda cursor, row: list(row[1:])
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
		self.cursor.row_factory = sqlite3.Row
	def getDataGas(self):
		dbcomand = " SELECT * FROM {0} ;".format(self.tableName)
		self.cursor.row_factory = lambda cursor, row: list(row[1:])
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
		self.cursor.row_factory = sqlite3.Row
	def updateGas(self,updateSentence, id):
		dbcomand = str("UPDATE {0} SET {1} WHERE item_id = {2}; ".format((self.tableName),updateSentence,id))
		self.cursor.execute(dbcomand)
		self.cursor.connection.commit()
	def getDistinctColumnGAS(self,row):
		dbcomand = " SELECT DISTINCT {0} FROM {1} ;".format(row,self.tableName)
		self.cursor.execute(dbcomand)
		self.cursor.row_factory = lambda cursor, row: row[0]
		alldata = self.cursor.fetchall()
		return alldata
		self.cursor.row_factory = sqlite3.Row
	def getDistinctWhere(self,equals):
		dbcomand = " SELECT DISTINCT * FROM {0} WHERE item_id = {1} ;".format(self.tableName,equals)
		self.cursor.execute(dbcomand)
		alldata = self.cursor.fetchall()
		return alldata
	def closeDB(self):
		self.cursor.close()