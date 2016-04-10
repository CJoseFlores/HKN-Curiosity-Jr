import RPi.GPIO as GPIO
import time
import os
import numpy as np
import cv2
import argparse
import imutils
from collections import deque
import sys
sys.path.append("Arms/")
import mcp3008
import irdist
from arms_module import *
#sys.path.append("CamTracking/")
import Tracking
#import cvDistance

GPIO.setmode(GPIO.BCM)#Sets the pin Numbering system to GPIO scheme
GPIO.setwarnings(False)

#Enums for Controlling the Motors
U = 1
D = 0
R = U
L = D

#Enums for seek()
blue = 0
green = 1
red = 2

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

arm1 = Arm(m1,m2,m3,m4,25)
tracks = RWD_Tracks(mR,mL)

start = 0 #generic variable that will start the code.

c1 = 0 #generic condition for openCV Camera
c2 = 0 #""
c3 = 0 #""
xcenter = 0 #x-coordinate of the center of the camera

jr = Rover(arm1,tracks)

print("before Rover")
jr.navigate(9,1)
jr.lunge(6)
jr.claw(D)
jr.default()
#below is experimental code that will execute.
'''
while(start == 0):
    print("Waiting for the AGSE to tell the rover to begin")



while(1):
    arm1.defaultconfig4()

    while(c1 == 0): #Turn the rover right until object is in the camera
        tracks.turnright()
    tracks.stoptracks()
###Center Calibration Fcn, will turn into a method or seperate function later.
    if(c2 > xcenter): #If object is to the left of the camera center
        while(c2 > xcenter): #Turn the rover until the object is centered on the camera frame
            tracks.turnleft()
        tracks.stoptracks()
    else:
        while(c2 < xcenter):
            tracks.turnright()
        tracks.stoptracks()
###End Center Calibration Fcn
    while(irdist.get_distance2(4)):#
'''










