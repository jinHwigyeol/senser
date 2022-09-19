import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
# PWM class instance p, output pin GPIO4, freq 50Hz
p = GPIO.PWM(4, 50)
p.start(0) # PWM start, duty cycle = 0%

try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc) # change duty cycle to dc%
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt: # Ctrl+C exception
    pass
p.stop() # PWM stop
GPIO.cleanup() # GPIO reset