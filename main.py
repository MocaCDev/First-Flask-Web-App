""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from datetime import datetime
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
time_now = datetime.now()

@app.route('/Submitted')
def Submit():
	return render_template('homePage.html', usernames=usernames_)

"""
	Home Page is the page where user will enter credentials
"""
@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	if request.method == 'POST':
		usernames_.append(request.form['Username']+'(TIME {})'.format(time_now.strftime("%H:%M:%S")))
		for i in filter_out:
			for x in range(len(usernames_)):
				if i in usernames_[x].lower():
					del usernames_[x]
					return '<h1>Username is bad.</h1> <a href="/" style="text-decoration:none"><button type="submit" style="background-color:black;color:white">Go Back</button></a>'
		return render_template('submit.html', username=usernames_)
	else:
		return render_template("userSetup.html", username=usernames_)

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True)