""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
import os
from flask import (
	Flask,
	render_template
)

app = Flask(__name__)

@app.route('/')
def HOME_PAGE():
	temp_HOME = os.path.abspath('home.html')
	return render_template(temp_HOME)

if __name__=='__main__':
	app.run(debug=True)