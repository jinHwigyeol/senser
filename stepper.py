#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
in1 = 17
in2 = 18
in3 = 27
in4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
direction = True # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (half-stepping. 1-2 phase)
step_sequence = [[1,0,0,1],
 [1,0,0,0],
 [1,1,0,0],
 [0,1,0,0],
 [0,1,1,0],
 [0,0,1,0],
 [0,0,1,1],
 [0,0,0,1]]

# setting up
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# initializing
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pins = [in1,in2,in3,in4]
step_counter = 0

def cleanup():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()

try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(pins)):
            GPIO.output(pins[pin], step_sequence[step_counter][pin])
        if direction == True: # 시계방향 회전
            step_counter = (step_counter - 1) % 8
        elif direction == False: # 시계반대방향 회전
            step_counter = (step_counter + 1) % 8
        else:
            break
        time.sleep(step_sleep)

except KeyboardInterrupt:
    cleanup()
    exit(1)

cleanup()
exit(0)