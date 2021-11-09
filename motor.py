import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [11, 13, 15, 16]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
def motorR(ControlPin):
    seq_r = [ [1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1] ]

    rotation = 512

    for i in range(rotation):
        for step in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq_r[step][pin])
                time.sleep(0.001)

def motorL(ControlPin):
    seq_l = [ [0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 1, 0, 0],
              [1, 0, 0, 0] ]

    rotation = 512

    for i in range(rotation):
        for step in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq_l[step][pin])
                time.sleep(0.001)
            
GPIO.cleanup()