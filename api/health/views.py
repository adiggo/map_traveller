import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../db')
from flask import Blueprint
from database import db_session

health = Blueprint('health', __name__)

@health.route('')
def health_check():
    return 'Server is running!'  