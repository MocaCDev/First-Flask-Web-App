""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from flask import (
	Flask,
	render_template
)

app = Flask(__name__)

for i in os.listdir():
	if i == 'templates':
		temp = os.path.abspath(i)

@app.route('/')
def HOME_PAGE():
	temp_HOME = os.path.abspath(temp+'/home.html')
	return render_template(temp_HOME)

if __name__=='__main__':
	app.run(debug=True)