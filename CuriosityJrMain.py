import RPi.GPIO as GPIO
import sys
sys.path.append("Arms/")
from arms_module import *
import Tracking


GPIO.setmode(GPIO.BCM) #Sets the pin Numbering system to GPIO scheme
GPIO.setwarnings(False)

#Enums for Controlling the Motors
Up = 1
Down = 0
Right = Up
Left = Down

#Enums for fwd()
payloaddist = 25252 #change this value after testing
baydist = 25252 #change this value after testing

#Motor(UpPin,DownPin). Below initializes motor objects
m1 = Motor(21,20)
m2 = Motor(16,12)#
m3 = Motor(26,19)
m4 = Motor(6,13)
#DOWN is close, UP is open
#m1-m4 are motors for the arm
mL = Motor(22,27)     #Left Track
mR = Motor(23,24)     #Right Track


SArm = 4;
SClaw = 8;
arm1 = Arm(SArm,SClaw)
tracks = RWD_Tracks(mR,mL)

start = 0 #generic variable that will start the code.

jr = Rover(arm1,tracks)

jr.navigate(9,2) 
# Search for green.

jr.lunge();
