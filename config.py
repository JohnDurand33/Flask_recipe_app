import os

from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
	'''
		Set config variables for the flask app
    using Environment variables where available.
    Otherwise create the config variable if not done already
    '''

FLASK_APP = os.getenv('FLASKAPP')
FLASK_ENV = os.getenv('Flask_ENV')
SECRET_KEY = os.environ.get('Winter23#')


