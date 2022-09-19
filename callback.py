import RPi.GPIO as GPIO
import time
button_pin = 15
led_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

# boolean flag for LED state
GPIO.output(led_pin,0)
light_on = False

# button_callback function
def button_callback(channel):
    if light_on == False:
        GPIO.output(led_pin,1) #if LED off -> on
    else:
        GPIO.output(led_pin,0) #if LED on -> off
    light_on = not light_on  #toggle LED state

# callback 등록
# callback event -> Rising edge
# callback function -> button_callback
# bounce time -> 300ms
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback,bouncetime=300)

while 1:
    time.sleep(0.1)