# BMP85/180 module
import Adafruit_BMP.BMP085 as BMP085

# BMP180 instance
sensor = BMP085.BMP085()

# 센서에서 측정값 읽기
temp = sensor.read_temperature()
pressure = sensor.read_pressure()
altitude = sensor.read_altitude()

# 측정값 출력
print('Temp = {0:0.2f} *C'.format(temp))
print('Pressure = {0:0.2f} Pa'.format(pressure))
print('Altitude = {0:0.2f} m'.format(altitude))