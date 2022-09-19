from gpiozero import Button
from gpiozero import LED
import time
from signal import pause

def light_on():
    led.on()
def light_off():
    led.off()
button = Button(15)
led = LED(4)

button.when_pressed = light_on
button.when_released = light_off

pause()