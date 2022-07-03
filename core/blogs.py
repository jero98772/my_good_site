from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/blogmenu.html")
	def blogmenu():
		return render_template("blog/blogmenu.html")
	@app.route("/blog/blog/blog7.html")
	def blogblog7():
		return render_template("blog/blog/blog7.html")
	@app.route("/blog/blog/blog5.html")
	def blogblog5():
		return render_template("blog/blog/blog5.html")
	@app.route("/blog/blog/blogT.html")
	def blogblogT():
		return render_template("blog/blog/blogT.html")
	@app.route("/blog/blog/blog3.html")
	def blogblog3():
		return render_template("blog/blog/blog3.html")
	@app.route("/blog/blog/blog6.html")
	def blogblog6():
		return render_template("blog/blog/blog6.html")
	@app.route("/blog/blog/blog2.html")
	def blogblog2():
		return render_template("blog/blog/blog2.html")
	@app.route("/blog/blog/manifest.html")
	def blogmanifest():
		return render_template("blog/blog/manifest.html")
	@app.route("/blog/blog/blog4.html")
	def blogblog4():
		return render_template("blog/blog/blog4.html")
	@app.route("/blog/blog/blog1.html")
	def blogblog1():
		return render_template("blog/blog/blog1.html")
	@app.route("/blog/config/addkey.html")
	def configaddkey():
		return render_template("blog/config/addkey.html")
	@app.route("/blog/config/token.html")
	def configtoken():
		return render_template("blog/config/token.html")
	@app.route("/blog/config/createNewTopic.html")
	def configcreateNewTopic():
		return render_template("blog/config/createNewTopic.html")
	@app.route("/blog/config/author.html")
	def configauthor():
		return render_template("blog/config/author.html")
	@app.route("/blog/config/thisSite.html")
	def configthisSite():
		return render_template("blog/config/thisSite.html")
	@app.route("/blog/config/deleteFiles.html")
	def configdeleteFiles():
		return render_template("blog/config/deleteFiles.html")
	@app.route("/blog/config/addData.html")
	def configaddData():
		return render_template("blog/config/addData.html")
	@app.route("/blog/config/configmenu.html")
	def configconfigmenu():
		return render_template("blog/config/configmenu.html")
	@app.route("/blog/temp/presentacion_euskadi.html")
	def temppresentacion_euskadi():
		return render_template("blog/temp/presentacion_euskadi.html")
	@app.route("/blog/proyectos.html")
	def proyectos():
		return render_template("blog/proyectos.html")