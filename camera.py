#!/usr/bin/python3
from gpiozero import Button
from picamera import PiCamera
from time import sleep
from signal import pause

#create buttons and a PiCamera objects
button1 = Button(2) # capture still image
button2 = Button(3) # quit the program

camera = PiCamera()
# start the camera
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(100,200,500,600))

# var for image serial number 
i = 0

# stop the camera when the quit button pressed
def quit_camera():
    camera.stop_preview()
    exit()

# take still image when the capture button pressed
def capture_image():
    global i
    i = i + 1
    camera.capture('image_{}s.jpg'.format(i))
    print('still image taken')
    sleep(5)

# register a function that capture a image when the button1 pressed
button1.when_pressed = capture_image

# register a function that quit the camera when the button2 pressed
button2.when_pressed = quit_camera

# wait until a signal is delivered
pause() 
