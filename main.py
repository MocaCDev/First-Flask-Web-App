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
	try:
		os.system('pip3 install -r requirements.txt')
		from flask import (
			Flask,
			render_template,
			#url_for,
			request
		)
	except:
		raise ImportError('pip3 is not installed. pip3 is needed in order to download imported module "Flask"')

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
lastUsers_ = []
emails_ = []
#time_now = datetime.now().strftime("%H:%M:%S")

@app.route('/Submitted')
def Submit():
	return render_template('homePage.html', usernames=usernames_)

"""
	Home Page is the page where user will enter credentials
"""
@app.route('/', methods=['POST','GET'])
def HOME_PAGE():
	lastUsernameAdded=''
	if request.method == 'POST':
		lastUsernameAdded=request.form['Username']
		# This will append all previous added usernames
		if os.path.exists('username_info.json'):
			old = json.loads(str(open('username_info.json','r').read()))

			for i in range(len(old['USERNAMES'])):
				lastUsers_.append(old['USERNAMES'][i])
				if i == len(old['USERNAMES'])-1:break
		
		# There is no checking for bad names in this. It is an email.
		# If there is, perhaps, a bad name in the email, and we return an error to the webpage saying the name is invalid
		# then the user would either a. Have to create a new email or b. type a fake email
		if len(request.form['Email']) > 1:
			emails_.append(request.form['Email'])
		else:
			# Might as well check if they're both less than one
			if len(request.form['Username']) < 1 and len(request.form['Email']) < 1:
				return render_template('userSetup.html',username=usernames_,email=emails_,ERR_MSG="Email and Username input was left blank...please complete the inputs",lastUsers=lastUsers_)
			else:
				return render_template('userSetup.html',username=usernames_,email=emails_,ERR_MSG="Email input was left blank...please complete the Email input",lastUsername=request.form['Username'],lastUsers=lastUsers_)

		if len(request.form['Username']) > 1:
			inIt = None
			for i in range(len(filter_out)):
				if filter_out[i] in request.form['Username'].lower():
					if request.form['Username'][0].lower() == filter_out[i][0]:
						return '<h3>Username %s is bad.</h3><br><p>Word Found: %s</p><a href="/" style="text-decoration:none"><button type="submit" style="background-color:black;color:white">Go Back</button></a>'%(request.form['Username'],filter_out[i])
					else:
						usernames_.append(request.form['Username'])
						break
				if i == len(filter_out)-1 and not filter_out[i] in request.form['Username']:
					inIt=False
			
			if inIt != None:
				usernames_.append(request.form['Username'])

			DATA = {'USERNAMES':usernames_, 'EMAILS':emails_}
			with open('username_info.json','w') as file:
				file.write(json.dumps(
					DATA,
					indent=2,
					sort_keys=False
				))
				file.flush()
				file.close()
			return render_template('submit.html',username=usernames_,email=emails_)
		else:
			# This repeates in second else statement..
			# To-Do: Possibly add a better way to check if the file exists?
			if len(lastUsers_)>0:
				"""
				info = json.loads(str(open('username_info.json','r').read()))
				users = []
				for i in info['USERNAMES']:
					users.append(i)
				"""
				return render_template('userSetup.html',lastUsers=lastUsers_,email=emails_,badNames=filter_out, ERR_MSG="ERROR: Username was empty. Must have at least 2 characters",lastEmail=request.form['Email'])
			else:
				return render_template('userSetup.html',username=usernames_,email=emails_,badNames=filter_out,ERR_MSG="ERROR: Username was empty. Must have at least 2 characters",lastEmail=request.form['Email'],lastUsers=lastUsers_)
	else:
		if len(lastUsers_)>0:
			"""
			info = json.loads(str(open('username_info.json','r').read()))
			usernames = []
			for i in info['USERNAMES']:
				usernames.append(i)
			"""
			return render_template('userSetup.html',lastUsers=lastUsers_,email=emails_,badNames=filter_out,lastUsername=lastUsernameAdded)
		else:
			return render_template("userSetup.html",username=usernames_, email=emails_,badNames=filter_out,lastUsername=lastUsernameAdded,lastUsers=lastUsers_)

@app.route('/about')
def ABOUT_PAGE():
	return render_template("about.html")

if __name__=='__main__':
	app.run(debug=True,port=8080)