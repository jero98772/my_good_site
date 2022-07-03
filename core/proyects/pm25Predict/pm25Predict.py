from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy as np
#pendiente para unlouqer y canairio
class pm25predict:
	def __init__(self,db,host):
			self.db = str(db)
			self.host = host
			self.client = InfluxDBClient(host=self.host, port=8086)
	def SensorsName(self):
		self.resultsaqa= self.client.query('SHOW MEASUREMENTS ON "'+self.db+'"').raw
		self.arrnamesaqa = eval(str(self.resultsaqa)[88:-4])
		return self.arrnamesaqa
	def setupUnloquer(self,name):
		self.name = name
		try:
			self.q = self.client.query('SELECT mean("pm25") AS "pm25" FROM "'+self.db+'"."autogen".'+self.name+' WHERE time > now() - 5h GROUP BY time(10s) FILL(none)')
			self.pms25 = []
			for self.pm25points in self.q.get_points():
				self.pms25.append(self.pm25points["pm25"])
			return self.pms25
		except:
			pass
			print("query error in line 17 of pm25predict , dont found data in influxdbd with"+str(self.name))
	def setupCanairio(self,name):
		self.name = name
		try:
			self.q = self.client.query('SELECT * from "'+self.name+'" WHERE time >= now() - 5h')
			#self.q = self.client.query('SELECT mean("pm25") AS "pm25" FROM "'+self.db+'"."autogen".'+self.name+' WHERE time > now() - 5h GROUP BY time(10s) FILL(none)')
			self.pms25 = []
			for self.pm25points in self.q.get_points():
				self.pms25.append(self.pm25points["pm25"])
			return self.pms25
		except:
			pass
			print("query error in line 17 of pm25predict , dont found data in influxdbd with"+str(self.name))

def fpm25preditc(name,pm25):
	name = str(name)
	sumy = 0
	epoch = [epoch for epoch in range(len(pm25))]
	epoch = np.asanyarray(epoch)
	pm25 = np.asanyarray(pm25)
	epochs = epoch.reshape((1,-1))
	pm25s = pm25.reshape((1,-1))
	y = pm25s
	for i in y:
		sumy +=y
	b = sumy/len(epochs)
	for i in range(len(epochs)):
		w = ((epochs[i]*epochs)-(pm25s[i]*pm25s))/((epochs[i]*epochs)**2)
	prediction = w*epochs+b
	for x in epochs:
		for y2 in y:
			filtred = np.polyfit(x, y2, 1)
	predictions = np.polyval(filtred, epochs)
	Y = np.polyval(predictions, epochs)
	plt.xlabel("epochs")
	plt.ylabel("pm25")
	plt.title("predict")
	plt.plot(epoch,pm25,'bo',label='pm25')
	plt.plot(epochs*2,Y,"go",label='prediction')
	plt.savefig('my_good_site/core/static/img/proyects/pm25predict/preditc_'+name+'.png')
	plt.clf()
def genpredsunloquer(db,host):
	aqa = pm25predict(db,host)
	sensornames = aqa.SensorsName()
	working = []
	for i in sensornames:
		sensor = i[0]
		data = aqa.setupUnloquer(sensor)
		try:
			fpm25preditc(sensor,data)
			working.append(sensor)
		except:
			pass
		#print(sensor)
	return working
def genpredscanairio(db):
	canairio = pm25predict(db)
	canairio.setup(name)