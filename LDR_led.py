import spidev
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

led_pin = 4
delay = 0.5
ldr_channel = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def SPI_read_adc(channel):
    r = spi.xfer2([1, 8 + channel << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    try:  
        ldr_value = SPI_read_adc(ldr_channel)
        print("LDR messured value: %d" % ldr_value)
        time.sleep(delay)
        
        if idr_value>500:
            GPIO.output(led_pin,1)

    except KeyboardInterrupt:
        exit(0)