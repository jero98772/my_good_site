from core.tools.webUtils import readtxtline
import sqlite3
def shortcut():
	connection = sqlite3.connect('data/dataBases/personalweb.db')
	db = connection.cursor()
	return db
def clearimg(file):
	try:
		from removebg import RemoveBg
		rmbg = RemoveBg(readtxtline("data/keys/removeBg.txt"), "error.log")
		img = rmbg.remove_background_from_img_file(file)
	except:
		img = file
	return img