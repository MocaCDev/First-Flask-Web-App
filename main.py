""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from flask import (
	Flask,
	render_template,
	url_for
)

app = Flask(__name__)

@app.route('/')
def HOME_PAGE():
	return render_template("home.html")

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True)