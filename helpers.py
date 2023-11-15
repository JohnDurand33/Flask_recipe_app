from functools import wraps
import secrets
from flask import request, jsonify, json
import decimal

from models import User #, and also whatever the other class name ends up as

def token_required(our_flask_function):   #Flask built-in to use for token creation / sign-up / login / logout
    @wraps(our_flask_function)   #Brandt - Curious what this is
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers: #If token doesn't exist
            token = request.headers['x-access-token'].split(' ')[1] 
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first() #Token given, checking if in db)
            print(token)
            print(current_user_token)
        except:
            owner=User.query.filter_by(token=token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token): #If token doesn't line up with wgat is in db
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            #Convert decimal instances into strings
            return str(obj)
        return super(JSONEncoder,self).default(obj)