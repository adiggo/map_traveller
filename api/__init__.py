#imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os



app = Flask(__name__)
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
