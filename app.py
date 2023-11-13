from flask import Flask

app = Flask(__name__) #Chexks to make sure only one app running at a time

@app.route('/')
def home():
	return 'Hello, World!'