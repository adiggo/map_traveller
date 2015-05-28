from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    
    

@app.route('/')
if __name__ == '__main__':
    app.run()
