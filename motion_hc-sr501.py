import RPi.GPIO as GPIO
import time
# RED LED, Blue LED pins
led_red = 20
led_blue= 21
sensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_Y, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

time.sleep(5) # PIR 센서 준비 시간

try:
    while True:
        if GPIO.input(sensor) == 1: # HC-SR501 high
            GPIO.output(led_blue, 0) # blue LED off
            GPIO.output(led_red, 1) # red LED on
            print("Motion Detected !")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0: # HC-SR501 low
            GPIO.output(led_blue, 1) # blue LED on
            GPIO.output(led_red, 0) # red LED off
            time.sleep(0.2)

except KeyboardInterrupt:
        print("interrupted... ")
        GPIO.cleanup()