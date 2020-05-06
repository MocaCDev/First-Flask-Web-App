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
# NAMES TO FILTER OUT
filter_out = [
	'fuck','dick','pussy','bombed','sex','porn','porno',
	'suck'
]
usernames_ = []

@app.route('/Submitted')
def Submit():
	return render_template('homePage.html', usernames=usernames_)

"""
	Home Page is the page where user will enter credentials
"""
@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	if request.method == 'POST':
		usernames_.append(request.form['Username'])
		for i in filter_out:
			for x in range(len(usernames_)):
				if i in usernames_[x]:
					del usernames_[x]
					return '<h1>Username is bad.</h1> <button type="submit"><a href="/" style="color:white;text-decoration:none">BACK</a></button>'
		return render_template('submit.html', username=usernames_)
	else:
		return render_template("userSetup.html")

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True)