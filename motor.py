import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [11, 13, 15, 16]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
seq = [ [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1] ]

for i in range(512):
    for halfstep in range(4):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
            time.sleep(0.001)
            
GPIO.cleanup()