import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../db')
from flask import Blueprint
from database import db_session
from flask import request
from flask import json
from db.models.users.model import User

users = Blueprint('users', __name__)

@users.route('/login', methods=['POST', 'GET'])
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