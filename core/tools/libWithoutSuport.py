import sqlite3
def shortcut():
	connection = sqlite3.connect('data/dataBases/personalweb.db')
	db = connection.cursor()
	return db
