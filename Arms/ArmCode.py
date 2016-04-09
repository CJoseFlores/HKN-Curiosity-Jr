#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import mcp3008
import irdist
import os
from arms_module import Motor
from arms_module import Arm

GPIO.setmode(GPIO.BCM)#Sets the ping Numbering System
GPIO.setwarnings(False)

U = 1
D = 0
R = U
L = D

#InitPin,UpPin,DownPin
#time.sleep(timeinseconds) -> Same as arduino Delay(timeinms)
m1 = Motor(21,20)
m2 = Motor(16,12)
m3 = Motor(26,19)
m4 = Motor(13,6)

# DOWN is close
# UP is open

arm1 = Arm(m1, m2, m3, m4, 25)
#tmove(direction, time in seconds)
#m1.tmove(U,1.1)

#print("Sensor 1's Distance: ", irdist.get_distance2(1))
#print("Sensor 2's Distance: ", irdist.get_distance2(2))
#print("Sensor 3's Distance: ", irdist.get_distance2(3))

#arm1.defaultconfig3()
#arm1.lunge3()
#arm1.claw(D)
#arm1.defaultconfig3()
#arm1.lunge3()
#arm1.claw(U)
#arm1.slowclaw(U)

#Testing the pin that stops the arm.
m1.tmove(D, 1.5)
arm1.defaultconfig4()