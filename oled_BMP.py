#!/usr/bin/python3
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import RPi.GPIO as GPIO
from bmp280 import BMP280
from smbus2 import SMBus
import time
from ast import Pass

# substitute spi(device=0, port=0) below if using that interface
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
bus = SMBus(1) # use i2c bus1
bmp280 = BMP280(i2c_dev=bus)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 20), "Hello, World", fill="white")

time.sleep(2)

for step in range(30):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 20), "Temperature = {:.2f}C".format(temperature), "Pressure = {:.1f}hPa".format(pressure), "Time = {}s".format(step), fill="white")
        time.sleep(2)