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
		# This will append all previous added usernames
		if os.path.exists('username_info.json'):
			old = json.loads(str(open('username_info.json','r').read()))

			for i in old['USERNAMES']:
				usernames_.append(i)

		if len(request.form['Username']) > 1:
			for i in filter_out:
				if i in request.form['Username']:
					if request.form['Username'][0].lower() == i[0]:
						return '<h3>Username %s is bad.</h3><br><p>Word Found: %s</p><a href="/" style="text-decoration:none"><button type="submit" style="background-color:black;color:white">Go Back</button></a>'%(request.form['Username'],i)
						break
					else:
						if request.form['Username'][0].lower() != i[0]:
							usernames_.append(request.form['Username'])
							break
				else:
					if i not in request.form['Username']:
						usernames_.append(request.form['Username'])
						break

			DATA = {'USERNAMES':usernames_}
			with open('username_info.json','w') as file:
				file.write(json.dumps(
					DATA,
					indent=2,
					sort_keys=False
				))
				file.flush()
				file.close()
			return render_template('submit.html',username=usernames_)
		else:
			# This repeates in second else statement..
			# To-Do: Possibly add a better way to check if the file exists?
			if os.path.exists('username_info.json'):
				info = json.loads(str(open('username_info.json','r').read()))
				users = []
				for i in info['USERNAMES']:
					users.append(i)
				return render_template('userSetup.html',username=users,badNames=filter_out, ERR_MSG="ERROR: Username was empty. Must have at least 2 characters")
			else:
				return render_template('userSetup.html',username=usernames_,badNames=filter_out,ERR_MSG="ERROR: Username was empty. Must have at least 2 characters")
	else:
		if os.path.exists('username_info.json'):
			info = json.loads(str(open('username_info.json','r').read()))
			usernames = []
			for i in info['USERNAMES']:
				usernames.append(i)
			return render_template('userSetup.html',username=usernames,badNames=filter_out)
		else:
			return render_template("userSetup.html",username=usernames_, badNames=filter_out)

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True,port=8080)