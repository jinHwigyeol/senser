import gpiozero import LED
import time

# GPIO핀 번호지정 (GPIO4)
led = LED(4) # GPIO4
for i in range(10):
 led.on() # LED on
 time.sleep(1) # 1초동안 대기상태
 led.off() # LED off
 time.sleep(1) # 1초동안 대기상태