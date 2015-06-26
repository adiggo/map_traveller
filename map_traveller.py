from flask import Flask, render_template
import sys
import os
sys.path.insert(0, os.path.dirname(
   os.path.realpath(__file__)) + '/api')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/conf')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/db')
from flask.ext.sqlalchemy import SQLAlchemy
from flask import make_response, jsonify
from flask.ext.bcrypt import Bcrypt
from database import init_engine, db_session


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
bcrypt = Bcrypt(app)
init_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_recycle=3600)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def default_error_handle(error=None):
    """ handle all errors with json output """
    return jsonify(error=error.code, message=str(error), success=False),\
        error.code        


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

from api.health.views import health
from api.users.views import users
app.register_blueprint(health, url_prefix="/health")
app.register_blueprint(users, url_prefix="/users")

# set debug as true currently
if __name__ == '__main__':
    app.run(debug=True)
