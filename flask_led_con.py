#! /usr/bin/python3
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('led_control.html')

@app.route('/flask_led', methods=['POST', 'GET'])
def led_control():
    if request.method == 'GET':
        control = request.args.get('action')
        if control == 'on':
            GPIO.output(4, GPIO.HIGH)
        elif control == 'off':
            GPIO.output(4, GPIO.LOW)
        else:
            return "<h1> Bad comannd!</h1>"
            return render_template('result.html', status=control)
    elif request.method == 'POST':
        #control = request.form['action']
        return "<h1> Post request not supported!</h1>"
    else:
        return '<h1> Bad Request! </h1>'

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=8080, threaded=True)