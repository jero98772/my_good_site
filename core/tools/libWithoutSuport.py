import sqlite3
from removebg import RemoveBg
def shortcut():
	connection = sqlite3.connect('data/dataBases/personalweb.db')
	db = connection.cursor()
	return db
def clearimg(file):
	try:
		rmbg = RemoveBg("you api key here", "error.log")
		img = rmbg.remove_background_from_img_file(file)
	except:
		img = file
	return img