#! /usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def welcome():
 return render_template('welcome.html')
@app.route('/login')
def login():
 return render_template('login.html')
if __name__ == '__main__' :
 app.run(host='127.0.0.1', port=8080, threaded=True)
