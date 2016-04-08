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
sys.path.append("CamTracking/")
import Tracking
import cvDistance

GPIO.setmode(GPIO.BCM)#Sets the pin Numbering system to GPIO scheme
GPIO.setwarnings(False)

U = 1 #Enums for Controlling the Motors
D = 0
R = U
L = D

#Motor(UpPin,DownPin). Below initializes motor objects
m1 = Motor(21,20)
m2 = Motor(13,6)
m3 = Motor(16,12)
m4 = Motor(26,19)
#DOWN is close, UP is open
#m1-m4 are motors for the arm

#Ltrackm = Motor(x,w)     Set the pins for the Left Track later
#Rtrackm = Motor(y,z)     Same for the Right Track

arm1 = Arm(m1,m2,m3,m4)

