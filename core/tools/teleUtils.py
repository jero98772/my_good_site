from urllib import request
from socket import gethostname ,gethostbyname
def webIsOniline(web):
	"""webIsOniline(<web for check>) , Return true or False"""
	if web == "":
		return False
	else:	
		status = request.urlopen(web).getcode()
		if status == 200:
			return True
		else: 
			return False
def getData():
	"""get ip and hostname when you acces to this web"""
	hostname = gethostname()
	ip = gethostbyname()
	return ip, hostname