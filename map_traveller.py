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
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/api')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/conf')

#app = Flask(__name__)
#app.config.from_object('config.DevelopmentConfig')
#engine = create_engine('mysql://luss:luss@localhost:3306/Users')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://luss:luss@localhost:3306/Users'
#db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.headers['Content-Type'] == 'application/json':
        json = request.json
        users = db.session.query(User).filter(User.name == json["name"]).all()
        
        if users is not None:
            return users[0].name    
        return "Not found"
if __name__ == '__main__':
    app.run(debug=True)
