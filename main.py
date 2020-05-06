""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from flask import (
	Flask,
	render_template,
	url_for,
	request
)

app = Flask(__name__)

@app.route('/Submit', methods=['POST','GET'])
def Submit():
	return render_template('submit.html')

@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	return render_template("home.html")

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True)