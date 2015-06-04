from flask import request, redirect, url_for
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user
import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../')
from db.models.users.model import User
from map_traveller import app


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


# login_required annotation means this part need to be authenticated beforehand
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) 


@app.route('/login')
def login():
    if request.method == 'GET':
        return "ECHO: GET\n"


