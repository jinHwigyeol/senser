import RPi.GPIO as GPIO
import time
# RED LED, Blue LED pins
led_red = 20
led_yellow= 21
sensor = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
time.sleep(5) # PIR 센서 준비 시간
try:
 while True:
  if GPIO.input(sensor) == 1: # HC-SR501 high
     GPIO.output(led_yellow, 0) # blue LED off
     GPIO.output(led_red, 1) # red LED on
     print("Motion Detected !")
 elif GPIO.input(sensor) == 0: # HC-SR501 low
      GPIO.output(led_yellow, 1) # blue LED on
      GPIO.output(led_red, 0) # red LED off
 else:
     pass
 time.sleep(0.5)

except KeyboardInterrupt:
      print("interrupted... ")
      GPIO.cleanup()