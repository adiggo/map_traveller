from api import app
from flask import Blueprint

test_app = Blueprint('test_app', __name__, template_folder ='template')

@test_app.route('/test')
def test():
    return "just test"
