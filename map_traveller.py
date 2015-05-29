from flask import Flask
import sys
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/api')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/conf')

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
engine = create_engine('mysql://luss:luss@localhost:3306/Users')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://luss:luss@localhost:3306/Users'
db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
