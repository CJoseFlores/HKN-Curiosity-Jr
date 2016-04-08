import RPi.GPIO as GPIO
import time
import random
from DualServos import DualServos
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Tracks = DualServos(14, 18)
Counter = 0
while (Counter < 100):
    Tracks.Forward()
    Counter += 1
    print(Counter)
Counter = 0
while (Counter < 100):
    Tracks.Reverse()
    Counter += 1
    print(Counter)