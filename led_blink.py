import RPi.GPIO as GPIO
import time

# GPIO핀 번호 지정 (BCM 모드)
led_pin = 4 # GPIO4
# warning off

GPIO.setwarnings(False)
# GPIO핀 번호모드 BCM으로 설정

GPIO.setmode(GPIO.BCM)
# GPIO핀 출력으로 설정

GPIO.setup(led_pin, GPIO.OUT)
for i in range(10):
 GPIO.output(led_pin,1) # LED on
 time.sleep(1) # 1초동안 대기상태
 GPIO.output(led_pin,0) # LED off
 time.sleep(1) # 1초동안 대기상태
GPIO.cleanup() # GPIO 설정 reset