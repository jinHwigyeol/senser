#!/usr/bin/python3
from ast import Pass
import time
import RPi.GPIO as GPIO
from bmp280 import BMP280
from smbus2 import SMBus

print("press ctrl-c to stop!")
bus = SMBus(1) # use i2c bus1
bmp280 = BMP280(i2c_dev=bus)
led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    try:
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        print('Temperature = {:.2f}C'.format(temperature))
        print('Pressure = {:.1f}hPa'.format(pressure))
        print("=======================")
        
        if temperature>20:
             for i in range(5):
                GPIO.output(led_pin,1)
                time.sleep(1)
                GPIO.output(led_pin,0)
                time.sleep(1)
        time.sleep(3)
    except KeyboardInterrupt:
        exit(0)