from flask import Flask
from .site.routes import site

app = Flask(__name__) #  Everything flows from here AKA headquarters.  
#Also checks to make sure only one app running at a time

app.register_blueprint(site)