from flask import Flask
import sys
import os

sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/api')
sys.path.insert(0, os.path.dirname(
    os.path.realpath(__file__)) + '/conf')


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
