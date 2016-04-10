#! /usr/bin/env python
import RPi.GPIO as GPIO
import numpy as np
import time
import mcp3008
import irdist
import Tracking

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
    __upin = None
    __dpin = None
    __speed = None
    __index = None

    def __init__(self, upin, dpin):
        self.__upin = upin
        self.__dpin = dpin
        GPIO.setup(upin, GPIO.OUT)
        GPIO.setup(dpin, GPIO.OUT)
        return

    def tmove(self, direction, t):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        elif(direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        else:
            return

    def move(self,direction):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
        elif (direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
        else:
            return
    def stop(self):
        GPIO.output(self.__upin, GPIO.LOW)
        GPIO.output(self.__dpin, GPIO.LOW)
        return

class Servo:
    __spin = None
    __freq = None
    __pwm = None
    __neutral = None
    __delay = None

    def __init__(self, spin, freq, neutralduty, delay): #default the freq to 50hz
        self.__spin = spin
        self.__freq = freq
        self.__neutral = neutralduty
        self.__delay = delay
        GPIO.setup(spin, GPIO.OUT)
        self.__pwm = GPIO.PWM(spin, freq) #pin, frequency in hertz
        self.__pwm.start(self.__neutral)
        return

    def servoDefault(self):
        self.__pwm.ChangeDutyCycle(self.__neutral)
        time.sleep(self.__delay)
        return

    def servoMove(self, position):
        self.__pwm.ChangeDutyCycle(position)
        time.sleep(self.__delay)
        return

    def servoStop(self):
        self.__pwm.stop()
        return

class Arm:
    __s1 = None  # abstract servos (1 is the lower one)
    __s2 = None

    def __init__(self, s1, s2):
        self.__s1 = s1
        self.__s2 = s2
        self.default()
        return

    def default(self):
        self.__s1.servoDefault()
        self.__s2.servoDefault()
        return

'''
class Arm:
    __m1= None
    __m2 = None
    __m3 = None
    __m4 = None
    __button = None
    #Note that Arm() can only take in Motor Objects as parameters
    def __init__(self, m1, m2, m3, m4, button):
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        self.__button = button

        GPIO.setup(button, GPIO.IN)

        return

    #This dconfig is based from the original plan.
    #This function will set the robot arm to the default state.
    #The first if statement refers to the sensor connected to channel 1 of the mcp3008
    #The second if statement refers to the sensor connected to channel 2 of the mcp 3008
    def defaultconfig1(self):
        self.stoparm()
        stopflag = [0,0]
        while(stopflag[0] == 0 or stopflag[1] == 0):
            if(irdist.get_distance(1)>123123): #12123 will be replaced with a certain distance reading, reading from channel 1. Ch1 sensor on top of m1
                self.__m1.move(1)#moves up
            else:
                self.__m1.stop()
                stopflag[0] = 1
            if(irdist.get_distance(2)>123123): #Sensor Connected to Channel 2, next to the baseplate
                self.__m2.move(0)#moves down
            else:
                self.__m2.stop()
                stopflag[1] = 1
        return
    #This is from the second plan, where we have 1 sensor on the bottom, 1 on top of m5, and then
    #1 one possibly on top of m1

    def defaultconfig2(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(1)>5): #ch1 sensor is ontop of m1. If the sensor doesn't detect the arm part, the following if statements
                if(irdist.get_distance(2)<123123):
                    self.__m1.move(1) #m1 begins to move up if the sensor is too low to the ground.
                    self.__m2.stop()
                elif(irdist.get_distance(2)>123123):
                    self.__m2.move(0) #m2 begins to move down if the sensor is too high from the ground.
                    self.__m1.stop()
            else:
                self.__stoparm() #stops all arm movement/operation. The arm should now be in default position.
            stopflag = 1
        return

    def defaultconfig3(self):
        self.stoparm()
        snsr1 = irdist.get_distance2(1)
        if(snsr1 > 8):
            while(snsr1 > 8): #The arm is below default position
                self.__m1.move(1) #m1 moves up
                self.__m2.stop()
                snsr1 = irdist.get_distance2(1)
            self.stoparm()

        else: #The arm is above or at default position
            while(snsr1 < 8):
                self.__m1.move(0)#m1 moves down
                self.__m2.stop()
                snsr1 = irdist.get_distance2(1)
            self.stoparm()
        return

    def defaultconfig4(self):
        self.stoparm()
        self.__m1.move(1)
        while(GPIO.input(self.__button) == 0):
           pass
           #self.__m2.stop()
           #self.__m3.stop()
        self.stoparm()
        return

    #The code below is the original plan.
    #This function will lunge into position to grab or drop the payload
    def lunge1(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(2)<123123):
                self.__m1.move(0)#moves down
                self.__m2.move(1)#moves up
            else:
                self.stoparm()
                stopflag = 1
        return

    def lunge2(self):
        self.stoparm()
        stopflag = 0
        while (stopflag == 0):
            if (irdist.get_distance(3) < 123123):#ch3 sensor is the sensor on top of the rover.
                if (irdist.get_distance(2) < 123123):
                        self.__m1.move(0)  # m2 begins to move down if the sensor is too high to the ground.
                        self.__m2.stop()
                elif (irdist.get_distance(2) > 123123):
                        self.__m2.move(1)  # m3 begins to move up if the sensor is too low from the ground.
                        self.__m1.stop()
            else:
                self.__stoparm()
                stopflag = 1
        return

    def lunge3(self, dist): #REMEBER TO MODIFY THE SNSR2 < 4 CONDITION IT WILL NO LONGER BE THIS LOW!!!
        self.stoparm()
        done = False
        oldValue = irdist.get_distance2(2)

        while not done:
            self.__m1.move(0)
            self.__m2.stop()

            value = irdist.get_distance2(2)

            print("new value is {}".format(value))
            print("old value is {}".format(oldValue))
            if abs(value - oldValue) < 5:
                if(value < dist):
                    done = True
                oldValue = value

        self.stoparm()

    #This function grabs or releases the payload. "action" means either grab or release
    def claw(self, action):
        self.stoparm()
        self.__m4.tmove(action,.80)#Moves for .75 seconds
        return

    def slowclaw(self, action):
        self.stoparm()
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .10)
        time.sleep(.10)
        self.__m4.tmove(action, .9)
        return

    def stoparm(self):
        self.__m1.stop()
        self.__m2.stop()
        self.__m3.stop()
        self.__m4.stop()
        return
'''
class RWD_Tracks:
    __mR = None
    __mL = None

    def __init__(self, mR, mL):
        self.__mR = mR
        self.__mL = mL
        return

    def forward(self):
        self.stoptracks()
        self.__mR.move(1)#Both Motors move up
        self.__mL.move(1)
        return

    def turnright(self):
        self.stoptracks()
        self.__mR.move(0)
        self.__mR.move(1)
        return

    def turnleft(self):
        self.stoptracks()
        self.__mR.move(1)
        self.__mL.move(0)
        return

    def reverse(self):
        self.stoptracks()
        self.__mR.move(0)#Both Motors move down
        self.__mL.move(0)
        return

    def stoptracks(self):
        self.__mR.stop()
        self.__mL.stop()
        return

class Rover:
    __arm = None
    __tracks = None
    __bluerange = (np.array([110, 50, 100]),np.array([130, 255, 255])) #lower, upper color boundaries, in RGB
    __greenrange = (np.array([0,170,43]),np.array([17,255,77])) #dark green to light green
    __redrange = (np.array([191, 0, 0]),np.array([255, 132, 9]))#dark red to light orange

    __colorList = {1:__bluerange,2:__greenrange,3:__redrange}

    def __init__(self, arm, tracks):
        self.__arm = arm
        self.__tracks = tracks
        self.__arm.defaultconfig4()
        self.__arm.claw(1) #will force the claw open

        return

    def default(self):
        self.__arm.defaultconfig4()
        return

    def lunge(self,dist):
        self.__arm.lunge3(dist)
        return

    def claw(self, action):
        self.__arm.claw(action)
        return

    def seek(self, color):
        '''
            This method seeks a payload with an specific color. It moves the rover
                until it finds the payload.
        :param color: color = {1,2,3}. Color that we want the system to track.
            1 - Blue Range
            2 - Green Range
            3 - Red Range
        :return:
        '''
        colorSelection = self.__colorList[color]  #choose the color from the list
        cvcondition = Tracking.track(colorSelection[0], colorSelection[1]) #getting current state of the target in the frame
        print("Seeking object")
        while (cvcondition == 0):
            self.__tracks.turnright()
            print("Moving Right")
            cvcondition = Tracking.track(colorSelection[0], colorSelection[1])
        self.__tracks.stoptracks()
        print("Found!!!")
        return

    def center(self, color):
        '''
            This method centers the screen to an specific color payload. It moves the rover
                depending on the position of the payload on the screen.
        :param color: color = {1,2,3}. Color that we want the system to track.
            1 - Blue Range
            2 - Green Range
            3 - Red Range
        :return:
        '''
        colorSelection = self.__colorList[color]  #choose the color from the list
        cvcondition = Tracking.track(colorSelection[0], colorSelection[1]) #getting current state of the target in the frame

        print("Centering")
        while cvcondition != 2: #is going to be trying to center until it is in the middle

            if(cvcondition < 2):#left of center frame
                self.__tracks.turnleft()
                print("Moving left")

            elif(cvcondition > 2):#right of center frame
                self.__tracks.turnright()
                print("Moving Right")

            self.__tracks.stoptracks()
            cvcondition = Tracking.track(colorSelection[0], colorSelection[1])
        print("CENTERED!!!")
        return

    def fwd(self, dist, color):
        glitchfilter = 0
        #While the payload has not yet been detected
        done = False
        oldValue = irdist.get_distance2(4)

        while not done:
            self.__tracks.forward()
            print("moving forward")
            self.center(color)
            value = irdist.get_distance2(4)

            print("new value is {}".format(value))
            print("old value is {}".format(oldValue))

            if abs(value - oldValue) < 10:
                if(value < dist):
                    done = True
                oldValue = value;

        self.__tracks.stoptracks()
        return

    def back(self):#possibly not use this?
        self.reverse()

        return

    def navigate(self, dist, color):
        print("here")
        self.seek(color)
        self.center(color)
        self.fwd(dist, color)
        return







