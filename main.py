""" ------ FLASK WEB APP ------"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def HOME_PAGE():
	return "<h1>HELLO WORLD</h1>"

if __name__=='__main__':
	app.run(debug=True)