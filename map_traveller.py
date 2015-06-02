from flask import Flask
from flask import request
from flask import json
import sys
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from api import app
from api import db
from api.model import User
from flask import make_response, jsonify




#sys.path.insert(0, os.path.dirname(
#    os.path.realpath(__file__)) + '/api')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/conf')

#app = Flask(__name__)
#app.config.from_object('config.DevelopmentConfig')
#engine = create_engine('mysql://luss:luss@localhost:3306/Users')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://luss:luss@localhost:3306/Users'
#db = SQLAlchemy(app)
from test import test_app
app.register_blueprint(test_app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.headers['Content-Type'] == 'application/json':
        json = request.json
        type = json['type']
        register_user = ''
        # step to decode token to fbid and wechat id
        token_id = get_id_by_token(json['token'])
        if token_id is None:
            return 'facebook or wechat not validated'
        if type == 'fb':
            fid = get_id_by_token(json['token'])
            register_user = User.query.filter_by(fid=fid).first()
        elif type == 'wechat':
            wid = get_id_by_token(json['token'])
            register_user = User.query.filter_by(wid=wid).first()
        if register_user is None:
            #push user into our db
            #get basic info from token_id
            db.session.add(User("li2", "adiggo@gmail.com", "pass", token_id, None, None, None, datetime.utcnow(), datetime.utcnow()))
            
        else:
            return "good return"

        
        return "donothing"
        #users = db.session.query(User).filter(User.name == json["name"]).all()
                
        #if users is not None:
         #   return users[0].name    
        #return "Not found"i

#validation with fb or wechat
def get_id_by_token(token):
    #call fb/wechat api to validate
    return 1



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
