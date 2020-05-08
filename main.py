""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os, json
#from datetime import datetime
try:
	from flask import (
		Flask,
		render_template,
		#url_for,
		request
	)
except ImportError as IE:
	print("IE ERR: %s" % IE)
	os.system('pip3 install -r requirements.txt')
	from flask import (
		Flask,
		render_template,
		#url_for,
		request
	)

app = Flask(__name__)
# NAMES TO FILTER OUT
# don't even bother reading these...it is just needed so no innapropriate names are inputted
filter_out = [
	'fuck','dick','pussy','bitch','nigga','bombed','sex',
	'porn','porno','suck','xnxx','pornhub','cunt','slut',
	'hoe','whore','shit','penis','cock','vagina','boobs',
	'anal','ass','ball sack','cum','sperm'
]
usernames_ = []
#time_now = datetime.now().strftime("%H:%M:%S")

@app.route('/Submitted')
def Submit():
	return render_template('homePage.html', usernames=usernames_)

"""
	Home Page is the page where user will enter credentials
"""
@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	if request.method == 'POST':
		if len(request.form['Username']) > 1:
			usernames_.append(request.form['Username'])
			data = {'USERNAMES':usernames_}
			with open('username_info.json','w') as file:
				file.write(json.dumps(
					data,
					indent=2,
					sort_keys=False
				))
				file.flush()
				file.close()
			for i in filter_out:
				for x in range(len(usernames_)):
					if i in usernames_[x].lower():
						message='<h3>Username %s is bad.</h3><br><p>Contains the word: %s</p><a href="/" style="text-decoration:none"><button type="submit" style="background-color:black;color:white">Go Back</button></a>'%(usernames_[x],i)
						del usernames_[x]
						return message
			return render_template('submit.html',username=usernames_)
		else:
			return render_template('userSetup.html',username=usernames_,badNames=filter_out, ERR_MSG="ERROR: Username was empty. Must have at least 2 characters")
	else:
		if os.path.exists('username_info.json'):
			info = json.loads(str(open('username_info.json','r').read()))
			usernames = []
			for i in info['USERNAMES']:
				usernames.append(i)
			return render_template('userSetup.html',username=usernames,badNames=filter_out)
		else:
			return render_template("userSetup.html", badNames=filter_out)

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True,port=8080)