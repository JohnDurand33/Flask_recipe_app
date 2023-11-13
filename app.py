from flask import Flask

app = Flask(__name__) #  Everything flows from here AKA headquarters.  Also checks to make sure only one app running at a time

@app.route('/')
def home():
	return 'Hello, World!'