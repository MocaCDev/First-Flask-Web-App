""" ------ FLASK WEB APP ------"""
""" ------ LINUX/UNIX BASED ------"""
from flask import (
	Flask,
	render_template
)

app = Flask(__name__)

@app.route('/')
def HOME_PAGE():
	return render_template("/templates/home.html")

if __name__=='__main__':
	app.run(debug=True)