#!/usr/bin/python3
import os
import RPi.GPIO as GPIO
from urllib.parse import parse_qs

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

#qString = sys.stdin.readline() # POST method
qString = os.environ['QUERY_STRING']
qVal = parse_qs(qString)
request = qVal['action'][0]

if request.upper() == 'ON':
    GPIO.output(4, GPIO.HIGH)
    responseBody='<HTML><BODY><H1> LED Turned ON!</H1><BR>
    <a href="../led_control.html"> Back To Control Page! </a><BR></BODY></HTML>'
elif request.upper() == 'OFF':
    GPIO.output(4, GPIO.LOW)
    responseBody='<HTML><BODY><H1> LED Turned OFF!</H1><BR> 
    <a href="../led_control.html"> Back To Control Page! </a><BR></BODY></HTML>'
else:
    responseBody='<HTML><BODY><H1> Bad Command!</H1><BR> 
    <a href="../led_control.html"> Back To Control Page! </a><BR></BODY></HTML>'
 
print('Content-type: text/html\n\n')
print(responseBody)