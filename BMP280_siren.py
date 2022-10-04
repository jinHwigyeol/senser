#!/usr/bin/python3
from ast import Pass
import time
import RPi.GPIO as GPIO
from bmp280 import BMP280
from smbus2 import SMBus

print("press ctrl-c to stop!")
bus = SMBus(1) # use i2c bus1
bmp280 = BMP280(i2c_dev=bus)
p = GPIO.PWM(4, 50)
p.start(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


while True:
    try:
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        print('Temperature = {:.2f}C'.format(temperature))
        print('Pressure = {:.1f}hPa'.format(pressure))
        print("=======================")

        if temperature>20:
             for dc in range(0,100):
                p.ChangeDutyCycle(610)
                time.sleep(0.1)
                p.ChangeDutyCycle(690)
                time.sleep(0.1)
        time.sleep(3)

    except KeyboardInterrupt:
        exit(0)