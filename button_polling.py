import RPi.GPIO as GPIO
import time

# 버튼연결 핀 지정
button_pin = 15
led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# 버튼 핀의 입력설정, PULL DOWN 저항사용
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while 1:
 if GPIO.input(button_pin) == GPIO.HIGH: # button pressed
    GPIO.output(led_pin, 1)
 else:
    GPIO.output(led_pin, 0)
 time.sleep(0.1) # delay 0.1sec
