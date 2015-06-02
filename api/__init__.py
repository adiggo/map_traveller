from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os



app = Flask(__name__)
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '**',
        'secret': '*'
    },
    'twitter': {
        'id': '*',
        'secret': '*'
    }
}
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://luss:luss@localhost:3306/Users'
db = SQLAlchemy(app)
